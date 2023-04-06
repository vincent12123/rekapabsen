import pandas as pd

# membaca file CSV
df = pd.read_csv("rekap.csv")

# menentukan tanggal yang akan dianalisis
tanggal = "7/14/2022"

# menemukan orang yang alpa pada tanggal tersebut
orang_alpa = df.loc[df[tanggal] == "Alpa", "Nama"]
orang_sakit = df.loc[df[tanggal] == "Sakit", "Nama"]
orang_izin = df.loc[df[tanggal] == "Izin", "Nama"]
# menampilkan hasil
print("Orang yang alpa pada tanggal", tanggal, "adalah:")
print(orang_alpa.to_string(index=False))
print("Orang yang Sakit pada tanggal", tanggal, "adalah:")
print(orang_sakit.to_string(index=False))
print("Orang yang Izin pada tanggal", tanggal, "adalah:")
print(orang_izin.to_string(index=False))