import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
import time
from datetime import datetime
from datetime import date
from time import gmtime, strftime


today = str(date.today())
now = datetime.now()
current_time = now.strftime("%I:%M %p")

if not "Name" in st.session_state:
    st.switch_page("pages/login.py")

conn = st.connection("gsheets", type=GSheetsConnection)
position = conn.read(worksheet="Knitting Positions", ttl="10s")
position = pd.DataFrame(position)

for x, row in position.iterrows():
    if row["Operator"] == st.session_state.Name:
        machine_1 = row["Machine 1"]
        machine_2 = row["Machine 2"]

machine_1_flags_data = conn.read(worksheet=f"Knitting Machine {machine_1} Flag Sheet", ttl="35s")
machine_1_flags_data = pd.DataFrame(machine_1_flags_data)
machine_2_flags_data = conn.read(worksheet=f"Knitting Machine {machine_2} Flag Sheet", ttl="35s")
machine_2_flags_data = pd.DataFrame(machine_2_flags_data)
machine_1_doff_data = conn.read(worksheet=f"Knitting Machine {machine_1} Doff Log", ttl="35s")
machine_1_doff_data = pd.DataFrame(machine_1_doff_data)
machine_2_doff_data = conn.read(worksheet=f"Knitting Machine {machine_2} Doff Log", ttl="35s")
machine_2_doff_data = pd.DataFrame(machine_2_doff_data)








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
            machine_1_flags_data.loc[len(machine_1_flags_data.index)] = [st.session_state.Name, st.session_state.Shift, today, current_time, defect_time, defect_type]
            conn.update(worksheet=f"Knitting Machine {machine_1} Flag Sheet", data=machine_1_flags_data)
            success_defect_update_1 = st.success("Successfully Submitted")
            time.sleep(2)
            success_defect_update_1 = success_defect_update_1.empty()




    with st.form("Machine 1 Doff", clear_on_submit=False):
        st.write(f"Machine {machine_1} Doff Log")
        start_roll = st.form_submit_button("Start Roll")
        if start_roll:
            check_current_stats = machine_1_doff_data["Start/Doff"].iloc[-1:]
            if "Start" in check_current_stats.values:
                error_cant_start = st.error("Roll Hasn't Doffed Yet")
                time.sleep(2)
                error_cant_start = error_cant_start.empty()
            else:
                machine_1_doff_data.loc[len(machine_1_doff_data.index)] = [st.session_state.Name, today, current_time, st.session_state.Shift, "Start"]
                conn.update(worksheet=f"Knitting Machine {machine_1} Doff Log", data=machine_1_doff_data)
                success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                time.sleep(2)
                success_new_roll_submit = success_new_roll_submit.empty()

        end_roll = st.form_submit_button("Doff Roll")
        if end_roll:
            check_current_stats = machine_1_doff_data["Start/Doff"].iloc[-1:]
            if "Doff" in check_current_stats.values:
                error_cant_doff = st.error(f"Machine {machine_1} Hasn't Started A New Roll Yet")
                time.sleep(2)
                error_cant_doff = error_cant_doff.empty()
            else:
                machine_1_doff_data.loc[len(machine_1_doff_data.index)] = [st.session_state.Name, today, current_time, st.session_state.Shift, "Doff"]
                conn.update(worksheet=f"Knitting Machine {machine_1} Doff Log", data=machine_1_doff_data)
                success_doff_submit = st.success(f"Successfully Started New Roll On Machine {machine_1}")
                time.sleep(2)
                success_doff_submit = success_doff_submit.empty()








































with tab2:
    with st.form("Machine 2", clear_on_submit=True):
        st.write(f"Machine {machine_2} Defect Log")
        defect_time = st.number_input("Defect REVS", min_value=0, max_value=None, value=None, key="Defect REV2")
        defect_type = st.selectbox(
            "Defect Type",
            ("Unknown Stop", "Needle Run", "Drop Stitch", "Hole", "Press Off", "Oil Spot", "Slub Hole", "Heavy Ends",
             "Thin Ends", "Closed Latch"),
            index=None,
        )
        submit = st.form_submit_button("Submit")
        if submit:
            if not defect_time is None:
                if not defect_type is None:
                    machine_2_flags_data.loc[len(machine_2_flags_data.index)] = [st.session_state.Name, st.session_state.Shift, today, current_time, defect_time, defect_type]
                    conn.update(worksheet=f"Knitting Machine {machine_2} Flag Sheet", data=machine_2_flags_data)
                    success_defect_update_2 = st.success("Successfully Submitted")
                    time.sleep(2)
                    success_defect_update_2 = success_defect_update_2.empty()

                else:
                    error_input_type = st.error("Defect Type Is Empty")
                    time.sleep(2)
                    error_input_type = error_input_type.empty()

            else:
                error_input_time = st.error("Defect Revs Is Empty")
                time.sleep(2)
                error_input_time = error_input_time.empty()




    with st.form("Machine 2 Doff", clear_on_submit=False):
        st.write(f"Machine {machine_2} Doff Log")
        start_roll = st.form_submit_button("Start Roll")
        if start_roll:
            check_current_stats = machine_2_doff_data["Start/Doff"].iloc[-1:]
            if "Start" in check_current_stats.values:
                error_cant_start = st.error("Roll Hasn't Doffed Yet")
                time.sleep(2)
                error_cant_start = error_cant_start.empty()
            else:
                machine_2_doff_data.loc[len(machine_2_doff_data.index)] = [st.session_state.Name, today, current_time, st.session_state.Shift, "Start"]
                conn.update(worksheet=f"Knitting Machine {machine_2} Doff Log", data=machine_2_doff_data)
                success_new_roll_submit = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                time.sleep(2)
                success_new_roll_submit = success_new_roll_submit.empty()

        end_roll = st.form_submit_button("Doff Roll")
        if end_roll:
            check_current_stats = machine_2_doff_data["Start/Doff"].iloc[-1:]
            if "Doff" in check_current_stats.values:
                error_cant_doff = st.error(f"Machine {machine_2} Hasn't Started A New Roll Yet")
                time.sleep(2)
                error_cant_doff = error_cant_doff.empty()
            else:
                machine_2_doff_data.loc[len(machine_2_doff_data.index)] = [st.session_state.Name, today, current_time, st.session_state.Shift, "Doff"]
                conn.update(worksheet=f"Knitting Machine {machine_2} Doff Log", data=machine_2_doff_data)
                success_doff_submit = st.success(f"Successfully Started New Roll On Machine {machine_2}")
                time.sleep(2)
                success_doff_submit = success_doff_submit.empty()
