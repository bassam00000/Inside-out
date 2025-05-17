import streamlit as st
import pandas as pd

def app():
    st.title("My Orders")
    st.write("Order and manage your food.")
    name = st.text_input("Enter your name:")
    item = st.text_input("What would you like to order?")
    if st.button("Place Order"):
        new_order = pd.DataFrame([[name, item]], columns=["name", "item"])
        new_order.to_csv("data/orders.csv", mode='a', header=False, index=False)
        st.success(f"Order placed: {item}")
