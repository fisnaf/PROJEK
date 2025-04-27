import streamlit as st

def hitung_kadar_cn(massa_sampel, volume_larutan, absorbansi, faktor_kalibrasi=0.0125):
    kadar_cn = (absorbansi * faktor_kalibrasi * volume_larutan) / massa_sampel
    kadar_cn_ppm = kadar_cn * 1000
    return kadar_cn, kadar_cn_ppm

def main():
    st.title("Perhitungan Kadar Cn")
    st.write("Masukkan data di bawah ini:")

    massa_sampel = st.number_input("Massa sampel (gram)", min_value=0.0, format="%.6f")
    volume_larutan = st.number_input("Volume larutan (mL)", min_value=0.0, format="%.2f")
    absorbansi = st.number_input("Absorbansi", min_value=0.0, format="%.6f")
    faktor_kalibrasi = st.number_input("Faktor Kalibrasi (default 0.0125)", value=0.0125, format="%.6f")
    
    if st.button("Hitung Kadar Cn"):
        if massa_sampel <= 0 or volume_larutan <= 0:
            st.error("Massa sampel dan volume larutan harus lebih besar dari 0")
        else:
            kadar_cn, kadar_cn_ppm = hitung_kadar_cn(massa_sampel, volume_larutan, absorbansi, faktor_kalibrasi)
            st.success("Hasil Perhitungan:")
            st.write(f"Kadar Cn: {kadar_cn:.6f} g/g")
            st.write(f"Kadar Cn: {kadar_cn_ppm:.2f} ppm")

if _name_ == "_main_":
    main()
