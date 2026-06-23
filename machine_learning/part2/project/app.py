import streamlit as st 
import pandas as pd
import joblib
from pathlib import Path

# Get the directory where app.py lives
BASE_DIR = Path(__file__).parent

# Load saved model, scaler, and expected columns
model = joblib.load(BASE_DIR / "LR_model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")

st.set_page_config(
    page_title="Insurance Charges Predictor",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Insurance Charges Predictor")
st.write("Predict medical insurance charges using Machine Learning")

# -----------------------------
# User Inputs
# -----------------------------

age = st.slider("Age", 18, 65, 25)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

bmi = st.number_input(
    "BMI",
    min_value=10.0,
    max_value=60.0,
    value=25.0
)

children = st.number_input(
    "Number of Children",
    min_value=0,
    max_value=10,
    value=0
)

smoker = st.selectbox(
    "Smoker",
    ["No", "Yes"]
)

region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

# -----------------------------
# Feature Engineering
# -----------------------------

is_female = 1 if gender == "Female" else 0
is_smoker = 1 if smoker == "Yes" else 0

region_southeast = 1 if region == "Southeast" else 0
region_northwest = 1 if region == "Northwest" else 0

bmi_category_obese = 1 if bmi >= 30 else 0

# Scaling numerical features
scaled_values = scaler.transform(
    [[age, bmi, children]]
)

scaled_age = scaled_values[0][0]
scaled_bmi = scaled_values[0][1]
scaled_children = scaled_values[0][2]

# Create DataFrame exactly as model expects
input_df = pd.DataFrame({
    "age": [scaled_age],
    "is_female": [is_female],
    "bmi": [scaled_bmi],
    "children": [scaled_children],
    "is_smoker": [is_smoker],
    "region_southeast": [region_southeast],
    "bmi_category_Obese": [bmi_category_obese],
    "region_northwest": [region_northwest]
})

# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Insurance Charges"):
    prediction = model.predict(input_df)[0]

    st.success(
        f"Estimated Insurance Charges: ₹ {prediction:,.2f}"
    )

    st.balloons()

    st.subheader("Input Summary")

    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"BMI: {bmi}")
    st.write(f"Children: {children}")
    st.write(f"Smoker: {smoker}")
    st.write(f"Region: {region}")