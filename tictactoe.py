# ==========================================================
# 🐍 IMPLEMENTASI PYTHON LENGKAP UNTUK TIC-TAC-TOE
# (Nama Fungsi dalam Bahasa Indonesia)
# ==========================================================

import sys 
import os

def inisialisasi_papan():
    """
    Menginisialisasi papan 3x3 dengan angka 1-9.
    """
    # Menggunakan list comprehension untuk inisialisasi yang ringkas
    PAPAN = [i for i in range(1, 10)]
    return PAPAN

def tampilkan_papan(papan):
    """
    Mencetak papan ke konsol dalam format 3x3.
    """
    print("\n")
    print(f" {papan[0]} | {papan[1]} | {papan[2]} ")
    print("---+---+---")
    print(f" {papan[3]} | {papan[4]} | {papan[5]} ")
    print("---+---+---")
    print(f" {papan[6]} | {papan[7]} | {papan[8]} ")
    print("\n")

def dapatkan_gerakan_valid(papan, simbol_pemain):
    """
    Meminta input posisi (1-9) dari pemain dan memvalidasinya.
    """
    while True:
        try:
            # Meminta input dari pengguna
            input_gerakan = input(f"Masukkan posisi (1-9) untuk {simbol_pemain}: ")
            gerakan = int(input_gerakan)
            
            # Validasi 1: Cek batas angka (1-9)
            if gerakan < 1 or gerakan > 9:
                print(">>> Input harus berupa angka antara 1 dan 9.")
                continue

            # Konversi posisi ke indeks (0-8)
            indeks = gerakan - 1
            
            # Validasi 2: Cek apakah posisi sudah terisi
            if not isinstance(papan[indeks], int):
                print(f">>> Posisi {gerakan} sudah terisi. Pilih yang lain.")
                continue
                
            # Jika lolos kedua validasi
            return gerakan

        except ValueError:
            print(">>> Input tidak valid. Harap masukkan angka.")
        except Exception as e:
            print(f">>> Terjadi kesalahan: {e}")

def lakukan_gerakan(papan, gerakan, simbol):
    """
    Memperbarui papan dengan simbol pemain pada posisi yang dipilih.
    """
    indeks = gerakan - 1
    papan[indeks] = simbol
    return papan

def cek_menang(papan, simbol):
    """
    Memeriksa 8 kombinasi kemenangan untuk simbol yang diberikan.
    """
    # Daftar 8 kombinasi kemenangan (menggunakan indeks 0-8)
    KOMBINASI_MENANG = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Baris
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Kolom
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    
    for kombinasi in KOMBINASI_MENANG:
        i, j, k = kombinasi[0], kombinasi[1], kombinasi[2]
        
        # Cek apakah semua posisi dalam kombinasi ini berisi simbol pemain
        if papan[i] == simbol and papan[j] == simbol and papan[k] == simbol:
            return True # Menang!
            
    return False

def cek_seri(papan):
    """
    Memeriksa apakah papan sudah penuh (draw).
    """
    # Papan penuh jika tidak ada lagi angka (integer) 1-9 yang tersisa.
    for sel in papan:
        if isinstance(sel, int):
            return False # Masih ada angka, berarti masih ada tempat kosong
            
    return True # Semua tempat sudah terisi

def ganti_pemain(pemain_saat_ini):
    """
    Mengganti pemain dari 'P1' ke 'P2' atau sebaliknya.
    """
    if pemain_saat_ini == 'P1':
        return 'P2'
    else:
        return 'P1'


def utama():
    """
    Fungsi utama yang menjalankan alur game.
    """
    print("================================")
    print("Selamat datang di Tic-Tac-Toe!")
    print("================================")
    
    # 1. INISIALISASI
    papan = inisialisasi_papan()
    pemain_saat_ini = 'P1'
    simbol_pemain = {'P1': 'X', 'P2': 'O'}
    game_selesai = False
    
    # 2. MAIN GAME LOOP
    while not game_selesai:
        
        if os.name == 'posix':
            os.system('clear')
        else:
            # Jika bukan posix (misalnya Windows), gunakan 'cls'
            os.system('cls')
            
        # A. Tampilkan Papan & Info Pemain
        simbol = simbol_pemain[pemain_saat_ini]
        print(f"\n--- Giliran Pemain {pemain_saat_ini} ({simbol}) ---")
        tampilkan_papan(papan)
        
        # B. Dapatkan dan Lakukan Gerakan
        gerakan = dapatkan_gerakan_valid(papan, simbol)
        papan = lakukan_gerakan(papan, gerakan, simbol)
        
        # C. Cek Kondisi Akhir Game
        if cek_menang(papan, simbol):
            print("================================")
            print(f"!!! PEMAIN {pemain_saat_ini} ({simbol}) MENANG !!!")
            print("================================")
            game_selesai = True
        elif cek_seri(papan):
            print("================================")
            print("!!! Permainan berakhir SERI !!!")
            print("================================")
            game_selesai = True
        else:
            # D. Ganti Pemain
            pemain_saat_ini = ganti_pemain(pemain_saat_ini)

    # Tampilkan papan terakhir setelah game berakhir
    tampilkan_papan(papan)
    print("Game Selesai.")


# Jalankan fungsi utama saat skrip dieksekusi
if __name__ == "__main__":
    utama()
