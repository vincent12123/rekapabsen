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

# menampilkan rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
st.write('### Rata-rata Kehadiran')
st.write(mean_data)

# menampilkan tabel kehadiran, sakit, izin, dan alpa untuk setiap individu
st.write('### Tabel Kehadiran Individu')
st.write(data)

#menghitung jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
selected_columns = st.multiselect('Pilih kolom:', data.columns[1:].tolist())
count_data = data[selected_columns].replace(['Alpa', 'Sakit', 'Izin'], [0, 1, 2]).apply(lambda x: pd.Series({
    'Alpa': (x == 0).sum(),
    'Sakit': (x == 1).sum(),
    'Izin': (x == 2).sum(),
}), axis=0).fillna(0).astype(int)

#menambahkan prefix 'Jumlah' pada nama kolom
count_data.columns = pd.MultiIndex.from_tuples([(f"Jumlah {col}", f"{col}") for col in count_data.columns])

#menampilkan tabel jumlah kehadiran, sakit, izin, dan alpa pada kolom-kolom yang dipilih
st.write('### Tabel Jumlah Kehadiran pada Kolom Tertentu')
st.write(count_data)


# menampilkan total alpa, sakit, dan izin pada kolom-kolom yang dipilih
total_data = count_data.sum()
total_data = total_data.rename(('Total', ''))
total_data = pd.DataFrame(total_data).transpose()

st.write('### Total Alpa, Sakit, dan Izin pada Kolom Tertentu')
st.write(total_data)
