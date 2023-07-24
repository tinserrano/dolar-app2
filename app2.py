import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd


st.title("Dol-APP")
st.write("Algunas cotizaciones de los diferentes tipos de cambio de dólar. DYOR")
st.write("New connection feature, with <st.experimental_connection>")

#url = "https://docs.google.com/spreadsheets/d/1cXhsbQFNZeNPcPqtK0vLQx7GD28LQSmj4eveFnFdV9A/edit#gid=0"

url = st.secrets["public"]
#url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"

conn = st.experimental_connection("gsheets", type=GSheetsConnection)

data = conn.read(spreadsheet=url, usecols=[0, 1, 2, 3, 4])
st.dataframe(data)

#df = pd.DataFrame(data)
#st.title("Esto es en pandas")

#df = df.replace("\$","", regex=True)
#df = df.replace(",",".", regex=True)
#st.write(df)
#df["Cotizacion"] = df["Cotizacion"].astype(float, errors="raise")
#st.write(float(df["Cotizacion"][1]) * 5)
#st.write(df["Cotizacion"][2] * 7)
#st.write(df["Cotizacion"][3])
#st.write(df["Cotizacion"][4])
