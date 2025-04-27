import streamlit as st
def hitung_kadar_cn():
    print("PROGRAM PERHITUNGAN KADAR Cn")
    print("============================")
    
    try:
        # Input data
        massa_sampel = float(input("Masukkan massa sampel (gram): "))
        volume_larutan = float(input("Masukkan volume larutan (mL): "))
        absorbansi = float(input("Masukkan nilai absorbansi: "))
        
        # Validasi input
        if massa_sampel <= 0 or volume_larutan <= 0:
            print("Error: Massa sampel dan volume larutan harus lebih besar dari 0")
            return
        
        # Asumsi faktor kalibrasi (sesuaikan dengan kebutuhan)
        # Ini contoh saja, Anda perlu menyesuaikan dengan metode analisis Anda
        faktor_kalibrasi = 0.0125  # Nilai contoh, ganti dengan nilai sebenarnya
        
        # Hitung kadar Cn (rumus ini contoh saja, sesuaikan dengan kebutuhan)
        kadar_cn = (absorbansi * faktor_kalibrasi * volume_larutan) / massa_sampel
        kadar_cn_ppm = kadar_cn * 1000  # Konversi ke ppm jika perlu
        
        # Tampilkan hasil
        print("\nHASIL PERHITUNGAN")
        print("-----------------")
        print(f"Massa sampel: {massa_sampel} g")
        print(f"Volume larutan: {volume_larutan} mL")
        print(f"Absorbansi: {absorbansi}")
        print(f"Faktor kalibrasi: {faktor_kalibrasi}")
        print(f"\nKadar Cn: {kadar_cn:.6f} g/g atau {kadar_cn_ppm:.2f} ppm")
        
    except ValueError:
        print("Error: Input harus berupa angka")
    except Exception as e:
        print(f"Terjadi kesalahan: {str(e)}")

# Jalankan program
if _name_ == "_main_":
    hitung_kadar_cn()
