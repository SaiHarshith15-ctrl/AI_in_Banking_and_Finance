import streamlit as st
import pandas as pd
from backend.predict import (
    predict_loan_approval,
    predict_loan_amount,
    detect_fraud,
    bulk_loan_approval,
    bulk_loan_amount,
    bulk_fraud_detection
)

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Banking Intelligence System",
    page_icon="🏦",
    layout="wide"
)

# =========================
# SESSION STATE
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"

# =========================
# GLOBAL CSS (PREMIUM UI)
# =========================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0b132b, #1c2541, #3a506b);
    color: white;
}
.main {
    padding: 0;
}
.center {
    text-align: center;
}
.title {
    font-size: 46px;
    font-weight: 800;
    color: #ffffff;
}
.subtitle {
    font-size: 18px;
    opacity: 0.85;
    color: #cbd5e1;
}
.card-btn button {
    height: 120px;
    font-size: 18px;
    font-weight: 600;
    border-radius: 18px;
    background: linear-gradient(135deg, #5bc0be, #6fffe9);
    color: #0b132b;
}
.card-btn button:hover {
    transform: scale(1.04);
}
.back-btn button {
    background-color: #5bc0be !important;
    color: #0b132b !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
@keyframes softMove {
    0% {
        background-position: 0% 50%;
    }
    50% {
        background-position: 100% 50%;
    }
    100% {
        background-position: 0% 50%;
    }
}

body {
    background: linear-gradient(
        120deg,
        #0b132b,
        #1c2541,
        #243b55,
        #3a506b
    );
    background-size: 300% 300%;
    animation: softMove 20s ease-in-out infinite;
    color: white;
}

/* Keep content clean */
.main {
    background: transparent;
}

/* Buttons slightly glowing */
button {
    border-radius: 14px !important;
    transition: all 0.25s ease-in-out;
}

button:hover {
    box-shadow: 0 0 18px rgba(91, 192, 190, 0.35);
    transform: scale(1.03);
}
</style>
""", unsafe_allow_html=True)


# =========================
# BACK BUTTON
# =========================
def back_button():
    st.markdown("<div class='back-btn'>", unsafe_allow_html=True)
    if st.button("⬅ Back to Home"):
        st.session_state.page = "home"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# =========================
# HOME PAGE
# =========================
if st.session_state.page == "home":

    st.markdown("<div style='height:160px'></div>", unsafe_allow_html=True)

    st.markdown("<div class='center title'>AI Banking Intelligence System</div>", unsafe_allow_html=True)
    st.markdown("<div class='center subtitle'>Smart, secure & scalable banking powered by AI</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([3, 2, 3])
    with col2:
        if st.button("🚀 Get Started", use_container_width=True):
            st.session_state.page = "services"
            st.rerun()

# =========================
# SERVICES PAGE
# =========================
elif st.session_state.page == "services":

    back_button()
    st.markdown("## 🔍 Select a Banking Service")

    st.markdown("<div style='height:40px'></div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    with c1:
        with st.container():
            st.markdown("<div class='card-btn'>", unsafe_allow_html=True)
            if st.button("🏦\n\nLoan Approval", use_container_width=True):
                st.session_state.page = "loan_approval"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    with c2:
        with st.container():
            st.markdown("<div class='card-btn'>", unsafe_allow_html=True)
            if st.button("💰\n\nLoan Amount Prediction", use_container_width=True):
                st.session_state.page = "loan_amount"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    with c3:
        with st.container():
            st.markdown("<div class='card-btn'>", unsafe_allow_html=True)
            if st.button("🚨\n\nFraud Detection", use_container_width=True):
                st.session_state.page = "fraud"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

    with c4:
        with st.container():
            st.markdown("<div class='card-btn'>", unsafe_allow_html=True)
            if st.button("📂\n\nBulk File Processing", use_container_width=True):
                st.session_state.page = "bulk"
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

# =========================
# LOAN APPROVAL
# =========================
elif st.session_state.page == "loan_approval":

    back_button()
    st.markdown("## 🏦 Loan Approval Prediction")

    income = st.number_input("Income (₹)", min_value=0)
    credit = st.number_input("Credit Score", min_value=0)
    loan = st.number_input("Requested Loan Amount (₹)", min_value=0)
    dti = st.number_input("DTI Ratio (%)", min_value=0.0)

    emp = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Unemployed"])
    emp_map = {"Salaried": 0, "Self-Employed": 1, "Unemployed": 2}

    if st.button("Check Approval"):
        result = predict_loan_approval({
            "Income": income,
            "Credit_Score": credit,
            "Loan_Amount": loan,
            "DTI_Ratio": dti,
            "Employment_Status": emp_map[emp]
        })
        if "APPROVED" in result:
          st.success(result)
        else:
          st.error(result)


# =========================
# LOAN AMOUNT
# =========================
elif st.session_state.page == "loan_amount":

    back_button()
    st.markdown("## 💰 Loan Amount Prediction")

    income = st.number_input("Income (₹)", min_value=0)
    credit = st.number_input("Credit Score", min_value=0)
    dti = st.number_input("DTI Ratio (%)", min_value=0.0)

    emp = st.selectbox("Employment Status", ["Salaried", "Self-Employed", "Unemployed"])
    emp_map = {"Salaried": 0, "Self-Employed": 1, "Unemployed": 2}

    if st.button("Predict Loan Amount"):
        amount = predict_loan_amount({
            "Income": income,
            "Credit_Score": credit,
            "DTI_Ratio": dti,
            "Employment_Status": emp_map[emp]
        })
        st.success(f"Predicted Loan Amount: ₹ {amount:,}")

# =========================
# FRAUD DETECTION
# =========================
elif st.session_state.page == "fraud":

    back_button()
    st.markdown("## 🚨 Fraud Detection")

    amt = st.number_input("Transaction Amount (₹)", min_value=0)
    bal = st.number_input("Account Balance (₹)", min_value=0)
    age = st.number_input("Customer Age", min_value=0)

    ttype = st.selectbox("Transaction Type", ["Transfer", "Debit", "Bill Payment"])
    merch = st.selectbox("Merchant Category", ["Groceries", "Restaurant", "Entertainment"])
    device = st.selectbox("Transaction Device", ["ATM", "POS", "Mobile App", "Voice Assistant"])

    maps = {
        "Transfer": 0, "Debit": 1, "Bill Payment": 2,
        "Groceries": 0, "Restaurant": 1, "Entertainment": 2,
        "ATM": 0, "POS": 1, "Mobile App": 2, "Voice Assistant": 3
    }

    if st.button("Analyze Transaction"):
        decision, cluster = detect_fraud({
            "Transaction_Amount": amt,
            "Account_Balance": bal,
            "Age": age,
            "Transaction_Type": maps[ttype],
            "Merchant_Category": maps[merch],
            "Transaction_Device": maps[device]
        })
        st.info(f"Cluster: {cluster}")
        
        if "FRAUD" in decision:
           st.error(decision)
        else:
           st.success(decision)


# =========================
# BULK FILE PROCESSING
# =========================
elif st.session_state.page == "bulk":

    back_button()
    st.markdown("## 📂 Bulk File Processing")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    task = st.selectbox("Select Analysis Type", [
        "Loan Approval",
        "Loan Amount Prediction",
        "Fraud Detection"
    ])

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        if st.button("⚙ Process File"):
            if task == "Loan Approval":
                result = bulk_loan_approval(df)
            elif task == "Loan Amount Prediction":
                result = bulk_loan_amount(df)
            else:
                result = bulk_fraud_detection(df)

            st.success("Processing Completed")
            st.dataframe(result.head())

            st.download_button(
                "⬇ Download Result CSV",
                result.to_csv(index=False),
                "processed_output.csv",
                "text/csv"
            )
