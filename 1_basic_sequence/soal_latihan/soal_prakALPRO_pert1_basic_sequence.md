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
Sudut dalam radian: 0.7853981633974483 rad
Sudut dalam radian (fraksi pi): pi/4 rad
```


Tujuan:
Buatlah sebuah program yang mengkonversi sudut dari satuan derajat ke radian dan mencetak hasilnya dalam dua format: sebagai angka desimal dan sebagai fraksi dari $\pi$.



#### **Petunjuk**

  * Tentukan sebuah variabel untuk sudut dalam derajat, misalnya **$45^\circ$**.
  * Hitung nilai radian dari sudut tersebut menggunakan rumus konversi.
  * Cetak hasil konversi dalam bentuk angka desimal.
  * Cetak juga hasil konversi dalam bentuk fraksi $\pi$.

**Rumus**
$$\text{Radians} = \text{Derajat} \times \frac{\pi}{180}$$




============================================================================

### **2: Kalkulator Torsi**

#### **Contoh Tampilan Program yang Diharapkan**
(Silakan ubah sesuai kemauanmu)

``` 
=== No.2 ===
==== Diketahui : ====
F = 25.5 N
r = 0.45 m
theta = 60°

==== Ditanya : ====
Berapa besar torsi (tau)?

==== Jawaban : ====
τ = 9.937641508426433 N·m

```
Budi, seorang mahasiswa Elektro yang *mager* akut, sedang *rebahan* sambil menatap tumpukan soal. Soal ke-7 sangat menyebalkan baginya: harus menghitung torsi yang dibutuhkan untuk mengencangkan baut besar. Baginya, itu adalah kerjaan tangan yang melelahkan karena harus mengalikan angka-angka desimal. "Astaga, masa harus ngitung manual lagi sih?"

Torsi ($\tau$) adalah **kekuatan putar** yang dihasilkan saat sebuah gaya mendorong atau menarik suatu benda hingga berputar.

**Tujuan:**
Buatlah program yang menghitung dan mencetak torsi ($\tau$) menggunakan fungsi trigonometri.

**Rumus**
$$\tau = r \cdot F \cdot \sin(\theta)$$

**Keterangan:**

  * $\tau$ adalah torsi (kekuatan putar).
  * $r$ adalah panjang lengan tuas.
  * $F$ adalah besar gaya yang diberikan.
  * $\theta$ (theta) adalah sudut antara lengan tuas dan arah gaya.


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
F = 25.5 N
r = 0.45 m
theta = 60°

==== Ditanya : ====
Berapa besar torsi (tau)?

==== Jawaban : ====
τ = 9.937641508426433 N·m

```

Budi, si mahasiswa Elektro yang *mager* itu, kini menghadapi musuh bebuyutan lain: gaya tarik-menarik antara muatan. Ia harus menghitung gaya Coulomb antara dua partikel, dan angka-angkanya sangat kecil dengan banyak nol. "Kalau salah ketik nol, hancur sudah nilai UAS," pikirnya. Daripada pusing, Budi memutuskan untuk menulis program yang bisa menghitungnya dalam sekejap.

**Tujuan:**
Buatlah program yang menghitung dan mencetak gaya Coulomb ($F$) antara dua muatan titik.
s
**Rumus:**
$$F = k_e \frac{|q_1 q_2|}{r^2}$$



#### **Petunjuk**

  * Tentukan variabel untuk konstanta Coulomb ($k\_e$) dan dua muatan ($q\_1$, $q\_2$).
  * Tentukan variabel untuk jarak antara muatan ($r$).
  * Berikan nilai numerik pada variabel-variabel ini.
  * Hitung gaya Coulomb menggunakan rumus.
  * Cetak nilai dari $q\_1$, $q\_2$, $r$, dan gaya yang dihasilkan ($F$).


---

## ===== TUGAS T1 ================================================  

### **1: Navigasi Robot**


### **Misi:**

Nyoh si Robot adalah robot navigasi sederhana yang bertugas untuk mencapai titik tujuan. Jalur lurus menuju tujuan terhalang oleh sebuah rintangan. Tugasmu adalah memprogram Nyoh agar bisa mencapai tujuan tanpa menabrak rintangan.

---

**Tujuan:**

Buatlah sebuah program yang berisi urutan (sekuens) gerakan untuk mengarahkan Nyoh si Robot dari posisi awal ke posisi tujuan.

**Skenario:**

* **Posisi Awal:** (0, 0)
* **Tujuan:** (200, 200)
* **Rintangan:** Sebuah tumpukan batu besar menghalangi jalur lurus dari (0,0) ke (200,200). Rintangan ini berada di area sekitar **x = 100 dan y = 100**.

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

