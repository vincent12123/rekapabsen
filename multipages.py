import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

def intro():
    import streamlit as st
    import pandas as pd
    data = pd.read_csv('rekap.csv')
    st.write("# Selamat Datang di Rekap Harian RPL XII")
    st.markdown(
        """
        Halo Orang Tua RPL XII, selamat datang di rekap absensi kelas RPL XII. Rekap absensi ini akan memberikan informasi mengenai kehadiran, Ke tidak Hadiran dan izin anak Anda di kelas.

Kami telah memonitor absensi setiap anak di kelas dengan cermat dan secara teratur meng-update data ini untuk memastikan keakuratan informasi yang kami sampaikan kepada Anda.

Kami berharap dengan adanya rekap absensi ini, Anda dapat mengetahui seberapa sering anak Anda hadir di kelas dan membantu Anda memantau perkembangan akademiknya dengan lebih baik.

Terima kasih atas perhatian dan kerjasamanya.
    """
    ) 
    st.write('### Tabel Kehadiran Individu')
    st.write(data)
   
    st.sidebar.success("Silahkan pilih menu diatas .")

    
    
def daftar_hadir():
    import streamlit as st
    import pandas as pd
    

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

def Grafik():
    import pandas as pd
    import streamlit as st
    import matplotlib.pyplot as plt

    # membaca file csv
    data = pd.read_csv('rekap.csv')

    # membuat list nama-nama yang ada di data
    nama_list = data['Nama'].unique().tolist()

    # menambahkan pilihan dropdown untuk memilih nama individu
    selected_name = st.selectbox('Pilih nama individu:', nama_list)

    # memilih data untuk individu yang dipilih
    selected_data = data[data['Nama'] == selected_name]

    # menghitung jumlah kehadiran, sakit, izin, dan alpa dalam rentang waktu tertentu
    hadir = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Hadir').sum())
    sakit = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Sakit').sum())
    izin = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Izin').sum())
    alpa = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Alpa').sum())

    # membuat chart bar
    fig, ax = plt.subplots()
    ax.bar(['Hadir', 'Sakit', 'Izin', 'Alpa'], [hadir.sum(), sakit.sum(), izin.sum(), alpa.sum()])

    # menambahkan label pada setiap bar chart
    for i, v in enumerate([hadir.sum(), sakit.sum(), izin.sum(), alpa.sum()]):
        ax.text(i, v + 1, str(v), ha='center', fontsize=10)

    ax.set_title('Chart Kehadiran {}'.format(selected_name))
    ax.set_xlabel('Kategori')
    ax.set_ylabel('Jumlah')

    # menampilkan chart
    st.pyplot(fig)
        
        
def peranak():
  import pandas as pd
  import streamlit as st

  # membaca file csv
  data = pd.read_csv('rekap.csv')

  # membuat list nama-nama yang ada di data
  nama_list = data['Nama'].unique().tolist()

  # menambahkan pilihan dropdown untuk memilih nama individu
  selected_name = st.selectbox('Pilih nama individu:', nama_list)

  # memilih data untuk individu yang dipilih
  selected_data = data[data['Nama'] == selected_name]

  # menghitung rata-rata kehadiran, sakit, izin, dan alpa untuk setiap nama
  mean_data = data.iloc[:, 1:].apply(lambda x: pd.Series({
      'Hadir': x.str.contains('Hadir').sum(),
      'Sakit': x.str.contains('Sakit').sum(),
      'Izin': x.str.contains('Izin').sum(),
      'Alpa': x.str.contains('Alpa').sum()
  })).reset_index().groupby('index').mean()

  # menghitung total alpa, sakit, dan izin untuk individu yang dipilih
  total_alpa = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Alpa').sum()).sum()
  total_sakit = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Sakit').sum()).sum()
  total_izin = selected_data.iloc[:, 1:].apply(lambda x: x.str.contains('Izin').sum()).sum()

  # menampilkan rata-rata kehadiran, jumlah alpa, sakit, dan izin untuk individu yang dipilih
  st.write('### Rata-rata Kehadiran, Jumlah Alpa, Sakit, dan Izin untuk Setiap Nama')
  st.write(mean_data)

  st.write('### Analisis Kehadiran untuk {}'.format(selected_name))
  st.write('**Total Alpa:** {}'.format(total_alpa))
  st.write('**Total Sakit:** {}'.format(total_sakit))
  st.write('**Total Izin:** {}'.format(total_izin))
  st.write('**Daftar Kolom dengan Alpa:**')
  for col in selected_data.columns[selected_data.isin(['Alpa']).any()]:
      st.write('- {}'.format(col))
  st.write('**Daftar Kolom dengan Sakit:**')
  for col in selected_data.columns[selected_data.isin(['Sakit']).any()]:
      st.write('- {}'.format(col))
  st.write('**Daftar Kolom dengan Izin:**')
  for col in selected_data.columns[selected_data.isin(['Izin']).any()]:
      st.write('- {}'.format(col))     
        
        
page_names_to_funcs = {
    "—": intro,
    "Rekap Attendance Harian": daftar_hadir,
    "Grafik Kehadiran 1 Tahun": Grafik,
    "Rekap Peranak": peranak
}

demo_name = st.sidebar.selectbox("Silahkan Pilih", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()