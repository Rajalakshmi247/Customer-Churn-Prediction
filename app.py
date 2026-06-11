
import streamlit as st
import joblib
import numpy as np

model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure", 0, 100)
monthly_charges = st.number_input("Monthly Charges", 0.0)
total_charges = st.number_input("Total Charges", 0.0)

if st.button("Predict"):
    data = np.array([[tenure, monthly_charges, total_charges]])
    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer is likely to stay")
