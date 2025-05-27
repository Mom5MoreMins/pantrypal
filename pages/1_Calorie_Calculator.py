import streamlit as st

def show_calculator():
    st.header("Daily Calorie Calculator")
    age = st.number_input("Age", min_value=0, max_value=120)
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    gender = st.selectbox("Gender", ["Male", "Female"])
    if st.button("Calculate"):
        # example: Mifflin-St Jeor
        if gender == "Male":
            bmr = 10*weight + 6.25*height - 5*age + 5
        else:
            bmr = 10*weight + 6.25*height - 5*age - 161
        st.write(f"Your BMR: {bmr:.0f} kcal/day")
        # …store bmr in session_state or pass it on…