import pandas as pd
import streamlit as st
from streamlit import success
from streamlit_gsheets import GSheetsConnection
import time

conn = st.connection("gsheets", type=GSheetsConnection)  # Connects to gSheet conn used for connect
employee_data = conn.read(worksheet="Employees", ttl=0)
employee_data = pd.DataFrame(employee_data)

placeholder = st.empty()

with placeholder.form("login"):
    st.markdown("#### Enter your credentials")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    col1, col2 = st.columns([1, 6])
    with col1:
        submit = st.form_submit_button("Login")
    with col2:
        create = st.form_submit_button("Create Account")

if create:
    st.switch_page("pages/create.py")


if submit:
    for x, row in employee_data.iterrows():
        if row['Username'] == username and row["Password"] == password:
            if row['Position'] == "Knitting Operator":
                st.switch_page("pages/Knitting Operator Page.py")

            elif row['Position'] == "Knitting Doffer":
                st.switch_page('pages/Knitting Doffer Page.py')
                
            elif row['Position'] == "Knitting Tech":
                st.switch_page('pages/Knitting Tech Page.py')

            elif row['Position'] == "Knitting Over Hauler":
                st.switch_page('pages/Knitting Over Hauler Page.py')

            elif row['Position'] == "Cut and Sew":
                st.switch_page('pages/Cut and Sew Page.py')

            elif row['Position'] == "Ring Spinning Operator":
                st.switch_page('pages/Ring Spinning Operator Page.py')

            elif row['Position'] == "Ring Spinning Tech":
                st.switch_page('pages/Ring Spinning Tech Page.py')

            elif row['Position'] == "Ring Spinning Over Hauler":
                st.switch_page('pages/Ring Spinning Over Hauler Page.py')

            elif row['Position'] == "Winder Operator":
                st.switch_page('pages/Winder Operator Page.py')

            elif row['Position'] == "Winder Tech":
                st.switch_page('pages/Winder Tech Page.py')

            elif row['Position'] == "Winder Over Hauler":
                st.switch_page('pages/Winder Over Hauler Page.py')

            elif row['Position'] == "MVS Operator":
                st.switch_page('pages/MVS Operator Page.py')

            elif row['Position'] == "MVS Tech":
                st.switch_page('pages/MVS Tech Page.py')

            elif row['Position'] == "MVS Over Hauler":
                st.switch_page('pages/MVS Over Hauler Page.py')

            elif row['Position'] == "MJS Operator":
                st.switch_page('pages/MJS Operator Page.py')

            elif row['Position'] == "MJS Tech":
                st.switch_page('pages/MJS Tech Page.py')

            elif row['Position'] == "MJS Over Hauler":
                st.switch_page('pages/MJS Over Hauler Page.py')

            elif row['Position'] == "Card Room Operator":
                st.switch_page('pages/Card Room Operator Page.py')

            elif row['Position'] == "Card Room Tech":
                st.switch_page('pages/Card Room Tech Page.py')

            elif row['Position'] == "Card Room Over Hauler":
                st.switch_page('pages/Card Room Over Hauler Page.py')

    error_login = st.error("Incorrect Username/Password")
    time.sleep(3)
    error_login = error_login.empty()
