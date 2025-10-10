# File: calculator_cli.py
import math
import sys 
from fractions import Fraction 

# ====================================================================
# LOGIKA UTAMA PROGRAM (MAIN CLI)
# ====================================================================
print("SELAMAT DATANG DI TERMINAL KALKULATOR INTERAKTIF")

# 1. Inisialisasi variabel kontrol loop
is_exit = 0

# Perulangan utama yang berjalan terus menerus selama is_exit BUKAN 1
while is_exit != 1:
    print("\n" + "-"*40)
    print("Pilih mode kalkulator:")
    print("  [1] Kalkulator Derajat (Derajat ke Radian)")
    print("  [2] Kalkulator Gaya Coulomb")
    print("  [q] Keluar dari program")
    print("-"*40)
    
    # Minta input mode dari user
    mode_input = input("Masukkan pilihan Anda (1, 2, atau q): ").lower()

    # Logika Kontrol Program (Sintaks Dasar: if/elif/else)
    
    if mode_input == '1':
        # ====================================================================
        # INLINE LOGIC UNTUK KALKULATOR DERAJAT (MODE 1)
        # ====================================================================
        print("\n" + "="*40)
        print("KALKULATOR DERAJAT (Derajat -> Radian)")
        print("="*40)
        
        # 1. Minta input sudut dari user (dengan validasi sederhana)
        while True:
            derajat_input = input("Masukkan sudut dalam derajat (misal: 45 atau 90.5): ")
            
            # Cek dasar: memastikan input terlihat seperti angka (membolehkan satu titik desimal)
            if derajat_input.replace('.', '', 1).isdigit():
                sudut_derajat = float(derajat_input)
                break
            else:
                print("Input tidak valid. Harap masukkan nilai angka yang valid.")
        
        # 2. Hitung nilai radian dalam bentuk desimal
        sudut_radian_desimal = sudut_derajat * (math.pi / 180)

        # 3. Hitung nilai sudut sebagai sesuatu dikali pi (sebagai pecahan)
        berapa_pi = Fraction(sudut_derajat).limit_denominator(1000) * Fraction(1, 180)

        # 4. Cetak semua hasil
        print("=== Hasil Perhitungan ===")
        print(f"Sudut dalam derajat: {sudut_derajat}")
        print(f"Sudut dalam radian (desimal): {sudut_radian_desimal:.3f} rad")
        print(f"Sudut dalam radian (fraksi pi): {berapa_pi} pi rad")
        print("="*40)
        
    elif mode_input == '2':
        # ====================================================================
        # INLINE LOGIC UNTUK KALKULATOR GAYA COULOMB (MODE 2)
        # ====================================================================
        print("\n" + "="*40)
        print("KALKULATOR GAYA COULOMB")
        print("="*40)
        
        # Definisikan konstanta Coulomb
        konstanta_coulomb = 8.99e9    # N·m²/C²

        print("==== Input Nilai Baru ====")
        
        # Minta Muatan q1 (dengan validasi sederhana)
        while True:
            q1_input = input("  Muatan q1 (C) [termasuk tanda minus]: ")
            temp_input = q1_input
            if temp_input.startswith('-'):
                temp_input = temp_input[1:] 
            
            if temp_input.replace('.', '', 1).isdigit():
                muatan_q1 = float(q1_input)
                break
            else:
                print("Input tidak valid. Harap masukkan nilai angka yang valid.")

        # Minta Muatan q2
        while True:
            q2_input = input("  Muatan q2 (C) [termasuk tanda minus]: ")
            temp_input = q2_input
            if temp_input.startswith('-'):
                temp_input = temp_input[1:]

            if temp_input.replace('.', '', 1).isdigit():
                muatan_q2 = float(q2_input)
                break
            else:
                print("Input tidak valid. Harap masukkan nilai angka yang valid.")

        # Minta Jarak r
        while True:
            r_input = input("  Jarak (r) dalam meter [hanya positif]: ")
            if r_input.replace('.', '', 1).isdigit() and float(r_input) > 0:
                jarak_r = float(r_input)
                break
            else:
                print("Input tidak valid. Harap masukkan nilai angka yang positif.")

        
        # 2. Hitung gaya Coulomb sesuai rumus
        # F = ke * |q1 * q2| / r^2
        gaya_coulomb = konstanta_coulomb * abs(muatan_q1 * muatan_q2) / (jarak_r**2)

        # 3. Cetak semua informasi
        print("\n==== Hasil Perhitungan : ====")
        print(f"Muatan q1 = {muatan_q1} C")
        print(f"Muatan q2 = {muatan_q2} C")
        print(f"Jarak (r) = {jarak_r} m")
        print("\nBesar Gaya Coulomb (F):")
        print(f"F = {gaya_coulomb:.2e} N") 
        print("="*40)
        
    elif mode_input == 'q':
        # Ketika user memasukkan 'q', kita set variabel is_exit menjadi 1
        print("Terima kasih. Program dihentikan.")
        is_exit = 1 # Ini akan menghentikan perulangan 'while'
        
    else:
        # Menangani input yang tidak valid
        print(f"Pilihan '{mode_input}' tidak valid. Silakan coba lagi.")

# Setelah perulangan 'while' selesai, kita keluar dari program.
if is_exit == 1:
    sys.exit()
