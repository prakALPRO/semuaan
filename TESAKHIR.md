# Tes akhir ALPRO

ada 2 nomor:

- Transpose Matriks (30)
- Tic Tac Toe (70) atau RPG (70)



## (30) Transpose Matriks



buatkan 2 hal:
a) pseudocode / flowchart
b) melengkapi kodingan python

### PSEUDOCODE:
misal:
jika matrix_M = [[10, 20, 30], [40, 50, 60]]
kolom_matrix_M = 3
baris_matrix_M = 2

maka di-return:
Transpose_M = [[10, 40], [20, 50], [30, 60]]
kolom_Transpose_M = 2
baris_Transpose_M = 3

### KODING PYTHON:
**kode program yg belum lengkap:**

```python
matrix_M = [
    [10, 20, 30],
    [40, 50, 60]
]

kolom_matrix_M = 3
baris_matrix_M = 2


```

**Output yang Diharapkan:**

```python
# Matriks Hasil jadi berdimensi 3 baris x 2 kolom
[
    [10, 40],
    [20, 50],
    [30, 60]
]
```

Matriks M berukuran **3 baris x 2 kolom** 
$$M = \begin{pmatrix}
\mathbf{10} & \mathbf{20} & \mathbf{30} \\
\mathbf{40} & \mathbf{50} & \mathbf{60}
\end{pmatrix}$$


Matriks hasil *transpose* berukuran **3 baris x 2 kolom** . Angka dari Baris $M$ menjadi Kolom $M^T$.

$$M^T = \begin{pmatrix}
\mathbf{10} & \mathbf{40} \\
\mathbf{20} & \mathbf{50} \\
\mathbf{30} & \mathbf{60}
\end{pmatrix}$$

---

### CLUE

Perhatikan bagaimana elemen berpindah sesuai aturan $M[i][j] \to M^T[j][i]$:

| Posisi di $M$ | Nilai | Posisi di $M^T$ |
| :--- | :--- | :--- |
| **$M[0][0]$** | 10 | **$M^T[0][0]$** |
| **$M[0][1]$** | 20 | **$M^T[1][0]$** |
| **$M[0][2]$** | 30 | **$M^T[2][0]$** |
| **$M[1][0]$** | 40 | **$M^T[0][1]$** |
| **$M[1][1]$** | 50 | **$M^T[1][1]$** |
| **$M[1][2]$** | 60 | **$M^T[2][1]$** |


## (70)TICTACTOE

diberikan kode program yang belum modular pada file `tictactoe.py`. rapihkanlah kodenya menggunakan function/procedure sebanyak 5 buah, agar kode di `def utama` lebih mudah dibaca oleh orang lain.


## 📊 Tabel Fungsi Modular: Function vs. Procedure

| Tingkat Kesulitan | Fungsi (Python `def`) | Klasifikasi Konsep | Tugas Utama | Output/Return Eksplisit |
| :--- | :--- | :--- | :--- | :--- |
| **Easy** | `bersihkan_layar()` | **Procedure Murni** | Membersihkan layar konsol. | Tidak ada (mengembalikan `None`). |
| **Easy** | `tampilkan_papan(papan)` | **Procedure Murni** | Mencetak visual papan $3 \times 3$. | Tidak ada (mengembalikan `None`). |
| **Easy** | `inisialisasi_papan()` | **Function Murni** | Membuat *list* papan awal (1-9). | `list` papan baru. |
| **Easy** | `ganti_pemain(pemain_saat_ini)` | **Function Murni** | Menukar pemain ('P1' $\leftrightarrow$ 'P2'). | `string` pemain berikutnya. |
| **Medium** | `validasi_gerakan(papan, gerakan)` | **Function Murni** | Memeriksa apakah gerakan valid (**Proses Murni**). | `True` atau `False`. |
| **Medium** | `lakukan_gerakan(papan, gerakan, simbol)` | **Function Murni** | Menempatkan simbol ke papan. | `list` papan yang dimodifikasi. |
| **Hard** | `dapatkan_gerakan_valid(papan, simbol)` | **Function/Procedure Campuran** | Menangani `input()` (**Aksi**) dan memanggil validasi (**Proses**). | `int` posisi gerakan yang valid (1-9). |
| **Hard** | `cek_menang(papan, simbol)` | **Function Murni** | Memeriksa 8 kombinasi kemenangan. | `True` atau `False`. |



