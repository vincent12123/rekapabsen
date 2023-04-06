import pandas as pd
import streamlit as st

# membaca file csv
data = pd.read_csv('rekap.csv')

# memilih kolom yang akan ditampilkan daftar kehadirannya
selected_column = st.selectbox('Pilih kolom:', data.columns[1:].tolist())

if selected_column:
    # mengambil data pada kolom yang dipilih
    column_data = data[selected_column]

    # membuat daftar nama yang alpa, sakit, dan izin pada kolom tertentu
    alpa_names = column_data[column_data.str.contains('Alpa', case=False)].index.tolist()
    sakit_names = column_data[column_data.str.contains('Sakit', case=False)].index.tolist()
    izin_names = column_data[column_data.str.contains('Izin', case=False)].index.tolist()

    # menampilkan daftar nama yang alpa, sakit, dan izin pada kolom tertentu
    st.write('### Daftar Nama yang Alpa')
    st.write(alpa_names)

    st.write('### Daftar Nama yang Sakit')
    st.write(sakit_names)

    st.write('### Daftar Nama yang Izin')
    st.write(izin_names)
