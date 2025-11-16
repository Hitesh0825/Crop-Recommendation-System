---
title: Crop Recommendation System
emoji: 🌾
colorFrom: green
colorTo: yellow
sdk: streamlit
sdk_version: 1.28.1
app_file: app.py
pinned: false
license: mit
---

# 🌾 Crop Recommendation System

An intelligent crop recommendation system that helps farmers and agricultural experts determine the best crop to plant based on soil conditions and weather parameters.

[![Live Demo](https://img.shields.io/badge/🌐_Live_Demo-HuggingFace_Spaces-yellow)](https://huggingface.co/spaces/Hitesh0825/crop_recommendation)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28.1-red.svg)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🚀 Live Demo

**Try it now!** 👉 [https://huggingface.co/spaces/Hitesh0825/crop_recommendation](https://huggingface.co/spaces/Hitesh0825/crop_recommendation)

## 📋 About

This Streamlit application uses a machine learning model (Random Forest) trained on agricultural data to recommend the optimal crop for a given set of environmental and soil conditions. The system analyzes 7 key parameters to provide accurate crop recommendations with confidence scores.

## 🎯 Features

- **Real-time Crop Prediction**: Get instant crop recommendations based on input parameters
- **Confidence Scores**: View prediction confidence and probabilities for all crops
- **Interactive Interface**: User-friendly interface with intuitive input controls
- **Data Visualization**: Visual representation of prediction probabilities using bar charts
- **Comprehensive Analysis**: View probabilities for all crop options, not just the top recommendation

## 📊 Input Parameters

The system requires the following 7 parameters:

1. **Nitrogen (N)** - Soil nitrogen content (ppm)
2. **Phosphorus (P)** - Soil phosphorus content (ppm)
3. **Potassium (K)** - Soil potassium content (ppm)
4. **Temperature** - Average temperature (°C)
5. **Humidity** - Relative humidity (%)
6. **pH Level** - Soil pH value (0-14)
7. **Rainfall** - Annual rainfall (mm)

## 🚀 How to Use

### Online (HuggingFace Spaces)

1. Visit the [live demo](https://huggingface.co/spaces/Hitesh0825/crop_recommendation)
2. Enter the soil and weather parameters in the input fields
3. The system will automatically predict the best crop recommendation
4. View the recommended crop along with confidence scores
5. Explore the probability distribution for all crops in the chart below

### Local Installation

To run this application locally:

```bash
# Clone the repository
git clone <your-github-repo-url>
cd crop-system

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

The application will be available at `http://localhost:8501`

## 🧠 Model Information

- **Algorithm**: Random Forest Classifier
- **Preprocessing**: StandardScaler for feature normalization
- **Label Encoding**: Encoded crop names for multi-class classification
- **Model Files**: 
  - `crop_model_rf.joblib` - Trained Random Forest model
  - `scaler.joblib` - Feature scaler
  - `labelencoder.joblib` - Label encoder for crop names

## 📦 Technologies Used

- **Streamlit** - Web application framework
- **Scikit-learn** - Machine learning library
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation
- **Joblib** - Model serialization

## 📁 Project Structure

```
crop-system/
│
├── app.py                      # Streamlit application
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Docker configuration
├── README.md                   # Project documentation
│
├── crop_model_rf.joblib       # Trained Random Forest model
├── scaler.joblib              # Feature scaler
└── labelencoder.joblib        # Label encoder
```

## 📝 Requirements

- Python 3.10+
- See `requirements.txt` for the complete list of dependencies:
  - streamlit==1.28.1
  - joblib==1.3.2
  - pandas==2.0.3
  - numpy==1.26.4
  - scikit-learn==1.3.0

## 🐳 Docker Deployment

The project includes a `Dockerfile` for containerized deployment:

```bash
# Build the Docker image
docker build -t crop-recommendation .

# Run the container
docker run -p 7860:7860 crop-recommendation
```

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Dataset and model training based on agricultural crop recommendation data
- Built with Streamlit for easy deployment and sharing
- Deployed on HuggingFace Spaces

## 👤 Author

**Hitesh0825**

- HuggingFace Spaces: [@Hitesh0825](https://huggingface.co/Hitesh0825)

---

Made with ❤️ using Streamlit and HuggingFace Spaces
