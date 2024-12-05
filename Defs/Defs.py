import streamlit as st
from datetime import datetime

def hitungbiaya(jenis, jammasuk, jamkeluar):
    durasi = (jamkeluar - jammasuk)
    
    if durasi <= 1:
        if jenis == "Motor":
            harga = durasi * 3000
        elif jenis == "Mobil":
            harga = durasi * 4000
        else:
            harga = "Unknown"
    elif durasi <= 2:
        if jenis == "Motor":
            harga = durasi * 4000
        elif jenis == "Mobil":
            harga = durasi * 5000
        else:
            harga = "Unknown"
    else:
        if jenis == "Motor":
            harga = durasi * 5000
        elif jenis == "Mobil":
            harga = durasi * 6000
        else:
            harga = "Unknown"
    st.write(f"Total Biaya: Rp {harga}.")
    return harga

def karcis(karcisid, jenis, platno, jammasuk, jamkeluar):
    st.write("ID Karcis : ", karcisid)
    st.write("Jenis Kendaraan : ", jenis)
    st.write("Plat Nomor Kendaraan : ", platno)
    st.write("Jam Masuk Kendaraan : ", jammasuk)
    st.write("Jam Keluar Kendaraan : ", jamkeluar)
