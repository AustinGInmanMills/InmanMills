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

st.write("Knitting Tech Page")
