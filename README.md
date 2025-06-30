# Mental Health Predictor 🧠

A web-based machine learning application that predicts mental health conditions based on user input features. Built with Flask and TensorFlow/Keras.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-v2.0+-green.svg)
![TensorFlow](https://img.shields.io/badge/tensorflow-v2.0+-orange.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Features

![image](https://github.com/user-attachments/assets/8724619e-d26e-41e3-a804-9ff049862b84)
![image](https://github.com/user-attachments/assets/46176dad-0c4f-4d83-8d25-6ebbe3c893bd)



- **Mental Health Prediction**: Predict 13 different mental health conditions
- **Interactive Web Interface**: User-friendly form for input data
- **Data Visualization**: Dynamic charts showing prediction confidence
- **RESTful API**: JSON API endpoints for integration
- **Real-time Results**: Instant predictions with confidence scores
- **Responsive Design**: Works on desktop and mobile devices

## 🏥 Supported Mental Health Conditions

The model can predict the following conditions:

1. **ADHD** - Attention Deficit Hyperactivity Disorder
2. **ASD** - Autism Spectrum Disorder  
3. **Loneliness** - Social isolation and loneliness
4. **MDD** - Major Depressive Disorder
5. **OCD** - Obsessive Compulsive Disorder
6. **PDD** - Persistent Depressive Disorder
7. **PTSD** - Post Traumatic Stress Disorder
8. **Anxiety** - Anxiety Disorder
9. **Bipolar** - Bipolar Disorder
10. **Eating Disorder** - Various eating disorders
11. **Psychotic Depression** - Depression with psychotic features
12. **Sleeping Disorder** - Sleep-related disorders
13. **Inconclusive** - Unable to determine specific condition

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.8 or higher
- pip (Python package installer)
- Git

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/mental-health-predictor.git
   cd mental-health-predictor
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure model file exists**
   - Make sure `mental_health_model-2.h5` is in the `model/` directory
   - If you don't have the model file, you'll need to train it first using the provided notebooks

## 🏃‍♂️ Running the Application

1. **Start the Flask application**
   ```bash
   python app.py
   ```

2. **Open your browser**
   ```
   http://localhost:5000
   ```

3. **Fill out the form** with the required 28 features and get your prediction!

## 📁 Project Structure

```
mental-health-predictor/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # Project documentation
├── app.log                        # Application logs
├── dataset/                       # Training data
│   ├── train_data.csv
│   └── val_data.csv
├── history/                       # Training history
│   └── mental_health_cnn_history.json
├── model/                         # Trained models
│   ├── mental_health_cnn_model.h5
│   └── mental_health_model-2.h5
├── static/                        # Static files (CSS, JS, images)
│   └── images/
│       └── favicon.png
├── templates/                     # HTML templates
│   ├── index.html                # Main form page
│   ├── result.html               # Results page
│   └── error.html                # Error page (optional)
├── notebooks/                     # Jupyter notebooks
│   ├── best_model.h5
│   ├── mental-health-cnn.ipynb
│   ├── mental-health-neural-network.ipynb
│   └── mental-health-preprocess.ipynb
└── test_model.h5                 # Test model file
```

## 🔧 API Usage

The application provides RESTful API endpoints:

### Predict Mental Health Condition

**Endpoint:** `POST /api/predict`

**Request Body:**
```json
{
  "features": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
}
```

**Response:**
```json
{
  "predicted_label": "Anxiety",
  "confidence": 85.6,
  "all_predictions": {
    "ADHD": 2.1,
    "ASD": 1.8,
    "Loneliness": 3.2,
    "MDD": 5.4,
    "OCD": 1.9,
    "PDD": 2.8,
    "PTSD": 4.1,
    "Anxiety": 85.6,
    "Bipolar": 1.2,
    "Eating Disorder": 0.8,
    "Psychotic Depression": 0.7,
    "Sleeping Disorder": 0.3,
    "Inconclusive": 0.1
  }
}
```

### Health Check

**Endpoint:** `GET /health`

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "timestamp": "2025-06-30T10:30:00"
}
```

## 📊 Model Information

- **Architecture**: Deep Neural Network
- **Framework**: TensorFlow/Keras
- **Input Features**: 28 numerical features
- **Output Classes**: 13 mental health conditions
- **Training Data**: Preprocessed mental health survey data

## 🛠️ Development

### Training the Model

1. Open `mental-health-preprocess.ipynb` to preprocess your data
2. Use `mental-health-neural-network.ipynb` or `mental-health-cnn.ipynb` to train models
3. Save the best model as `mental_health_model-2.h5` in the `model/` directory

### Adding New Features

1. Update the model architecture in the notebooks
2. Retrain with new features
3. Update `app.py` to handle additional input fields
4. Modify templates to include new form fields

## 📝 Requirements

Create a `requirements.txt` file with these dependencies:

```
Flask==2.3.2
tensorflow==2.13.0
numpy==1.24.3
matplotlib==3.7.1
seaborn==0.12.2
pandas==2.0.3
scikit-learn==1.3.0
```

## 🚨 Important Notes

- This application is for educational and research purposes only
- **DO NOT use for actual medical diagnosis**
- Always consult healthcare professionals for mental health concerns
- The model's predictions should be interpreted by qualified medical personnel

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👥 Authors

- **Adam Tampubolon** - *Initial work* - [YourGitHub](https://github.com/baniadamtampubolon)

## 🙏 Acknowledgments

- Thanks to the mental health research community
- TensorFlow and Flask communities
- Contributors to the mental health datasets used

## 📞 Support

If you have any questions or issues:

1. Check the [Issues](https://github.com/baniadamtampubolon/mental-health-predictor/issues) page
2. Create a new issue if your problem isn't already reported
3. Contact: baniadam.tampubolon@gmail.com

---

⚠️ **Disclaimer**: This tool is not a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.
