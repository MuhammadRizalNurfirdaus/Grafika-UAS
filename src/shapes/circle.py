"""
Modul untuk menggambar lingkaran (circle).

Lingkaran didefinisikan oleh titik pusat dan radius.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


def draw_circle(ax):
    """
    Meminta input dari pengguna untuk pusat dan radius lingkaran.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib tempat menggambar
        
    Returns:
    --------
    dict : Dictionary berisi tipe, pusat, dan radius lingkaran
           atau None jika input tidak valid
           
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> shape_data = draw_circle(ax)
    >>> plt.show()
    """
    try:
        center_x = float(input("Masukkan koordinat X pusat lingkaran: "))
        center_y = float(input("Masukkan koordinat Y pusat lingkaran: "))
        radius = float(input("Masukkan radius lingkaran: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

    if radius <= 0:
        print("Radius harus bernilai positif.")
        return None

    # Membuat patch lingkaran
    circle = Circle((center_x, center_y), radius, edgecolor='red', 
                    facecolor='lightyellow', alpha=0.5)

    # Menambahkan patch ke axes
    ax.add_patch(circle)
    
    # Menambahkan label
    ax.text(center_x, center_y, 'Lingkaran', ha='center', va='center', fontsize=9)

    print(f"Lingkaran berhasil digambar dengan pusat ({center_x}, {center_y}) dan radius {radius}.")

    # Menghitung titik-titik pada lingkaran untuk transformasi
    theta = np.linspace(0, 2 * np.pi, 100)
    x_points = center_x + radius * np.cos(theta)
    y_points = center_y + radius * np.sin(theta)
    vertices = list(zip(x_points, y_points))

    return {
        'type': 'circle',
        'center': (center_x, center_y),
        'radius': radius,
        'vertices': vertices  # Untuk keperluan transformasi
    }
