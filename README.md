AI Banking Intelligence System

AI-powered decision-support system for modern banking operations.
This project integrates Machine Learning models into a working web application to assist banks in loan approval, loan amount prediction, and fraud detection.

Project Overview

The AI Banking Intelligence System is a web-based application that helps financial institutions make faster and smarter decisions using Artificial Intelligence.

It supports:

Loan Approval Prediction (Classification)

Loan Amount Prediction (Regression)

Fraud Detection (Clustering)

Bulk CSV File Processing for large-scale banking data

This system is designed as a decision-support tool, not a replacement for human banking professionals.

Problem Statement

Traditional banking systems face several operational challenges:

Manual loan verification is time-consuming

Fixed rule-based systems lack adaptability

Increasing digital transactions lead to rising fraud risks

Bulk customer data processing is slow and inefficient

There is a need for an intelligent system that can:

Automate repetitive decisions

Analyze customer risk profiles

Detect suspicious transaction patterns

Scale efficiently for large datasets

Tech Stack
-> Frontend

Streamlit (Interactive Web Application)

->Machine Learning

Scikit-learn

Pandas

NumPy

->Models Used

Logistic Regression (Loan Approval - Classification)

Linear Regression (Loan Amount - Regression)

KMeans Clustering (Fraud Detection)

-> Backend

Python

Joblib (Model Serialization)

-> Model Performance
Loan Approval (Decision Tree)

Accuracy: 95.58%

Precision: 0.98

Recall: 0.97

F1 Score: 0.97

Loan Amount Prediction (Random Forest)

MAE: ₹22,729

R² Score: 0.27

Fraud Detection (KMeans Clustering)

Cluster-based anomaly grouping implemented

Suspicious behavior pattern identified using cluster analysis

-> How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/yourusername/AI_Banking_System.git
cd AI_Banking_System
2️⃣ Install Dependencies
pip install -r requirements.txt
3️⃣ Run the Application
streamlit run app.py

The application will open in your browser at:

http://localhost:8501

-> Project Features

✔ Individual customer prediction
✔ Bulk CSV upload and processing
✔ Real-time AI results
✔ Clean interactive UI
✔ Modular backend architecture
