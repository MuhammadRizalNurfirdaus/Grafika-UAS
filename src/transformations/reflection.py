"""
Modul untuk transformasi pencerminan (reflection).

Pencerminan menghasilkan bayangan cermin dari objek
terhadap sumbu tertentu.

Jenis pencerminan:
1. Terhadap sumbu X: y' = -y
2. Terhadap sumbu Y: x' = -x
3. Terhadap origin: x' = -x, y' = -y
4. Terhadap garis y = x: x' = y, y' = x
"""

import matplotlib.pyplot as plt
import numpy as np


def reflect_vertices(vertices, axis='x'):
    """
    Menerapkan transformasi pencerminan pada vertices.
    
    Parameters:
    -----------
    vertices : list of tuples
        List koordinat vertices [(x1, y1), (x2, y2), ...]
    axis : str
        Sumbu pencerminan: 'x', 'y', 'origin', atau 'y=x'
        
    Returns:
    --------
    list : List koordinat vertices yang sudah dicerminkan
    
    Example:
    --------
    >>> vertices = [(1, 1), (2, 1), (2, 2), (1, 2)]
    >>> reflected = reflect_vertices(vertices, 'x')
    >>> print(reflected)
    [(1, -1), (2, -1), (2, -2), (1, -2)]
    """
    reflected_vertices = []
    
    for x, y in vertices:
        if axis == 'x':
            # Cermin terhadap sumbu X
            x_new, y_new = x, -y
        elif axis == 'y':
            # Cermin terhadap sumbu Y
            x_new, y_new = -x, y
        elif axis == 'origin':
            # Cermin terhadap origin
            x_new, y_new = -x, -y
        elif axis == 'y=x':
            # Cermin terhadap garis y = x
            x_new, y_new = y, x
        else:
            print(f"Sumbu '{axis}' tidak dikenali. Menggunakan sumbu X.")
            x_new, y_new = x, -y
            
        reflected_vertices.append((x_new, y_new))
    
    return reflected_vertices


def apply_reflection(ax, shape_data=None):
    """
    Meminta input jenis pencerminan dari pengguna dan menerapkannya.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib
    shape_data : dict, optional
        Data bentuk yang akan dicerminkan
        
    Returns:
    --------
    dict : Data bentuk yang sudah dicerminkan, atau None jika gagal
    """
    if shape_data is None:
        print("Tidak ada bentuk yang dipilih untuk pencerminan.")
        return None
    
    print("\nPilih jenis pencerminan:")
    print("1. Terhadap sumbu X")
    print("2. Terhadap sumbu Y")
    print("3. Terhadap origin (0, 0)")
    print("4. Terhadap garis y = x")
    
    try:
        choice = input("Pilihan (1-4): ")
    except ValueError:
        print("Input tidak valid.")
        return None
    
    axis_map = {
        '1': 'x',
        '2': 'y',
        '3': 'origin',
        '4': 'y=x'
    }
    
    axis = axis_map.get(choice, 'x')
    
    vertices = shape_data.get('vertices', [])
    if len(vertices) == 0:
        print("Bentuk tidak memiliki vertices.")
        return None
    
    # Terapkan pencerminan
    reflected_vertices = reflect_vertices(vertices, axis)
    
    # Bersihkan axes dan gambar ulang
    for p in ax.patches:
        p.remove()
    for txt in ax.texts:
        txt.remove()
    
    # Gambar bentuk yang sudah dicerminkan
    polygon = plt.Polygon(reflected_vertices, closed=True, edgecolor='blue', 
                          facecolor='lightblue', alpha=0.5)
    ax.add_patch(polygon)
    
    # Update shape_data
    new_shape_data = shape_data.copy()
    new_shape_data['vertices'] = reflected_vertices
    
    print(f"Pencerminan berhasil diterapkan terhadap sumbu {axis}.")
    
    return new_shape_data


def get_reflection_matrix(axis='x'):
    """
    Menghasilkan matriks transformasi pencerminan 2D.
    
    Parameters:
    -----------
    axis : str
        Sumbu pencerminan: 'x', 'y', 'origin', atau 'y=x'
        
    Returns:
    --------
    numpy.ndarray : Matriks pencerminan 2x2
    
    Note:
    -----
    Matriks pencerminan:
    - Sumbu X: | 1  0  |
               | 0 -1  |
    
    - Sumbu Y: | -1  0 |
               |  0  1 |
    
    - Origin:  | -1  0 |
               |  0 -1 |
    
    - y = x:   |  0  1 |
               |  1  0 |
    """
    if axis == 'x':
        return np.array([[1, 0], [0, -1]])
    elif axis == 'y':
        return np.array([[-1, 0], [0, 1]])
    elif axis == 'origin':
        return np.array([[-1, 0], [0, -1]])
    elif axis == 'y=x':
        return np.array([[0, 1], [1, 0]])
    else:
        return np.array([[1, 0], [0, -1]])  # Default: sumbu X
