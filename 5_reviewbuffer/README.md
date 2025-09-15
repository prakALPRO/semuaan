### Minggu 5: (Review Buffer) Pemecahan Masalah & Berpikir Algoritmik 🧠

Tujuan minggu ini adalah membantu siswa mengembangkan keterampilan inti dalam pemrograman: kemampuan untuk memecah masalah besar menjadi bagian-bagian yang lebih kecil dan menggunakan alat yang mereka miliki untuk menyelesaikannya.



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

1.  **Kerangka Pemecahan Masalah**

      * **Mengapa:** Ajarkan siswa cara berpikir sistematis, bukan hanya menulis kode. Ini adalah keterampilan yang bisa diterapkan pada masalah apa pun.
      * **Bagaimana:** Kenalkan kerangka kerja 4 langkah:
        1.  **Pahami (Decomposition):** Pecah masalah menjadi bagian-bagian kecil.
        2.  **Rencanakan (Pattern Recognition):** Cari pola yang bisa diulang.
        3.  **Kode (Abstraction):** Tulis kode yang rapi.
        4.  **Uji (Algorithm Design):** Pastikan kode berfungsi untuk semua kasus.

2.  **Sesi Pemecahan Masalah Langsung**

      * **Mengapa:** Demonstrasi langsung adalah cara terbaik untuk menunjukkan kerangka kerja ini beraksi.
      * **Bagaimana:** Pimpin siswa melalui dua atau tiga tantangan coding klasik yang menggabungkan perulangan dan kondisional.
          * **Tantangan 1 (FizzBuzz):** Sebuah program yang mencetak angka dari 1 hingga 100, tetapi mengganti kelipatan 3 dengan "Fizz", kelipatan 5 dengan "Buzz", dan kelipatan 3 dan 5 dengan "FizzBuzz".
          * **Tantangan 2 (Palindrome Checker):** Buat program yang memeriksa apakah sebuah kata dibaca sama dari depan dan belakang. Ini akan memaksa mereka untuk menggunakan perulangan pada sebuah string.
---

### Cheatsheet


**Kerangka Pemecahan Masalah:**

1.  Pahami masalahnya.
2.  Rencanakan solusinya (pseudocode/flowchart).
3.  Tulis kode.
4.  Uji kode dengan berbagai masukan.

---

### Soal

* **Tugas5: TUG5_PengaplikasianTeknikElektro** 
* Carilah satu rumus matematika yang ingin kamu aplikasikan ke dalam program kalkulatormu sendir. jelaskan apa saja variabelnya dan jelaskan isi programmu dengan flowchart dan pseudocode. taro di github repo class kita.


# Materi 5: MAT5_KalkulatorRangkaianResistor 🔌
konsep dasar:
 **input**, **perulangan**, **kondisional**, dan **perhitungan sekuensial** untuk memecahkan masalah Teknik Elektro praktis.

### Kalkulator Rangkaian Resistor 🔌**

Anda diminta untuk membuat sebuah program yang dapat menghitung total resistansi dari sebuah rangkaian listrik murni. Program ini harus bisa menghitung dua jenis rangkaian: seri dan paralel.

**Penjelasan Materi 5:**

1.  Buat program yang bisa menerima input dari pengguna tentang jenis rangkaian (`seri` atau `paralel`).
2.  Minta pengguna untuk memasukkan jumlah resistor yang ada di rangkaian tersebut.
3.  Kemudian, minta pengguna untuk memasukkan nilai resistansi dari setiap resistor satu per satu.
4.  Setelah semua nilai dimasukkan, hitung total resistansi menggunakan logika yang benar.
5.  Cetak hasil akhirnya ke layar dengan format yang jelas.

---

### **Logika dan Rumus**

* **Rangkaian Seri:** Total resistansi adalah jumlah dari semua nilai resistansi.
    $R_{total} = R_1 + R_2 + ... + R_n$
    
* **Rangkaian Paralel:** Total resistansi adalah kebalikan dari jumlah kebalikan setiap nilai resistansi.
    $1/R_{total} = 1/R_1 + 1/R_2 + ... + 1/R_n$

---

### **Contoh Alur Program**

**Skenario Rangkaian Seri:**
* **Input 1:** "seri"
* **Input 2:** "3" (untuk 3 resistor)
* **Input 3:** "10", "20", "30"
* **Output:** "Total resistansi seri adalah: 60 ohm"

**Skenario Rangkaian Paralel:**
* **Input 1:** "paralel"
* **Input 2:** "2" (untuk 2 resistor)
* **Input 3:** "10", "10"
* **Output:** "Total resistansi paralel adalah: 5.0 ohm"

**Catatan:** Pastikan program Anda bisa menangani input yang tidak valid, misalnya jika pengguna memasukkan jenis rangkaian yang tidak dikenali atau input yang bukan angka.
