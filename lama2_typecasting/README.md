### Minggu 2: Typecasting dan Perhitungan Dasar 📝

Tujuan minggu ini adalah mengajarkan siswa cara melakukan perhitungan dengan data yang diterima dari pengguna.


```

INI BLOM DIGANTI KABEH YO ISINYA. BARU README
minggu-0/
├── CONFIDENTIAL_MATERI/           # Soal Materi mingguan. cuma ada di repo semuaan.      
│   ├── M0_test_hello_world.md           
│   └── M0_test_hello_world.pdf  
│ 
├── CONFIDENTIAL_PEMBAHASAN/       # Pembahasan. publish klo nilai udh keluar.         
│   ├── kunci_T0_test_hello_world.md   
│   │   
│   └── kunci_M0_test_hello_world.md    
│  
├── KONTEN_TUTOR/                   
│   ├── tutor0_setup_lab.md        # Buku Prak. isinya link pretest + tutor + live coding + instruksi tugas.
│   ├── tutor0_setup_lab.pdf      
│   │   
│   └── tes_awal0.pdf              # Tes_Awal mingguan.      
│   
├── README_assets/                 
│   ├── git-flowchart.png
│   └── diagram-venv.png
│
├── README.md                      # penjelasan singkat prak mingguan                       
│ 
├── tests/
│   └── test_T0_hello_world.py     # Unit test supaya kamu bisa cek jawabanmu sendiri.
│            
└─── TUGAS/                   
    └── T0_test_hello_world.py     # Lembar Tugas minggu 0. boleh kerjain di sini.
```

---

### Konsep Utama & Kegiatan Lab

### 2. Interaksi Pengguna: Fungsi `input()`
* **Tujuan:** Membuat program yang bisa berinteraksi dengan pengguna.
* **Materi:**
    * Fungsi `input()`: Ajarkan cara menggunakan fungsi `input()` untuk menerima data dari pengguna.
    * Perhatian Penting: Jelaskan bahwa `input()` akan **selalu mengembalikan string**. Ini adalah poin krusial yang harus mereka pahami.
* **Praktik:** Buat program interaktif sederhana, seperti meminta nama atau usia, lalu mencetaknya. Tunjukkan bagaimana data dari `input()` harus diubah (*type casting*) menjadi *integer* atau *float* jika ingin digunakan untuk perhitungan.

1. **Typecasting sebagai Solusi**  
   
   * **Mengapa:** Ingatkan siswa tentang masalah di mana input() selalu mengembalikan string. Perlihatkan lagi bagaimana Python akan menggabungkan teks ("5" + "5" = "55") daripada menjumlahkan angka. Typecasting adalah solusi untuk mengubah data dari satu jenis ke jenis lain.  
   
   * **Bagaimana:** Perkenalkan fungsi int() dan float(). Gunakan analogi mesin konverter data yang mengubah teks angka menjadi angka asli, sehingga dapat digunakan untuk perhitungan.  
   
   * **Live Coding:** Tunjukkan cara typecasting lewat interpreter shell dan di program.  

2. **Melakukan Perhitungan**  
   
   * **Mengapa:** Ini adalah inti dari sebagian besar program. Dengan menguasai perhitungan, mereka dapat membuat program yang melakukan tugas yang lebih berguna
   
   * **Bagaimana:** Setelah mengonversi data, ajarkan mereka cara menggunakan operator aritmatika (+, -, *, /, mod, ^)  
   
   * **Live Coding:** playing around with data types. python interpreter shell.

3. **Membuat Pesan yang Bermakna**  

   * **Mengapa:** Program yang baik tidak hanya memberikan jawaban, tetapi juga menyajikannya dengan jelas.
   
   * **Bagaimana:** Ajarkan cara menggabungkan string dan variabel yang sudah dihitung untuk membuat pesan keluaran yang informatif.  
   
   * **Live Coding:** ASCII outputs, one path storybook?
---

### Cheatsheet


**Fungsi `Typecasting`:**

  * `int(nilai)`: Mengubah ke bilangan bulat.
  * `float(nilai)`: Mengubah ke bilangan desimal.
  * `str(nilai)`: Mengubah ke teks.

**Operator Aritmatika:**

  * `+` (penjumlahan)
  * `-` (pengurangan)
  * `*` (perkalian)
  * `/` (pembagian)

**Contoh Kode:**

```python
# Menerima masukan dari pengguna
panjang_str = input("Masukkan panjang: ")
lebar_str = input("Masukkan lebar: ")

# Mengubah tipe data
panjang = float(panjang_str)
lebar = float(lebar_str)

# Melakukan perhitungan
luas = panjang * lebar

# Mencetak hasilnya
print(f"Luas persegi panjang adalah: {luas}")
```


---

### Soal

* **Tugas:** 
*  Buat program yang meminta panjang sisi persegi, lalu hitung keliling dan luasnya. Cetak kedua hasilnya dalam kalimat yang berbeda. 

* **Pluspoint:** 
* Buat ASCII art yg ke-print sama hasil cetakan kalkulasinya

* **Materi:** 
* Debugging type error code. Berikan potongan kode dengan kesalahan TypeError dan minta siswa untuk memperbaikinya menggunakan typecasting yang benar.
* 
