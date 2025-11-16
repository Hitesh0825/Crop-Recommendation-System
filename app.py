import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Set page config
st.set_page_config(
    page_title="🌾 Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# Load the pre-trained model, scaler, and label encoder
@st.cache_resource
def load_models():
    model = joblib.load("crop_model_rf.joblib")
    scaler = joblib.load("scaler.joblib")
    le = joblib.load("labelencoder.joblib")
    return model, scaler, le

model, scaler, le = load_models()

# Get feature names from the model or define them
feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

# App title and description
st.title("🌾 Crop Recommendation System")
st.markdown("---")
st.write("This system predicts the best crop to plant based on soil and weather conditions.")

# Create two columns for layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📋 Input Features")
    
    # Create input fields for each feature
    N = st.number_input(
        "Nitrogen (N) content",
        min_value=0,
        max_value=150,
        value=50,
        step=1,
        help="Nitrogen content in soil (ppm)"
    )
    
    P = st.number_input(
        "Phosphorus (P) content",
        min_value=0,
        max_value=150,
        value=50,
        step=1,
        help="Phosphorus content in soil (ppm)"
    )
    
    K = st.number_input(
        "Potassium (K) content",
        min_value=0,
        max_value=150,
        value=50,
        step=1,
        help="Potassium content in soil (ppm)"
    )
    
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=50.0,
        value=20.0,
        step=0.1,
        help="Average temperature in Celsius"
    )
    
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=80.0,
        step=0.1,
        help="Relative humidity percentage"
    )
    
    ph = st.number_input(
        "pH level",
        min_value=0.0,
        max_value=14.0,
        value=7.0,
        step=0.1,
        help="Soil pH level"
    )
    
    rainfall = st.number_input(
        "Rainfall (mm)",
        min_value=0.0,
        max_value=500.0,
        value=200.0,
        step=1.0,
        help="Annual rainfall in millimeters"
    )

with col2:
    st.subheader("🎯 Prediction Results")
    
    # Add a button to trigger prediction (prevents running on every input change)
    if st.button("🔮 Get Crop Recommendation", type="primary", use_container_width=True):
        with st.spinner("Analyzing conditions and predicting crop..."):
            # Create feature array
            features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            
            # Scale features
            features_scaled = scaler.transform(features)
            
            # Make prediction
            prediction_encoded = model.predict(features_scaled)[0]
            prediction_proba = model.predict_proba(features_scaled)[0]
            
            # Decode prediction
            crop_prediction = le.inverse_transform([prediction_encoded])[0]
            
            # Store in session state to persist results
            st.session_state['crop_prediction'] = crop_prediction
            st.session_state['prediction_proba'] = prediction_proba
            st.session_state['confidence'] = np.max(prediction_proba) * 100
            st.session_state['features'] = [N, P, K, temperature, humidity, ph, rainfall]
    
    # Display results if available
    if 'crop_prediction' in st.session_state:
        # Display the main prediction
        st.success(f"### 🌱 Recommended Crop")
        st.markdown(f"## {st.session_state['crop_prediction'].upper()}")
        
        # Display confidence
        st.info(f"**Confidence: {st.session_state['confidence']:.2f}%**")
        
        # Display prediction probabilities for all crops
        st.subheader("📊 Prediction Probabilities")
        
        # Create a dataframe with probabilities
        proba_df = pd.DataFrame({
            'Crop': le.classes_,
            'Probability': st.session_state['prediction_proba'],
            'Percentage': st.session_state['prediction_proba'] * 100
        }).sort_values('Probability', ascending=False)
        
        # Display as a bar chart
        st.bar_chart(proba_df.set_index('Crop')['Percentage'])
        
        # Display probabilities as a table (formatted better)
        display_df = proba_df[['Crop', 'Percentage']].copy()
        display_df['Percentage'] = display_df['Percentage'].apply(lambda x: f"{x:.2f}%")
        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info("👆 Click the button above to get crop recommendations based on your inputs.")

# Display summary statistics (only if prediction has been made)
if 'features' in st.session_state:
    st.markdown("---")
    st.subheader("📈 Input Summary")
    
    summary_data = {
        'Feature': feature_names,
        'Value': st.session_state['features']
    }
    summary_df = pd.DataFrame(summary_data)
    st.table(summary_df)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center'>
    <p>🌾 Crop Recommendation System | Built with Streamlit & Random Forest</p>
    </div>
    """,
    unsafe_allow_html=True
)
