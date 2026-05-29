# ============================================================================
# FLASK API BACKEND - Connect ML Models to Website
# Save this as: app.py
# ============================================================================

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import joblib

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# ============================================================================
# LOAD ALL MODELS AND DATA
# ============================================================================

# print("Loading models...")

# try:
#     # Load best model (from your training code)
#     best_model = joblib.load('best_model.pkl')
#     print("✅ Best model loaded")
# except:
#     print("⚠️ best_model.pkl not found, trying alternative...")
#     try:
#         best_model = pickle.load(open('rf_model.pkl', 'rb'))
#         print("✅ Random Forest model loaded as fallback")
#     except:
#         print("❌ No model found!")
#         best_model = None

# try:
#     # Load label encoder
#     label_encoder = pickle.load(open('disease_encoder.pkl', 'rb'))
#     print("✅ Label encoder loaded")
# except:
#     try:
#         label_encoder = pickle.load(open('label_encoder.pkl', 'rb'))
#         print("✅ Alternative label encoder loaded")
#     except:
#         print("❌ No label encoder found!")
#         label_encoder = None

import os, traceback

print("Loading models...")
print("➡ CWD:", os.getcwd())
print("➡ Files here:", os.listdir("."))

# ---------- Load best_model.pkl ----------
best_model = None
try:
    best_model = joblib.load('best_model.pkl')
    print("✅ Best model loaded from best_model.pkl")
except Exception as e:
    print("❌ Failed to load best_model.pkl")
    print("   Error type:", type(e).__name__)
    print("   Error:", e)
    traceback.print_exc()

# ---------- Load disease_encoder.pkl ----------
label_encoder = None
try:
    with open('disease_encoder.pkl', 'rb') as f:
        label_encoder = pickle.load(f)
    print("✅ Label encoder loaded from disease_encoder.pkl")
except Exception as e:
    print("❌ Failed to load disease_encoder.pkl")
    print("   Error type:", type(e).__name__)
    print("   Error:", e)
    traceback.print_exc()
# ============================================================================
try:
    # Load medicine database
    medicine_db = pickle.load(open('medicine_database.pkl', 'rb'))
    print("✅ Medicine database loaded")
except:
    print("⚠️ Creating default medicine database...")
    medicine_db = {
        'Influenza': {
            'medicines': [
                '💊 Oseltamivir (Tamiflu) 75mg - Take twice daily for 5 days',
                '💊 Acetaminophen 500mg - Every 6 hours for fever',
                '💊 Ibuprofen 400mg - Every 8 hours for body aches',
                '💧 Increase fluid intake to 8-10 glasses daily'
            ],
            'advice': [
                '🛏️ REST: Get 8-10 hours of sleep per night',
                '💧 HYDRATION: Drink at least 8-10 glasses of water daily',
                '🏠 ISOLATION: Stay home for 7 days',
                '🤧 HYGIENE: Cover mouth when coughing',
                '🌡️ MONITOR: Check temperature twice daily',
                '📞 SEEK HELP: If difficulty breathing develops'
            ]
        }
    }

print("\n🎉 Backend ready!\n")

# ============================================================================
# MEDICINE DATABASE (Comprehensive)
# ============================================================================

