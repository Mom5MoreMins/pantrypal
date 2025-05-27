import streamlit as st

def show_substitute():
    st.header("Ingredient Substitute 🔄")

    ing = st.text_input("Ingredient name", key="ing_name")
    qty = st.text_input("Quantity (e.g. '1 cup')", key="ing_qty")

    if st.button("Find Substitute"):
        # placeholder: call Gemini API or your logic here
        st.write(f"Substitute for {qty} of {ing}: …")
