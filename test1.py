import streamlit as st
import pandas as pd

# membaca file csv
data = pd.read_csv('rekap.csv')

# memilih data untuk individu dan tanggal tertentu
selected_name = 'Yuvensius Rimbaka Liska Isongori'
selected_date = '7/11/2022'
selected_data = data[(data['Nama'] == selected_name) & (data['Tanggal'] == selected_date)]

# menampilkan dataframe pada Streamlit
st.dataframe(selected_data)
