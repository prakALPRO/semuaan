\newpage
# **SOAL Pertemuan 1 - Basic Sequence**


## ===== MATERI M1 ================================================  

### **1: Kalkulator Konversi Derajat ke Radian**

#### **Contoh Tampilan Program yang Diharapkan**

![ss soal](file_pendukung/foto/ss_M1_1.png){width=100%}  

(Silakan ubah sesuai kemauanmu)

```
=== No.1 ===
Sudut dalam derajat: 45
Sudut dalam radian: 0.783 rad
Sudut dalam radian : 0.25 pi rad
```


**Goal**
Buatlah sebuah program yang mengkonversi sudut dari satuan derajat ke radian dan mencetak hasilnya dalam dua format: sebagai angka desimal dan sebagai pecahan dari $\pi$.



#### **Petunjuk**

  * Tentukan sebuah variabel untuk sudut dalam derajat, misalnya **$45^\circ$**.
  * Hitung nilai radian dari sudut tersebut menggunakan rumus konversi.
  * Cetak hasil konversi dalam bentuk angka desimal, cukup 3 angka di belakang koma
  * Cetak juga hasil konversi dalam bentuk pecahan dikali $\pi$.

**Rumus**  
$$\text{Radians} = \text{Derajat} \times \frac{\pi}{180}$$




============================================================================

\newpage

### **2: Kalkulator Torsi**

#### **Contoh Tampilan Program yang Diharapkan**
![ss soal](file_pendukung/foto/ss_M1_2.png){width=100%}  

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


**Goal**
Buatlah program yang menghitung dan mencetak torsi ($\tau$) menggunakan fungsi trigonometri.


**Keterangan:**

  * $\tau$ adalah torsi (N·m)
  * $r$ adalah panjang lengan tuas (m)
  * $F$ adalah besar gaya yang diberikan (N)
  * $\theta$ adalah sudut antara lengan tuas dan arah gaya (derajat)


    
#### **Petunjuk**

  * Impor modul `math` agar bisa menggunakan fungsi matematika.
  * Tentukan variabel untuk gaya ($F$), panjang lengan tuas ($r$), dan sudut ($\theta$) dalam satuan derajat.
  * Ubah nilai sudut dari derajat ke radian menggunakan `math.radians()`.
  * Hitung torsi menggunakan rumus: `τ=rFsin(θ)`.
  * Cetak semua nilai yang digunakan dan hasil akhir torsi dengan label yang jelas.

**Rumus**  
 $$\tau = r \cdot F \cdot \sin(\theta)$$



=========================================================================

\newpage

### **3: Kalkulator Gaya Coulomb**

#### **Contoh Tampilan Program yang Diharapkan**
![ss soal](file_pendukung/foto/ss_M1_3.png){width=100%}  

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

**Goal**
Buatlah program yang menghitung dan mencetak gaya Coulomb ($F$) antara dua muatan titik. satuan yang akan dimasukkan ke program sudah dalam satuan Coulomb dan meter.


#### **Petunjuk**

  * Tentukan variabel untuk konstanta Coulomb ($k\_e$), dua muatan ($q\_1$, $q\_2$), dan jarak antara muatan ($r$).
  * Berikan nilai numerik pada variabel-variabel ini (kamu bisa menggunakan notasi `e` untuk pangkat 10, contoh: `8.99e9`).
  * Hitung gaya Coulomb menggunakan rumus. Gunakan fungsi `abs()` untuk nilai mutlak $|q\_1 q\_2|$.
  * Cetak semua nilai yang diketahui dan gaya yang dihasilkan ($F$) dengan rapi.

**Rumus:**  
 $$F = k_e \frac{|q_1 q_2|}{r^2}$$

\newpage

## ===== TUGAS T1 ================================================  

### **1: Navigasi Robot**

**Tujuan:**

Buatlah sebuah program yang berisi urutan (sekuens) gerakan untuk menavigasikan robot dari posisi awal ke posisi tujuan.

**Skenario:**

* **Posisi Awal:** (0, 0)
* **Tujuan:** (200, 200)
* **Rintangan:** semua lingkaran merah  

![gambar rintangan](file_pendukung/foto/ss_T1_interactivemode_awal.png){width=100%}  

**Instruksi Pengerjaan:**

1.  Buka file `jawabanmu_M1_navigasirobot.py` yang berada di dalam folder `jawaban_akhir`.
2.  Tuliskan urutan gerakanmu di dalam fungsi yang telah disediakan.
3.  Gunakan perintah berikut untuk menggerakkan robot:
* `maju(pixel)`
    * Membuat robot bergerak maju lurus sejauh jumlah `pixel` yang ditentukan. Contoh: `maju(123)`.

* `mundur(pixel)`
    * Membuat robot bergerak mundur lurus sejauh jumlah `pixel` yang ditentukan. Contoh: `mundur(9)`.

* `putar_kanan(derajat)`
    * Membuat robot berputar di tempat ke **kanan** sebesar `derajat`. Contoh: `putar_kanan(-120)`.

* `putar_kiri(derajat)`
    * Membuat robot berputar di tempat ke **kiri** sebesar `derajat`. Contoh: `putar_kiri(90)`.

4.  Susun gerakan sedemikian rupa sehingga robot bisa melewati rintangan dan sampai ke tujuan.

#### **Petunjuk**

-   **Melihat Pergerakan Robot:** Setelah selesai menulis kode, jalankan skrip `assetlab_M1_navigasirobot_wrapper.py` untuk melihat visualisasi pergerakan robotmu.
-   **Menguji Jawaban:** Untuk memastikan robotmu sampai di tujuan dengan benar, jalankan `test_M1_goalachieved.py` yang ada di folder `penguji_otomatis`. Jika tes berhasil, jawabanmu sudah benar.
-   **Mengumpulkan Jawaban:** Jika semua tes sudah lolos, simpan file jawabanmu dan kirimkan dengan perintah `git push`.

