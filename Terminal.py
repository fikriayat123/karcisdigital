import streamlit as st
from random import randint as rng
from Defs.Defs import hitungbiaya, karcis
from Data.History import gethistory, historypage

st.title("Karcis Parkiran Digital")

halaman = st.sidebar.radio(
    "Halaman",
    ["Karcis", "Histori Karcis"]
)

if halaman == "Karcis":
    jenis = st.selectbox(
        "Jenis Kendaraan", 
        ["Motor", "Mobil"],
        index = None,
        placeholder="Pilih Jenis Kendaraan"
    )

    if jenis == "Motor":
        st.write("Harga Perkiran Motor")
        st.write('1. Satu Jam Pertama : Rp.3.000')
        st.write('2. Dua Jam : Rp.4.000')
        st.write('3. Lebih Dari tiga Jam : Rp.5.000\n')
    elif jenis == "Mobil":
        st.write("Harga Perkiran Mobil")
        st.write('1. Satu Jam Pertama : Rp.4.000')
        st.write('2. Dua Jam : Rp.5.000')
        st.write('3. Lebih Dari tiga Jam : Rp.6.000\n')
    else:
        st.write("")

    platno = st.text_input("Masukkan Plat Nomor Kendaraan: ")
    jammasuk = st.number_input("Jam Masuk: ")
    jamkeluar = st.number_input("Jam Keluar: ")

    if st.button("Hitung Biaya"):
        karcisid = rng(1000, 9999)
        karcis(karcisid, jenis, platno, jammasuk, jamkeluar)
        totalharga = hitungbiaya(jenis, jammasuk, jamkeluar)
        gethistory(karcisid, jenis, platno, jammasuk, jamkeluar, totalharga)
        st.success("Karcis Telah Disimpan ke History!")

elif halaman == "Histori Karcis":
    historypage()
