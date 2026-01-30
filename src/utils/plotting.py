"""
Modul untuk inisialisasi dan utilitas plotting.

Modul ini menyediakan fungsi-fungsi untuk:
- Menginisialisasi lingkungan plotting Matplotlib
- Setup sistem koordinat Kartesius
- Helper untuk menggambar bentuk pada axes
"""

import matplotlib.pyplot as plt
import numpy as np


def init_cartesian_plot(figsize=(8, 8), xlim=(-10, 10), ylim=(-10, 10), title="Cartesian Coordinate System"):
    """
    Inisialisasi lingkungan plotting dengan sistem koordinat Kartesius.
    
    Parameters:
    -----------
    figsize : tuple
        Ukuran figure (width, height) dalam inches
    xlim : tuple
        Batas sumbu X (min, max)
    ylim : tuple  
        Batas sumbu Y (min, max)
    title : str
        Judul plot
        
    Returns:
    --------
    fig : Figure
        Objek figure Matplotlib
    ax : Axes
        Objek axes Matplotlib
        
    Example:
    --------
    >>> fig, ax = init_cartesian_plot()
    >>> plt.show()
    """
    # Membuat figure dan axes
    fig, ax = plt.subplots(figsize=figsize)
    
    # Set label sumbu
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    
    # Set batas sumbu
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    
    # Tambahkan grid
    ax.grid(True)
    
    # Set aspect ratio equal agar bentuk tidak terdistorsi
    ax.set_aspect('equal')
    
    # Set judul
    plt.title(title)
    
    print("Matplotlib plotting environment initialized with Cartesian coordinate system.")
    
    return fig, ax


def plot_shape_on_ax(ax, shape_data, clear_previous=True):
    """
    Menggambar bentuk pada axes berdasarkan data bentuk.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib
    shape_data : dict
        Dictionary berisi informasi bentuk:
        - 'type': tipe bentuk ('square', 'triangle', 'rectangle', 'circle', 'trapezoid')
        - 'vertices': list koordinat vertices (untuk polygon)
        - 'center': koordinat pusat (untuk lingkaran)
        - 'radius': radius (untuk lingkaran)
    clear_previous : bool
        Apakah menghapus bentuk sebelumnya
        
    Returns:
    --------
    patch : Patch
        Objek patch yang ditambahkan
    """
    if clear_previous:
        # Hapus semua patches sebelumnya
        for p in ax.patches:
            p.remove()
        for txt in ax.texts:
            txt.remove()
    
    if shape_data is None:
        return None
        
    shape_type = shape_data.get('type')
    
    if shape_type == 'circle':
        # Untuk lingkaran
        from matplotlib.patches import Circle
        center = shape_data['center']
        radius = shape_data['radius']
        circle = Circle(center, radius, edgecolor='red', facecolor='lightyellow', alpha=0.5)
        ax.add_patch(circle)
        return circle
    else:
        # Untuk polygon (square, triangle, rectangle, trapezoid)
        vertices = shape_data.get('vertices', [])
        if len(vertices) > 0:
            polygon = plt.Polygon(vertices, closed=True, edgecolor='blue', 
                                  facecolor='lightblue', alpha=0.5)
            ax.add_patch(polygon)
            return polygon
    
    return None


def adjust_plot_limits(ax, vertices, padding=2):
    """
    Menyesuaikan batas plot berdasarkan vertices bentuk.
    
    Parameters:
    -----------
    ax : Axes
        Objek axes Matplotlib
    vertices : list
        List koordinat vertices
    padding : float
        Padding tambahan di sekitar bentuk
    """
    if len(vertices) == 0:
        return
        
    x_coords = [v[0] for v in vertices]
    y_coords = [v[1] for v in vertices]
    
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    
    ax.set_xlim(x_min - padding, x_max + padding)
    ax.set_ylim(y_min - padding, y_max + padding)
