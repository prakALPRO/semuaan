SANGAT Terinspirasi dari buku:

“Think-C” karya Thomas Scheffler terbitan  Green Tea Press   
[](https://github.com/tscheffl/ThinkC/blob/master/PDF/Think-C.pdf)  


"Think Python" karya Allen Downey terbitan  Green Tea Press   
[](https://greenteapress.com/thinkpython2/thinkpython2.pdf)  

-----

# **Minggu 1: Basic Sequence** 📝

```
1_basic_sequence/
├── CONFIDENTIAL_MATERI/
│   ├── M1_basic_sequence.md
│   └── M1_basic_sequence.pdf
│
├── CONFIDENTIAL_PEMBAHASAN/
│   ├── kunci_T1_kalkulator.md
│   └── kunci_M1_basic_sequence.md
│
├── KONTEN_TUTOR/
│   ├── tutor1_basic_sequence.md
│   ├── tutor1_basic_sequence.pdf
│   └── tes_awal1.pdf
│
├── README_assets/
│   ├── git-flowchart.png
│   └── diagram-venv.png
│
├── README.md
│
├── tests/
│   └── test_T1_kalkulator.py
│
└── TUGAS/
    └── T1_kalkulator.py
```

## **Overview Konsep Utama & Kegiatan Lab**

### **0. Menyiapkan Lingkungan Pemrograman 💻**

* **Tujuan:** Mengenal dan menyiapkan *software* esensial yang membentuk **lingkungan pemrograman (coding environment)**, serta memahami fungsi **Git** dan **GitHub** sebagai alat untuk manajemen kode dan kolaborasi.

* **Materi:**
  
  * **Komponen Utama Lingkungan Pemrograman:**
    
    1. **Text Editor / IDE (Integrated Development Environment):** Ini adalah tempat kita menulis kode. Untuk memulai, kita akan menggunakan **Visual Studio Code (VS Code)**. VS Code adalah *editor* modern yang dilengkapi fitur-fitur canggih seperti *syntax highlighting* (memberi warna pada kode agar mudah dibaca), *code completion* (saran kode otomatis), dan terminal terintegrasi. 
    2. **Python Interpreter:** Ini adalah "penerjemah" yang membaca kode Python-mu dan memberitahu komputer cara menjalankannya. Tanpa ini, komputermu tidak akan mengerti file `.py` yang kamu tulis.
    3. **Terminal (Command Line):** Ini adalah antarmuka berbasis teks untuk berinteraksi langsung dengan komputermu. Kita akan menggunakannya untuk menjalankan perintah-perintah penting seperti menginstal *library* atau menggunakan Git.
  
  * **Manajemen Kode dengan Git & GitHub:**
    
    * **Git:** Anggap saja Git sebagai "mesin waktu" untuk kodemu yang ada di komputermu. Ia melacak setiap perubahan yang kamu buat, jadi kamu bisa kembali ke versi sebelumnya jika terjadi kesalahan. Proses ini disebut ***version control***.
    * **GitHub:** Ini adalah platform *online* untuk menyimpan *repository* (folder proyek) Git-mu. Anggap saja GitHub sebagai "Google Drive" untuk kode, yang memungkinkanmu menyimpan kodemu dengan aman dan berkolaborasi dengan orang lain.
    * **Alur Kerja Dasar:** Untuk praktikum ini, kita akan fokus pada dua perintah: `git pull` untuk mengambil *template* soal dari *repository* dan `git push` untuk mengirimkan jawabanmu.

* **Praktik:**
  
  1. **Instalasi:** Tunjukkan proses instalasi **Python**, **VS Code**, dan **Git** di komputer.
  2. **Konfigurasi Awal:** Lakukan konfigurasi dasar Git di terminal dengan mengatur *username* dan *email*.
  3. **Demonstrasi Alur Kerja:** Tunjukkan proses lengkap mulai dari `git pull` untuk mengunduh folder materi, membuka folder tersebut di VS Code, melakukan sedikit perubahan pada kode, lalu menggunakan `git push` untuk mengunggah hasilnya kembali ke GitHub.

---

### 1. Variabel dan Tipe Data

* **Tujuan:** Memahami konsep dasar **variabel** dan **tipe data** dalam pemrograman.
* **Materi:**
  * **Variabel:** Jelaskan variabel sebagai wadah untuk menyimpan data, layaknya "kotak berlabel" yang bisa diisi dan diganti isinya. 
  * **Tipe Data:** Kenalkan tiga tipe data utama: **string** (untuk teks), **integer** (untuk bilangan bulat), dan **float** (untuk bilangan desimal). Jelaskan bahwa setiap data memiliki "jenisnya" sendiri.
* **Praktik:** Lakukan *live coding* untuk membuat, mengisi, dan mencetak nilai dari variabel untuk setiap tipe data.

---

### 2. Operator Aritmetika

* **Tujuan:** Memahami cara menggunakan operator matematika untuk memanipulasi dan memproses data numerik yang tersimpan dalam variabel.
* **Materi:**
  * **Ekspresi:** Jelaskan bahwa kombinasi antara nilai, variabel, dan operator yang menghasilkan sebuah nilai baru disebut sebagai **ekspresi** (contoh: `harga_barang * jumlah`).
  * **Operator Aritmetika:** Kenalkan operator dasar: `+` (tambah), `-` (kurang), `*` (kali), `/` (bagi), `%` (sisa bagi/modulo), dan `**` (pangkat).
* **Praktik:** Lakukan *live coding*. Definisikan beberapa variabel (misal: `panjang = 10`, `lebar = 5`). Kemudian, buat ekspresi untuk menghitung luas dan keliling (`luas = panjang * lebar`), simpan hasilnya di variabel baru, lalu cetak hasilnya dengan teks yang jelas.

---

### 3. Komentar dalam Kode

* **Tujuan:** Memahami pentingnya **komentar** untuk membuat kode lebih jelas dan mudah dibaca oleh manusia.
* **Materi:**
  * **Fungsi Komentar:** Jelaskan bahwa komentar adalah catatan yang diabaikan oleh program, tapi sangat penting untuk dokumentasi dan kolaborasi.
  * **Cara Menulis Komentar:** Tunjukkan cara membuat komentar satu baris (`#`).
* **Praktik:** Berikan contoh kode lalu tambahkan komentar untuk setiap baris atau blok kode. Bandingkan versi dengan dan tanpa komentar untuk menyoroti perbedaannya.

-----

## ============== **Cheatsheet** ======================

| Kategori          | Sintaks            | Contoh                           | Penjelasan                                      |
|:----------------- |:------------------ |:-------------------------------- |:----------------------------------------------- |
| **Tipe Data**     | `str`              | `"Halo"`                         | Teks atau kumpulan karakter.                    |
|                   | `int`              | `100`                            | Bilangan bulat.                                 |
|                   | `float`            | `3.14`                           | Bilangan desimal.                               |
| **Sintaks Dasar** | `print()`          | `print("Hello")`                 | Menampilkan output ke terminal.                 |
|                   | `input()`          | `nama = input("Siapa namamu? ")` | Menerima input dari user (selalu `string`).     |
| **Type Casting**  | `int()`            | `angka = int("25")`              | Mengubah nilai menjadi `integer`.               |
|                   | `float()`          | `desimal = float("99.5")`        | Mengubah nilai menjadi `float`.                 |
| **Komentar**      | `#`                | `# Ini tidak akan dieksekusi`    | Membuat komentar satu baris.                    |
| **Operator**      | `+`, `-`, `*`, `/` | `5 + 2`                          | Penjumlahan, Pengurangan, Perkalian, Pembagian. |
|                   | `%`                | `10 % 3`                         | Sisa Hasil Bagi (Modulo), hasilnya `1`.         |
|                   | `**`               | `2 ** 3`                         | Perpangkatan, hasilnya `8`.                     |

-----

-----

### **EKSPLORASI LIVE CODING**

#### **Tutor 1.1: Utak-atik Kode**

Salin kode ini dan lakukan eksperimen berikut:

```python
# Program Hello World
print("Hello, World.")
```

a. Jalankan program. Apa outputnya?
b. Tambahkan `print("Apakabssss ?")` di bawahnya. Jalankan lagi. Apa outputnya sekarang?
c. Tambahkan komentar `# Ini eksperimenku`. Apakah outputnya berubah?
d. Hapus salah satu tanda kutip, misalnya jadi `print("Hello, World.)`. Apa pesan error yang muncul?
e. Salah ketik `print` menjadi `prnt`. Apa pesan error yang muncul?

-----

#### **Tutor 1.2: Men-debug Kode **

Program di bawah ini penuh dengan *bug*. Di versi ini, tanggalnya sudah ditentukan di dalam variabel, jadi kamu hanya perlu fokus memperbaiki **kesalahan sintaks** agar program bisa berjalan dan menghasilkan output yang benar.

```python
# Program ini penuh dengan bug! Ayo perbaiki.

# Tanggal pertama sudah ditentukan (di-hardcode)
tanggal1 = 15
bulan1 = 5
tahun1 = 2024

# Tanggal kedua sudah ditentukan (di-hardcode)
tanggal2 = 20
bulan2 = 8
tahun2 = 2025

printtt(f"Tanggal pertama adalah: {tanggal1}-{bulan1}-{tahun1}") # hemmm, nama fungsinya aneh

print(f"Tanggal kedua adalah: {tanggal2}-{bulanke2}-{tahun2}") # hemmm, nama variabelnya suspicious…

# Menghitung total hari dari tanggal 1 Januari tahun 0
days1 = tanggal1 + (bulan1 * 30) + (tahun1 * 365)
days2 = tanggal2 + (bulan2 * 30) + (tahun2 * 365)

selisih = abs(days1 - days2)

print(f"Selisih diantara 2 hari tersebut adalah: {selisih} hari.) # hemmm, ada yang aneh dengan tanda kurungnya

# Mengubah selisih hari kembali ke format tahun, bulan, hari
hasil_tahun = selisih // 365
selisih = selisih % 365
hasil_bulan = selisih // 30
hasil_tanggal = selisih % 30

print(f"atau: {hasil_tahun} tahun, {hasil_bulan} bulan, {hasil_tanggal} hari")
```

-----

#### **Tutor 1.3: Mencoba Python Interactive Shell**

Bayangkan kamu punya sebuah "area eksperimen" atau "kalkulator super" di mana kamu bisa mencoba perintah Python satu per satu dan langsung melihat hasilnya, tanpa perlu menyimpan dan menjalankan file. Itulah **Python Interactive Shell**\!

Ini adalah salah satu *tool* terbaik untuk belajar dan mencoba ide-ide kecil dengan cepat.

#### **Bagaimana Cara Membukanya?**

1. Buka **Terminal** (bisa langsung di dalam VS Code).
2. Ketik `python` (atau `python3` pada beberapa sistem) lalu tekan **Enter**.
3. Kamu akan melihat prompt berubah menjadi `>>>`. Ini tandanya Python Shell sudah siap menerima perintahmu\!

#### **Ayo Bermain\! Skenario: Toko Kue Ajaib**

Ketik perintah di bawah ini satu per satu setelah `>>>` dan lihat apa yang terjadi setelah kamu menekan **Enter**.

1. **Sebagai Kalkulator Instan**
   Shell ini bisa langsung melakukan perhitungan. Mari kita hitung harga 3 potong kue, di mana satu potongnya seharga Rp 15.000.
   
   ```python
   >>> 15000 * 3
   ```
   
   Python akan langsung menjawab `45000`. Cepat, kan?

2. **Menyimpan Informasi (Variabel)**
   Sekarang, mari kita simpan informasi itu ke dalam **variabel**.
   
   ```python
   >>> harga_kue = 15000
   >>> jumlah_beli = 3
   >>> total_harga = harga_kue * jumlah_beli
   ```
   
   Tidak ada output yang muncul? Tenang, nilainya sudah tersimpan. Untuk mengeceknya, cukup ketik nama variabelnya:
   
   ```python
   >>> total_harga
   ```
   
   Dan `45000` pun akan muncul\! Ini sangat berguna untuk mengecek nilai variabel saat kamu sedang *coding*.

3. **Bermain dengan Teks (String)**
   Shell juga bisa menggabungkan teks dengan mudah.
   
   ```python
   >>> nama_pembeli = "Budi"
   >>> ucapan = "Terima kasih, " + nama_pembeli + "! Silakan datang kembali."
   >>> ucapan
   ```
   
   Kamu akan langsung melihat kalimat lengkapnya.

4. **Momen "Aha\!" - Jebakan Tipe Data**
   Ini adalah eksperimen paling penting. Anggap setiap pembelian memberi 100 poin. Budi membeli lagi dan dapat 50 poin tambahan.
   
   ```python
   >>> poin_awal = "100"   # Perhatikan, ini adalah string (ada tanda kutip)
   >>> poin_tambahan = "50"  # Ini juga string
   >>> total_poin = poin_awal + poin_tambahan
   >>> total_poin
   ```
   
   Lho, kok hasilnya `'10050'` bukan `150`?
   **Inilah keajaiban shell\!** Kamu baru saja menemukan secara langsung bahwa operator `+` akan **menggabungkan** jika bertemu *string*, bukan menjumlahkan. Ini adalah pelajaran fundamental yang sangat mudah diuji di sini.

#### **Kapan Sebaiknya Menggunakan Shell Ini?**

* Saat kamu ingin **menguji ide kecil** atau satu baris kode dengan cepat.
* Saat kamu **lupa sebuah sintaks** dan ingin mencobanya terlebih dahulu.
* Saat kamu ingin **mengecek tipe data** atau nilai dari sebuah variabel.

Untuk keluar dari shell, cukup ketik `exit()` dan tekan **Enter**.

Tentu, ini draf untuk seksi 1.4 yang berisi instruksi pengerjaan soal berdasarkan file yang kamu berikan.

---

### **Tutor 1.4: Petunjuk Pengerjaan Soal 📝**

*Wait!* Sebelum mulai, baca dulu panduan ini agar kamu tahu persis apa yang harus dilakukan untuk setiap jenis soal. Ada dua bagian utama: **Materi M1** dan **Tugas T1**. Cara mengerjakannya sedikit berbeda.

#### **Untuk Soal-soal Materi M1 (Kalkulator)**

Soal-soal di bagian ini (Radian, Torsi, Gaya Coulomb) bertujuan untuk melatih logika dasar, penggunaan variabel, dan operator matematika. Kamu akan membuat program dari nol.

1.  **Buat File Baru:** Untuk setiap nomor soal, buatlah sebuah file Python baru di dalam folder kerjamu. Beri nama yang jelas, misalnya:
    * `M1_1_radian.py`
    * `M1_2_torsi.py`
    * `M1_3_coulomb.py`

2.  **Baca Petunjuk & Rumus:** Perhatikan bagian **"Petunjuk"** dan **"Rumus"** yang ada di setiap soal. Semua informasi yang kamu butuhkan ada di sana.

3.  **Tulis Kodenya:**
    * **Impor Modul (jika perlu):** Untuk soal yang butuh fungsi matematika seperti sinus atau nilai pi, awali kodemu dengan `import math`.
    * **Tentukan Variabel:** Buat variabel untuk semua nilai yang diketahui di soal (misalnya `derajat = 45`, `F = 25.5`, dll.). Proses ini disebut ***hardcoding***.
    * **Terapkan Rumus:** Tuliskan rumus matematika yang diberikan ke dalam sintaks Python untuk melakukan perhitungan.
    * **Cetak Hasil:** Gunakan fungsi `print()` untuk menampilkan jawaban. Buatlah outputmu serapi mungkin dan mirip dengan **"Contoh Tampilan Program"**. Kamu bisa menggunakan f-string untuk memformat teks dengan mudah.

4.  **Jalankan & Periksa:** Buka terminal, lalu jalankan file-mu dengan perintah `python nama_file.py`. Bandingkan output programmu dengan contoh yang ada di soal.

---

#### **Untuk Soal Tugas T1 (Navigasi Robot)**

Soal ini berbeda! Kamu tidak membuat file baru, tetapi **mengisi kode** pada file yang sudah disediakan untuk menggerakkan sebuah robot.

1.  **Buka File yang Tepat:** Cari dan buka file bernama `jawabanmu_M1_navigasirobot.py` yang ada di dalam folder `jawaban_akhir`.

2.  **Isi Fungsi:** Kamu akan melihat sebuah fungsi yang sudah disiapkan. Tuliskan logikamu **di dalam fungsi tersebut**.

3.  **Gunakan Perintah Gerakan:** Kamu hanya perlu menggunakan dua perintah yang sudah disediakan:
    * `maju(langkah)`: Untuk bergerak lurus.
    * `belok(derajat)`: Untuk berbelok. Gunakan angka positif (misal: `90`) untuk belok kanan dan angka negatif (misal: `-90`) untuk belok kiri.

4.  **Visualisasikan & Uji Jawabanmu:** Ini adalah langkah terpenting.
    * **Untuk Melihat Robot Bergerak:** Jalankan file `assetlab_M1_navigasirobot_wrapper.py`. Ini akan membuka jendela simulasi yang menampilkan pergerakan robotmu secara visual.     * **Untuk Memastikan Jawaban Benar:** Jalankan file `test_M1_goalachieved.py` dari folder `penguji_otomatis`. Terminal akan memberimu pesan "OK" atau "FAILED". Jawabanmu dianggap benar jika tes ini berhasil.

5.  **Kumpulkan Jawaban:** Setelah pengujian otomatis berhasil, simpan file `jawabanmu_M1_navigasirobot.py` dan kumpulkan tugasmu menggunakan `git push`.

Jika ada kesulitan, jangan ragu untuk bertanya. Selamat mengerjakan!
