import pandas as pd
import matplotlib.pyplot as plt

# membaca data dari file CSV
data = pd.read_csv("rekap.csv")

# mengubah nilai "Hadir" menjadi 0, "Izin" menjadi 1, "Sakit" menjadi 2, dan "Alpa" menjadi 3
data = data.replace({"Hadir": 0, "Izin": 1, "Sakit": 2, "Alpa": 3})

# menghitung total izin, sakit, dan alpa yang diambil oleh setiap orang
total_izin = data.iloc[:, 1:].apply(lambda x: (x == 1).sum(), axis=1)
total_sakit = data.iloc[:, 1:].apply(lambda x: (x == 2).sum(), axis=1)
total_alpa = data.iloc[:, 1:].apply(lambda x: (x == 3).sum(), axis=1)

# membuat bar chart untuk total izin, sakit, dan alpa
plt.bar(data["Nama"], total_izin, label="Izin")
plt.bar(data["Nama"], total_sakit, label="Sakit", bottom=total_izin)
plt.bar(data["Nama"], total_alpa, label="Alpa", bottom=total_izin+total_sakit)

# menambahkan label dan judul
plt.xlabel("Nama")
plt.ylabel("Jumlah")
plt.title("Grafik Izin, Sakit, dan Alpa")

# menampilkan legenda
plt.legend()

# menampilkan grafik
plt.show()
