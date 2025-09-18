import math

## Kunci Jawaban ===== MATERI =================================================

import math
from fractions import Fraction

# 1. Tentukan variabel untuk sudut dalam derajat
sudut_derajat = 45

# 2. Hitung nilai radian dalam bentuk desimal
# Rumus: Derajat * (pi / 180)
sudut_radian_desimal = sudut_derajat * (math.pi / 180)

# 3. Hitung nilai sudut sebagai sesuatu dikali pi
berapa_pi = sudut_derajat/ 180

# 4. Cetak semua hasil sesuai format yang diminta
print("=== No.1 ===")
print(f"Sudut dalam derajat: {sudut_derajat} derajat")

# Gunakan f-string format ".3f" untuk membulatkan hasil menjadi 3 angka di belakang koma
print(f"Sudut dalam radian: {sudut_radian_desimal:.3f} rad")

# Cetak objek fraksi yang sudah disederhanakan
print(f"Sudut dalam radian (fraksi pi): {berapa_pi} pi rad")


# Problem 2: Torque Calculator with Angle


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

# Problem 3: Coulomb Force Calculator
# Constants and given values
k_e = 8.9875517923e9  # Coulomb's constant in N·m²/C²
q1 = 1.602e-19       # Charge 1 in Coulombs (e.g., proton)
q2 = -1.602e-19      # Charge 2 in Coulombs (e.g., electron)
r = 5.29e-11         # Distance in meters (e.g., Bohr radius)

# Calculate Coulomb force (using absolute value for magnitude)
force = k_e * abs(q1 * q2) / r**2

# Print the results

rumus = """

==============================
Bentuk Umum Persamaan Gaya Coulomb:
==============================
      │q₁⋅q₂│
F = kₑ⋅───────
         r²


"""
print(f"Charge 1 (q1): {q1} C")
print(f"Charge 2 (q2): {q2} C")
print(f"Distance (r): {r} m")
print(f"Coulomb Force (F): {force:.20f} N")


## Kunci Jawaban ===== TUGAS =================================================
















