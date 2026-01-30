# Dokumentasi Proyek UAS Praktikum Grafika Komputer

Aplikasi Python untuk menggambar bentuk geometris 2D dan menerapkan transformasi 2D menggunakan Matplotlib.

## 📋 Daftar Isi

- [Deskripsi](#deskripsi)
- [Instalasi](#instalasi)
- [Cara Menjalankan](#cara-menjalankan)
- [Struktur Proyek](#struktur-proyek)
- [Fitur](#fitur)
- [Dokumentasi API](#dokumentasi-api)
- [Contoh Penggunaan](#contoh-penggunaan)

## Deskripsi

Proyek ini merupakan implementasi praktikum Grafika Komputer yang mencakup:

1. Inisialisasi lingkungan grafis dengan sistem koordinat Kartesius
2. Menggambar 5 jenis bentuk geometris dasar
3. Menerapkan 3 jenis transformasi 2D

## Instalasi

### Prasyarat

- Python 3.7 atau lebih baru
- pip (Python package manager)

### Instalasi Dependencies

```bash
pip install matplotlib numpy
```

## Cara Menjalankan

```bash
cd /home/asephs/Grafika-UAS/src
python main.py
```

## Struktur Proyek

```
Grafika-UAS/
├── docs/                        # Dokumentasi
│   ├── README.md               # Dokumentasi ini
│   └── Bahan Proyek UAS Praktikum Grafika Komputer.docx
│
└── src/                         # Source code
    ├── main.py                  # Aplikasi interaktif utama
    ├── shapes/                  # Modul bentuk geometris
    │   ├── __init__.py
    │   ├── square.py           # Bujursangkar
    │   ├── triangle.py         # Segitiga
    │   ├── rectangle.py        # Persegi panjang
    │   ├── circle.py           # Lingkaran
    │   └── trapezoid.py        # Trapesium
    ├── transformations/        # Modul transformasi 2D
    │   ├── __init__.py
    │   ├── scaling.py          # Penskalaan
    │   ├── reflection.py       # Pencerminan
    │   └── rotation.py         # Rotasi
    └── utils/                  # Utilitas
        ├── __init__.py
        └── plotting.py         # Setup plotting
```

## Fitur

### 🔷 Bentuk Geometris

| No  | Bentuk          | Deskripsi                      | Input                          |
| --- | --------------- | ------------------------------ | ------------------------------ |
| 1   | Bujursangkar    | Segi empat sama sisi           | Sisi, koordinat pojok          |
| 2   | Segitiga        | Tiga titik                     | 3 koordinat (x, y)             |
| 3   | Persegi Panjang | Segi empat                     | Lebar, tinggi, koordinat pojok |
| 4   | Lingkaran       | Bentuk bulat                   | Pusat (x, y), radius           |
| 5   | Trapesium       | Segi empat dengan sisi sejajar | Lebar atas/bawah, tinggi       |

### 🔄 Transformasi 2D

| No  | Transformasi | Deskripsi       | Rumus                            |
| --- | ------------ | --------------- | -------------------------------- |
| 1   | Penskalaan   | Mengubah ukuran | x' = x × sx, y' = y × sy         |
| 2   | Pencerminan  | Bayangan cermin | Terhadap sumbu X, Y, origin, y=x |
| 3   | Rotasi       | Memutar objek   | x' = x×cos(θ) - y×sin(θ)         |

## Dokumentasi API

### utils.plotting

```python
from utils.plotting import init_cartesian_plot, plot_shape_on_ax

# Inisialisasi plot
fig, ax = init_cartesian_plot(figsize=(8, 8), xlim=(-10, 10), ylim=(-10, 10))

# Gambar bentuk
plot_shape_on_ax(ax, shape_data, clear_previous=True)
```

### shapes

```python
from shapes import draw_square, draw_triangle, draw_rectangle, draw_circle, draw_trapezoid

# Semua fungsi draw_* menerima parameter ax dan mengembalikan dict
shape_data = draw_square(ax)
# Returns: {'type': 'square', 'vertices': [...], 'side': ...}
```

### transformations

```python
from transformations import apply_scaling, apply_reflection, apply_rotation
from transformations.scaling import scale_vertices, get_scaling_matrix
from transformations.reflection import reflect_vertices, get_reflection_matrix
from transformations.rotation import rotate_vertices, get_rotation_matrix

# Terapkan transformasi
new_shape_data = apply_scaling(ax, shape_data)
new_shape_data = apply_reflection(ax, shape_data)
new_shape_data = apply_rotation(ax, shape_data)

# Fungsi tingkat rendah
scaled = scale_vertices(vertices, sx=2, sy=2)
reflected = reflect_vertices(vertices, axis='x')
rotated = rotate_vertices(vertices, angle_degrees=45)

# Matriks transformasi
S = get_scaling_matrix(sx=2, sy=2)
R = get_reflection_matrix(axis='y')
T = get_rotation_matrix(angle_degrees=90)
```

## Contoh Penggunaan

### Menggunakan Modul Secara Terpisah

```python
import matplotlib.pyplot as plt
from utils.plotting import init_cartesian_plot
from shapes.square import draw_square
from transformations.rotation import rotate_vertices

# Inisialisasi
fig, ax = init_cartesian_plot()

# Gambar bujursangkar manual
vertices = [(0, 0), (2, 0), (2, 2), (0, 2)]
square = plt.Polygon(vertices, edgecolor='blue', facecolor='lightblue', alpha=0.5)
ax.add_patch(square)

# Rotasi 45 derajat
rotated = rotate_vertices(vertices, angle_degrees=45)
rotated_square = plt.Polygon(rotated, edgecolor='red', facecolor='lightyellow', alpha=0.5)
ax.add_patch(rotated_square)

plt.show()
```

### Menu Interaktif

```
=== APLIKASI GRAFIKA KOMPUTER 2D ===

--- Menggambar Bentuk ---
1. Gambar Bujursangkar (Square)
2. Gambar Segitiga (Triangle)
3. Gambar Persegi Panjang (Rectangle)
4. Gambar Lingkaran (Circle)
5. Gambar Trapesium (Trapezoid)

--- Transformasi 2D ---
6. Terapkan Penskalaan (Scale)
7. Terapkan Pencerminan (Reflect)
8. Terapkan Rotasi (Rotate)

--- Lainnya ---
9. Hapus Semua Bentuk (Clear All)
10. Keluar (Exit)

Pilih opsi (1-10): _
```

## Teori Dasar

### Sistem Koordinat Kartesius

Sistem koordinat 2D dengan sumbu X (horizontal) dan sumbu Y (vertikal) yang berpotongan di origin (0, 0).

### Matriks Transformasi

**Penskalaan:**

```
| sx  0  |   | x |   | sx*x |
|        | × |   | = |      |
| 0   sy |   | y |   | sy*y |
```

**Rotasi (θ derajat):**

```
| cos(θ)  -sin(θ) |   | x |   | x*cos(θ) - y*sin(θ) |
|                 | × |   | = |                     |
| sin(θ)   cos(θ) |   | y |   | x*sin(θ) + y*cos(θ) |
```

**Pencerminan terhadap sumbu X:**

```
| 1   0 |   | x |   |  x |
|       | × |   | = |    |
| 0  -1 |   | y |   | -y |
```

---

**Author:** Rio Priantama  
**Tanggal:** Januari 2026  
**Mata Kuliah:** Praktikum Grafika Komputer
