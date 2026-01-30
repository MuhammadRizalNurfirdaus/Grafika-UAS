"""
Modul untuk menggambar persegi panjang (rectangle).

Persegi panjang adalah segi empat dengan sudut 90 derajat,
dimana panjang dan lebar dapat berbeda.
"""

import matplotlib.pyplot as plt


def draw_rectangle(ax):
    """
    Meminta input dari pengguna untuk panjang dan lebar persegi panjang.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib tempat menggambar
        
    Returns:
    --------
    dict : Dictionary berisi tipe dan vertices persegi panjang
           atau None jika input tidak valid
           
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> shape_data = draw_rectangle(ax)
    >>> plt.show()
    """
    try:
        width = float(input("Masukkan lebar persegi panjang: "))
        height = float(input("Masukkan tinggi persegi panjang: "))
        x_start = float(input("Masukkan koordinat X pojok kiri bawah: "))
        y_start = float(input("Masukkan koordinat Y pojok kiri bawah: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

    # Menghitung vertices persegi panjang
    vertices = [
        (x_start, y_start),                      # Kiri bawah
        (x_start + width, y_start),              # Kanan bawah
        (x_start + width, y_start + height),     # Kanan atas
        (x_start, y_start + height)              # Kiri atas
    ]

    # Membuat polygon patch
    rectangle = plt.Polygon(vertices, closed=True, edgecolor='purple', 
                            facecolor='lavender', alpha=0.5)

    # Menambahkan patch ke axes
    ax.add_patch(rectangle)
    
    # Menambahkan label
    center_x = x_start + width / 2
    center_y = y_start + height / 2
    ax.text(center_x, center_y, 'Persegi Panjang', ha='center', va='center', fontsize=9)

    print(f"Persegi panjang berhasil digambar dengan ukuran {width}x{height} pada ({x_start}, {y_start}).")

    return {
        'type': 'rectangle',
        'vertices': vertices,
        'width': width,
        'height': height,
        'start_point': (x_start, y_start)
    }
