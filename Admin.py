import streamlit as st
import pandas as pd

def app():
    st.title("Admin Panel")
    st.write("Manage menu and orders")

    menu = pd.read_csv("data/menu.csv")
    st.subheader("Menu")
    st.table(menu)

    st.subheader("Add new item")
    name = st.text_input("Dish Name")
    price = st.number_input("Price", min_value=0.0)
    if st.button("Add to Menu"):
        pd.DataFrame([[name, price]], columns=["name", "price"]).to_csv("data/menu.csv", mode='a', header=False, index=False)
        st.success("Item added!")
