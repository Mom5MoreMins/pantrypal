# CalorieCalculator.py
import streamlit as st
from storage import save_profile, load_profile

def show_calculator():
    st.header("🍏 Calorie & Allergy Profile")

    user = st.session_state.user
    existing_bmr, existing_allergies = load_profile(user)

    # 1) Unit system toggle
    unit = st.radio(
        "Unit System",
        ("Metric (kg, cm)", "US (lb, in)"),
        key="unit_radio"
    )
    use_metric = unit.startswith("Metric")

    # 2) Age & Gender
    age = st.number_input("Age (years)", min_value=0, max_value=120,
                          value=st.session_state.get("age", 0), key="age")
    gender = st.selectbox(
        "Gender", ["Male", "Female"],
        index=0 if st.session_state.get("gender","Male")=="Male" else 1,
        key="gender"
    )

    st.markdown("---")

    # 3) Weight & Height inputs
    if use_metric:
        weight = st.number_input("Weight (kg)",
                                 min_value=0.0,
                                 value=st.session_state.get("weight_metric", 0.0),
                                 key="weight_metric")
        height = st.number_input("Height (cm)",
                                 min_value=0.0,
                                 value=st.session_state.get("height_metric", 0.0),
                                 key="height_metric")
    else:
        weight = st.number_input("Weight (lb)",
                                 min_value=0.0,
                                 value=st.session_state.get("weight_us", 0.0),
                                 key="weight_us")
        height = st.number_input("Height (in)",
                                 min_value=0.0,
                                 value=st.session_state.get("height_us", 0.0),
                                 key="height_us")

    st.markdown("---")

    # 4) Common allergy checklist
    st.subheader("Your Allergies")
    common_allergies = [
        "Soy", "Peanuts", "Tree Nuts", "Dairy",
        "Eggs", "Gluten", "Shellfish", "Seafood"
    ]
    cols = st.columns(2)
    selected = []
    for i, allergy in enumerate(common_allergies):
        pre = allergy in existing_allergies
        chk = cols[i % 2].checkbox(allergy, value=pre, key=f"allergy_{allergy}")
        if chk:
            selected.append(allergy)

    st.markdown("---")

    # 5) Goal selection
    goal = st.selectbox(
        "Your Goal",
        ["Maintain weight", "Weight loss (−200 kcal)", "Weight gain (+200 kcal)"],
        key="goal"
    )

    st.markdown("---")

    # 6) Calculate & Save button
    if st.button("Calculate & Save Profile"):
        # unit conversion
        if not use_metric:
            kg = weight * 0.453592
            cm = height * 2.54
        else:
            kg = weight
            cm = height

        # Revised Harris–Benedict
        if gender == "Male":
            bmr = 88.362 + 13.397 * kg + 4.799 * cm - 5.677 * age
        else:
            bmr = 447.593 + 9.247 * kg + 3.098 * cm - 4.330 * age

        # adjust for goal
        delta = 0
        if "loss" in goal:
            delta = -200
        elif "gain" in goal:
            delta = 200
        target = bmr + delta

        # save baseline BMR and allergies
        save_profile(user, bmr, selected)

        st.success(
            f"**Saved!**\n\n"
            f"- Baseline BMR: **{bmr:.0f} kcal/day**\n"
            f"- Calorie target ({goal}): **{target:.0f} kcal/day**"
        )

    # 7) Display saved profile
    saved_bmr, saved_allergies = load_profile(user)
    if saved_bmr is not None:
        st.subheader("📋 Saved Profile")
        st.write(f"- **Baseline BMR:** {saved_bmr:.0f} kcal/day")
        if saved_allergies:
            st.write("- **Allergies:**")
            for a in saved_allergies:
                st.write(f"  • {a}")
