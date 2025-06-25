import streamlit as st
import pandas as pd
import pickle

# Load encoder, scaler, and model
encoder = pickle.load(open("models/encoder.pkl", 'rb'))
scaler = pickle.load(open("models/scaler.pkl", 'rb'))  # Ensure this file exists
model_gbc = pickle.load(open("models/model_gbc.pkl", 'rb'))

# Prediction function
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])
    input_scaled = scaler.transform(input_df)
    prediction_encoded = model_gbc.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction_encoded)
    return prediction[0]

# Streamlit UI
st.title('🌾 Crop Recommendation System')

st.markdown("#### Please enter the soil and environmental values:")

col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, value=50.0)
    P = st.number_input("Phosphorous (P)", min_value=0.0, value=50.0)
    K = st.number_input("Potassium (K)", min_value=0.0, value=50.0)
    ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)

with col2:
    temperature = st.number_input("Temperature (°C)", min_value=-10.0, value=25.0)
    humidity = st.number_input("Humidity (%)", min_value=0.0, value=80.0)
    rainfall = st.number_input("Rainfall (mm)", min_value=0.0, value=100.0)

# Predict button
if st.button('🌱 Recommend'):
    crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"✅ Recommended Crop: **{crop}**")