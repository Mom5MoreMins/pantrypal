import streamlit as st
from storage import save_profile, load_profile

def show_calculator():
    st.header("🍏 Calorie & Allergy Profile")

    user = st.session_state.user

    # Load existing data if present
    existing_bmr, existing_allergies = load_profile(user)

    # Inputs
    age    = st.number_input("Age", min_value=0, max_value=120,
                             value=25 if existing_bmr is None else st.session_state.get("age", 25),
                             key="age")
    weight = st.number_input("Weight (kg)",
                             value=70 if existing_bmr is None else st.session_state.get("weight", 70),
                             key="weight")
    height = st.number_input("Height (cm)",
                             value=170 if existing_bmr is None else st.session_state.get("height", 170),
                             key="height")
    gender = st.selectbox("Gender", ["Male", "Female"],
                          index=0 if existing_bmr is None else (0 if st.session_state.get("gender","Male")=="Male" else 1),
                          key="gender")

    # Manage allergies list in session_state
    if "allergies" not in st.session_state:
        st.session_state.allergies = existing_allergies.copy()

    st.subheader("Your Allergies")
    col1, col2 = st.columns([3,1])
    with col1:
        new_allergy = st.text_input("Add an allergy", key="new_allergy")
    with col2:
        if st.button("Add", use_container_width=True):
            if new_allergy and new_allergy not in st.session_state.allergies:
                st.session_state.allergies.append(new_allergy)
                st.rerun()

    # Show current allergies with remove buttons
    for idx, allergy in enumerate(st.session_state.allergies):
        remove = st.button(f"❌ {allergy}", key=f"rm_{idx}")
        st.write(f"- {allergy}")
        if remove:
            st.session_state.allergies.pop(idx)
            st.rerun()

    st.markdown("---")
    # Calculate & Save
    if st.button("Calculate BMR & Save Profile"):
        # Mifflin-St Jeor equation
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height - 5 * age - 161

        save_profile(user, bmr, st.session_state.allergies)
        st.success(f"Saved! Your BMR: **{bmr:.0f} kcal/day**")

    # Show saved profile
    saved_bmr, saved_allergies = load_profile(user)
    if saved_bmr is not None:
        st.subheader("📋 Saved Profile")
        st.write(f"- **BMR:** {saved_bmr:.0f} kcal/day")
        if saved_allergies:
            st.write("- **Allergies:**")
            for a in saved_allergies:
                st.write(f"  • {a}")
