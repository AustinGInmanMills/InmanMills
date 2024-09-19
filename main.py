import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection



conn = st.connection("gsheets",type=GSheetsConnection)
cdf = conn.read(worksheet="Knitting Machines Data", ttl=0)
cdf = pd.DataFrame(cdf)
st.write(cdf, hide_index=True)