import pandas as pd
import streamlit as st

#membaca file csv
data = pd.read_csv('rekap.csv')
#membuat list nama-nama yang ada di data
nama_list = data['Nama'].unique().tolist()

#menambahkan pilihan dropdown untuk memilih nama individu
selected_name = st.selectbox('Pilih nama individu:', nama_list)

#memilih data untuk individu yang dipilih
selected_data = data[data['Nama'] == selected_name]

#menghitung rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
mean_data = data.iloc[:, 1:].apply(lambda x: pd.Series({
    'Hadir': x.str.contains('Hadir').sum(),
    'Sakit': x.str.contains('Sakit').sum(),
    'Izin': x.str.contains('Izin').sum(),
    'Alpa': x.str.contains('Alpa').sum()
})).reset_index().groupby('index').mean()

#menghitung jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
selected_columns = st.multiselect('Pilih kolom:', data.columns[1:].tolist())
count_data = selected_data[selected_columns].apply(pd.Series.value_counts).fillna(0).astype(int)
count_data.columns = pd.MultiIndex.from_product([[selected_name], count_data.columns.tolist()])

#menampilkan rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
st.write('### Rata-rata Kehadiran')
st.write(mean_data)

#menampilkan tabel kehadiran, sakit, izin, dan alpa untuk individu yang dipilih
st.write('### Tabel Kehadiran Individu')
st.write(selected_data)

#menampilkan tabel jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
count_data = count_data.stack().reset_index().rename(columns={'level_0': 'Keterangan', 'level_1': 'Kolom', 0: 'Jumlah'})
count_data['Keterangan'] = count_data['Keterangan'].replace({'Alpa': 'Alpa', 'Sakit': 'Sakit', 'Izin': 'Izin'})
st.write('### Tabel Jumlah Kehadiran pada Kolom Tertentu')
st.write(count_data)

#menampilkan total alpa, sakit, dan izin pada kolom-kolom yang dipilih
total_data = count_data.groupby('Keterangan').sum().reset_index().rename(columns={'Keterangan': 'Keterangan Tidak Hadir'})
st.write('### Total Alpa, Sakit, dan Izin pada Kolom Tertentu')
st.write(total_data)
