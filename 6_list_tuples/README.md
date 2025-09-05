### Minggu 6: Struktur Data (Lists & Tuples) 📦  

Tujuan minggu ini adalah mengajarkan siswa cara menyimpan dan mengelola banyak item dalam satu wadah. Ini adalah langkah penting untuk menangani data skala besar.  



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

1.  **Lists: Koleksi yang Fleksibel**

      * **Mengapa:** Jelaskan bahwa `list` adalah cara Python untuk menyimpan daftar item yang dapat diubah dan diurutkan. Pikirkan sebagai **daftar belanjaan** — Anda bisa menambah atau menghapus barang sesuka hati.  
      
      * **Bagaimana:** Tunjukkan cara membuat `list` dengan tanda kurung siku `[]` dan metode manipulasi paling relevan:
        * `.append()` untuk menambahkan item ke akhir daftar.
        * `.remove()` untuk menghapus item berdasarkan nilai.
        * `.pop()` untuk menghapus item berdasarkan indeks.
        * `.sort()` untuk mengurutkan item.
        
      * **Live Coding:** Tunjukkan cara membuat `list` dan memanipulasinya, seperti menambahkan nama baru atau menghapus nama yang sudah ada  

2.  **Tuples: Koleksi yang Tetap**

      * **Mengapa:** `tuple` juga menyimpan daftar item, tetapi bersifat **immutable** (tidak dapat diubah). Gunakan ini saat Anda memiliki data yang tidak boleh berubah.  
      
      * **Bagaimana:** Tunjukkan cara membuat `tuple` dengan tanda kurung biasa `()` dan demonstrasikan bahwa Anda **tidak dapat** memanipulasinya.  
      
3.  **Kapan Menggunakan yang Mana?**
    * Berikan panduan sederhana: Gunakan `list` saat Anda perlu mengubah data, dan gunakan `tuple` saat data Anda harus tetap konstan.

---

### Cheatsheet


**Sintaks Lists:**
* `daftar = ["apel", "jeruk"]`
* `daftar.append("mangga")`
* `daftar.pop(0)`

**Sintaks Tuples:**
* `nilai_tes = (85, 92, 78)`

**Fungsi Penting:**
* `len(koleksi)`: Mengembalikan jumlah item.

---

### Soal

* **Tugas:** 
*  Buat program database.


* **Materi:** 
* Buat program yang melacak skor harian. Minta pengguna untuk memasukkan skor selama lima hari berturut-turut. Simpan skor tersebut dalam sebuah `list`, hitung rata-rata, lalu cetak skor tertinggi dan terendah.
