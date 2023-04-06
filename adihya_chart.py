import pandas as pd
import matplotlib.pyplot as plt

# membaca file csv
data = pd.read_csv('rekap.csv')

# memilih data untuk Adhitya Deva Saputra
aditya_data = data[data['Nama'] == 'Yuvensius Rimbaka Liska Isongori']

# menghitung jumlah kehadiran, sakit, izin, dan alpa dalam rentang waktu tertentu
#hadir = aditya_data.iloc[:, 1:].apply(lambda x: x.str.contains('Hadir').sum())
sakit = aditya_data.iloc[:, 1:].apply(lambda x: x.str.contains('Sakit').sum())
izin = aditya_data.iloc[:, 1:].apply(lambda x: x.str.contains('Izin').sum())
alpa = aditya_data.iloc[:, 1:].apply(lambda x: x.str.contains('Alpa').sum())

# membuat chart bar
#plt.bar(['Hadir', 'Sakit', 'Izin', 'Alpa'], [hadir.sum(), sakit.sum(), izin.sum(), alpa.sum()])
#plt.bar(['Hadir', 'Sakit', 'Izin', 'Alpa'], [sakit.sum(), izin.sum(), alpa.sum()])
plt.bar(['Sakit', 'Izin', 'Alpa'], [sakit.sum(), izin.sum(), alpa.sum()])
plt.title('Chart Kehadiran Adhitya Deva Saputra')
plt.xlabel('Kategori')
plt.ylabel('Jumlah')
plt.show()
