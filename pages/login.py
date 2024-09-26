import pandas as pd
import streamlit as st
import gspread.exceptions
from streamlit_gsheets import GSheetsConnection
import time

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

conn = st.connection("gsheets", type=GSheetsConnection)

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
    try:
        employee_data = conn.read(worksheet="Employees Login", ttl="60s")
        employee_data = pd.DataFrame(employee_data)
        employee_name = conn.read(worksheet="Employees Data", ttl="120s")
        employee_name = pd.DataFrame(employee_name)

        if not username in employee_data.values or not password in employee_data.values:
            error_user_not_found = st.error("Incorrect Username/Password")
            time.sleep(3)
            error_user_not_found = error_user_not_found.empty()

        for x, row in employee_data.iterrows():
            if row['Username'] == username and row["Password"] == password:
                for i, rows in employee_name.iterrows():
                    if rows["Employee ID"] == row["EmployeeID"]:
                        row["Status"] = "Online"
                        conn.update(worksheet="Employees Login", data=employee_data)
                        st.session_state.username = row["Username"]
                        st.session_state.name = str(rows["First Name"])
                        st.session_state.shift = str(rows["Shift"])
                        success_login = st.success(f"Welcome {rows["First Name"]}")
                        time.sleep(2)
                        success_login = success_login.empty()
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
    except gspread.exceptions.APIError:
        error_gsheet_connection = st.error("Connection to server lost reconnecting please wait")
        time.sleep(5)
        st.rerun()