COMPLETE_MEDICINE_DB = {
    'Influenza': {
        'medicines': [
            '💊 Oseltamivir (Tamiflu) 75mg - Twice daily for 5 days',
            '💊 Acetaminophen 500mg - Every 6 hours for fever',
            '💊 Ibuprofen 400mg - Every 8 hours for body aches',
            '💧 Plenty of fluids - 8-10 glasses daily'
        ],
        'advice': [
            '🛏️ REST: Get 8-10 hours of sleep',
            '💧 HYDRATION: Drink water, juice, warm liquids',
            '🏠 ISOLATION: Stay home for 7-10 days',
            '🤧 HYGIENE: Cover mouth, wash hands frequently',
            '🌡️ MONITOR: Check temperature twice daily',
            '📞 SEEK HELP: If breathing difficulty or chest pain'
        ]
    },
    'Asthma': {
        'medicines': [
            '💨 Albuterol Inhaler - 2 puffs every 4-6 hours as needed',
            '💨 Fluticasone 110mcg - 2 puffs twice daily',
            '💊 Montelukast 10mg - Once daily at bedtime',
            '🆘 Emergency rescue inhaler always accessible'
        ],
        'advice': [
            '🚭 AVOID: Smoke, dust, pollen, cold air',
            '💨 BREATHING: Practice breathing exercises',
            '🏃 EXERCISE: Moderate with proper warm-up',
            '📊 MONITOR: Keep peak flow readings',
            '🆘 EMERGENCY: Use rescue inhaler, call 911',
            '💊 COMPLIANCE: Never skip medications'
        ]
    },
    'Diabetes': {
        'medicines': [
            '💊 Metformin 500mg - Twice daily with meals',
            '💉 Insulin (if prescribed) - Per schedule',
            '📊 Blood glucose test strips',
            '🍬 Glucose tablets for emergencies'
        ],
        'advice': [
            '🍽️ DIET: Low carb, high fiber meals',
            '🏃 EXERCISE: 30 minutes daily',
            '📊 MONITORING: Test 3-4 times daily',
            '👣 FOOT CARE: Inspect daily',
            '💉 INSULIN: Store properly, rotate sites',
            '🚨 HYPOGLYCEMIA: Treat immediately'
        ]
    },
    'Hypertension': {
        'medicines': [
            '💊 Lisinopril 10mg - Once daily morning',
            '💊 Amlodipine 5mg - Once daily',
            '💊 Losartan 50mg - Once daily',
            '🧂 Low sodium diet (<1500mg/day)'
        ],
        'advice': [
            '🧂 DIET: Drastically limit salt',
            '🏃 EXERCISE: 30-45 minutes daily',
            '📈 MONITOR: Check BP daily',
            '😌 STRESS: Meditation, yoga',
            '⚖️ WEIGHT: Lose 5-10% if overweight',
            '🚫 AVOID: Alcohol, smoking, caffeine'
        ]
    },
    'Pneumonia': {
        'medicines': [
            '💊 Amoxicillin 500mg - Three times daily 7-10 days',
            '💊 Azithromycin 500mg - Once daily 5 days',
            '💊 Acetaminophen for fever',
            '💨 Oxygen therapy if O2 < 92%'
        ],
        'advice': [
            '💊 ANTIBIOTICS: Complete FULL course',
            '💧 FLUIDS: Warm liquids continuously',
            '🛏️ REST: Bed rest 1-2 weeks',
            '🌡️ MONITOR: Temp, breathing, O2',
            '🚨 EMERGENCY: Worsening breathing',
            '🔄 FOLLOW-UP: X-ray after 6 weeks'
        ]
    },
    'Common Cold': {
        'medicines': [
            '💊 Acetaminophen 500mg - Every 6 hours',
            '💊 Pseudoephedrine 30mg - Every 6 hours',
            '💊 Vitamin C 1000mg - Once daily',
            '🍯 Honey with warm lemon water'
        ],
        'advice': [
            '💧 HYDRATION: Warm liquids',
            '🛏️ REST: Extra sleep',
            '🤧 HYGIENE: Wash hands frequently',
            '🏠 STAY HOME: Avoid spreading',
            '🍯 HONEY: Natural cough suppressant',
            '⏱️ DURATION: Resolves in 7-10 days'
        ]
    },
    'Bronchitis': {
        'medicines': [
            '💨 Albuterol inhaler - 2 puffs every 4-6 hrs',
            '💊 Prednisone 20mg - Once daily 5 days',
            '💊 Dextromethorphan cough syrup',
            '💧 Warm mist humidifier'
        ],
        'advice': [
            '💨 HUMIDITY: Use humidifier 24/7',
            '☕ WARM DRINKS: Tea with honey',
            '🚭 AVOID: Smoking, all irritants',
            '🛏️ REST: No strenuous activity',
            '🌡️ MONITOR: Fever >3 days see doctor',
            '⏱️ COUGH: May last 2-3 weeks'
        ]
    },
    'Depression': {
        'medicines': [
            '💊 Sertraline (Zoloft) 50mg - Once daily',
            '💊 Fluoxetine (Prozac) 20mg - Morning',
            '🧠 Cognitive Behavioral Therapy weekly',
            '🏃 Exercise 30 minutes daily'
        ],
        'advice': [
            '🧠 THERAPY: Weekly counseling essential',
            '👥 SUPPORT: Join support group',
            '🏃 EXERCISE: Daily activity crucial',
            '😴 SLEEP: Regular 7-8 hour schedule',
            '🍽️ NUTRITION: Balanced meals',
            '⚠️ CRISIS: Call 988 if needed'
        ]
    },
    'Stroke': {
        'medicines': [
            '🚨 CALL 911 IMMEDIATELY',
            '💊 Aspirin 325mg - CHEW ONE now',
            '💉 tPA - Hospital only, <4.5 hours',
            '💊 BP medications - Hospital'
        ],
        'advice': [
            '🚨 EMERGENCY: Life-threatening',
            '⏱️ TIME CRITICAL: Minutes matter',
            '📱 FAST: Face, Arm, Speech, Time',
            '🏥 HOSPITAL: Immediate care',
            '🚫 DO NOT: Give food/water',
            '🔄 RECOVERY: Rehab required'
        ]
    },
    'Anxiety Disorders': {
        'medicines': [
            '💊 Sertraline 50mg - Once daily',
            '💊 Buspirone 10mg - Twice daily',
            '💊 Alprazolam 0.25mg - As needed',
            '🧘 CBT therapy weekly'
        ],
        'advice': [
            '🧘 RELAXATION: Deep breathing 3x daily',
            '☕ LIMIT: Reduce caffeine, alcohol',
            '😴 SLEEP: 7-8 hours nightly',
            '📱 APPS: Use Calm, Headspace',
            '🏃 EXERCISE: Regular activity',
            '💬 THERAPY: CBT most effective'
        ]
    }
}

