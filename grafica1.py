import streamlit as st
import datetime
import pandas as pd
import matplotlib.pyplot as plt

titanic_data = pd.read_csv("https://raw.githubusercontent.com/adsoftsito/ciencia-datos/refs/heads/main/titanic.csv")
st.dataframe(titanic_data)
st.header("Data Description")

fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del titanic")
st.pyplot(fig)

st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')

st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

st.markdown("___")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)


import pandas as pd
import numpy as np
import streamlit as st

st.title('Uber pickups in NYC')
DATE_COLUMN = 'date/time'
DATA_URL = ('/content/uber_dataset.csv')

def load_data(nrows):
 data = pd.read_csv(DATA_URL, nrows=nrows)
 lowercase = lambda x: str(x).lower()
 data.rename(lowercase, axis='columns', inplace=True)
 data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
 return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader('Map of all pickups at %s:00' % hour_to_filter)

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)