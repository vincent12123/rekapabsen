import pandas as pd
import streamlit as st

# membaca file csv
data = pd.read_csv('rekap.csv')

# menghitung rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
mean_data = data.iloc[:, 1:].apply(lambda x: pd.Series({
    'Hadir': x.str.contains('Hadir').sum(),
    'Sakit': x.str.contains('Sakit').sum(),
    'Izin': x.str.contains('Izin').sum(),
    'Alpa': x.str.contains('Alpa').sum()
})).reset_index().groupby('index').mean()

# menampilkan nama-nama yang alpa pada setiap kolom
alpa_columns = []
for column in data.columns[1:]:
    alpa_data = data[data[column] == 'Alpa']['Nama'].tolist()
    alpa_columns.append(alpa_data)

# menampilkan hasil
st.write('Rata-rata Kehadiran, Sakit, Izin, dan Alpa per Nama')
st.write(mean_data)

st.write('Nama-nama yang Alpa pada Setiap Kolom')
for i, column in enumerate(data.columns[1:]):
    st.write(column)
    st.write(alpa_columns[i])
