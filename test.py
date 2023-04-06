import pandas as pd
import streamlit as st

# load data dari file CSV
data = pd.read_csv("rekap.csv")

# membuat kolom baru untuk status kehadiran
data["Status"] = "Hadir"
data.loc[data["7/11/2022"] == "Alpa", "Status"] = "Alpa"
data.loc[data["7/11/2022"] == "Sakit", "Status"] = "Sakit"
data.loc[data["7/11/2022"] == "Izin", "Status"] = "Izin"

# menghitung jumlah hadir, alpa, sakit, dan izin untuk setiap orang
summary = data.groupby("Nama")["Status"].value_counts().unstack(fill_value=0)
summary = summary[["Hadir", "Alpa", "Sakit", "Izin"]]

# menampilkan tabel hasil
st.write("""
    ## Rekap Kehadiran Karyawan
""")
st.table(summary.style.set_properties(**{'text-align': 'center', 'border': '1px solid black', 'font-size': '14px', 'font-family': 'Arial'}).set_table_styles([{'selector': 'th', 'props': [('text-align', 'center'), ('font-size', '16px'), ('border', '1px solid black')]}]).set_page_width(800))