### Catatan Tambahan:

* **Function Murni:** Semua fungsi yang berorientasi pada pengecekan data atau perhitungan (`cek_menang`, `validasi_gerakan`) harus selalu menggunakan `return` secara eksplisit.
* **Procedure Murni:** Fungsi yang berurusan dengan Interaksi Pengguna atau Sistem (`bersihkan_layar`, `tampilkan_papan`) tidak perlu menggunakan `return` (atau hanya `return None`).
* **Fungsi Campuran (`dapatkan_gerakan_valid`):** Fungsi ini berada di tingkat kesulitan **Hard** karena ia melakukan **Aksi** (meminta input/mencetak pesan *error*) sambil juga harus menghasilkan **Nilai** (`return` posisi yang valid).

---

## (70) RPGPLUS

diberikan kode program yang belum modular pada file `Dungeon_Plus_Battle.py`. rapihkanlah kodenya menggunakan function/procedure sebanyak minimal 4 vyag, agar kode di `def main` lebih mudah dibaca oleh orang lain.

### 🟢 Level: Mudah

Fungsi-fungsi ini biasanya pendek, memiliki satu tanggung jawab yang jelas, dan tidak mengelola *state* yang kompleks.

| Nama Fungsi / Prosedur | Argumen yang Dibutuhkan | Nilai Kembali (Return Value) | Deskripsi |
| :--- | :--- | :--- | :--- |
| `clear_screen` | `(Tidak ada)` | `Tidak ada (Prosedur)` | Membersihkan layar terminal (`clear` atau `cls`). |
| `get_player_input` | `(Tidak ada)` | `string` | Menunggu user menekan tombol dan mengembalikan input tersebut (misal: 'w', 'a', 's', 'd', 'x'). |
| `initialize_map` | `map_data` (list of string) | `list` (Grid peta) | Mengonversi data peta statis (`MAP_DATA`) menjadi grid 2D (list of list) yang bisa dimodifikasi. |
| `calculate_new_position` | `player_y` (int)<br>`player_x` (int)<br>`key` (string) | `tuple` (new\_y, new\_x) | Menghitung *potensi* posisi baru berdasarkan posisi lama dan input tombol. Tidak memvalidasi gerakan. |
| `move_player` | `map_grid` (list of list)<br>`old_y` (int)<br>`old_x` (int)<br>`new_y` (int)<br>`new_x` (int) | `Tidak ada (Prosedur)` | Memperbarui `map_grid` dengan menghapus 'P' dari posisi lama dan meletakkannya di posisi baru. |

-----

### 🟡 Level: Sedang

Fungsi-fungsi ini melibatkan perulangan (loop) pada struktur data (seperti grid peta) untuk mencari atau menampilkan sesuatu.

| Nama Fungsi / Prosedur | Argumen yang Dibutuhkan | Nilai Kembali (Return Value) | Deskripsi |
| :--- | :--- | :--- | :--- |
| `find_start_position` | `map_grid` (list of list)<br>`char_to_find` (string) | `tuple` (y, x) atau `None` | Mencari koordinat (y, x) dari karakter pertama yang ditemukan (misal 'P') di dalam grid. |
| `render_game` | `map_grid` (list of list)<br>`player_y` (int)<br>`player_x` (int)<br>`player_hp` (int)<br>`player_hp_max` (int)<br>`view_radius` (int) | `Tidak ada (Prosedur)` | Menggambar seluruh tampilan game, termasuk HUD (HP) dan peta dengan *Field of View* (kabut '?'). |

-----
