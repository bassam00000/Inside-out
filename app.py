import streamlit as st
from pages import Home, Menu, Orders, Social, Admin

st.set_page_config(page_title="New Rest App", layout="wide")

PAGES = {
    "Home": Home,
    "Menu": Menu,
    "My Orders": Orders,
    "Social": Social,
    "Admin": Admin
}

st.sidebar.title("New Rest App")
selection = st.sidebar.radio("Navigate", list(PAGES.keys()))
page = PAGES[selection]
page.app()
