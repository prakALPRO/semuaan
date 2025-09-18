SANGAT Terinspirasi dari buku:

“Think-C” karya Thomas Scheffler terbitan  Green Tea Press   
[Think-C](https://github.com/tscheffl/ThinkC/blob/master/PDF/Think-C.pdf)  


"Think Python" karya Allen Downey terbitan  Green Tea Press   
[Think Python 2nd Edition, Version 2.4.0 ](https://greenteapress.com/thinkpython2/thinkpython2.pdf)  

-----

# **Minggu 1: Basic Sequence** 📝

```
1_basic_sequence/
├── file_pendukung
│   ├── assetlab_T1_interactivemode.py
│   ├── assetlab_T1_navigasirobot_wrapper.py
│   ├── foto
│   │   ├── ss_M1_1.png
│   │   ├── ss_M1_2.png
│   │   ├── ss_M1_3.png
│   │   ├── ss_T1_blomberhasil_unittestgagal.png
│   │   ├── ss_T1_interactivemode_awal.png
│   │   └── ss_T1_nyobainteractivemode.png
│   └── __init__.py
├── InstruksiUntuk1BasicSequence.md
├── jawaban_akhir
│   ├── __init__.py
│   └── jawabanmu_T1_navigasirobot.py
├── koleksi_jawaban_bagus
├── materi_belajar
│   ├── Panduan_ALPRO_pert1.md
│   └── README.md -> Panduan_ALPRO_pert1.md
├── penguji_otomatis
│   ├── __init__.py
│   └── test_T1_goalachieved.py
├── README.md -> InstruksiUntuk1BasicSequence.md
└── soal_latihan
    ├── KUNCI_prakALPRO_pert1_basic_sequence.md
    └── soal_prakALPRO_pert1_basic_sequence.md

```



## ============== **Cheatsheet** ======================


#### **Tipe Data Dasar **

| Sintaks | Contoh | Penjelasan |
| :--- | :--- | :--- |
| `str` | `"Halo"` | Teks atau kumpulan karakter. |
| `int` | `100` | Bilangan bulat. |
| `float` | `3.14` | Bilangan desimal (pecahan). |

-----

#### **Output Dasar **

| Metode | Sintaks & Contoh | Catatan |
| :--- | :--- | :--- |
| **%-formatting (Old Style)** | `print("Nama: %s, Umur: %d" % (nama, umur))` | Dianggap kuno. Perlu penanda tipe data (`%s`, `%d`, `%f`). Kurang fleksibel. |
| **Metode `.format()`** | `print("Nama: {}, Umur: {}".format(nama, umur))` | Fleksibel dan kuat. Lebih mudah dibaca daripada %-formatting. |
| **F-String (Disarankan)** | `print(f"Nama: {nama}, Umur: {umur}")` | Paling modern, singkat, dan mudah dibaca. Bisa memasukkan ekspresi langsung (`{harga*jumlah}`). |


#### **Komentar **

| Sintaks | Contoh | Penjelasan |
| :--- | :--- | :--- |
| `#` | `x = 5 # Ini komentar inline` | **Komentar satu baris.** Mengabaikan sisa teks di baris itu. |
| `""" ... """` | `"""Ini komentar` <br> `multi-baris."""` | **Komentar multi-baris.** Sering digunakan untuk komentar blok. |

-----

#### **Operator Aritmetika **

| Sintaks | Contoh | Penjelasan |
| :--- | :--- | :--- |
| `+`, `-`, `*`, `/` | `5 + 2` | Penjumlahan, Pengurangan, Perkalian, Pembagian. |
| `%` | `10 % 3` | **Sisa Hasil Bagi (Modulo),** hasilnya `1`. |
| `**` | `2 ** 3` | **Perpangkatan,** hasilnya `8`. |
-----

-----

### **EKSPLORASI LIVE CODING**

#### **Tutor 1.1: Utak-atik Kode**

Salin kode ini dan lakukan eksperimen berikut:

```python
# Program Hello World
print("Hello, World.")
```

1.  Jalankan program. Apa outputnya?
2.  Tambahkan `print("Apakabssss ?")` di bawahnya. Jalankan lagi. Apa outputnya sekarang?
3.  Tambahkan komentar `# Ini eksperimenku`. Apakah outputnya berubah?
4.  Hapus salah satu tanda kutip, misalnya jadi `print("Hello, World.)`. Apa pesan error yang muncul?
5.  Salah ketik `print` menjadi `prnt`. Apa pesan error yang muncul?
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

##### **Bagaimana Cara Membukanya?**

1. Buka **Terminal** (bisa langsung di dalam VS Code).
2. Ketik `python` (atau `python3` pada beberapa sistem) lalu tekan **Enter**.
3. Kamu akan melihat prompt berubah menjadi `>>>`. Ini tandanya Python Shell sudah siap menerima perintahmu\!

##### **Ayo Bermain\! Skenario: Toko Kue Ajaib**

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

##### **Kapan Sebaiknya Menggunakan Shell Ini?**

* Saat kamu ingin **menguji ide kecil** atau satu baris kode dengan cepat.
* Saat kamu **lupa sebuah sintaks** dan ingin mencobanya terlebih dahulu.
* Saat kamu ingin **mengecek tipe data** atau nilai dari sebuah variabel.

Untuk keluar dari shell, cukup ketik `exit()` dan tekan **Enter**.

Tentu, ini draf untuk seksi 1.4 yang berisi instruksi pengerjaan soal berdasarkan file yang kamu berikan.

---

#### **Tutor 1.4: Petunjuk Pengerjaan Soal 📝**

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
Tentu, ini versi instruksi yang diperbaiki agar lebih jelas dan alurnya lebih baik.

#### **Untuk Soal Tugas T1 (Navigasi Robot) 🤖**

Soal ini berbeda! Kamu tidak membuat file baru, tetapi **mengisi kode** pada file yang sudah ada untuk menggerakkan sebuah robot.

---

### **Perintah yang Tersedia 📜**

Gunakan perintah-perintah berikut di dalam kodemu untuk mengontrol pergerakan robot:

* `restart()`
    * Mengembalikan robot ke posisi awal (0, 0) dan menghadap ke arah semula.

* `maju(pixel)`
    * Membuat robot bergerak maju lurus sejauh jumlah `pixel` yang ditentukan. Contoh: `maju(123)`.

* `mundur(pixel)`
    * Membuat robot bergerak mundur lurus sejauh jumlah `pixel` yang ditentukan. Contoh: `mundur(9)`.

* `putar_kanan(derajat)`
    * Membuat robot berputar di tempat ke **kanan** sebesar `derajat`. Contoh: `putar_kanan(-120)`.

* `putar_kiri(derajat)`
    * Membuat robot berputar di tempat ke **kiri** sebesar `derajat`. Contoh: `putar_kiri(90)`.

---

### **Langkah Pengerjaan ✍️**

1.  **Buka File Jawaban:**
    Cari dan buka file bernama `jawabanmu_M1_navigasirobot.py` yang ada di dalam folder `jawaban_akhir`.

2.  **Isi Logika di Dalam Fungsi:**
    Kamu akan melihat sebuah fungsi yang sudah disiapkan. Tuliskan urutan perintahmu **di dalam fungsi tersebut**.

3.  **Visualisasikan & Uji Jawabanmu:**
    Ini adalah langkah terpenting untuk memastikan solusimu benar.
    
    * **Untuk Mencoba Hasil Jawabanmu:** Jalankan file `jawabanmu_M1_navigasirobot.py` yang ada di dalam folder `jawaban_akhir`. Klik jendela simulasinya nya kalau mau kamu tutup.
    * **Untuk Mencoba Robot Secara Interaktif:** Jalankan file `assetlab_T1_interactivemode.py` yang ada di folder `file_pendukung`. Sebuah jendela simulasi akan muncul dan menampilkan pergerakan robotmu secara visual. Ketik perintahmu sebaris sebaris di terminal.
    * **Untuk Memastikan Jawaban Benar:** Jalankan file `test_M1_goalachieved.py` yang ada di folder `penguji_otomatis`. Terminal akan memberimu pesan **"OK"** jika berhasil atau **"FAILED"** jika gagal.

4.  **Kumpulkan Jawaban:**
    Setelah pengujian otomatis menunjukkan **"OK"**, simpan file jawabanmu dan kumpulkan tugasmu menggunakan `git push`.

Jika ada kesulitan, jangan ragu untuk bertanya. Selamat mengerjakan!
