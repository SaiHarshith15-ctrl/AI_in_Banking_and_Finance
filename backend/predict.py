import joblib
import os
import pandas as pd
import numpy as np

# =========================
# SAFE ABSOLUTE PATH SETUP
# =========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# =========================
# LOAD MODELS
# =========================

loan_model = joblib.load(os.path.join(MODEL_DIR, "loan_classifier.pkl"))
loan_scaler = joblib.load(os.path.join(MODEL_DIR, "loan_scaler.pkl"))

amount_model = joblib.load(os.path.join(MODEL_DIR, "loan_amount_regressor.pkl"))
amount_scaler = joblib.load(os.path.join(MODEL_DIR, "loan_amount_scaler.pkl"))

fraud_model = joblib.load(os.path.join(MODEL_DIR, "fraud_cluster.pkl"))
fraud_scaler = joblib.load(os.path.join(MODEL_DIR, "fraud_scaler.pkl"))

# =========================
# LOAN APPROVAL
# =========================

def predict_loan_approval(input_dict):
    # Rule-based safety checks (banking logic)
    if input_dict["Credit_Score"] < 500:
        return "REJECTED (Low Credit Score)"

    if input_dict["DTI_Ratio"] > 50:
        return "REJECTED (High Debt Ratio)"

    if input_dict["Employment_Status"] == 2:  # Unemployed
        return "REJECTED (Unemployed)"

    # ML-based decision
    df = pd.DataFrame([input_dict])
    scaled = loan_scaler.transform(df)
    pred = loan_model.predict(scaled)[0]

    return "APPROVED" if pred == 1 else "REJECTED"



# =========================
# LOAN AMOUNT
# =========================

def predict_loan_amount(input_dict):
    # Sanity limits (banking rules)
    if input_dict["Income"] > 200000:
        input_dict["Income"] = 200000

    if input_dict["DTI_Ratio"] > 60:
        input_dict["DTI_Ratio"] = 60

    df = pd.DataFrame([input_dict])
    scaled = amount_scaler.transform(df)
    amount = amount_model.predict(scaled)[0]

    return int(max(amount, 0))



# =========================
# FRAUD DETECTION
# =========================

SUSPICIOUS_CLUSTER = 0

def fraud_decision(cluster_id):
    return "🚨 FRAUD ALERT" if cluster_id == SUSPICIOUS_CLUSTER else "✅ NORMAL TRANSACTION"


def detect_fraud(txn_dict):
    df = pd.DataFrame([txn_dict])
    scaled = fraud_scaler.transform(df)
    cluster = fraud_model.predict(scaled)[0]
    decision = fraud_decision(cluster)
    return decision, cluster

def bulk_loan_approval(df):
    results = []

    for _, row in df.iterrows():
        result = predict_loan_approval({
            "Income": row["Income"],
            "Credit_Score": row["Credit_Score"],
            "Loan_Amount": row["Loan_Amount"],
            "DTI_Ratio": row["DTI_Ratio"],
            "Employment_Status": row["Employment_Status"]
        })
        results.append(result)

    df["Loan_Status"] = results
    return df


def bulk_loan_amount(df):
    amounts = []

    for _, row in df.iterrows():
        amount = predict_loan_amount({
            "Income": row["Income"],
            "Credit_Score": row["Credit_Score"],
            "DTI_Ratio": row["DTI_Ratio"],
            "Employment_Status": row["Employment_Status"]
        })
        amounts.append(amount)

    df["Eligible_Loan_Amount"] = amounts
    return df

def bulk_fraud_detection(df):
    decisions = []

    for _, row in df.iterrows():
        decision, _ = detect_fraud({
            "Transaction_Amount": row["Transaction_Amount"],
            "Account_Balance": row["Account_Balance"],
            "Age": row["Age"],
            "Transaction_Type": row["Transaction_Type"],
            "Merchant_Category": row["Merchant_Category"],
            "Transaction_Device": row["Transaction_Device"]
        })
        decisions.append(decision)

    df["Fraud_Status"] = decisions
    return df


