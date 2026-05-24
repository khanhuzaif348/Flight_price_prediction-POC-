import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model
model = joblib.load("D:\\ProductionProject(Internship)\\Flight_price_prediction\\flight_price_model.joblib")

# Title
st.title("Flight Price Prediction")

st.write("Enter Flight Details")

# -----------------------------
# Airline
# -----------------------------

airline = st.selectbox(
    "Select Airline",
    ["IndiGo", "Air India", "SpiceJet", "Vistara", "GoAir"]
)

# -----------------------------
# Source
# -----------------------------

source = st.selectbox(
    "Source",
    ["Delhi", "Mumbai", "Kolkata", "Chennai"]
)

# -----------------------------
# Destination
# -----------------------------

destination = st.selectbox(
    "Destination",
    ["Cochin", "Delhi", "Hyderabad", "Kolkata"]
)

# -----------------------------
# Stops
# -----------------------------

total_stops = st.slider(
    "Total Stops",
    0,
    4
)

# -----------------------------
# Journey Date
# -----------------------------

journey_date = st.date_input("Journey Date")

year = journey_date.year
month = journey_date.month
day = journey_date.day

# -----------------------------
# Departure Time
# -----------------------------

dep_time = st.time_input("Departure Time")

dep_hour = dep_time.hour
dep_min = dep_time.minute

# -----------------------------
# Arrival Time
# -----------------------------

arrival_time = st.time_input("Arrival Time")

arrival_hour = arrival_time.hour
arrival_min = arrival_time.minute

# -----------------------------
# Duration
# -----------------------------

duration_hour = st.number_input(
    "Duration Hours",
    min_value=0
)

duration_min = st.number_input(
    "Duration Minutes",
    min_value=0
)

# =============================
# Prediction
# =============================

if st.button("Predict Flight Price"):

    try:

        # Create dataframe
        data = pd.DataFrame({
            'Airline': [airline],
            'Source': [source],
            'Destination': [destination],
            'Total_Stops': [total_stops],
            'year_of_Journey': [year],
            'month_of_Journey': [month],
            'day_of_Journey': [day],
            'Dep_Time_hour': [dep_hour],
            'Dep_Time_min': [dep_min],
            'Arrival_Time_hour': [arrival_hour],
            'Arrival_Time_min': [arrival_min],
            'duration_hour': [duration_hour],
            'Duration_min': [duration_min]
        })

        # Prediction
        prediction = model.predict(data)

        st.success(f"Predicted Flight Price: ₹ {prediction[0]:,.2f}")

    except Exception as e:

        st.error(f"Error: {e}")
    
