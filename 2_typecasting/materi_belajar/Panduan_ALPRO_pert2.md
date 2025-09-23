SANGAT Terinspirasi dari buku:

"Think Python" karya Allen Downey terbitan  Green Tea Press   
[Think Python 2nd Edition, Version 2.4.0 ](https://greenteapress.com/thinkpython2/thinkpython2.pdf)  

-----

# **Minggu 2: Typecasting** 📝

```
IKO HORONGGGG

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
Tentu, ini adalah *cheatsheet* yang bisa Anda gunakan.

### Konversi Tipe Data (Typecasting)

Tabel ini menunjukkan fungsi-fungsi dasar untuk mengubah satu tipe data ke tipe data lainnya.

| Fungsi (Sintaks) | Contoh Penggunaan | Hasil & Penjelasan |
| :--- | :--- | :--- |
| **`int()`** | `int(15.7)`<br>`int("15")` | `15`<br>`15`<br>Mengonversi ke bilangan bulat (**integer**). Perhatikan bahwa nilai desimal akan dihilangkan, bukan dibulatkan. |
| **`float()`** | `float(15)`<br>`float("15.7")` | `15.0`<br>`15.7`<br>Mengonversi ke bilangan desimal (**float**). |
| **`str()`** | `str(15)`<br>`str(15.7)` | `"15"`\<br`"15.7"`<br>Mengonversi ke **string** (teks). Sangat berguna untuk menggabungkan angka dengan teks. |
| **`bool()`** | `bool(15)`<br>`bool(0)`<br>`bool("Halo")`<br>`bool("")` | `True`<br>`False`<br>`True`<br>`False`<br>Mengonversi ke **boolean**. Angka `0`, `0.0`, dan *string* kosong (`""`) dianggap `False`, sementara nilai lainnya dianggap `True`. |

---

### Ringkasan Error Umum & Solusinya

| Error | Penyebab Kunci | Contoh Singkat | Solusi Cepat |
| :--- | :--- | :--- | :--- |
| **`TypeError`** | Operasi tipe data tidak cocok. | `"teks" + 5` | Samakan tipe datanya (pakai `str()`, `int()`). |
| **`ValueError`** | Nilai tidak valid untuk fungsi. | `int("halo")` | Pastikan nilai input bisa dikonversi. |
| **`SyntaxError`**| Salah ketik atau aturan dilanggar. | `print("lupa tutup` | Cek *typo*, kurung `()`, dan kutip `""`. |
| **`NameError`** | Variabel/fungsi salah ketik. | `printt("salah")` | Cek nama variabel/fungsi & huruf besar/kecilnya. |

### **EKSPLORASI LIVE CODING**

#### **Tutor 1.1: Utak-atik Kode**

Salin kode ini dan lakukan eksperimen berikut:

```python
nama_pengguna = input("halo, apakabs! namamu siapa ? ")
print(f"Halo, {nama_pengguna}! Senang bertemu denganmu.")

```

1.  Jalankan kode di atas. Apa yang terjadi saat program mencapai baris input()? Perhatikan bagaimana program berhenti dan menunggu Anda mengetik sesuatu.
2.  Sekarang, coba "isengi" programnya. Jalankan lagi, tetapi masukkan angka 123 sebagai namamu. Apa outputnya? Apakah ada error? Mengapa tidak?
3.  Coba ganti kets di dalam input(). Apa yang berubah?
4.  Coba tambahkan baris kode di akhir untuk menampilkan `print(nama_pengguna * 3)`. Sekarang, apa yang tercetak? Apakah hasilnya sesuai dugaanmu? Ini adalah petunjuk pertama bahwa input() menganggap angka dan huruf sama saja.
5.  Salah ketik `input()` menjadi `Input()`. Apa pesan error yang muncul?
-----

#### **Tutor 1.2: kenapa perlu typecasting **

Program di bawah ini penuh dengan *bug*. Di versi ini, tanggalnya sudah ditentukan di dalam variabel, jadi kamu hanya perlu fokus memperbaiki **kesalahan sintaks** agar program bisa berjalan dan menghasilkan output yang benar.

```python
# Program Pengecek Tahun Kelahiran (Versi Error)
umur_sekarang_str = input("Masukkan umurmu tahun ini: ")

# Kita asumsikan tahun ini 2025
tahun_lahir = 2025 - umur_sekarang_str # Baris ini akan menyebabkan TypeError!

print(f"Wah, berarti kamu lahir sekitar tahun {tahun_lahir}.")
```

    1.  Jalankan kode di atas dan masukkan umurmu. **Boom\!** Anda akan disambut dengan `TypeError`. Pesan *error*-nya mengatakan Anda tidak bisa melakukan operasi pengurangan antara `int` (2025) dan `str` (hasil input).
    2.  **Pembuktian**: Tambahkan baris `print(type(umur_sekarang_str))` tepat setelah baris `input()` dan jalankan lagi. Ini akan mengonfirmasi bahwa tipe datanya memang `str`.
    3.  **Perbaikan**: Sekarang, perbaiki programnya. Buat variabel baru `umur_sekarang_int` dengan mengonversi `umur_sekarang_str` menggunakan `int()`. Ganti variabel di dalam perhitungan matematika dengan variabel baru ini.
    4.  **Eksperimen Lanjutan**: Setelah berhasil, coba jalankan lagi dan masukkan `25.5` sebagai umur. *Error* apa yang muncul sekarang? Ini adalah `ValueError`, yang menunjukkan bahwa `int()` tidak bisa menangani *string* yang berisi titik desimal. Ubah `int()` menjadi `float()` untuk menyelesaikannya.

-----

#### **Tutor 1.3: Mengupgrade salah satu kalkulator M1 **

kita akan coba salah satu kalkulator yg lalu~
![kita pilih satu buat contoh ](file_pendukung/foto/wheelofnames_tutorinM1ygmana.png)  

1.  **Cari Variabel Statis**: Temukan baris yang hardcoded. Ini adalah target kita.
2.  **Ganti dengan `input()`**: Hapus baris tersebut. Gantikan dengan kode yang meminta input dari pengguna.
3.  **Lakukan Typecasting**: Bungkus fungsi `input()` dengan `float()` agar teks masukan dari pengguna diubah menjadi angka desimal yang bisa dihitung. 


| Langkah Upgrade | Kalkulator Radian | Kalkulator Torsi | Kalkulator Gaya Coulomb |
| :--- | :--- | :--- | :--- |
| **1. Cari Variabel Statis** | `sudut_derajat = 45` | `gaya_f = 25.5`<br>`panjang_r = 0.45`<br>`sudut_theta_derajat = 60` | `muatan_q1 = 2e-6`<br>`muatan_q2 = -3e-6`<br>`jarak_r = 0.05` |
| **2. Ganti dengan `input()** | `sudut_derajat = float(input("..."))` | `gaya_f = float(input("..."))`<br>`panjang_r = float(input("..."))`<br>`sudut_theta_derajat = float(input("..."))` | `muatan_q1 = float(input("..."))`<br>`muatan_q2 = float(input("..."))`<br>`jarak_r = float(input("..."))` |
| **3. Catatan Khusus (Konstanta)** | - | - | Variabel `konstanta_coulomb` **dibiarkan tetap** karena merupakan nilai tetapan fisika. |

---

#### **Tutor 1.4: Petunjuk Pengerjaan Soal 📝**

Kali ini, hanya ada soal **Materi M2**. gaada tugas yeyyyy! 

**Instruksi Umum:** Buka kembali file-file jawaban Anda dari **Materi M1** YANG BELUM KITA UBAH MENJADI INTERAKTIF. Untuk setiap soal buatlah salinan file tersebut (misalnya `M1_1_radian.py` menjadi `M2_1_radian_interaktif.py`), lalu modifikasi salinan tersebut sesuai petunjuk.

#### **1: Kalkulator Konversi Derajat ke Radian (Interaktif)**

  * **Goal**: Mengubah skrip kalkulator radian statis menjadi program interaktif yang menanyakan pengguna sudut berapa yang ingin dikonversi.
  * **Petunjuk Pengerjaan**:
    1.  Cari baris kode di mana Anda mendefinisikan `sudut_derajat` secara manual (misal: `sudut_derajat = 45`).
    2.  Gantilah baris tersebut. Gunakan `float(input(...))` untuk meminta pengguna memasukkan nilai sudut.
    3.  Pastikan sisa dari program menggunakan variabel hasil input tersebut untuk kalkulasi.
  * **Contoh Tampilan Program**:
    ```
    Masukkan sudut dalam derajat: 30

    === Hasil Konversi ===
    Sudut dalam derajat: 30.0
    Sudut dalam radian= 0.524 rad
    Sudut dalam pi radian= 0.16666666666666666 pi rad
    ```

#### **2: Kalkulator Torsi (Interaktif)**

  * **Goal**: Mengubah skrip kalkulator torsi menjadi program interaktif yang meminta semua variabel (gaya, panjang lengan, dan sudut) dari pengguna.
  * **Petunjuk Pengerjaan**:
    1.  Identifikasi tiga variabel statis di awal program: `gaya_f`, `panjang_r`, dan `sudut_theta_derajat`.
    2.  Gantilah ketiga baris tersebut dengan tiga panggilan `float(input(...))` yang terpisah, masing-masing dengan pesan yang jelas untuk pengguna.
  * **Contoh Tampilan Program**:
    ```
    === No.2 ===
    ==== Diketahui : ====
    Gaya (F) dalam Newton:  15.5 
    Panjang Lengan (r) dalam meter = 0.5 
    Sudut (theta) dalam derajat = 90.0

    ==== Jawaban : ====
    Besar torsi adalah 7.750 N·m
    ```

