<div align="center">

<!-- BANNER -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=220&section=header&text=Health%20AI%20Recommender&fontSize=50&fontColor=ffffff&animation=twinkling&fontAlignY=36&desc=AI-Powered%20Personalized%20Healthcare%20Recommendation%20System&descSize=18&descAlignY=62&descColor=c8d6e5" width="100%" alt="Banner" />

<br/>

<!-- TECH STACK BADGES -->
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.x-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=for-the-badge&logo=pandas&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

<br/>

<!-- STATUS BADGES -->
![Status](https://img.shields.io/badge/Status-Active-success?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)
![Contributions](https://img.shields.io/badge/Contributions-Open-orange?style=flat-square)
![ML Powered](https://img.shields.io/badge/ML-Powered-blueviolet?style=flat-square&logo=tensorflow)
![Healthcare](https://img.shields.io/badge/Domain-Healthcare%20AI-red?style=flat-square&logo=heart)

<br/><br/>

> **An intelligent, AI-driven healthcare platform that predicts diseases from user-reported symptoms and delivers fully personalized recommendations — covering medicines, dietary guidance, precautionary measures, and treatment pathways — through a clean, responsive web interface built on a production-grade Flask backend.**

<br/>

[🚀 Deployment Guide](#-deployment) · [📖 Installation](#-installation--setup) · [🐛 Report Bug](../../issues) · [✨ Request Feature](../../issues)

</div>

---

## 📌 Table of Contents

- [🧠 Overview](#-overview)
- [✨ Key Features](#-key-features)
- [🏗️ System Architecture](#-system-architecture)
- [🤖 Machine Learning Pipeline](#-machine-learning-pipeline)
- [📁 Project Structure](#-project-structure)
- [🛠️ Technology Stack](#-technology-stack)
- [⚙️ Installation & Setup](#-installation--setup)
- [🚀 Deployment](#-deployment)
- [💡 Application Highlights](#-application-highlights)
- [📊 Model Performance](#-model-performance)
- [🔮 Future Enhancements](#-future-enhancements)
- [🎓 Learning Outcomes](#-learning-outcomes)
- [🤝 Contributing](#-contributing)
- [👤 Author](#-author)
- [📄 License](#-license)

---

## 🧠 Overview

The **Personalized Health Care Recommendation System** is a full-stack, AI-powered web application engineered to bridge the gap between symptom recognition and actionable medical guidance. Developed with a Python/Flask backend and a responsive HTML/CSS/JavaScript frontend, the system employs trained Scikit-Learn machine learning classifiers to analyze user-reported symptoms and generate accurate, real-time disease predictions accompanied by calibrated confidence scores.

What sets this system apart from simple prediction tools is its end-to-end **health advisory engine** — upon predicting a condition, the system queries a structured medicine database to surface relevant drug recommendations, nutritional guidance, lifestyle precautions, and treatment direction, all tailored to the predicted diagnosis.

This project is architected to reflect the standards of production-grade health-tech platforms and serves as a comprehensive demonstration of applied machine learning, RESTful backend development, data engineering, and responsive UI design — skills directly aligned with roles in data engineering, ML engineering, and full-stack AI development.

> ⚕️ **Medical Disclaimer:** This system is developed strictly for educational, research, and portfolio demonstration purposes. It is not intended to replace professional medical advice, clinical diagnosis, or treatment. Always consult a licensed healthcare provider for any health-related concerns.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔬 **Disease Prediction** | Predicts the most probable disease from a set of user-selected symptoms using a trained and serialized ML classifier |
| 💊 **Medicine Recommendations** | Surfaces appropriate medicines and treatment options via a curated, structured medicine database keyed to predicted conditions |
| 🥗 **Personalized Diet Suggestions** | Delivers targeted dietary guidance designed to support recovery, prevention, and overall health management |
| 🛡️ **Precaution & Lifestyle Guidance** | Provides clinically-informed precautionary steps and lifestyle modifications for each predicted condition |
| 📈 **Confidence Score Analysis** | Exposes model prediction probabilities using `predict_proba()`, enabling transparent and interpretable diagnostic output |
| 🤖 **Multi-Model Training & Selection** | Trains, benchmarks, and compares multiple ML classifiers — automatically selecting and persisting the best-performing model |
| ⚡ **Real-Time Inference** | Delivers low-latency predictions via Flask REST API, enabling seamless real-time user interaction |
| 📱 **Responsive Web Interface** | Fully responsive UI built with HTML5, CSS3, and JavaScript, ensuring a consistent experience across desktop and mobile |
| 🧩 **Modular, Scalable Architecture** | Clean separation of ML, backend, and frontend layers designed for maintainability, testability, and future extension |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER INTERFACE                          │
│          (HTML5 + CSS3 + JavaScript — Responsive Web App)      │
└──────────────────────────┬──────────────────────────────────────┘
                           │  HTTP POST Request — Symptoms Payload (JSON)
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                  FLASK BACKEND  ·  WEB Code/app.py             │
│        Route Handling · Input Validation · Response Builder    │
└──────────────────────────┬──────────────────────────────────────┘
                           │  Model Inference Layer
           ┌───────────────┼────────────────────────┐
           ▼               ▼                        ▼
┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐
│   ML Classifier  │  │  Disease Encoder │  │   Medicine Database  │
│  best_model.pkl  │  │ disease_encoder  │  │  medicine_database   │
│  (Scikit-Learn)  │  │     .pkl         │  │       .pkl           │
│                  │  │ (LabelEncoder)   │  │  (Recommendation     │
│  predict_proba() │  │                  │  │     Engine)          │
└──────┬───────────┘  └────────┬─────────┘  └──────────┬───────────┘
       │                       │                        │
       └───────────────────────▼────────────────────────┘
                               │
                  ┌────────────▼───────────┐
                  │     Response Payload   │
                  │  ·  Predicted Disease  │
                  │  ·  Confidence Score % │
                  │  ·  Medicines          │
                  │  ·  Diet Plan          │
                  │  ·  Precautions        │
                  │  ·  Treatment Guidance │
                  └────────────────────────┘
```

---

## 🤖 Machine Learning Pipeline

This project implements a rigorous, end-to-end ML pipeline from raw data ingestion through to serialized model deployment — mirroring industry-standard MLOps workflows.

### 1. 📥 Data Collection & Preprocessing
- Symptom-disease datasets ingested and cleaned using **Pandas**
- Systematic handling of missing values, duplicate records, and label inconsistencies
- Binary multi-hot encoding of symptom features to produce model-ready input vectors

### 2. 🔧 Feature Engineering
- Multi-label symptom vectorization to represent symptom combinations accurately
- Target variable encoded using Scikit-Learn's **LabelEncoder**, persisted as `disease_encoder.pkl` for consistent inference-time decoding
- Stratified train/test splitting to maintain class distribution across data subsets

### 3. 🧪 Model Training & Comparative Evaluation

Multiple supervised classifiers are trained and rigorously benchmarked to identify the strongest performer for this symptom-disease classification task:

| Algorithm | Key Characteristic |
|---|---|
| **Random Forest Classifier** | Ensemble method; robust against overfitting, handles high-dimensional symptom vectors effectively |
| **Decision Tree Classifier** | Highly interpretable; exposes clear symptom-to-disease decision logic |
| **Support Vector Machine (SVM)** | Strong generalization in high-dimensional feature spaces |
| **K-Nearest Neighbors (KNN)** | Non-parametric baseline; useful for evaluating instance-based learning |
| **Naive Bayes** | Probabilistic classifier; computationally efficient with strong baseline performance |

### 4. 🏆 Automated Model Selection & Serialization
- All models evaluated against **Accuracy**, **Precision**, **Recall**, and **F1-Score** on the held-out test set
- The best-performing classifier is serialized to `Models/best_model.pkl` via **Joblib** for production inference
- Confidence scores surfaced through `predict_proba()` provide transparent, interpretable diagnostic output

### 5. 💊 Recommendation Engine
- Predicted class label decoded from integer encoding using `Models/disease_encoder.pkl`
- Decoded disease name used as a lookup key against `Models/medicine_database.pkl` — a structured mapping of conditions to medicines, diet plans, precautions, and treatment guidance
- Lookup results packaged into a JSON response and rendered dynamically on the frontend

---

## 📁 Project Structure

```
Personalized-HealthCare-Recommendation-System/
│
├── 📂 Models/
│   ├── best_model.pkl               # Serialized best-performing ML classifier
│   ├── disease_encoder.pkl          # LabelEncoder for disease class decoding
│   └── medicine_database.pkl        # Structured disease-to-recommendation mapping
│
├── 📂 WEB Code/
│   ├── app.py                       # Flask application — routes, inference logic, API
│   ├── 📂 templates/
│   │   └── index.html               # Jinja2 HTML template — main application view
│   └── 📂 static/
│       ├── css/
│       │   └── style.css            # Custom stylesheet — layout, theme, responsiveness
│       └── js/
│           └── script.js            # Client-side logic — API calls, DOM interactions
│
├── 📂 data/
│   └── (Symptom-disease training datasets — CSV format)
│
├── requirements.txt                 # Python package dependencies
├── .gitignore                       # Git exclusion rules
└── README.md                        # Project documentation
```

---

## 🛠️ Technology Stack

<div align="center">

| Layer | Technology | Role |
|---|---|---|
| **Core Language** | Python 3.10+ | Application logic, data processing, and ML pipeline |
| **Web Framework** | Flask | RESTful API backend, routing, and server-side rendering |
| **ML Framework** | Scikit-Learn | Classifier training, evaluation, and serialized inference |
| **Data Engineering** | Pandas, NumPy | Dataset loading, preprocessing, and feature engineering |
| **Model Persistence** | Joblib | Efficient serialization and deserialization of trained models |
| **Frontend** | HTML5, CSS3, JavaScript (ES6+) | Responsive, interactive user interface |
| **Templating Engine** | Jinja2 | Dynamic HTML generation via Flask |

</div>

---

## ⚙️ Installation & Setup

### Prerequisites

Ensure the following are available on your system before proceeding:
- Python **3.9 or higher**
- `pip` — Python package manager
- `git` — Version control

### Step 1 — Clone the Repository

```bash
git clone https://github.com/samyakGIT-cloud/Personalized-HealthCare-Recommendation-System.git
cd Personalized-HealthCare-Recommendation-System
```

### Step 2 — Create & Activate a Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

**Core packages in `requirements.txt`:**

```
flask>=2.3.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
gunicorn>=21.0.0
```

### Step 4 — Launch the Application

```bash
cd "WEB Code"
python app.py
```

Navigate to **`http://127.0.0.1:5000`** in your browser to access the application.

---

## 🚀 Deployment

### Option A — Render *(Recommended — Free Tier Available)*

1. Push the repository to GitHub.
2. Visit [render.com](https://render.com) → **New Web Service** → connect your repository.
3. Configure the service:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn "WEB Code.app:app" --bind 0.0.0.0:10000`
   - **Environment:** Python 3
4. Click **Deploy**. Render will build and serve the application automatically.

### Option B — Railway

```bash
# Install Railway CLI
npm install -g @railway/cli

# Authenticate and initialize
railway login
railway init

# Deploy
railway up
```

### Option C — Linux VPS (DigitalOcean / AWS EC2 / Linode)

```bash
# Install Gunicorn
pip install gunicorn

# Navigate to the app directory
cd "WEB Code"

# Start with Gunicorn — production WSGI server
gunicorn --bind 0.0.0.0:8000 --workers 4 app:app

# Optional: configure NGINX as a reverse proxy
sudo apt install nginx
# Add a server block in /etc/nginx/sites-available/healthai
```

### Option D — Docker Container

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "WEB Code/app:app"]
```

```bash
# Build the image
docker build -t healthai-recommender .

# Run the container
docker run -p 5000:5000 healthai-recommender
```

---

## 💡 Application Highlights

The web interface is designed for clarity, accessibility, and a guided user experience — making complex ML inference approachable for non-technical users.

**Symptom Selection Interface**
A structured, intuitive input panel allows users to select from a comprehensive list of recognized symptoms. The interface is built to minimize friction and guide users through the input process step by step.

**Real-Time Prediction Display**
Upon submission, the system invokes the Flask inference endpoint and renders the predicted disease name alongside a confidence score — giving users a transparent view of the model's diagnostic certainty.

**Comprehensive Recommendation Panel**
The results view presents a complete healthcare recommendation card: prescribed medicines, dietary suggestions tailored to the condition, a list of precautionary measures, and general treatment guidance — all organized for easy reading.

**Responsive & Mobile-Friendly Design**
The UI adapts gracefully across screen sizes, from desktop browsers to mobile devices, ensuring the application is accessible and functional in any context.

**Lightweight & Fast**
Built on a minimal Flask backend with pre-loaded serialized models, the application delivers near-instant predictions with minimal server overhead — no database queries required for inference.

---

## 📊 Model Performance

The system trains and evaluates multiple classifiers — including Random Forest, Decision Tree, SVM, KNN, and Naive Bayes — and automatically selects the best-performing model based on cross-validated metrics.

> **Note:** Specific accuracy, precision, recall, and F1-score values are intentionally not listed here, as performance metrics are highly dependent on dataset quality, class distribution, feature engineering methodology, and training configuration. Evaluation results can be reproduced by running the training pipeline against your dataset and reviewing the generated classification reports.

To evaluate model performance locally, run the training script and inspect the output:

```bash
# Example — run from the project root
python train_models.py
```

Metrics for each classifier will be printed to the console and can be logged to a file for comparison.

---

## 🔮 Future Enhancements

- [ ] 🔐 **User Authentication & Profiles** — Secure login system with personalized health history tracking
- [ ] 🗄️ **Persistent Database Layer** — PostgreSQL or MongoDB integration for storing user queries and recommendation logs
- [ ] 🌐 **Multi-Language Support** — Internationalized UI to serve a broader, more diverse user base
- [ ] 🩺 **NLP-Powered Symptom Search** — Natural language symptom input with autocomplete and spell correction
- [ ] 📊 **Admin Analytics Dashboard** — Real-time monitoring of prediction trends, model usage metrics, and potential data drift
- [ ] 📱 **Cross-Platform Mobile App** — React Native or Flutter application for on-the-go health guidance
- [ ] 🤝 **Telemedicine API Integration** — Direct referral links to licensed healthcare professionals based on prediction
- [ ] 🔄 **Automated MLOps Retraining Pipeline** — Scheduled model retraining on refreshed data with performance regression checks
- [ ] 🧬 **Deep Learning Enhancement** — Neural network-based symptom encoder (e.g., MLP or Transformer) for improved classification
- [ ] 📋 **Exportable Health Summary Report** — Downloadable PDF summarizing the prediction and all associated recommendations

---

## 🎓 Learning Outcomes

This project develops and demonstrates the following industry-aligned, career-ready competencies:

**Machine Learning & Data Science**
- Designed and implemented a complete ML pipeline: data ingestion → preprocessing → feature engineering → multi-model training → evaluation → serialization → inference
- Applied multi-model comparative evaluation using Accuracy, Precision, Recall, and F1-Score to drive data-informed model selection
- Gained hands-on proficiency with Scikit-Learn, Pandas, NumPy, and Joblib in an applied, production-style context

**Backend & API Engineering**
- Built a RESTful API using Flask, handling request parsing, model inference orchestration, and structured JSON response construction
- Integrated serialized ML artifacts into a live web backend for real-time, stateless prediction serving
- Managed application routing, error handling, and server-side rendering with Jinja2 templates

**Frontend Development**
- Constructed an interactive, responsive UI using semantic HTML5, modern CSS3, and vanilla JavaScript (ES6+)
- Implemented asynchronous API communication and real-time DOM updates to deliver a seamless user experience
- Applied responsive design principles to ensure cross-device compatibility

**Data Engineering Fundamentals**
- Processed and transformed raw symptom-disease datasets into model-ready feature matrices
- Designed a structured recommendation lookup database (`medicine_database.pkl`) mapping disease predictions to actionable healthcare guidance
- Applied label encoding and binary vectorization strategies suited to multi-class classification

**Software Engineering Practices**
- Maintained a modular project structure with clear separation of ML, backend, and frontend concerns
- Practiced Git-based version control with meaningful, conventional commit messages
- Configured and deployed the application to cloud platforms using Gunicorn and Docker

---

## 🤝 Contributing

Contributions are genuinely welcome and help improve the quality and reach of this project. Whether you're fixing a bug, improving documentation, or proposing a new feature — your input is valued.

### How to Contribute

1. **Fork** this repository
2. **Create** a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit** your changes with a descriptive message:
   ```bash
   git commit -m "feat: describe what your change does"
   ```
4. **Push** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Open a Pull Request** — describe your changes and link any relevant issues

### Code Standards

- Follow [PEP 8](https://pep8.org/) conventions for all Python code
- Use [Conventional Commits](https://www.conventionalcommits.org/) for commit message formatting
- Include docstrings for all new functions and classes
- Update `README.md` if your changes affect setup, structure, or usage
- Verify that existing functionality is not broken before submitting a PR

### Reporting Issues

To report a bug or request a feature, [open an issue](../../issues) and include:
- A clear, descriptive title
- Detailed reproduction steps (for bugs)
- Expected vs. actual behavior
- Relevant screenshots or error logs where applicable

---

## 👤 Author

<div align="center">

### Samyak Kamble

*Data Engineering Enthusiast*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-samyakGIT--cloud-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/samyakGIT-cloud)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/samyak-kamble)
[![Portfolio](https://img.shields.io/badge/Portfolio-Visit-FF5722?style=for-the-badge&logo=google-chrome&logoColor=white)](https://samyakkamble.dev)
[![Email](https://img.shields.io/badge/Email-Contact-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:samyak@example.com)

<br/>

> *"Building intelligent systems at the intersection of data, machine learning, and real-world impact."*

</div>

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for full terms.

```
MIT License — Free to use, modify, and distribute with appropriate attribution.
```

---

<div align="center">

### ⭐ Found this project valuable?

**Star the repository to help others discover it and support open-source ML in healthcare.**

<br/>

*Built with precision and purpose by [Samyak Kamble](https://github.com/samyakGIT-cloud)*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%" alt="Footer" />

</div>
