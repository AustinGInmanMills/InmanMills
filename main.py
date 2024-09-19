import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("Read Google Sheet as DataFrame")

conn = st.connection("gsheets",type=GSheetsConnection)
cdf = conn.read(worksheet="Machine #1")

st.write(cdc)