# ============================================================================
# API ENDPOINTS
# ============================================================================

@app.route('/')
def home():
    return render_template('index.html')
    # """Serve the main page"""
    # return """
    # <html>
    #     <head><title>MediCare AI API</title></head>
    #     <body style="font-family: Arial; padding: 40px; background: #f5f5f5;">
    #         <h1 style="color: #0066FF;">🏥 MediCare AI - Backend API</h1>
    #         <p style="font-size: 18px;">Backend is running successfully!</p>
    #         <h3>Available Endpoints:</h3>
    #         <ul style="font-size: 16px;">
    #             <li><code>POST /predict</code> - Disease prediction</li>
    #             <li><code>GET /health</code> - Health check</li>
    #             <li><code>GET /models</code> - List loaded models</li>
    #         </ul>
    #         <p>Frontend URL: Open <code>index.html</code> in browser</p>
    #     </body>
    # </html>
    # """
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': best_model is not None,
        'encoder_loaded': label_encoder is not None,
        'message': 'Backend is running!'
    })

@app.route('/models', methods=['GET'])
def list_models():
    """List available models"""
    return jsonify({
        'available_models': ['rf', 'gb', 'lr'],
        'current_model': 'best_model',
        'diseases_count': len(label_encoder.classes_) if label_encoder else 0
    })

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    """Main prediction endpoint"""
    
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return jsonify({'status': 'ok'}), 200
    
    try:
        # Get data from request
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided',
                'message': 'Please send JSON data'
            }), 400
        
        print("\n" + "="*60)
        print("📥 Received prediction request")
        print("="*60)
        print("Data:", data)
        
        # Extract features with defaults
        fever = int(data.get('fever', 0))
        cough = int(data.get('cough', 0))
        fatigue = int(data.get('fatigue', 0))
        difficulty_breathing = int(data.get('breathing', 0))
        age = int(data.get('age', 30))
        gender = int(data.get('gender', 0))
        blood_pressure = int(data.get('bloodPressure', 1))
        cholesterol = int(data.get('cholesterol', 1))
        model_choice = data.get('model', 'rf')
        
        print(f"\n👤 Patient: Age {age}, Gender {'M' if gender else 'F'}")
        print(f"🔬 Symptoms: Fever={fever}, Cough={cough}, Fatigue={fatigue}, Breathing={difficulty_breathing}")
        
        # Check if model is loaded
        if best_model is None:
            return jsonify({
                'success': False,
                'error': 'Model not loaded',
                'message': 'ML model files not found. Please ensure .pkl files are in the correct location.'
            }), 500
        
        # Prepare input for prediction
        input_dict = {
            'fever': [fever],
            'cough': [cough],
            'fatigue': [fatigue],
            'difficulty_breathing': [difficulty_breathing],
            'age': [age],
            'gender': ['male' if gender == 1 else 'female'],
            'blood_pressure': [blood_pressure],
            'cholesterol_level': [cholesterol]
        }
        
        input_df = pd.DataFrame(input_dict)
        # 👇 FIX MISSING TRAINING COLUMNS (PATCH)
        if "age_scaled" not in input_df.columns:
             input_df["age_scaled"] = input_df["age"]

        if "bp_scaled" not in input_df.columns:
            input_df["bp_scaled"] = input_df["blood_pressure"]

        if "chol_scaled" not in input_df.columns:
          input_df["chol_scaled"] = input_df["cholesterol_level"]

        if "outcome_variable" not in input_df.columns:
            input_df["outcome_variable"] = 0

        if "risk_level" not in input_df.columns:
            input_df["risk_level"] = 0

        print("📊 Input DataFrame columns:", list(input_df.columns))
        print("📊 Shape after patch:", input_df.shape)
        
        print(f"📊 Input DataFrame shape: {input_df.shape}")
        
        # Make prediction
        prediction = best_model.predict(input_df)[0]
        probabilities = best_model.predict_proba(input_df)[0]
        
        # Get disease name
        predicted_disease = label_encoder.classes_[prediction]
        main_confidence = float(probabilities[prediction] * 100)
        
        print(f"✅ Prediction: {predicted_disease} ({main_confidence:.1f}%)")
        
        # Get top 5 predictions
        top_5_idx = np.argsort(probabilities)[-5:][::-1]
        top_5_predictions = []
        
        for idx in top_5_idx:
            disease_name = label_encoder.classes_[idx]
            confidence = float(probabilities[idx] * 100)
            top_5_predictions.append({
                'disease': disease_name,
                'confidence': round(confidence, 2)
            })
        
        # Calculate risk level
        symptom_count = fever + cough + fatigue + difficulty_breathing
        if symptom_count >= 3 and (age > 60 or blood_pressure == 2):
            risk_level = "high"
        elif symptom_count >= 2:
            risk_level = "medium"
        else:
            risk_level = "low"
        
        print(f"⚠️  Risk Level: {risk_level.upper()}")
        
        # Get treatment info
        treatment = COMPLETE_MEDICINE_DB.get(predicted_disease, {
            'medicines': ['⚕️ Consult doctor for specific treatment'],
            'advice': ['📞 Schedule appointment with healthcare provider']
        })
        
        # Return response
        response = {
            'success': True,
            'disease': predicted_disease,
            'confidence': round(main_confidence, 2),
            'risk': risk_level,
            'top5': top_5_predictions,
            'medicines': treatment.get('medicines', []),
            'advice': treatment.get('advice', []),
            'model_used': model_choice,
            'timestamp': pd.Timestamp.now().isoformat()
        }
        
        print(f"📤 Sending response")
        print("="*60 + "\n")
        
        return jsonify(response), 200
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Prediction failed. Check server logs for details.'
        }), 500

# ============================================================================
# RUN SERVER
# ============================================================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🏥 MEDICARE AI - BACKEND SERVER")
    print("="*60)
    print("\n✅ Server starting...")
    print("📡 API will be available at: http://localhost:5000")
    print("🌐 Frontend should connect to: http://localhost:5000/predict")
    print("\n💡 To test: Send POST request to /predict endpoint")
    print("="*60 + "\n")
    
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
