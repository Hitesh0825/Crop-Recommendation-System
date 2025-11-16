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
- **Optimized Performance**: Button-triggered predictions prevent unnecessary computations on every input change
- **Fast Model Loading**: Cached model loading using Streamlit's caching mechanism

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

### Local Docker Deployment

The project includes a `Dockerfile` for containerized deployment:

```bash
# Build the Docker image
docker build -t crop-recommendation .

# Run the container
docker run -p 7860:7860 crop-recommendation
```

The application will be available at `http://localhost:7860`

### Deploying to HuggingFace Spaces with Docker

HuggingFace Spaces supports Docker deployments, allowing you to deploy your Streamlit app with full control over the environment.

#### Prerequisites

1. **HuggingFace Account**: Sign up at [huggingface.co](https://huggingface.co)
2. **Docker**: Ensure you have Docker installed locally (for testing)
3. **Git**: For version control

#### Step-by-Step Deployment Guide

1. **Create a New Space on HuggingFace**
   - Go to [HuggingFace Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose:
     - **SDK**: Docker
     - **Hardware**: Select based on your needs (CPU Basic is usually sufficient)
     - **Visibility**: Public or Private
   - Name your space (e.g., `crop-recommendation`)

2. **Prepare Your Files**
   Ensure your repository contains:
   ```
   crop-system/
   ├── Dockerfile              # Docker configuration
   ├── app.py                  # Streamlit application
   ├── requirements.txt        # Python dependencies
   ├── crop_model_rf.joblib   # Trained model
   ├── scaler.joblib          # Feature scaler
   └── labelencoder.joblib    # Label encoder
   ```

3. **Push to HuggingFace**
   ```bash
   # Clone your HuggingFace Space repository
   git clone https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME
   cd YOUR_SPACE_NAME
   
   # Copy all your files to the repository
   cp /path/to/crop-system/* .
   
   # Commit and push
   git add .
   git commit -m "Initial deployment"
   git push
   ```

4. **Automatic Build**
   - HuggingFace will automatically detect the `Dockerfile` and start building
   - Monitor the build logs in the "Logs" tab of your Space
   - The build typically takes 5-10 minutes

5. **Access Your App**
   - Once built, your app will be available at:
     `https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME`

#### Dockerfile Configuration for HuggingFace

The included `Dockerfile` is optimized for HuggingFace Spaces:
- Uses Python 3.10 slim image for smaller size
- Exposes port 7860 (HuggingFace default)
- Configures Streamlit for headless operation
- Includes health checks for container monitoring
- Optimized layer caching for faster rebuilds

#### Troubleshooting

**Build Fails:**
- Check the build logs in HuggingFace Spaces
- Ensure all model files are included in the repository
- Verify `requirements.txt` has correct package versions

**App Not Loading:**
- Check that port 7860 is exposed in Dockerfile
- Verify environment variables are set correctly
- Review application logs in the HuggingFace interface

**Performance Issues:**
- The app now uses a button-triggered prediction system (fixed in latest version)
- Model loading is cached using `@st.cache_resource`
- Consider upgrading hardware tier if needed

#### Updating Your Deployment

To update your deployed app:

```bash
cd YOUR_SPACE_NAME
# Make your changes
git add .
git commit -m "Update: description of changes"
git push
```

HuggingFace will automatically rebuild and redeploy your app.

#### Environment Variables

The Dockerfile sets these environment variables automatically:
- `STREAMLIT_SERVER_PORT=7860` - Server port
- `STREAMLIT_SERVER_ADDRESS=0.0.0.0` - Listen on all interfaces
- `STREAMLIT_SERVER_HEADLESS=true` - Headless mode
- `STREAMLIT_BROWSER_GATHER_USAGE_STATS=false` - Disable usage stats

#### Resource Requirements

- **Minimum**: CPU Basic (2 vCPU, 16GB RAM)
- **Recommended**: CPU Basic for most use cases
- Model files are typically 1-10MB, so storage is not a concern

#### Best Practices

1. **Keep Dockerfile minimal**: Only include necessary dependencies
2. **Use .dockerignore**: Exclude unnecessary files (if needed)
3. **Test locally first**: Build and run Docker image locally before pushing
4. **Monitor logs**: Check HuggingFace logs regularly for issues
5. **Version control**: Keep your code in Git for easy updates

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
