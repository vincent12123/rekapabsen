import pandas as pd
import streamlit as st

# membaca file CSV
def load_data():
    df = pd.read_csv("rekap.csv")
    return df

# menentukan kolom tanggal yang akan dianalisis
def get_date_columns(df):
    return df.columns[1:]

# melakukan analisis dan mengembalikan tabel hasil
def analyze_data(df, tanggal):
    orang_alpa = df.loc[df[tanggal] == "Alpa", "Nama"]
    orang_sakit = df.loc[df[tanggal] == "Sakit", "Nama"]
    orang_izin = df.loc[df[tanggal] == "Izin", "Nama"]
    
    if len(orang_alpa) > 0 or len(orang_sakit) > 0 or len(orang_izin) > 0:
        return pd.DataFrame({"Tanggal": [tanggal], "Alpa": [", ".join(list(orang_alpa))], "Sakit": [", ".join(list(orang_sakit))], "Izin": [", ".join(list(orang_izin))]})
    else:
        return None

# menampilkan tabel hasil
def show_table(tabel_hasil):
    if tabel_hasil is not None:
        tabel_hasil_styled = tabel_hasil.style.set_properties(**{'text-align': 'left'}) \
                                            .set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]) \
                                            .set_properties(subset=['Tanggal'], **{'font-weight': 'bold'})
        st.write(tabel_hasil_styled, wide_mode=True)  # menambahkan opsi wide_mode

# membaca file CSV dan menampilkan tabel hasil
def main():
    st.title("Analisis Kehadiran")
    
    # membaca data dari file CSV
    df = load_data()
    
    # mendapatkan kolom tanggal
    kolom_tanggal = get_date_columns(df)
    
    # mengolah data untuk setiap tanggal
    for tanggal in kolom_tanggal:
        tabel_hasil = analyze_data(df, tanggal)
        show_table(tabel_hasil)

if __name__ == "__main__":
    main()
