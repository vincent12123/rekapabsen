import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows

# membaca file CSV
df = pd.read_csv("rekap.csv")

# menentukan kolom tanggal yang akan dianalisis
kolom_tanggal = df.columns[1:]

# membuat tabel untuk menampung hasil
tabel_hasil = pd.DataFrame(columns=["Tanggal", "Alpa", "Sakit", "Izin"])

# loop melalui setiap tanggal dan menemukan orang yang alpa, sakit, atau izin
for tanggal in kolom_tanggal:
    orang_alpa = df.loc[df[tanggal] == "Alpa", "Nama"]
    orang_sakit = df.loc[df[tanggal] == "Sakit", "Nama"]
    orang_izin = df.loc[df[tanggal] == "Izin", "Nama"]
    
    # menambahkan baris pada tabel hasil
    if len(orang_alpa) > 0 or len(orang_sakit) > 0 or len(orang_izin) > 0:
        tabel_hasil = pd.concat([tabel_hasil, pd.DataFrame({"Tanggal": [tanggal], "Alpa": [", ".join(list(orang_alpa))], "Sakit": [", ".join(list(orang_sakit))], "Izin": [", ".join(list(orang_izin))]})])

# menyimpan tabel hasil ke dalam file Excel
with pd.ExcelWriter('hasil_analisis.xlsx', engine='openpyxl') as writer:
    writer.book = Workbook()
    tabel_hasil.to_excel(writer, sheet_name='Sheet1', index=False)
    sheet = writer.sheets['Sheet1']
    
    # mengatur lebar kolom
    for col in sheet.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        sheet.column_dimensions[column].width = adjusted_width
