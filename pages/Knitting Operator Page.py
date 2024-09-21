import streamlit as st
import pandas as pd
from streamlit import session_state
from streamlit_gsheets import GSheetsConnection

if not "Name" in st.session_state:
    st.switch_page("pages/login.py")

conn = st.connection("gsheets", type=GSheetsConnection)
position = conn.read(worksheet="Knitting Positions")
position = pd.DataFrame(position)

for x, row in position.iterrows():
    if row["Operator"] == st.session_state.Name:
        machine_1 = row["Machine 1"]
        machine_2 = row["Machine 2"]

tab1, tab2, tab3 = st.tabs([f"Machine {machine_1}", f"Machine {machine_2}", "Schedule Information"])

with tab1:
    st.write("Defect Log")
    defect_time = st.number_input("Defect REVS",value=None, key="Defect REV")
    defect_type = st.selectbox(
        "Defect Type",
        ("Unknown Stop", "Needle Run", "Drop Stitch", "Hole", "Press Off", "Oil Spot", "Slub Hole", "Heavy Ends", "Thin Ends", "Closed Latch"),
        index=None
    )
    submit_defect = st.button("Submit", key="SubmitDefect1")

    if submit_defect:
        st.write("Submited")
