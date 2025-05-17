import streamlit as st
import pandas as pd

def app():
    st.title("Menu")
    menu = pd.read_csv("data/menu.csv")
    st.table(menu)
