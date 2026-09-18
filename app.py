import streamlit as st
st.title("SafeRoute AI - Road Safety")
st.success("App is LIVE!")
st.write("Final Year Project")
name = st.text_input("Enter Name")
if st.button("Start"):
    st.balloons()
    st.write(f"Welcome {name}")
weather = st.selectbox("Weather", ["Clear","Rainy","Foggy"])
speed = st.slider("Speed", 20, 120, 60)
risk = 0
if weather != "Clear":
    risk += 40
if speed > 80:
    risk += 30
st.write(f"Risk Level: {risk}%")
if risk < 30:
    st.success("LOW RISK")
elif risk < 60:
    st.warning("MEDIUM RISK")
else:
    st.error("HIGH RISK")
