import pandas as pd
import streamlit as st

# membaca file csv
data = pd.read_csv('rekap.csv')

# memilih kolom-kolom yang akan dihitung jumlah kehadirannya
selected_columns = st.multiselect('Pilih kolom:', data.columns[1:].tolist())

if len(selected_columns) > 0:
    # menghitung jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
    count_data = data[selected_columns].apply(pd.Series.value_counts).fillna(0).astype(int)

    # memfilter data berdasarkan kondisi kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
    alpa_data = data[data[selected_columns].apply(lambda x: (x == 'Alpa').any(), axis=1)][['Nama']]
    sakit_data = data[data[selected_columns].apply(lambda x: (x == 'Sakit').any(), axis=1)][['Nama']]
    izin_data = data[data[selected_columns].apply(lambda x: (x == 'Izin').any(), axis=1)][['Nama']]

    # menampilkan daftar nama yang alpa, sakit, dan izin pada kolom-kolom yang dipilih
    st.write('### Daftar Nama Alpa')
    st.write(alpa_data)
    st.write('### Daftar Nama Sakit')
    st.write(sakit_data)
    st.write('### Daftar Nama Izin')
    st.write(izin_data)
else:
    st.warning('Silahkan pilih kolom terlebih dahulu.')
