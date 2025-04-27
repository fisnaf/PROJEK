import streamlit as st

def main():
    # Judul Halaman
    st.title("🧪 Kalkulator Kadar Cn dalam Sampel Kimia")

    # Pendahuluan
    st.header("📚 Pendahuluan")
    st.write("""
    Cn adalah simbol umum untuk menyatakan konsentrasi suatu senyawa (misalnya sianida, karbon, atau lainnya tergantung konteks) dalam sebuah sampel.
    
    Pengukuran kadar Cn penting dalam berbagai bidang seperti pengolahan limbah, analisis kualitas air, dan kontrol proses industri.
    """)

    # Penjelasan Parameter
    st.header("🔎 Parameter yang Digunakan")
    st.markdown("""
    - **Massa Sampel (gram)**: berat sampel yang dianalisis.
    - **Volume Larutan (mL)**: volume pelarut atau larutan hasil ekstraksi sampel.
    - **Absorbansi**: nilai absorbansi hasil pengukuran spektrofotometer.
    - **Faktor Kalibrasi**: konstanta berdasarkan kurva kalibrasi alat (biasanya didapat dari standar).
    """)

    # Rumus Perhitungan
    st.header("🧮 Rumus Perhitungan Kadar Cn")
    st.latex(r'''
    \text{Kadar Cn (g/g)} = \frac{\text{Absorbansi} \times \text{Faktor Kalibrasi} \times \text{Volume Larutan}}{\text{Massa Sampel}}
    ''')
    st.write("Hasil bisa dikonversi ke satuan ppm (mg/kg) dengan mengalikan 1000.")

    # Input User
    st.header("🛠️ Hitung Kadar Cn Anda")
    massa_sampel = st.number_input("Masukkan massa sampel (gram)", min_value=0.0, step=0.01)
    volume_larutan = st.number_input("Masukkan volume larutan (mL)", min_value=0.0, step=1.0)
    absorbansi = st.number_input("Masukkan nilai absorbansi", min_value=0.0, step=0.001)
    faktor_kalibrasi = st.number_input("Masukkan faktor kalibrasi (default contoh: 0.0125)", value=0.0125, step=0.0001)

    # Tombol untuk menghitung
    if st.button("Hitung Kadar Cn"):
        if massa_sampel <= 0 or volume_larutan <= 0:
            st.error("Massa sampel dan volume larutan harus lebih dari 0.")
        else:
            kadar_cn = (absorbansi * faktor_kalibrasi * volume_larutan) / massa_sampel
            kadar_cn_ppm = kadar_cn * 1000  # Konversi ke ppm

            st.success(f"Kadar Cn: {kadar_cn:.6f} g/g")
            st.success(f"Kadar Cn: {kadar_cn_ppm:.2f} ppm")

    # Footer
    st.markdown("---")
    st.caption("© 2025 | Dibuat untuk edukasi jurusan Pengolahan Limbah Industri 🌱")

if __name__ == "__main__":
    main()
