import time
from operator import index

import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from math import trunc

st.set_page_config(
    page_title="Inman Mills Saybrook",
    page_icon="",
)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

hide_st_style = """  
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """  # Hides streamlit information on web app
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 25px;
                }
        </style>
    """,
    unsafe_allow_html=True  # Deletes white space on top of web app
)


tab1, tab2, tab3 = st.tabs(["Home", "Departments", "Information"])

with tab1:
    st.markdown(
        "Welcome to Inman Mills Saybrook Plant new Employee website! You can view information about up coming layoffs, overtime, departments and much more")

with tab2:
    department_options_bttn = st.selectbox(
        "Department Options",
        ("Knitting", "Ring Spinning", "Winding", "Roven", "MJS", "MVS", "Card Room"),
        index=None,
        key="DepartmentBox"
    )
    if department_options_bttn == "Knitting":
        knitting_bttn = st.selectbox(
            "Knitting Department Options",
            ("Operator", "Technician", "Overhauler", "Supervisor"),
            index=None,
            key="KnittingBox",
        )