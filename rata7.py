import pandas as pd
import streamlit as st

#membaca file csv
data = pd.read_csv('rekap.csv')

#menghitung rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
mean_data = data.iloc[:, 1:].apply(lambda x: pd.Series({
    'Hadir': x.str.contains('Hadir').sum(),
    'Sakit': x.str.contains('Sakit').sum(),
    'Izin': x.str.contains('Izin').sum(),
    'Alpa': x.str.contains('Alpa').sum()
})).reset_index().groupby('index').mean()

#menampilkan rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
st.write('### Rata-rata Kehadiran')
st.write(mean_data)

#menghitung jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
selected_columns = st.multiselect('Pilih kolom:', data.columns[1:].tolist())
count_data = data[selected_columns].apply(pd.Series.value_counts).fillna(0).astype(int)


#menampilkan tabel jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
st.write('### Tabel Jumlah Kehadiran pada Kolom Tertentu')
st.write(count_data)

#menghitung total alpa, sakit, dan izin pada kolom-kolom yang dipilih
total_data = count_data.sum().rename('Total').to_frame().transpose()

#menampilkan total alpa, sakit, dan izin pada kolom-kolom yang dipilih
st.write('### Total Alpa, Sakit, dan Izin pada Kolom Tertentu')
st.write(total_data)
