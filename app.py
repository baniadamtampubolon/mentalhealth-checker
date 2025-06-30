from flask import Flask, render_template, request, jsonify
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64
import os
import logging
from datetime import datetime
from tensorflow.keras.models import load_model

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

app = Flask(__name__)

# Global variables
model = None
MODEL_PATH = 'model/mental_health_model-2.h5'

# Labels tetap sama seperti sebelumnya
labels = {
    0: "ADHD",
    1: "ASD", 
    2: "Loneliness",
    3: "MDD",
    4: "OCD",
    5: "PDD",
    6: "PTSD",
    7: "Anxiety",
    8: "Bipolar",
    9: "Eating Disorder",
    10: "Psychotic Depression",
    11: "Sleeping Disorder",
    12: "Inconclusive"
}

def load_ml_model():
    """Load the machine learning model with error handling"""
    global model
    try:
        if os.path.exists(MODEL_PATH):
            model = load_model(MODEL_PATH)
            logging.info(f"Model loaded successfully from {MODEL_PATH}")
            return True
        else:
            logging.error(f"Model file not found at {MODEL_PATH}")
            # Fallback ke path dengan backslash
            fallback_path = 'model\\mental_health_model-2.h5'
            if os.path.exists(fallback_path):
                model = load_model(fallback_path)
                logging.info(f"Model loaded from fallback path: {fallback_path}")
                return True
            return False
    except Exception as e:
        logging.error(f"Error loading model: {str(e)}")
        return False

def validate_input_data(form_data):
    """Validate and process input data from form"""
    try:
        input_data = []
        for i in range(28):
            feature_name = f'feature{i}'
            value = form_data.get(feature_name)
            
            if value is None or value == '':
                raise ValueError(f"Missing or empty value for {feature_name}")
            
            # Convert to int with validation
            try:
                int_value = int(value)
                # Optional: Add range validation if needed
                # if int_value < 0 or int_value > 10:
                #     raise ValueError(f"Value for {feature_name} out of range")
                input_data.append(int_value)
            except ValueError:
                raise ValueError(f"Invalid value for {feature_name}: {value}")
        
        return np.array([input_data])
    except Exception as e:
        logging.error(f"Input validation error: {str(e)}")
        raise

def create_enhanced_plot(predicted_percentages):
    """Create an enhanced visualization plot"""
    try:
        # Set better style
        plt.style.use('seaborn-v0_8' if 'seaborn-v0_8' in plt.style.available else 'default')
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 8))
        
        # Get disorder names
        disorder_names = [labels[i] for i in range(len(predicted_percentages))]
        
        # Create color palette
        colors = plt.cm.Set3(np.linspace(0, 1, len(predicted_percentages)))
        
        # Create bar plot
        bars = ax.bar(disorder_names, predicted_percentages, 
                     color=colors, alpha=0.8, edgecolor='black', linewidth=0.5)
        
        # Customize plot
        ax.set_xlabel('Mental Health Disorders', fontsize=12, fontweight='bold')
        ax.set_ylabel('Prediction Percentage (%)', fontsize=12, fontweight='bold')
        ax.set_title('Mental Health Disorder Prediction Results', fontsize=14, fontweight='bold')
        
        # Rotate x-axis labels
        plt.xticks(rotation=45, ha='right')
        
        # Add grid for better readability
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        
        # Add percentage labels on bars
        for i, (bar, percentage) in enumerate(zip(bars, predicted_percentages)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                   f'{percentage:.1f}%', ha='center', va='bottom', 
                   fontweight='bold', fontsize=9)
        
        # Highlight the highest prediction
        max_idx = np.argmax(predicted_percentages)
        bars[max_idx].set_color('red')
        bars[max_idx].set_alpha(0.9)
        
        plt.tight_layout()
        
        # Convert to base64
        img = io.BytesIO()
        plt.savefig(img, format='png', dpi=150, bbox_inches='tight')
        plt.close()
        img.seek(0)
        plot_url = base64.b64encode(img.getvalue()).decode()
        
        return plot_url
    except Exception as e:
        logging.error(f"Error creating plot: {str(e)}")
        # Fallback to original simple plot
        return create_simple_plot(predicted_percentages)

def create_simple_plot(predicted_percentages):
    """Fallback simple plot creation"""
    img = io.BytesIO()
    disorder_names = [labels[i] for i in range(len(predicted_percentages))]
    
    plt.figure(figsize=(10, 6))
    plt.bar(disorder_names, predicted_percentages, color='skyblue')
    plt.xticks(rotation=45, ha='right')
    plt.xlabel('Disorders')
    plt.ylabel('Prediction Percentage (%)')
    plt.title('Prediction Percentage for Each Disorder')

    for i, percentage in enumerate(predicted_percentages):
        plt.text(i, percentage + 1, f'{percentage:.2f}%', ha='center')

    plt.tight_layout()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()
    
    return plot_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Check if model is loaded
            if model is None:
                logging.error("Model not loaded")
                return render_template('index.html', error="Model not loaded. Please contact administrator.")
            
            # Validate and get input data
            input_data = validate_input_data(request.form)
            
            # Make prediction
            start_time = datetime.now()
            prediction = model.predict(input_data)
            prediction_time = (datetime.now() - start_time).total_seconds()
            
            # Process prediction results
            predicted_label = labels[np.argmax(prediction)]
            predicted_percentages = (prediction[0] / prediction[0].sum()) * 100
            confidence = np.max(predicted_percentages)
            
            # Create enhanced plot
            try:
                plot_url = create_enhanced_plot(predicted_percentages)
            except Exception as e:
                logging.warning(f"Enhanced plot failed, using simple plot: {str(e)}")
                plot_url = create_simple_plot(predicted_percentages)
            
            # Log prediction
            logging.info(f"Prediction: {predicted_label} ({confidence:.2f}%) - Time: {prediction_time:.3f}s")
            
            # Return results (menggunakan parameter yang sama seperti sebelumnya)
            return render_template('result.html', 
                                 label=predicted_label, 
                                 plot_url=plot_url,
                                 confidence=confidence,
                                 prediction_time=prediction_time)
            
        except Exception as e:
            logging.error(f"Error during prediction: {str(e)}")
            return render_template('index.html', error=f"Error during prediction: {str(e)}")

    return render_template('index.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions (bonus feature)"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        data = request.get_json()
        if not data or 'features' not in data:
            return jsonify({'error': 'No features provided'}), 400
        
        if len(data['features']) != 28:
            return jsonify({'error': 'Expected 28 features'}), 400
        
        # Make prediction
        input_data = np.array([data['features']])
        prediction = model.predict(input_data)
        
        predicted_label = labels[np.argmax(prediction)]
        predicted_percentages = (prediction[0] / prediction[0].sum()) * 100
        
        return jsonify({
            'predicted_label': predicted_label,
            'confidence': float(np.max(predicted_percentages)),
            'all_predictions': {labels[i]: float(predicted_percentages[i]) for i in range(len(predicted_percentages))}
        })
        
    except Exception as e:
        logging.error(f"API prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'timestamp': datetime.now().isoformat()
    })

# Load model saat aplikasi dimulai
try:
    load_ml_model()
    if model is None:
        logging.warning("Model could not be loaded at startup")
except Exception as e:
    logging.error(f"Error during model loading at startup: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)