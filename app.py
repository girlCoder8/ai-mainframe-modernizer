import streamlit as st
from orchestration_engine import handle_user_request

st.set_page_config(layout="centered", page_title="Mainframe AI Agent")

st.title("📱 AI-Powered Mainframe Modernizer")

customer_id = st.text_input("Enter Customer ID")

if st.button("Analyze"):
    with st.spinner("Processing..."):
        result = handle_user_request(customer_id)
        st.subheader("Profile")
        st.json(result["profile"])
        st.subheader("Personalized Recommendation")
        st.success(result["recommendation"])
        st.subheader("⚠️ Fraud Alerts")
        if result["fraud_alerts"]:
            st.error(result["fraud_alerts"])
        else:
            st.success("No fraud detected.")
