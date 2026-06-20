import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="AI Fraud Detection",
    page_icon="🛡️",
    layout="wide"
)

# Sidebar Menu
st.sidebar.title("☰ Features")

menu = st.sidebar.radio(
    "Select Feature",
    [
        "🏠 Home",
        "💳 Transaction Detection",
        "📱 QR Code Scanner",
        "🌐 Fraud Website Detector",
        "📊 Risk Dashboard",
        "🤖 AI Chatbot"
    ]
)

# HOME PAGE
if menu == "🏠 Home":
    st.title("🛡️ Welcome to AI Fraud Detection System")
    
    st.image(
        "https://images.unsplash.com/photo-1563013544-824ae1b704d",
        use_container_width=True
    )
    
    st.markdown("""
    ### Secure Your Digital Transactions
    
    Our AI-Powered Fraud Detection System helps users identify:
    
    ✅ Fraudulent Transactions
    
    ✅ Fake QR Codes
    
    ✅ Malicious Websites
    
    ✅ High-Risk Devices & IPs
    
    ✅ Financial Scams
    
    ---
    
    ### Features
    - Real-Time Fraud Detection
    - QR Code Analysis
    - Website Scam Detection
    - AI Chatbot Assistant
    - Risk Score Dashboard
    """)

# TRANSACTION DETECTION
elif menu == "💳 Transaction Detection":
    
    st.header("💳 Transaction Fraud Detection")
    
    amount = st.number_input("Transaction Amount", min_value=0.0)
    
    transaction_type = st.selectbox(
        "Transaction Type",
        ["UPI", "Credit Card", "Debit Card", "Net Banking"]
    )
    
    device_risk = st.slider(
        "Device Risk Score",
        0,
        100,
        20
    )
    
    ip_risk = st.slider(
        "IP Risk Score",
        0,
        100,
        10
    )
    
    if st.button("Check Fraud"):
        
        # Replace with your model
        risk_score = (device_risk + ip_risk) / 2
        
        if risk_score > 60:
            st.error("⚠️ High Fraud Risk Detected")
        else:
            st.success("✅ Transaction Looks Safe")

# QR CODE DETECTOR
elif menu == "📱 QR Code Scanner":
    
    st.header("📱 QR Code Fraud Detector")
    
    qr_file = st.file_uploader(
        "Upload QR Code Image",
        type=["png", "jpg", "jpeg"]
    )
    
    if qr_file:
        st.image(qr_file, width=300)
        
        if st.button("Scan QR"):
            st.success("QR Uploaded Successfully")
            
            # Connect your qr_code.ipynb logic here
            st.info("Result will be displayed here")

# WEBSITE DETECTOR
elif menu == "🌐 Fraud Website Detector":
    
    st.header("🌐 Fraud Website Detection")
    
    url = st.text_input(
        "Enter Website URL"
    )
    
    if st.button("Analyze Website"):
        
        # Connect Fraud_Website_Detector.ipynb model here
        
        if url:
            st.success("Website Analysis Completed")
            st.write("Prediction: Legitimate Website")

# DASHBOARD
elif menu == "📊 Risk Dashboard":
    
    st.header("📊 Risk Dashboard")
    
    data = pd.DataFrame({
        "Metric": [
            "Safe Transactions",
            "Fraud Alerts",
            "QR Scans",
            "Website Checks"
        ],
        "Count": [
            120,
            15,
            80,
            60
        ]
    })
    
    st.dataframe(data)
    
    st.bar_chart(
        data.set_index("Metric")
    )

# AI CHATBOT
elif menu == "🤖 AI Chatbot":
    
    st.header("🤖 AI Fraud Assistant")
    
    user_input = st.text_input(
        "Ask anything about fraud detection"
    )
    
    if st.button("Send"):
        
        if user_input:
            st.write("### Bot Response")
            
            st.info(
                f"You asked: {user_input}\n\n"
                "This response will come from your Gemini/OpenAI chatbot."
            )