import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# membaca file csv
data = pd.read_csv('rekap.csv')

# membuat list nama-nama yang ada di data
nama_list = data['Nama'].unique().tolist()

# menambahkan pilihan dropdown untuk memilih nama individu
selected_name = st.selectbox('Pilih nama individu:', nama_list)

# memilih data untuk individu yang dipilih
selected_data = data[data['Nama'] == selected_name]

# menghitung jumlah kehadiran, sakit, izin, dan alpa dalam rentang waktu tertentu
hadir = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Hadir').sum())
sakit = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Sakit').sum())
izin = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Izin').sum())
alpa = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Alpa').sum())

# membuat chart bar
fig, ax = plt.subplots()
ax.bar(['Hadir', 'Sakit', 'Izin', 'Alpa'], [hadir.sum(), sakit.sum(), izin.sum(), alpa.sum()])

# menambahkan label pada setiap bar chart
for i, v in enumerate([hadir.sum(), sakit.sum(), izin.sum(), alpa.sum()]):
    ax.text(i, v + 1, str(v), ha='center', fontsize=10)

ax.set_title('Chart Kehadiran {}'.format(selected_name))
ax.set_xlabel('Kategori')
ax.set_ylabel('Jumlah')

# menampilkan chart
st.pyplot(fig)
