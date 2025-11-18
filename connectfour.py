import os

def utama():
    # --- Variabel Global dan Inisialisasi Papan (Logika 1) ---
    BARIS = 5
    KOLOM = 5
    SIMBOL_KOSONG = '.'
    
    # Inisialisasi papan 5x5
    papan = [[SIMBOL_KOSONG] * KOLOM for _ in range(BARIS)]
    
    pemain_saat_ini = 'X'
    game_berjalan = True
    gerakan_total = 0

    print("=== Connect Four 5x5 Dimulai! (Monolithic Version) ===")

    while game_berjalan and gerakan_total < BARIS * KOLOM:
        
        # --- Tampilkan Papan (Logika 2) ---
        os.system('cls' if os.name == 'nt' else 'clear') # Clear screen
        print("\n  1 2 3 4 5")
        print("  " + "—" * 9)
        for r in range(BARIS):
            print(f"{r+1}|{' '.join(papan[r])}|")
        print("  " + "—" * 9)

        print(f"Giliran Pemain {pemain_saat_ini}")
        
        # --- Ambil dan Validasi Input (Logika 3) ---
        kolom_pilihan = -1
        while True:
            try:
                kolom_pilihan = int(input(f"Pilih kolom (1-{KOLOM}): "))
                if 1 <= kolom_pilihan <= KOLOM:
                    break
                else:
                    print(f"❌ Input harus antara 1 dan {KOLOM}.")
            except ValueError:
                print("❌ Input tidak valid. Masukkan angka.")
        
        kol_idx = kolom_pilihan - 1
        berhasil_gerak = False

        # --- Lakukan Gerakan (Logika 4) ---
        for r in range(BARIS - 1, -1, -1):
            if papan[r][kol_idx] == SIMBOL_KOSONG:
                papan[r][kol_idx] = pemain_saat_ini
                berhasil_gerak = True
                gerakan_total += 1
                break
        
        if not berhasil_gerak:
            print(f"Kolom {kolom_pilihan} penuh. Pilih kolom lain.")
            continue

        # --- Cek Kemenangan (Logika 5) ---
        menang = False
        # 1. Cek Horizontal
        for r in range(BARIS):
            for c in range(KOLOM - 3):
                if all(papan[r][c + i] == pemain_saat_ini for i in range(4)):
                    menang = True
                    break
            if menang: break

        # 2. Cek Vertikal
        if not menang:
            for c in range(KOLOM):
                for r in range(BARIS - 3):
                    if all(papan[r + i][c] == pemain_saat_ini for i in range(4)):
                        menang = True
                        break
                if menang: break

        # 3. Cek Diagonal (Kiri-Atas ke Kanan-Bawah)
        if not menang:
            for r in range(BARIS - 3):
                for c in range(KOLOM - 3):
                    if all(papan[r + i][c + i] == pemain_saat_ini for i in range(4)):
                        menang = True
                        break
                if menang: break

        # 4. Cek Diagonal (Kiri-Bawah ke Kanan-Atas)
        if not menang:
            for r in range(3, BARIS):
                for c in range(KOLOM - 3):
                    if all(papan[r - i][c + i] == pemain_saat_ini for i in range(4)):
                        menang = True
                        break
                if menang: break
        
        # --- Akhiri/Lanjutkan Game (Logika 6) ---
        if menang:
            os.system('cls' if os.name == 'nt' else 'clear')
            # Tampilkan papan sekali lagi
            print("\n  1 2 3 4 5")
            print("  " + "—" * 9)
            for r in range(BARIS):
                print(f"{r+1}|{' '.join(papan[r])}|")
            print("  " + "—" * 9)
            print(f"\n🎉🎉 Pemain {pemain_saat_ini} MENANG! 🎉🎉")
            game_berjalan = False
        
        elif gerakan_total == BARIS * KOLOM:
            os.system('cls' if os.name == 'nt' else 'clear')
            # Tampilkan papan sekali lagi
            print("\n  1 2 3 4 5")
            print("  " + "—" * 9)
            for r in range(BARIS):
                print(f"{r+1}|{' '.join(papan[r])}|")
            print("  " + "—" * 9)
            print("\n🤝 Pertandingan SERI! Papan penuh. 🤝")
            game_berjalan = False
        
        else:
            # --- Ganti Pemain (Logika 7) ---
            pemain_saat_ini = 'O' if pemain_saat_ini == 'X' else 'X'

if __name__ == "__main__":
    utama()
