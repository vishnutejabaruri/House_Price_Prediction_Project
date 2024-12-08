import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('model.pkl') 
scaler=joblib.load("scaler.pkl")

# Function to predict house price
def predict_price(living_area, num_views, condition, grade, latitude, longitude, area_excluding_basement, area_basement):
    input_data = np.array([[living_area, num_views, condition, grade, latitude, longitude, area_excluding_basement, area_basement]])
    prediction = model.predict(input_data)
    return prediction[0]

# Streamlit UI
st.title("House Price Prediction")
st.header("Enter the details of the house")

living_area = st.number_input("Living Area (sq ft)", min_value=0, value=2920)
num_views = st.number_input("Number of Views", min_value=0, value=0)
condition = st.slider("Condition of the House (1 to 5)", min_value=1, max_value=5, value=5)
grade = st.slider("Grade of the House (1 to 10)", min_value=1, max_value=10, value=8)
latitude = st.number_input("Latitude", value=52.8878)
longitude = st.number_input("Longitude", value=-114.470)
area_excluding_basement = st.number_input("Area of House Excluding Basement (sq ft)", value=1910)
area_basement = st.number_input("Area of the Basement (sq ft)", value=1010)

if st.button("Predict Price"):
    price = predict_price(living_area, num_views, condition, grade, latitude, longitude, area_excluding_basement, area_basement)
    st.write(f"Predicted House Price: ${price:,.2f}")

# Optional: Add more styling for the layout, colors, and elements
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 32px;
            font-size: 18px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .stTextInput input {
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)
