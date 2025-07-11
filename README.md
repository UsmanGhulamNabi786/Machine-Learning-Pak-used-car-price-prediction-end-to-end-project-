
# PakAuto Price:  Pakistani Used Car Price Predictor

A Streamlit web app for predicting the price of used cars in Pakistan using a machine learning model.

---

## Features
- User-friendly web interface
- Dropdowns for car features (with 'Other' option)
- Model inference using your trained pipeline
- Logo and clean UI

---

## Project Structure
```
car_price_app/
│
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── model/
│   └── predictive_model.pkl
│
├── data/
│   └── CleanedPakWheels.csv
│
├── utils/
│   └── preprocessing.py
│
└── assets/
    └── logo.png            # Place your logo here
```

---

## Setup Instructions

1. **Clone or download this repository.**
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Add your files:**
   - Place your trained model as `model/predictive_model.pkl`
   - Place your cleaned data as `data/CleanedPakWheels.csv`
   - Place your logo as `assets/logo.png` (optional)
4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
5. **Open the app in your browser** (Streamlit will provide a local URL).

---

## Notes
- If you select 'Other' in any dropdown, a text box will appear for custom input.
- The app expects the model to be a scikit-learn pipeline with preprocessing.
- For any issues, check the error messages in the app or your terminal.

---

## Credits
Developed by: Usman Ghulam Nabi for MS AI - Artificial Intelligence Course 