import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time
from datetime import datetime
from datetime import date
import pytz

if "name" not in st.session_state:
    name = str(st.query_params.name)
    username = str(st.query_params.username)
    shift = str(st.query_params.shift)
else:
    name = str(st.session_state.name)
    username = str(st.session_state.username)
    shift = str(st.session_state.shift)

conn = st.connection("gsheets", type=GSheetsConnection)
employee_login_status = conn.read(worksheet="Employees Login", ttl="35s")
employee_login_status = pd.DataFrame(employee_login_status)

for sd, rowzs in employee_login_status.iterrows():
    if rowzs["Username"] == username:
        if rowzs["Status"] != "Online":
            st.switch_page("pages/login.py")

position = conn.read(worksheet="Knitting Positions", ttl="35s")
position = pd.DataFrame(position)

for x, row in position.iterrows():
    if row["Operator"] == name:
        machine_1 = row["Machine 1"]
        machine_2 = row["Machine 2"]
        machine_1_flags_data = conn.read(worksheet=f"Knitting Machine {machine_1} Flag Sheet", ttl="2s")
        machine_1_flags_data = pd.DataFrame(machine_1_flags_data)
        machine_2_flags_data = conn.read(worksheet=f"Knitting Machine {machine_2} Flag Sheet", ttl="2s")
        machine_2_flags_data = pd.DataFrame(machine_2_flags_data)


today = str(date.today())
now = datetime.now(tz=pytz.timezone('US/Eastern'))
current_time = now.strftime("%I:%M %p")

tab1, tab2, tab3 = st.tabs([f"Machine {machine_1}", f"Machine {machine_2}", "Schedule Information"])

with tab1:
    with st.form("Machine 1", clear_on_submit=True):
        st.write(f"Machine {machine_1} Defect Log ")
        defect_time = st.number_input("Defect REVS", min_value=0, max_value=None, value=None,key="Defect REV")
        defect_type = st.selectbox(
            "Defect Type",
            ("Unknown Stop", "Needle Run", "Drop Stitch", "Hole", "Press Off", "Oil Spot", "Slub Hole", "Heavy Ends",
             "Thin Ends", "Closed Latch"),
            index=None,
        )
        submit = st.form_submit_button("Submit")
        if submit:
            machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [name, shift, today, current_time, "-", defect_time, defect_type]
            conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
            success_defect_update_1 = st.success("Successfully Submitted")
            time.sleep(2)
            success_defect_update_1 = success_defect_update_1.empty()

    with st.form("Machine 1 Doff", clear_on_submit=False):
        st.write(f"Machine {machine_1} Doff Log")
        start_roll = st.form_submit_button("Start Roll")
        if start_roll:
            if "Start" in machine_1_flags_data.values:
                for index, row in machine_1_flags_data[::-1].iterrows():
                    if row["Start/Doff"] == "-":
                        pass
                    elif row["Start/Doff"] == "Start":
                        error_cant_start = st.error("Roll Hasn't Doffed Yet")
                        time.sleep(2)
                        error_cant_start = error_cant_start.empty()
                        break
                    else:
                        machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [name, shift, today, current_time, "Start", "-", "-"]
                        conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
                        success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                        time.sleep(2)
                        success_new_roll_submit = success_new_roll_submit.empty()
            else:
                machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [name, shift, today, current_time, "Start", "-", "-"]
                conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
                success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                time.sleep(2)
                success_new_roll_submit = success_new_roll_submit.empty()

        end_roll = st.form_submit_button("Doff Roll")
        if end_roll:
            if "Doff" in machine_1_flags_data.values:
                for index, row in machine_1_flags_data[::-1].iterrows():
                    if row["Start/Doff"] == "-":
                        pass
                    elif row["Start/Doff"] == "Doff":
                        error_cant_start = st.error(f"Machine {machine_1} Hasn't Started A New Roll Yet")
                        time.sleep(2)
                        error_cant_start = error_cant_start.empty()
                        break
                    else:
                        machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [name, shift, today, current_time, "Doff", "-", "-"]
                        conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
                        success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                        time.sleep(2)
                        success_new_roll_submit = success_new_roll_submit.empty()
            else:
                machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [name, shift, today, current_time, "Doff", "-", "-"]
                conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
                success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                time.sleep(2)
                success_new_roll_submit = success_new_roll_submit.empty()

with tab2:
    with st.form("Machine 2", clear_on_submit=True):
        st.write(f"Machine {machine_2} Defect Log ")
        defect_time = st.number_input("Defect REVS", min_value=0, max_value=None, value=None,key="Defect REV2")
        defect_type = st.selectbox(
            "Defect Type",
            ("Unknown Stop", "Needle Run", "Drop Stitch", "Hole", "Press Off", "Oil Spot", "Slub Hole", "Heavy Ends",
             "Thin Ends", "Closed Latch"),
            index=None,
        )
        submit = st.form_submit_button("Submit")
        if submit:
            machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [name, shift, today, current_time, "-", defect_time, defect_type]
            conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
            success_defect_update_2 = st.success("Successfully Submitted")
            time.sleep(2)
            success_defect_update_2 = success_defect_update_2.empty()

    with st.form("Machine 2 Doff", clear_on_submit=False):
        st.write(f"Machine {machine_2} Doff Log")
        start_roll = st.form_submit_button("Start Roll")
        if start_roll:
            if "Start" in machine_2_flags_data.values:
                for index, row in machine_2_flags_data[::-1].iterrows():
                    if row["Start/Doff"] == "-":
                        pass
                    elif row["Start/Doff"] == "Start":
                        error_cant_start2 = st.error("Roll Hasn't Doffed Yet")
                        time.sleep(2)
                        error_cant_start2 = error_cant_start2.empty()
                        break
                    else:
                        machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [name, shift, today, current_time, "Start", "-", "-"]
                        conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
                        success_new_roll_submit2 = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                        time.sleep(2)
                        success_new_roll_submit2 = success_new_roll_submit2.empty()
            else:
                machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [name, shift, today, current_time, "Start", "-", "-"]
                conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
                success_new_roll_submit2 = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                time.sleep(2)
                success_new_roll_submit2 = success_new_roll_submit2.empty()

        end_roll = st.form_submit_button("Doff Roll")
        if end_roll:
            if "Doff" in machine_2_flags_data.values:
                for index, row in machine_2_flags_data[::-1].iterrows():
                    if row["Start/Doff"] == "-":
                        pass
                    elif row["Start/Doff"] == "Doff":
                        error_cant_start2 = st.error(f"Machine {machine_2} Hasn't Started A New Roll Yet")
                        time.sleep(2)
                        error_cant_start2 = error_cant_start2.empty()
                        break
                    else:
                        machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [name, shift, today, current_time, "Doff", "-", "-"]
                        conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
                        success_new_roll_submit2 = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                        time.sleep(2)
                        success_new_roll_submit2 = success_new_roll_submit2.empty()
            else:
                machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [name, shift, today, current_time, "Doff", "-", "-"]
                conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
                success_new_roll_submit2 = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                time.sleep(2)
                success_new_roll_submit2 = success_new_roll_submit2.empty()

sign_out = st.button("Sign out")
if sign_out:
    for sf, sows in employee_login_status.iterrows():
        if sows["Username"] == username:
            if sows["Status"] == "Online":
                sows["Status"] = "Offline"
                conn.update(worksheet="Employees Login", data=employee_login_status)
                st.session_state.clear()
                st.query_params.clear()
                time.sleep(0.5)
                st.switch_page("pages/login.py")
