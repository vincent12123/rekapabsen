import pandas as pd
import streamlit as st

# membaca file csv
data = pd.read_csv('rekap.csv')

# membuat list nama-nama yang ada di data
nama_list = data['Nama'].unique().tolist()

# menambahkan pilihan dropdown untuk memilih nama individu
selected_name = st.selectbox('Pilih nama individu:', nama_list)

# memilih data untuk individu yang dipilih
selected_data = data[data['Nama'] == selected_name]

# menghitung rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
mean_data = data.iloc[:, 1:].apply(lambda x: pd.Series({
    'Hadir': x.str.contains('Hadir').sum(),
    'Sakit': x.str.contains('Sakit').sum(),
    'Izin': x.str.contains('Izin').sum(),
    'Alpa': x.str.contains('Alpa').sum()
})).reset_index().groupby('index').mean()

# menghitung total alpa, sakit, dan izin untuk individu yang dipilih
total_alpa = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Alpa').sum()).sum()
total_sakit = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Sakit').sum()).sum()
total_izin = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Izin').sum()).sum()

# menampilkan rata-rata kehadiran, jumlah alpa, sakit, dan izin untuk individu yang dipilih
st.write('### Rata-rata Kehadiran, Jumlah Alpa, Sakit, dan Izin untuk Setiap Nama')
st.write(mean_data)

st.write('### Analisis Kehadiran untuk {}'.format(selected_name))
st.write('**Total Alpa:** {}'.format(total_alpa))
st.write('**Total Sakit:** {}'.format(total_sakit))
st.write('**Total Izin:** {}'.format(total_izin))
st.write('**Daftar Kolom dengan Alpa:**')
for col in selected_data.columns[selected_data.isin(['Alpa']).any()]:
    st.write('- {}'.format(col))
st.write('**Daftar Kolom dengan Sakit:**')
for col in selected_data.columns[selected_data.isin(['Sakit']).any()]:
    st.write('- {}'.format(col))
st.write('**Daftar Kolom dengan Izin:**')
for col in selected_data.columns[selected_data.isin(['Izin']).any()]:
    st.write('- {}'.format(col))
