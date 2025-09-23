
## Kunci Jawaban ===== MATERI =================================================

### 1: Kalkulator Konversi Derajat ke Radian
**Solusi**

```python

import math

# 1. Tentukan variabel untuk sudut dalam derajat
sudut_derajat = 45

# 2. Hitung nilai radian dalam bentuk desimal
# Rumus: Derajat * (pi / 180)
sudut_radian_desimal = sudut_derajat * (math.pi / 180)

# 3. Hitung nilai sudut sebagai sesuatu dikali pi
berapa_pi = sudut_derajat/ 180

# 4. Cetak semua hasil sesuai format yang diminta
print("=== No.1 ===")

print(f"Sudut dalam derajat: {sudut_derajat}")

# Gunakan f-string format ".3f" untuk membulatkan hasil menjadi 3 angka di belakang koma
print(f"Sudut dalam radian: {sudut_radian_desimal:.3f} rad")

# Cetak objek fraksi yang sudah disederhanakan
print(f"Sudut dalam radian (fraksi pi): {berapa_pi} pi rad")

```




### 2: Kalkulator Torsi
**Solusi**

``` python
import math

# 1. Siapkan semua variabel yang nilainya sudah diketahui.
gaya_f = 25.5                # dalam Newton
panjang_r = 0.45             # dalam meter
sudut_theta_derajat = 60     # dalam derajat

# 2. Konversi sudut dari derajat ke radian karena math.sin() menggunakan radian.
sudut_theta_radian = math.radians(sudut_theta_derajat)

# 3. Hitung torsi menggunakan rumus: r * F * sin(theta).
torsi = panjang_r * gaya_f * math.sin(sudut_theta_radian)

# 4. Cetak semua informasi dan hasil akhir dengan format yang rapi.
print("=== No.2 ===")
print("==== Diketahui : ====")
print(f"Gaya (F) = {gaya_f} N")
print(f"Panjang Lengan (r) = {panjang_r} m")
print(f"Sudut (theta) = {sudut_theta_derajat}°")
print("")
print("==== Ditanya : ====")
print("Berapa besar torsi (τ)?")
print("")
print("==== Jawaban : ====")
# Bulatkan hasil torsi menjadi 3 angka di belakang koma agar lebih rapi
print(f"Besar torsi adalah {torsi:.3f} N·m")
```

### 3: Kalkulator Gaya Coulomb
**Solusi**

```python

# 1. Definisikan semua nilai yang diketahui (konstanta dan variabel)
# Kita menggunakan notasi 'e' untuk menulis bilangan saintifik dengan mudah.

konstanta_coulomb = 8.99e9  # N·m²/C²
muatan_q1 = 2e-6            # Coulomb
muatan_q2 = -3e-6           # Coulomb
jarak_r = 0.05              # meter

"""
 2. Hitung gaya Coulomb sesuai rumus
 
       ke * |q1 * q2|
F = -----------------
           r^2

Gunakan fungsi abs() untuk mendapatkan nilai absolut (nilai mutlak) dari perkalian muatan.
"""
gaya_coulomb = konstanta_coulomb * abs(muatan_q1 * muatan_q2) / (jarak_r**2)

# 3. Cetak semua informasi dengan rapi agar sesuai dengan contoh
# Kita menggunakan f-string untuk memformat output dengan mudah.
print("=== No.3 ===")
print("==== Diketahui : ====")
print(f"Konstanta Coulomb (k_e) = {konstanta_coulomb} N·m^2 /C^2")
print(f"Muatan q1 = {muatan_q1} C")
print(f"Muatan q2 = {muatan_q2} C")
print(f"Jarak (r) = {jarak_r} m")
print("") # Memberi spasi
print("==== Ditanya : ====")
print("Berapa besar gaya Coulomb (F)?")
print("") # Memberi spasi
print("==== Jawaban : ====")
print(f"F = {gaya_coulomb} N")

```


## Kunci Jawaban ===== TUGAS =================================================
















