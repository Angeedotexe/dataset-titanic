import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as ptl 

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(titanic_data)
st.header("Data Description")

fig, ax = ptl.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del titanic")
st.pyplot(fig)
