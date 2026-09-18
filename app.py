import streamlit as st

st.title("SafeRoute AI - Road Safety")
st.success("App is LIVE!")
st.write("Final Year Project")

name = st.text_input("Enter Name")
vehicle_type = st.selectbox("Select Vehicle Type 🚗", ["Bike", "Car", "Truck", "Bus"])
weather = st.selectbox("Weather", ["Clear","Rainy","Foggy"])
speed = st.slider("Speed", 20, 120, 60)

if st.button("Submit"):
    st.balloons()
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
    
    st.write(f"Hi {name} | Vehicle: {vehicle_type} | Risk: {risk}%")
    
    if risk < 30:
        st.success("✅ YOU ARE SAFE - Have a safe journey!")
        st.balloons()
    elif risk < 60:
        st.warning("⚠️ BE CAREFUL - Drive slowly!")
    else:
        st.error("🚨 BE CAREFUL - HIGH RISK! Avoid travel or drive very slowly!")
