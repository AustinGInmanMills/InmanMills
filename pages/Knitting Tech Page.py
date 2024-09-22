import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

if not "Name" in st.session_state:
    st.switch_page("pages/login.py")

conn = st.connection("gsheets", type=GSheetsConnection)

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Flag Sheets", "Tech Requests", "Tech Duties", "Tech Chat", "Supervisor Chat", "Schedule Information"])



