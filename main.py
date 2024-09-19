from platform import machine
from types import NoneType

import streamlit as st
import pandas as pd
from streamlit import form_submit_button
from streamlit_gsheets import GSheetsConnection
from math import trunc

st.set_page_config(
    page_title="Inman Mills Saybrook",
    page_icon="",
)

conn = st.connection("gsheets", type=GSheetsConnection) # Connects to gSheet conn used for connect
machines_data = conn.read(worksheet="Knitting Machines Data", ttl=0)
machines_data = pd.DataFrame(machines_data)

hide_st_style = """  
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """ #Hides streamlit information on web app
st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(
    body="""
        <style>
            .block-container{
                    padding-top: 25px;
                }
        </style>
    """,
    unsafe_allow_html=True # Deletes white space on top of web app
)

tab1, tab2, tab3 = st.tabs(["Home", "Departments", "Information"])

########################################HOME PAGE###################################################################################################

with tab1:
    st.markdown("Welcome to Inman Mills Saybrook Plant new Employee website! You can view information about up coming layoffs, overtime, departments and much more.")



########################################DEPARTMENTS PAGE###################################################################################################

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
            ("Machine Information", "Update Machine Information", "Technician Chat"),
            index=None,
            key="KnittingBox",
        )

        if knitting_bttn == "Machine Information":
            st.dataframe(pd.DataFrame(machines_data), hide_index=True)

        if knitting_bttn == "Update Machine Information":
            st.caption("Double click a block to edit")
            knitting_machine_db_update = st.data_editor(str(machines_data), hide_index=True) #need to find way to edit ints and floats values
            with st.form(key="UpdateKnittingMachineDataForm", clear_on_submit=True):

                updateknittingmachinedataformbttn = form_submit_button("Submit")

#############################################DOFF CALCULATOR#######################################################################################

        if knitting_bttn is None:
            st.divider()
            st.subheader("Doff Time Calculator")

            calculator_machine_number = st.number_input("Machine Number ", value=None, min_value=0, max_value=21,
                                                        placeholder="")

            calculator_machine_revs = st.number_input("Current Revs", value=None, min_value=0, max_value=5000,
                                                      placeholder="")

            calculator_bttn = st.button("Calculate")

            if calculator_bttn:
                if calculator_machine_number is not None and calculator_machine_revs is not None:
                    calculator_machine_entered_rpms = machines_data.loc[int(calculator_machine_number), "Rpms"]
                    calculator_machine_entered_doff = machines_data.loc[int(calculator_machine_number), "Doff"]
                    sum = calculator_machine_entered_doff - calculator_machine_revs
                    sum = sum / calculator_machine_entered_rpms
                    if sum > 60:
                        sum = sum / 60
                        number_dec1 = trunc(sum)
                        number_dec2 = str(sum - int(sum))[1:]
                        minutes_calc = float(number_dec2) * 60
                        minutes_calc = trunc(minutes_calc)
                        calculation = str(sum)
                        st.write(str(number_dec1), "hour and", str(minutes_calc), "minutes left")
                    else:
                        number_dec1 = trunc(sum)
                        number_dec2 = str(sum - int(sum))[1:]
                        minutes_calc = float(number_dec2) * 60
                        minutes_calc = trunc(minutes_calc)
                        calculation = str(sum)
                        st.write(str(number_dec1), "minutes and", str(minutes_calc), "seconds left")

#############################################END CALCULATOR######################################################################################################

    elif department_options_bttn == "Ring Spinning":
        ring_spinning_bttn = st.selectbox(
            "Ring Spinning Department Options",
            ("Machine Information", "Update Machine Information", "Technician Chat"),
            index=None,
            key="RingSpinningBox"
        )

    elif department_options_bttn == "Winding":
        winding_btnn = st.selectbox(
            "Winding Department Options",
            ("Machine Information", "Update Machine Information", "Technician Chat"),
            index=None,
            key="WindingBox"
        )

    elif department_options_bttn == "Roven":
        roven_bttn = st.selectbox(
            "Roven Department Options",
            ("Machine Information", "Update Machine Information", "Technician Chat"),
            index=None,
            key="RovenBox"
        )
