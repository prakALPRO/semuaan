
## Kunci Jawaban ===== MATERI =================================================

### 1: Kalkulator Konversi Derajat ke Radian
**Solusi**

```python
import math

# Sudut dalam derajat yang akan dikonversi
angle_deg = 45.0

# 1. Konversi dari derajat ke radian
#    Kita menggunakan rumus: Radians = Degrees * (pi / 180)
angle_rad_decimal = angle_deg * (math.pi / 180)

# 2. Untuk mendapatkan fraksi pi, kita bisa membagi sudut derajat dengan 180,
#    lalu menyederhanakannya menjadi pecahan.
#    Untuk 45 derajat, fraksinya adalah 45/180 = 1/4
#    Jadi, hasilnya adalah pi/4 rad
pi_fraction_string = "pi/4"

# Tampilan Program
print("Sudut dalam derajat:", angle_deg, "°")
print("Sudut dalam radian:", angle_rad_decimal, "rad")
print("Sudut dalam radian (fraksi pi):", pi_fraction_string, "rad")
```





### 2: Kalkulator Torsi
**Solusi**

```python
# Problem 1: Torque Calculator with Angle
import math

# Given values
F = 15      # Force in Newtons
r = 0.5     # Lever arm in meters
theta_deg = 45  # Angle in degrees

# Convert the angle to radians for the sine function
theta_rad = math.radians(theta_deg)

# Calculate torque
torque = r * F * math.sin(theta_rad)

# Print the results
print(f"Force (F): {F} N")
print(f"Lever arm (r): {r} m")
print(f"Angle (θ): {theta_deg} degrees")
print(f"Torque (τ): {torque} N·m")
```


### 3: Kalkulator Gaya Coulomb
**Solusi**

```python
# Problem 3: Coulomb Force Calculator
# Constants and given values
k_e = 8.9875517923e9  # Coulomb's constant in N·m²/C²
q1 = 1.602e-19       # Charge 1 in Coulombs (e.g., proton)
q2 = -1.602e-19      # Charge 2 in Coulombs (e.g., electron)
r = 5.29e-11         # Distance in meters (e.g., Bohr radius)

# Calculate Coulomb force (using absolute value for magnitude)
force = k_e * abs(q1 * q2) / r**2

# Print the results
print(f"Charge 1 (q1): {q1} C")
print(f"Charge 2 (q2): {q2} C")
print(f"Distance (r): {r} m")
print(f"Coulomb Force (F): {force:.20f} N")
```


## Kunci Jawaban ===== TUGAS =================================================
















