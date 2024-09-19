import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.write("Knitting Machine Database")

conn = st.connection("gsheets",type=GSheetsConnection)
cdf = conn.read(worksheet="Knitting Machines Data", ttl=0)
ddd = pd.DataFrame(cdf)


st.write(ddd)