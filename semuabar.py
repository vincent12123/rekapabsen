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

# mengubah indeks menjadi kolom 'Tanggal'
selected_data = selected_data.reset_index()

# memutar data menggunakan method pivot()
pivot_data = selected_data.pivot(index='Tanggal', columns='Keterangan', values='Jam')

# membuat chart line
fig, ax = plt.subplots()
x_labels = pivot_data.index
hadir = pivot_data['Hadir']
sakit = pivot_data['Sakit']
izin = pivot_data['Izin']
alpa = pivot_data['Alpa']
ax.plot(x_labels, hadir, label='Hadir')
ax.plot(x_labels, sakit, label='Sakit')
ax.plot(x_labels, izin, label='Izin')
ax.plot(x_labels, alpa, label='Alpa')
ax.set_title('Chart Kehadiran {}'.format(selected_name))
ax.set_xlabel('Tanggal')
ax.set_ylabel('Jumlah')
ax.legend()

# menampilkan chart
st.pyplot(fig)
