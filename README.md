Customer Churn Prediction using Machine Learning & Streamlit
Overview

This project is an end-to-end Machine Learning application that predicts whether a customer is likely to churn (leave a service) based on their demographic, service usage, and billing information.

The model is deployed as an interactive web application using Streamlit Cloud, making it easily accessible for real-time predictions.

🚀 Live Demo

👉 Deployed App: (https://customer-churn-prediction-xf9uobvp49mv4njxsdojxw.streamlit.app/)

🧠 Problem Statement

Customer churn is a major challenge for subscription-based businesses.
The goal of this project is to:

Predict customer churn in advance

Help businesses take proactive retention actions

🛠️ Tech Stack

Programming Language: Python

Machine Learning: Scikit-learn

Model Used: Logistic Regression

Data Processing: Pandas, NumPy

Model Deployment: Streamlit Cloud

Version Control: Git & GitHub

Containerization: Docker 

📂 Project Structure
Customer_Churn_Prediction/
│
├── lg_app.py                 # Streamlit application
├── requirements.txt          # Python dependencies
├── Dockerfile                # Docker configuration
├── .dockerignore             # Docker ignore rules
├── Customer Churn Prediction using Logistic Regression    # Main Jupyter file
├── models/
│   └── logistic_Churn.pkl    # Trained ML model + scaler
└── README.md                 # Project documentation

📊 Dataset Description

Dataset Link: https://www.kaggle.com/datasets/rashadrmammadov/customer-churn-dataset

The dataset contains customer-level information such as:

Gender

Senior Citizen status

Partner & Dependents

Tenure

Phone & Internet Services

Contract type

Monthly & Total Charges

Churn (Target Variable)

⚙️ Machine Learning Workflow

Data Cleaning

Removed irrelevant columns

Handled missing values

Feature Encoding

Categorical variables encoded using Label Encoding

Feature Scaling

StandardScaler applied to numerical features

Model Training

Logistic Regression trained on 11 features

Model Serialization

Model and scaler saved using pickle

Deployment

Integrated with Streamlit for real-time inference

🧪 Model Performance

Evaluation Metric: Accuracy

Model chosen for:

Interpretability

Fast inference

Production suitability

🖥️ Application Features

Interactive user input form

Real-time churn prediction

Displays:

Churn or Not Churn

Actionable retention tips

Cloud-hosted and accessible via browser

🐳 Docker Support

The application can also be run using Docker:

docker build -t churn-app .
docker run -p 8501:8501 churn-app

▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/<your-username>/Customer-Churn-Prediction.git
cd Customer_Churn_Prediction

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app
streamlit run lg_app.py

🧠 Key Learnings

Importance of consistent preprocessing between training and inference

Handling feature mismatch errors in deployment

Using robust file paths for cloud environments

End-to-end ML lifecycle: training → serialization → deployment

👤 Author

Arpit Kumar
Aspiring Data Scientist | Machine Learning | Deep Learning
