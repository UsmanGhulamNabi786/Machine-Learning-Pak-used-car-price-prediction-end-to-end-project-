import streamlit as st
import pandas as pd
import pickle
import os
import base64
from utils.preprocessing import (
    get_make_options, get_model_options, get_variant_options,
    get_engine_type_options, get_transmission_options
)

# --- CONFIG ---
DATA_PATH = os.path.join('data', 'CleanedPakWheels.csv')
MODEL_PATH = os.path.join('model', 'predictive_model.pkl')
LOGO_PATH = os.path.join('assets', 'logo.png')

# --- PAGE SETUP ---
st.set_page_config(page_title="Pak Used Car Price Predictor", page_icon=LOGO_PATH, layout="centered")

# --- LOGO & TITLE ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

if os.path.exists(LOGO_PATH):
    logo_base64 = get_base64_image(LOGO_PATH)
    logo_html = f'''
        <div style="text-align: center;">
            <img src="data:image/png;base64,{logo_base64}" width="70" style="vertical-align: middle; margin-bottom: 0;" />
            <span style="display: block; font-size: 2.5rem; color: #0a4d8c; font-weight: bold; margin-top: 0.2em;">PakAuto Price</span>
        </div>
    '''
    st.markdown(logo_html, unsafe_allow_html=True)
else:
    st.markdown(
        "<h1 style='text-align: center; color: #0a4d8c;'>PakAuto Price</h1>",
        unsafe_allow_html=True
    )

st.markdown(
    """
    <h3 style='text-align: center; color: #0a4d8c; margin-top: 0.5em;'>Pakistani Used Car Price Predictor</h3>
    """,
    unsafe_allow_html=True
)
st.write("Enter car details below to estimate the market price using AI.")

# --- LOAD MODEL ---
@st.cache_resource(show_spinner=True)
def load_model():
    try:
        with open(MODEL_PATH, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Model could not be loaded: {e}")
        return None
model = load_model()

# --- DROPDOWN OPTIONS ---
def get_options():
    try:
        make_options = get_make_options(DATA_PATH)
        model_options = get_model_options(DATA_PATH)
        variant_options = get_variant_options(DATA_PATH)
        engine_type_options = get_engine_type_options(DATA_PATH)
        transmission_options = get_transmission_options(DATA_PATH)
        return make_options, model_options, variant_options, engine_type_options, transmission_options
    except Exception as e:
        st.error(f"Error loading dropdown options: {e}")
        return [], [], [], [], []

make_options, model_options, variant_options, engine_type_options, transmission_options = get_options()

# --- USER INPUT FORM ---
with st.form("car_form"):
    make = st.selectbox("Make", make_options)
    if make == "Other":
        make = st.text_input("Enter Make")
    model_name = st.selectbox("Model", model_options)
    if model_name == "Other":
        model_name = st.text_input("Enter Model")
    variant = st.selectbox("Variant", variant_options)
    if variant == "Other":
        variant = st.text_input("Enter Variant")
    year = st.number_input("Year", min_value=1980, max_value=2025, value=2018)
    mileage = st.number_input("Mileage (km)", min_value=0, value=50000)
    engine_capacity = st.number_input("Engine Capacity (cc)", min_value=600, max_value=6700, value=1300)
    engine_type = st.selectbox("Engine Type", engine_type_options)
    if engine_type == "Other":
        engine_type = st.text_input("Enter Engine Type")
    transmission = st.selectbox("Transmission", transmission_options)
    if transmission == "Other":
        transmission = st.text_input("Enter Transmission")
    submitted = st.form_submit_button("Predict Price")

# --- PREDICTION ---
if submitted and model is not None:
    input_dict = {
        'Make': [make],
        'Model': [model_name],
        'Variant': [variant],
        'Year': [year],
        'Mileage': [mileage],
        'Engine Capacity': [engine_capacity],
        'Engine Type': [engine_type],
        'Transmission': [transmission],
    }
    input_df = pd.DataFrame(input_dict)
    try:
        pred = model.predict(input_df)
        st.success(f"Estimated Price: Rs. {int(pred[0]):,}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")

# --- FOOTER ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #0a4d8c; font-size: 1.1em;'>
        Developed By: Usman Ghulam Nabi  MS AI - Artificial Intelligence Course
    </div>
""", unsafe_allow_html=True) 