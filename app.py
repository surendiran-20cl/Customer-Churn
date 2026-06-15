import streamlit as st
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Load the trained model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the LabelEncoder for the target variable
le = LabelEncoder()
le.classes_ = ['No', 'Yes']  # Must match the classes used during training

# Title
st.title("Customer Churn Prediction")

# User input form
st.header("Enter Customer Details")
tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=1)
monthly_charges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=50.0)

# Prepare input for prediction
input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
})

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)
    st.subheader("Prediction Result")
    if prediction[0] == 1:
        st.error("This customer is likely to **CHURN**.")
    else:
        st.success("This customer is likely to **STAY**.")
    st.write(f"Churn Probability: {probability[0][1]:.2f}")

# Optional: Batch prediction via CSV upload
st.header("Batch Prediction (CSV Upload)")
uploaded_file = st.file_uploader("Upload CSV", type=["csv"])
if uploaded_file:
    batch_data = pd.read_csv(uploaded_file)
    predictions = model.predict(batch_data)
    batch_data["Churn_Prediction"] = le.inverse_transform(predictions)
    st.write(batch_data)
