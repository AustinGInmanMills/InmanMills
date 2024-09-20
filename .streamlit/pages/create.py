from dbm import error

import pandas as pd
import streamlit as st
from streamlit import success
from streamlit_gsheets import GSheetsConnection
import time


conn = st.connection("gsheets", type=GSheetsConnection)


employee_data = conn.read(worksheet="Employees", ttl=0)
employee_data = pd.DataFrame(employee_data)


placeholder = st.empty()


with placeholder.form("Create"):
    username = st.text_input("Username", key="Create Account Username")
    password = st.text_input("Password", key="Create Account Password")
    employee_id = st.text_input("Employee ID", key="EmployeeID")
    registration_code = st.text_input("Registration Code", key="RegistrationCode")
    register = st.form_submit_button("Create Account")
    if register:
        if registration_code == "SBPKO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Knitting Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPKD":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Knitting Doffer", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPKT":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Knitting Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPKOH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Knitting Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPCS":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Cut and Sew", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPRSO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Ring Spinning Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPRST":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Ring Spinning Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPRSOH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Ring Spinning Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPWO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Winder Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPWT":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Winder Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPWOH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Winder Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMSO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MVS Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMST":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MVS Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMSOH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MVS Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMJO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MJS Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMJT":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MJS Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPMJOH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "MJS Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPCRO":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Card Room Operator", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPCRT":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Card Room Tech", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPCROH":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Card Room Over Hauler", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")


        elif registration_code == "SBPS":
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
                        success = success("Account successfully created")
                        employee_data.loc[len(employee_data.index)] = [username, password, "Supervisor", employee_id]
                        conn.update(worksheet="Employees", data=employee_data)
                        time.sleep(2)
                        success = success.empty()
                        st.switch_page("pages/login.py")
        else:
            error = st.error("Invalid Registration Code Contact Supervisor For Correct Code")
            time.sleep(3)
            error = error.empty()
