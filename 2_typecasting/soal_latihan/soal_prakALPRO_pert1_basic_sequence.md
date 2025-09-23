---
header-includes: |
  \usepackage{fontspec}
  \setmonofont{Ubuntu Mono}
---

 **PRAK ALPRO ELEKTRO 2025**

# **Pertemuan 1 - Basic Sequence**


## ===== MATERI M1 ================================================  

### **1: Kalkulator Konversi Derajat ke Radian**

#### **Contoh Tampilan Program yang Diharapkan**
(Silakan ubah sesuai kemauanmu)

```
=== No.1 ===
Sudut dalam derajat: 45
Sudut dalam radian: 0.783 rad
Sudut dalam radian : 0.25 pi rad
```


Tujuan:
Buatlah sebuah program yang mengkonversi sudut dari satuan derajat ke radian dan mencetak hasilnya dalam dua format: sebagai angka desimal dan sebagai pecahan dari $\pi$.



#### **Petunjuk**

  * Tentukan sebuah variabel untuk sudut dalam derajat, misalnya **$45^\circ$**.
  * Hitung nilai radian dari sudut tersebut menggunakan rumus konversi.
  * Cetak hasil konversi dalam bentuk angka desimal, cukup 3 angka di belakang koma
  * Cetak juga hasil konversi dalam bentuk pecahan dikali $\pi$.

**Rumus**
$$\text{Radians} = \text{Derajat} \times \frac{\pi}{180}$$




============================================================================

Tentu, ini adalah versi yang disempurnakan dengan frasa yang lebih familiar dan alur yang lebih jelas untuk mahasiswa.

-----

### **2: Kalkulator Torsi**

#### **Contoh Tampilan Program yang Diharapkan**

(Silakan ubah sesuai kemauanmu)

```
=== No.2 ===
==== Diketahui : ====
Gaya (F) = 25.5 N
Panjang Lengan (r) = 0.45 m
Sudut (theta) = 60 derajat

==== Ditanya : ====
Berapa besar torsi (τ)?

==== Jawaban : ====
Besar torsi adalah 9.938 N·m
```

Budi sedang mengerjakan laporan praktikum Fisika Dasar. Ia harus menghitung torsi untuk 10 set data yang berbeda, dan menghitungnya satu per satu dengan kalkulator manual sangat rawan *typo*. "Daripada hitung manual dan salah terus, mending aku buat programnya sekalian\!" pikirnya.

Torsi ($\\tau$) adalah **kekuatan putar**. Bayangkan saat kamu menggunakan kunci pas untuk mengencangkan baut. Gaya dorong tanganmu adalah **$F$**, panjang kunci pas adalah **$r$**, dan kekuatan putaran yang dihasilkan pada baut itulah yang disebut **torsi**.

**Tujuan:**
Buatlah program yang menghitung dan mencetak torsi ($\\tau$) menggunakan fungsi trigonometri.

**Rumus**
$$\tau = r \cdot F \cdot \sin(\theta)$$

**Keterangan:**

  * $\\tau$ adalah torsi (N·m)
  * $r$ adalah panjang lengan tuas (m)
  * $F$ adalah besar gaya yang diberikan (N)
  * $\\theta$ adalah sudut antara lengan tuas dan arah gaya (derajat)

-----

    
#### **Petunjuk**

  * Impor modul `math` agar bisa menggunakan fungsi matematika.
  * Tentukan variabel untuk gaya ($F$), panjang lengan tuas ($r$), dan sudut ($\theta$) dalam satuan derajat.
  * Ubah nilai sudut dari derajat ke radian menggunakan `math.radians()`.
  * Hitung torsi menggunakan rumus: `τ=rFsin(θ)`.
  * Cetak semua nilai yang digunakan dan hasil akhir torsi dengan label yang jelas.




=========================================================================


### **3: Kalkulator Gaya Coulomb**

#### **Contoh Tampilan Program yang Diharapkan**

(Silakan ubah sesuai kemauanmu)

```
=== No.3 ===
==== Diketahui : ====
Konstanta Coulomb (k_e) = 8.99e+09 N·m^2 /C^2
Muatan q1 = 2 x 10**(-6) C atau 2e-06 C
Muatan q2 = -3 x 10**(-6) C atau -3e-06 C
Jarak (r) = 5 x 10**(-2) m atau 0.05 m

==== Ditanya : ====
Berapa besar gaya Coulomb (F)?

==== Jawaban : ====
F = 21.576 N
```

Budi, si mahasiswa Elektro yang *mager* itu, kini menghadapi musuh bebuyutan lain: gaya tarik-menarik antara muatan. Ia ditantang untuk menhitung gaya Coulomb antara dua partikel, dan angka-angkanya sangat kecil dengan banyak nol. Daripada pusing, Budi memutuskan untuk menulis program yang bisa menghitungnya dalam sekejap.

**Tujuan:**
Buatlah program yang menghitung dan mencetak gaya Coulomb ($F$) antara dua muatan titik. satuan yang akan dimasukkan ke program sudah dalam satuan Coulomb dan meter.

**Rumus:**
$$F = k_e \frac{|q_1 q_2|}{r^2}$$

#### **Petunjuk**

  * Tentukan variabel untuk konstanta Coulomb ($k\_e$), dua muatan ($q\_1$, $q\_2$), dan jarak antara muatan ($r$).
  * Berikan nilai numerik pada variabel-variabel ini (kamu bisa menggunakan notasi `e` untuk pangkat 10, contoh: `8.99e9`).
  * Hitung gaya Coulomb menggunakan rumus. Gunakan fungsi `abs()` untuk nilai mutlak $|q\_1 q\_2|$.
  * Cetak semua nilai yang diketahui dan gaya yang dihasilkan ($F$) dengan rapi.
---
## Bonus: +5 untuk pertemuan minggu ini kalau...

bisa mengeprint hal ini:

---

## ===== TUGAS T1 ================================================  

### **1: Navigasi Robot**


### **Misi:**

**Tujuan:**

Buatlah sebuah program yang berisi urutan (sekuens) gerakan untuk menavigasikan robot dari posisi awal ke posisi tujuan.

**Skenario:**

* **Posisi Awal:** (0, 0)
* **Tujuan:** (200, 200)
* **Rintangan:** semua lingkaran merah
![gambar rintangan](file_pendukung/foto/ss_T1_interactivemode_awal.png)  

**Instruksi Pengerjaan:**

1.  Buka file `jawabanmu_M1_navigasirobot.py` yang berada di dalam folder `jawaban_akhir`.
2.  Tuliskan urutan gerakanmu di dalam fungsi yang telah disediakan.
3.  Gunakan dua perintah utama berikut untuk menggerakkan robot:
    * `maju(langkah)`: Membuat robot bergerak maju sejumlah `langkah`.
    * `belok(derajat)`: Membuat robot berbelok ke kanan (+) atau ke kiri (-) sejumlah `derajat`.
4.  Susun gerakan sedemikian rupa sehingga robot bisa melewati rintangan dan sampai ke tujuan.

#### **Petunjuk**

-   **Melihat Pergerakan Robot:** Setelah selesai menulis kode, jalankan skrip `assetlab_M1_navigasirobot_wrapper.py` untuk melihat visualisasi pergerakan robotmu.
-   **Menguji Jawaban:** Untuk memastikan robotmu sampai di tujuan dengan benar, jalankan `test_M1_goalachieved.py` yang ada di folder `penguji_otomatis`. Jika tes berhasil, jawabanmu sudah benar.
-   **Mengumpulkan Jawaban:** Jika semua tes sudah lolos, simpan file jawabanmu dan kirimkan dengan perintah `git push`.

