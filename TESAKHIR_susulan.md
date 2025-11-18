# Tes akhir ALPRO

ada 2 nomor:

- Pengisi karnaugh map (30)
- Connect four (70) atau RPG (70)



## (30) Pengisi karnaugh map



buatkan 2 hal:
a) pseudocode / flowchart
b) melengkapi kodingan python


## 🗺️ Visualisasi Pemetaan K-Map 4x4

### 1.  Matriks Input (List 1D)

Bayangkan *Truth Table* sebagai sebuah pita data linear yang berurutan.

| Indeks (Minterm $m_i$) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Nilai F** | $F_0$ | $F_1$ | $F_2$ | $F_3$ | $F_4$ | $F_5$ | $F_6$ | $F_7$ | $F_8$ | $F_9$ | $F_{10}$ | $F_{11}$ | $F_{12}$ | $F_{13}$ | $F_{14}$ | $F_{15}$ |


### 2. Matriks K-Map (Grid 2D)

K-Map tidak diisi secara berurutan. Kunci dari pemrogramannya adalah menggunakan sebuah **Tabel Pemetaan Indeks** untuk menentukan *dari mana* data harus diambil untuk setiap sel

| Posisi [r][c] | Kolom 00 | Kolom 01 | Kolom 11 | Kolom 10 |
| :---: | :---: | :---: | :---: | :---: |
| **Baris 00** | $F_0$ | $F_4$ | $F_{12}$ | $F_8$ |
| **Baris 01** | $F_1$ | $F_5$ | $F_{13}$ | $F_9$ |
| **Baris 11** | $F_3$ | $F_7$ | $F_{15}$ | $F_{11}$ |
| **Baris 10** | $F_2$ | $F_6$ | $F_{14}$ | $F_{10}$ |

### 3. Pemetaan Indeks (Langkah Program)

Loop program bisa melakukan iterasi dari $r=0, c=0$ hingga $r=3, c=3$. Untuk setiap iterasi $(r, c)$, program mengambil nomor minterm dari tabel pemetaan untuk mengambil nilai dari list 1D.

1.  ($F_0, F_4, F_{12}, F_8$) kini menjadi **Isi Baris 00** yang baru.
2.  ($F_0, F_1, F_3, F_2$) kini tersebar di **Kolom 00, 01, 11, 10** pada baris pertama.

### KODING PYTHON:
**kode program yg belum lengkap:**

```python

# Contoh input F(A, B, C, D) = Σm(0, 2, 5, 7, 8, 10, 12, 13, 14, 15)
TES_TRUTHTABLE= [
# F0 F1 F2 F3 F4 F5 F6 F7 F8 F9 F10 F11 F12 F13 F14 F15
  1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1
]

# diharapkan outputnya array 2D
output= [[1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 0, 1]]


# dan kalau diuji indeksnya,
TES_DEBUGINDEX = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# diharapkan outputnya array 2D
output= [[0, 1, 3, 2], [4, 5, 7, 6], [12, 13, 15, 14], [8, 9,  11, 10 ]]


```

## (70)CONNECT FOUR

diberikan kode program yang belum modular pada file `connectfour.py`. rapihkanlah kodenya menggunakan function/procedure minimal sebanyak 5 buah, agar kode di `def utama` lebih mudah dibaca oleh orang lain.


##  saran Function vs. Procedure

| Nama Fungsi yang Disarankan | Klasifikasi Konsep | Argumen yang Dibutuhkan | Nilai Kembali (Return Value) | Kegunaan/Detail |
| :--- | :--- | :--- | :--- | :--- |
| `inisialisasi_papan()` | **Function Murni** | `(Tidak ada)` | `list` papan baru (5x5) | Membuat *list of lists* papan awal yang kosong (`'.'`). |
| `ganti_pemain(pemain_saat_ini)` | **Function Murni** | `pemain_saat_ini` (string) | `string` pemain berikutnya | Menukar simbol pemain saat ini (`'X'` ke `'O'` atau sebaliknya). |
| `dapatkan_kolom_valid()` | **Function/Procedure Campuran** | `(Tidak ada)` | `int` kolom pilihan (1-5) | Mengelola `input()` dan validasi bahwa input adalah angka dan berada dalam rentang $1-5$. |
| `lakukan_gerakan(papan, kolom, simbol)` | **Function Murni** | `papan, kolom, simbol` | `list` papan yang dimodifikasi (atau `None` jika kolom penuh) | Menjatuhkan simbol ke posisi baris kosong **terbawah** pada kolom yang dipilih. |
| `cek_menang(papan, simbol)` | **Function Murni** | `papan, simbol` | `True` atau `False` | Memeriksa 4 sejajar (`Horizontal`, `Vertikal`, dan `2 Diagonal`) di papan $5 \times 5$ untuk simbol tertentu. |
| `tampilkan_papan(papan)` | **Procedure Murni** | `papan` (list of lists) | `Tidak ada (None)` | Mencetak representasi visual papan $5 \times 5$ (termasuk nomor kolom) ke konsol. |
| `bersihkan_layar()` | **Procedure Murni** | `(Tidak ada)` | `Tidak ada (None)` | Membersihkan tampilan konsol (`os.system('cls'/'clear')`) untuk tampilan game yang rapi. |


### Catatan Tambahan:

* **Function Murni:** Semua fungsi yang berorientasi pada pengecekan data atau perhitungan (`cek_menang`, `validasi_gerakan`) harus selalu menggunakan `return` secara eksplisit.
* **Procedure Murni:** Fungsi yang berurusan dengan Interaksi Pengguna atau Sistem (`bersihkan_layar`, `tampilkan_papan`) tidak perlu menggunakan `return` (atau hanya `return None`).
* **Fungsi Campuran (`dapatkan_gerakan_valid`):** Fungsi ini berada di tingkat kesulitan **Hard** karena ia melakukan **Aksi** (meminta input/mencetak pesan *error*) sambil juga harus menghasilkan **Nilai** (`return` posisi yang valid).
game` | `map_grid` (list of list)<br>`player_y` (int)<br>`player_x` (int)<br>`player_hp` (int)<br>`player_hp_max` (int)<br>`view_radius` (int) | `Tidak ada (Prosedur)` | Menggambar seluruh tampilan game, termasuk HUD (HP) dan peta dengan *Field of View* (kabut '?'). |

-----
