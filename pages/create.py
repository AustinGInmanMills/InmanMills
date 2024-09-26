import gspread
import pandas as pd
import streamlit as st
from streamlit import success
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

try:
    conn = st.connection("gsheets", type=GSheetsConnection)

    placeholder = st.empty()

    with placeholder.form("Create"):
        username = st.text_input("Username", key="Create Account Username")
        password = st.text_input("Password", key="Create Account Password")
        employee_id = st.text_input("Employee ID", key="EmployeeID")
        col1, col2 = st.columns([1, 4])
        with col1:
            register = st.form_submit_button("Create Account")
        with col2:
            back = st.form_submit_button("Cancel")
        if back:
            st.switch_page("pages/login.py")
        if register:
            try:
                employee_data = conn.read(worksheet="Employees Login", ttl="120s", max_entries=800)
                employee_name = conn.read(worksheet="Employees Data", ttl="120s", max_entries=800)
                employee_data = pd.DataFrame(employee_data)
                employee_name = pd.DataFrame(employee_name)
                if employee_id in employee_name.values:

                    if employee_id in employee_data.values:
                        error_id = st.error(
                            "You are already in the database contact Supervisor if you forgot your login")
                        time.sleep(2)
                        error_id = error_id.empty()
                    else:
                        if username in employee_data.values:
                            error_username = st.error("Username already exist")
                            time.sleep(3)
                            error_username = error_username.empty()
                        else:
                            for x, row in employee_name.iterrows():
                                if row["Employee ID"] == employee_id:
                                    position = row["Position"]
                                    break
                            success = success("Account Successfully Created")
                            employee_data.loc[len(employee_data.index)] = [username, password, position, employee_id, "Offline"]
                            conn.update(worksheet="Employees Login", data=employee_data)
                            time.sleep(2)
                            success = success.empty()
                            st.switch_page("pages/login.py")
                else:
                    error_no_id_found = st.error("Employee ID not found")
                    time.sleep(3)
                    error_username = error_no_id_found.empty()
            except gspread.exceptions.APIError:
                error_gsheet_connection = st.error("Connection to server lost reconnecting please wait")
                time.sleep(5)
                error_gsheet_connection.empty()
except gspread.exceptions.APIError:
    error_gsheet_connection = st.error("Connection to server lost reconnecting please wait")
    time.sleep(5)
    st.rerun()
