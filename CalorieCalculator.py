
import streamlit as st

def show_calculator():
    st.header("Daily Calorie Calculator 🍏")

    age = st.number_input("Age", min_value=0, max_value=120, key="age")
    weight = st.number_input("Weight (kg)", key="weight")
    height = st.number_input("Height (cm)", key="height")
    gender = st.selectbox("Gender", ["Male", "Female"], key="gender")

    if st.button("Calculate BMR"):
        if gender == "Male":
            bmr = 10*weight + 6.25*height - 5*age + 5
        else:
            bmr = 10*weight + 6.25*height - 5*age - 161
        st.success(f"Your BMR: {bmr:.0f} kcal/day")
        st.session_state["bmr"] = bmr
