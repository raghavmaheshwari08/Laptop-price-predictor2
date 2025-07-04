import streamlit as st
import pandas as pd
import numpy as np
import pickle # Changed import from joblib to pickle

# Load trained model pipeline
with open('laptop_price_model.pkl', 'rb') as f:
    pipeline= pickle.load(f) # Changed load from joblib to pickle

st.set_page_config(page_title="Laptop Price Predictor", layout="centered")
st.title("💻 Laptop Price Predictor")

# === User Inputs ===
brand = st.selectbox("Brand", ['ASUS', 'DELL', 'Lenovo', 'HP', 'acer', 'MSI', 'APPLE', 'Avita'])
ram = st.selectbox("RAM (GB)", [4, 8, 16, 32])
processor = st.selectbox("Processor", [
    'AMD Ryzen 3', 'AMD Ryzen 5', 'AMD Ryzen 7', 'AMD Ryzen 9',
    'Intel Celeron Dual', 'Intel Core i3', 'Intel Core i5', 'Intel Core i7',
    'Intel Core i9', 'Intel Pentium Quad', 'Intel Ryzen 7', 'M1 M1'
])
hdd = st.selectbox("HDD (GB)", [0, 512, 1024, 2048])
ssd = st.selectbox("SSD (GB)", [0, 128, 256, 512, 1024, 2048, 3072])
os = st.selectbox("Operating System", ['DOS', 'Mac', 'Windows'])
warranty = st.selectbox("Warranty", ['No Warranty', '1 Years', '2 Years', "3 Years"])
ram_type = st.selectbox("RAM Type", ['DDR3', 'DDR4', 'DDR5', 'LPDDR3', 'LPDDR4', 'LPDDR4X'])
graphic_card_gb = st.selectbox("Graphic Card (GB)", [0, 2, 4, 6, 8])
Touchscreen = st.selectbox("Touchscreen", ["Yes", "No"])

# === Prepare Data ===
input_df = pd.DataFrame([{
    'brand': brand,
    'ram_gb': ram,
    'processor': processor,
    'hdd': hdd,
    'ssd': ssd,
    'os': os,
    'warranty': warranty,
    'ram_type': ram_type,
    'graphic_card_gb': graphic_card_gb,
    'Touchscreen': Touchscreen
}])

# === Predict ===
if st.button("Predict Price"):
    try:
        log_price = model.predict(input_df)[0]
        price = np.expm1(log_price)  # Inverse of log1p
        st.success(f"💰 Predicted Laptop Price: ₹{price:,.0f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
