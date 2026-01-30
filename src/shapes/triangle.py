"""
Modul untuk menggambar segitiga (triangle).

Segitiga dapat digambar dengan menentukan tiga titik vertices.
"""

import matplotlib.pyplot as plt


def draw_triangle(ax):
    """
    Meminta input dari pengguna untuk tiga titik segitiga dan menggambarkannya.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib tempat menggambar
        
    Returns:
    --------
    dict : Dictionary berisi tipe dan vertices segitiga
           atau None jika input tidak valid
           
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> shape_data = draw_triangle(ax)
    >>> plt.show()
    """
    try:
        print("Masukkan koordinat tiga titik segitiga:")
        x1 = float(input("X1: "))
        y1 = float(input("Y1: "))
        x2 = float(input("X2: "))
        y2 = float(input("Y2: "))
        x3 = float(input("X3: "))
        y3 = float(input("Y3: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

    # Vertices segitiga
    vertices = [
        (x1, y1),  # Titik 1
        (x2, y2),  # Titik 2
        (x3, y3)   # Titik 3
    ]

    # Membuat polygon patch
    triangle = plt.Polygon(vertices, closed=True, edgecolor='green', 
                           facecolor='lightgreen', alpha=0.5)

    # Menambahkan patch ke axes
    ax.add_patch(triangle)
    
    # Menghitung centroid untuk label
    center_x = (x1 + x2 + x3) / 3
    center_y = (y1 + y2 + y3) / 3
    ax.text(center_x, center_y, 'Segitiga', ha='center', va='center', fontsize=9)

    print(f"Segitiga berhasil digambar dengan vertices: ({x1},{y1}), ({x2},{y2}), ({x3},{y3}).")

    return {
        'type': 'triangle',
        'vertices': vertices
    }
