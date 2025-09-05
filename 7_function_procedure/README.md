### Minggu 7: Fungsi & Prosedur ⚙️    

Tujuan minggu ini adalah mengajarkan siswa cara menulis kode yang rapi, terorganisir, dan dapat digunakan kembali. Ini adalah langkah besar menuju penulisan program yang lebih kompleks dan mudah dikelola.

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


1.  **Fungsi vs. Prosedur**

      * **Mengapa:** Jelaskan bahwa membedakan antara "melakukan sesuatu" dan "mengembalikan nilai" adalah konsep inti pemrograman. Sebuah **prosedur** melakukan tugas tanpa mengembalikan nilai (seperti `print()`), sementara sebuah **fungsi** menghitung atau memproses sesuatu dan **mengembalikan hasilnya** (seperti `len()` atau `max()`).
      * **Bagaimana:** Tunjukkan kedua konsep secara berdampingan.
          * **Prosedur:** Buat kode yang hanya mencetak pesan, tanpa `return`.
          * **Fungsi:** Buat kode yang menjumlahkan dua angka dan **mengembalikan** hasilnya menggunakan `return`.

2.  **Parameter dan Argumen**

      * **Mengapa:** Fungsi dan prosedur membutuhkan informasi untuk bekerja. Informasi ini disebut **parameter**.
      * **Bagaimana:** Jelaskan bahwa parameter adalah *input* yang diberikan saat fungsi dipanggil. Tunjukkan bagaimana membuat fungsi yang menerima parameter.

3.  **Menerapkan Fungsi**

      * **Live Coding:** Ambil tugas yang sudah mereka kerjakan sebelumnya (misalnya, kalkulator luas dari Minggu 2) dan tunjukkan cara mengubahnya menjadi sebuah fungsi yang dapat digunakan kembali. Ini menunjukkan manfaat nyata dari modularitas.
      * **Contoh:**

    <!-- end list -->

    ```python
    # Prosedur: Tidak mengembalikan nilai
    def sapa_pengguna(nama):
        print(f"Halo, {nama}!")

    # Fungsi: Mengembalikan nilai
    def hitung_luas_persegi(sisi):
        luas = sisi * sisi
        return luas
    ```

---

### Cheatsheet


**Sintaks Fungsi/Prosedur:**

  * `def nama_fungsi(parameter):`
  * Gunakan `return` untuk mengembalikan nilai.

**Contoh Praktis:**

  * **Prosedur:** `sapa_pengguna("Budi")` → hanya mencetak di layar.
  * **Fungsi:** `luas_kamar = hitung_luas_persegi(5)` → menyimpan nilai yang dikembalikan.

---

### Soal

* **Tugas:** 
*  refactor?


* **Materi:** 
* yg dibikin, jadiin function? procedure?
