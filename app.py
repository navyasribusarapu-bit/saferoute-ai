import streamlit as st

st.title("SafeRoute AI - Road Safety")
st.success("App is LIVE!")
st.write("Final Year Project")
name = st.text_input("Enter Name")

if st.button("Start"):
    st.balloons()
    st.write(f"Welcome {name}")

# Vehicle Type - Bike, Car, Truck, Bus
vehicle_type = st.selectbox("Select Vehicle Type 🚗", ["Bike", "Car", "Truck", "Bus"])

st.success(f"Vehicle Selected: {vehicle_type}")

weather = st.selectbox("Weather", ["Clear","Rainy","Foggy"])
speed = st.slider("Speed", 20, 120, 60)
risk = 0

if weather != "Clear":
    risk += 40
if speed > 80:
    risk += 30
if vehicle_type == "Bike":
    risk += 20
if vehicle_type == "Truck":
    risk += 15
if vehicle_type == "Bus":
    risk += 10

st.write(f"Risk Level: {risk}%")
st.write(f"Vehicle: {vehicle_type}")

if risk < 30:
    st.success("LOW RISK")
elif risk < 60:
    st.warning("MEDIUM RISK")
else:
    st.error("HIGH RISK")
