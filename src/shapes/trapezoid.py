"""
Modul untuk menggambar trapesium (trapezoid).

Trapesium adalah segi empat dengan sepasang sisi sejajar
(sisi atas dan sisi bawah).
"""

import matplotlib.pyplot as plt


def draw_trapezoid(ax):
    """
    Meminta input dari pengguna untuk parameter trapesium dan menggambarkannya.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib tempat menggambar
        
    Returns:
    --------
    dict : Dictionary berisi tipe dan vertices trapesium
           atau None jika input tidak valid
           
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> shape_data = draw_trapezoid(ax)
    >>> plt.show()
    """
    try:
        bottom_width = float(input("Masukkan lebar sisi bawah trapesium: "))
        top_width = float(input("Masukkan lebar sisi atas trapesium: "))
        height = float(input("Masukkan tinggi trapesium: "))
        x_start = float(input("Masukkan koordinat X pojok kiri bawah: "))
        y_start = float(input("Masukkan koordinat Y pojok kiri bawah: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

    # Menghitung offset untuk sisi atas agar simetris
    offset = (bottom_width - top_width) / 2

    # Menghitung vertices trapesium
    vertices = [
        (x_start, y_start),                                    # Kiri bawah
        (x_start + bottom_width, y_start),                     # Kanan bawah
        (x_start + bottom_width - offset, y_start + height),   # Kanan atas
        (x_start + offset, y_start + height)                   # Kiri atas
    ]

    # Membuat polygon patch
    trapezoid = plt.Polygon(vertices, closed=True, edgecolor='orange', 
                            facecolor='moccasin', alpha=0.5)

    # Menambahkan patch ke axes
    ax.add_patch(trapezoid)
    
    # Menambahkan label
    center_x = x_start + bottom_width / 2
    center_y = y_start + height / 2
    ax.text(center_x, center_y, 'Trapesium', ha='center', va='center', fontsize=9)

    print(f"Trapesium berhasil digambar dengan sisi bawah {bottom_width}, sisi atas {top_width}, tinggi {height}.")

    return {
        'type': 'trapezoid',
        'vertices': vertices,
        'bottom_width': bottom_width,
        'top_width': top_width,
        'height': height,
        'start_point': (x_start, y_start)
    }
