import streamlit as st
import pandas as pd
from prediction_helper import predict

st.title('Health care premium prediction application')
# Example options (from your data)
gender_options = ['Male', 'Female']
region_options = ['Northeast', 'Northwest', 'Southeast', 'Southwest']
marital_status_options = ['Unmarried', 'Married']
bmi_category_options = ['Overweight', 'Underweight', 'Normal', 'Obesity']
smoking_status_options = ['Regular', 'No Smoking', 'Occasional', 'Smoking=0', 'Does Not Smoke']
employment_status_options = ['Self-Employed', 'Freelancer', 'Salaried']
income_level_options = ['> 40L', '<10L', '10L - 25L', '25L - 40L']
medical_history_options = [
    'High blood pressure', 'No Disease', 'Diabetes & High blood pressure',
    'Diabetes & Heart disease', 'Diabetes', 'Diabetes & Thyroid',
    'Heart disease', 'Thyroid', 'High blood pressure & Heart disease'
]
insurance_plan_options = ['Silver', 'Bronze', 'Gold']

st.title("ML Model Prediction App")

# Create 3 columns per row
col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", gender_options)
with col2:
    region = st.selectbox("Region", region_options)
with col3:
    marital_status = st.selectbox("Marital Status", marital_status_options)

col4, col5, col6 = st.columns(3)
with col4:
    bmi_category = st.selectbox("BMI Category", bmi_category_options)
with col5:
    smoking_status = st.selectbox("Smoking Status", smoking_status_options)
with col6:
    employment_status = st.selectbox("Employment Status", employment_status_options)

col7, col8, col9 = st.columns(3)
with col7:
    genetical_risk = st.number_input("Genetical Risk", step = 1, min_value = 0, max_value = 5)
with col8:
    medical_history = st.selectbox("Medical History", medical_history_options)
with col9:
    insurance_plan = st.selectbox("Insurance Plan", insurance_plan_options)

col7, col8, col9 = st.columns(3)
with col7:
    age = st.number_input("Age", min_value=18,step = 1,max_value = 100)
with col8:
    number_of_dependants = st.number_input("Medical History", min_value = 0,step = 1,max_value = 20)

with col9:
    income_lakhs = st.number_input("Income in Lakhs", step = 1, min_value = 0,max_value = 200)

# creating a dictionary for input values
input_dict = {
    'Age':age,
    'Number of Dependants':number_of_dependants,
    'Income in Lakhs':income_lakhs,
    'Gentical Risk':genetical_risk,
    'Insurance_plan':insurance_plan,
    'Employement Status':employment_status,
    'Gender':gender,
    'Martial Status':marital_status,
    'BMI Category':bmi_category,
    'Smoking Status':smoking_status,
    'Region':region,
    'Medical History':medical_history,
}


if st.button('Predict'):
    prediction = predict(input_dict)
    st.success(f" Prediction Premium is {prediction}")

