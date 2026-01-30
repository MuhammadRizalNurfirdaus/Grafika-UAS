"""
Modul untuk transformasi rotasi (rotation).

Rotasi memutar objek terhadap titik pusat dengan sudut tertentu.

Rumus rotasi:
    x' = x * cos(θ) - y * sin(θ)
    y' = x * sin(θ) + y * cos(θ)
    
dimana θ adalah sudut rotasi dalam radian.
Sudut positif = rotasi berlawanan arah jarum jam (counter-clockwise).
"""

import matplotlib.pyplot as plt
import numpy as np


def rotate_vertices(vertices, angle_degrees, center=None):
    """
    Menerapkan transformasi rotasi pada vertices.
    
    Parameters:
    -----------
    vertices : list of tuples
        List koordinat vertices [(x1, y1), (x2, y2), ...]
    angle_degrees : float
        Sudut rotasi dalam derajat (positif = counter-clockwise)
    center : tuple, optional
        Titik pusat rotasi. Jika None, menggunakan centroid
        
    Returns:
    --------
    list : List koordinat vertices yang sudah dirotasi
    
    Example:
    --------
    >>> vertices = [(1, 0), (0, 0), (0, 1)]
    >>> rotated = rotate_vertices(vertices, 90)
    >>> # Hasil: rotasi 90 derajat counter-clockwise
    """
    # Konversi ke radian
    angle_rad = np.radians(angle_degrees)
    
    if center is None:
        # Hitung centroid sebagai pusat default
        cx = sum(v[0] for v in vertices) / len(vertices)
        cy = sum(v[1] for v in vertices) / len(vertices)
        center = (cx, cy)
    
    cx, cy = center
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    
    rotated_vertices = []
    
    for x, y in vertices:
        # Translasi ke origin (pusat rotasi)
        x_translated = x - cx
        y_translated = y - cy
        
        # Terapkan rotasi
        x_rotated = x_translated * cos_a - y_translated * sin_a
        y_rotated = x_translated * sin_a + y_translated * cos_a
        
        # Translasi kembali
        x_new = x_rotated + cx
        y_new = y_rotated + cy
        
        rotated_vertices.append((x_new, y_new))
    
    return rotated_vertices


def apply_rotation(ax, shape_data=None):
    """
    Meminta input sudut rotasi dari pengguna dan menerapkan rotasi.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib
    shape_data : dict, optional
        Data bentuk yang akan dirotasi
        
    Returns:
    --------
    dict : Data bentuk yang sudah dirotasi, atau None jika gagal
    """
    if shape_data is None:
        print("Tidak ada bentuk yang dipilih untuk rotasi.")
        return None
    
    try:
        angle = float(input("Masukkan sudut rotasi (dalam derajat, positif = CCW): "))
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")
        return None
    
    vertices = shape_data.get('vertices', [])
    if len(vertices) == 0:
        print("Bentuk tidak memiliki vertices.")
        return None
    
    # Terapkan rotasi
    rotated_vertices = rotate_vertices(vertices, angle)
    
    # Bersihkan axes dan gambar ulang
    for p in ax.patches:
        p.remove()
    for txt in ax.texts:
        txt.remove()
    
    # Gambar bentuk yang sudah dirotasi
    polygon = plt.Polygon(rotated_vertices, closed=True, edgecolor='blue', 
                          facecolor='lightblue', alpha=0.5)
    ax.add_patch(polygon)
    
    # Update shape_data
    new_shape_data = shape_data.copy()
    new_shape_data['vertices'] = rotated_vertices
    
    print(f"Rotasi berhasil diterapkan dengan sudut {angle} derajat.")
    
    return new_shape_data


def get_rotation_matrix(angle_degrees):
    """
    Menghasilkan matriks transformasi rotasi 2D.
    
    Parameters:
    -----------
    angle_degrees : float
        Sudut rotasi dalam derajat
        
    Returns:
    --------
    numpy.ndarray : Matriks rotasi 2x2
    
    Note:
    -----
    Matriks rotasi:
    | cos(θ)  -sin(θ) |
    | sin(θ)   cos(θ) |
    """
    angle_rad = np.radians(angle_degrees)
    cos_a = np.cos(angle_rad)
    sin_a = np.sin(angle_rad)
    
    return np.array([
        [cos_a, -sin_a],
        [sin_a, cos_a]
    ])
