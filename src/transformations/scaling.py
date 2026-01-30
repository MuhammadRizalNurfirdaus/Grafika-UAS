"""
Modul untuk transformasi penskalaan (scaling).

Penskalaan mengubah ukuran objek dengan mengalikan koordinat
dengan faktor skala tertentu.

Rumus penskalaan:
    x' = x * sx
    y' = y * sy
    
dimana sx dan sy adalah faktor skala untuk sumbu X dan Y.
"""

import matplotlib.pyplot as plt
import numpy as np


def scale_vertices(vertices, sx, sy, center=None):
    """
    Menerapkan transformasi penskalaan pada vertices.
    
    Parameters:
    -----------
    vertices : list of tuples
        List koordinat vertices [(x1, y1), (x2, y2), ...]
    sx : float
        Faktor skala sumbu X
    sy : float
        Faktor skala sumbu Y
    center : tuple, optional
        Titik pusat penskalaan. Jika None, menggunakan (0, 0)
        
    Returns:
    --------
    list : List koordinat vertices yang sudah diskalakan
    
    Example:
    --------
    >>> vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    >>> scaled = scale_vertices(vertices, 2, 2)
    >>> print(scaled)
    [(0, 0), (2, 0), (2, 2), (0, 2)]
    """
    if center is None:
        # Hitung centroid sebagai pusat default
        cx = sum(v[0] for v in vertices) / len(vertices)
        cy = sum(v[1] for v in vertices) / len(vertices)
        center = (cx, cy)
    
    cx, cy = center
    scaled_vertices = []
    
    for x, y in vertices:
        # Translasi ke origin
        x_translated = x - cx
        y_translated = y - cy
        
        # Terapkan penskalaan
        x_scaled = x_translated * sx
        y_scaled = y_translated * sy
        
        # Translasi kembali
        x_new = x_scaled + cx
        y_new = y_scaled + cy
        
        scaled_vertices.append((x_new, y_new))
    
    return scaled_vertices


def apply_scaling(ax, shape_data=None):
    """
    Meminta input faktor skala dari pengguna dan menerapkan penskalaan.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib
    shape_data : dict, optional
        Data bentuk yang akan diskalakan
        
    Returns:
    --------
    dict : Data bentuk yang sudah diskalakan, atau None jika gagal
    """
    if shape_data is None:
        print("Tidak ada bentuk yang dipilih untuk penskalaan.")
        return None
    
    try:
        sx = float(input("Masukkan faktor skala X: "))
        sy = float(input("Masukkan faktor skala Y: "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None
    
    vertices = shape_data.get('vertices', [])
    if len(vertices) == 0:
        print("Bentuk tidak memiliki vertices.")
        return None
    
    # Terapkan penskalaan
    scaled_vertices = scale_vertices(vertices, sx, sy)
    
    # Bersihkan axes dan gambar ulang
    for p in ax.patches:
        p.remove()
    for txt in ax.texts:
        txt.remove()
    
    # Gambar bentuk yang sudah diskalakan
    polygon = plt.Polygon(scaled_vertices, closed=True, edgecolor='blue', 
                          facecolor='lightblue', alpha=0.5)
    ax.add_patch(polygon)
    
    # Update shape_data
    new_shape_data = shape_data.copy()
    new_shape_data['vertices'] = scaled_vertices
    
    print(f"Penskalaan berhasil diterapkan dengan faktor ({sx}, {sy}).")
    
    return new_shape_data


def get_scaling_matrix(sx, sy):
    """
    Menghasilkan matriks transformasi penskalaan 2D.
    
    Parameters:
    -----------
    sx : float
        Faktor skala sumbu X
    sy : float
        Faktor skala sumbu Y
        
    Returns:
    --------
    numpy.ndarray : Matriks penskalaan 2x2
    
    Note:
    -----
    Matriks penskalaan:
    | sx  0  |
    | 0   sy |
    """
    return np.array([
        [sx, 0],
        [0, sy]
    ])
