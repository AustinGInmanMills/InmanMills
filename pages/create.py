import pandas as pd
import streamlit as st
from streamlit import success
from streamlit_gsheets import GSheetsConnection
import time


conn = st.connection("gsheets", type=GSheetsConnection)


employee_data = conn.read(worksheet="Employees Login", ttl=0)
employee_information = conn.read(worksheet="Employees Data", ttl=0)
employee_data = pd.DataFrame(employee_data)
employee_information = pd.DataFrame(employee_information)


placeholder = st.empty()


with placeholder.form("Create"):
    username = st.text_input("Username", key="Create Account Username")
    password = st.text_input("Password", key="Create Account Password")
    employee_id = st.text_input("Employee ID", key="EmployeeID")
    registration_code = st.text_input("Registration Code", key="RegistrationCode")
    col1, col2 = st.columns([1, 4])
    with col1:
        register = st.form_submit_button("Create Account")
    with col2:
        back = st.form_submit_button("Back")
    if back:
        st.switch_page("pages/login.py")
    if register:
        if registration_code == "Saybrook Plant":
            if employee_id in employee_information.values:

                if employee_id in employee_data.values:
                    error_id = st.error("You are already in the database contact Supervisor if you forgot your login")
                    time.sleep(3)
                    error_id = error_id.empty()
                else:
                    if username in employee_data.values:
                        error_username = st.error("Username already exist")
                        time.sleep(3)
                        error_username = error_username.empty()
                    else:
                        for x, row in employee_information.iterrows():
                            if row["Employee ID"] == employee_id:
                                position = row["Position"]
                                break
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, position, employee_id]
                        conn.update(worksheet="Employees Login", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")
            else:
                error_no_id_found = st.error("Employee ID not found")
                time.sleep(3)
                error_username = error_no_id_found.empty()
        else:
            error = st.error("Invalid Registration Code Contact Supervisor For Correct Code")
            time.sleep(3)
            error = error.empty()
