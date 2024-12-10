import streamlit as st
import pandas as pd

if 'karcisstrip' not in st.session_state:
    st.session_state['karcisstrip'] = []

def gethistory(karcisid, jenis, platno, jammasuk, jamkeluar, totalharga):
    if 'karcisstrip' not in st.session_state:
        st.session_state['karcisstrip'] = []
    st.session_state['karcisstrip'].append([karcisid, jenis, platno, jammasuk, jamkeluar, totalharga])

def historypage():
    if 'karcisstrip' in st.session_state and st.session_state['karcisstrip']:
        historyframe = pd.DataFrame(st.session_state['karcisstrip'], columns=["ID Karcis", "Jenis Kendaraan", "Plat Nomor", "Jam Masuk", "Jam Keluar", "Total Biaya"])
        st.dataframe(historyframe)
    else:
        st.write("Belum ada karcis yang tertulis.")
    
    if st.button("Hapus Histori"):
        st.write("Click lagi untuk menghapus atau pindah Halaman dan balik lagi")
        st.session_state['karcisstrip'] = []
        st.rerun()
