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
#################################################

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
            
        if knitting_bttn is None:
            st.divider()
            st.subheader("Doff Time Calculator")
            calculator_machine_number = st.number_input("Machine Number ", value=None, min_value=0, max_value=21,placeholder="")
            calculator_machine_revs = st.number_input("Current Revs", value=None, min_value=0, max_value=5000,placeholder="")
            calculator_bttn = st.button("Calculate")
            if calculator_bttn:
                if calculator_machine_number is not None and calculator_machine_revs is not None:
                    st.write("not added yet")
        
        if knitting_bttn == "Operator":
            placeholder = st.empty()

            actual_email = "email"
            actual_password = "password"

            # Insert a form in the container
            with placeholder.form("login"):
                st.markdown("#### Enter your credentials")
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                submit = st.form_submit_button("Login")

            if submit and email == actual_email and password == actual_password:
                # If the form is submitted and the email and password are correct,
                # clear the form/container and display a success message
                placeholder.empty()
                st.success("Login successful")
            elif submit and email != actual_email and password != actual_password:
                st.error("Login failed")
            else:
                pass