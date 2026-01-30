"""
Modul untuk menggambar bujursangkar (square).

Bujursangkar adalah segi empat dengan semua sisi sama panjang
dan semua sudut 90 derajat.
"""

import matplotlib.pyplot as plt


def draw_square(ax):
    """
    Meminta input dari pengguna untuk sisi bujursangkar dan menggambarkannya.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib tempat menggambar
        
    Returns:
    --------
    dict : Dictionary berisi tipe dan vertices bujursangkar
           atau None jika input tidak valid
           
    Example:
    --------
    >>> fig, ax = plt.subplots()
    >>> shape_data = draw_square(ax)
    >>> plt.show()
    """
    try:
        side = float(input("Masukkan panjang sisi bujursangkar: "))
        x_start = float(input("Masukkan koordinat X pojok kiri bawah: "))
        y_start = float(input("Masukkan koordinat Y pojok kiri bawah: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None

    # Menghitung vertices bujursangkar
    # (x_start, y_start) adalah pojok kiri bawah
    # (x_start + side, y_start) adalah pojok kanan bawah
    # (x_start + side, y_start + side) adalah pojok kanan atas  
    # (x_start, y_start + side) adalah pojok kiri atas
    vertices = [
        (x_start, y_start),                    # Kiri bawah
        (x_start + side, y_start),             # Kanan bawah
        (x_start + side, y_start + side),      # Kanan atas
        (x_start, y_start + side)              # Kiri atas
    ]

    # Membuat polygon patch
    square = plt.Polygon(vertices, closed=True, edgecolor='blue', 
                         facecolor='lightblue', alpha=0.5)

    # Menambahkan patch ke axes
    ax.add_patch(square)
    
    # Menambahkan label
    center_x = x_start + side / 2
    center_y = y_start + side / 2
    ax.text(center_x, center_y, 'Bujursangkar', ha='center', va='center', fontsize=9)

    print(f"Bujursangkar berhasil digambar dengan sisi {side} pada ({x_start}, {y_start}).")

    return {
        'type': 'square',
        'vertices': vertices,
        'side': side,
        'start_point': (x_start, y_start)
    }
