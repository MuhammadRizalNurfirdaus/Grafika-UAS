#!/usr/bin/env python3
"""
Aplikasi Interaktif Grafika Komputer 2D
========================================

Aplikasi untuk menggambar bentuk geometris 2D dan menerapkan 
transformasi menggunakan Matplotlib.

Fitur:
- Menggambar: Bujursangkar, Segitiga, Persegi Panjang, Lingkaran, Trapesium
- Transformasi: Penskalaan, Pencerminan, Rotasi

Penggunaan:
    python main.py

Author: Rio Priantama
Created: 2026-01-13
"""

import matplotlib.pyplot as plt
import numpy as np
import sys
import os

# Tambahkan path untuk import modul lokal
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import modul shapes
from shapes.square import draw_square
from shapes.triangle import draw_triangle
from shapes.rectangle import draw_rectangle
from shapes.circle import draw_circle
from shapes.trapezoid import draw_trapezoid

# Import modul transformations
from transformations.scaling import apply_scaling, scale_vertices
from transformations.reflection import apply_reflection, reflect_vertices
from transformations.rotation import apply_rotation, rotate_vertices

# Import utilities
from utils.plotting import init_cartesian_plot, plot_shape_on_ax


def show_menu():
    """Menampilkan menu utama aplikasi."""
    print("\n" + "="*50)
    print("   APLIKASI GRAFIKA KOMPUTER 2D")
    print("="*50)
    print("\n--- Menggambar Bentuk ---")
    print("1. Gambar Bujursangkar (Square)")
    print("2. Gambar Segitiga (Triangle)")
    print("3. Gambar Persegi Panjang (Rectangle)")
    print("4. Gambar Lingkaran (Circle)")
    print("5. Gambar Trapesium (Trapezoid)")
    print("\n--- Transformasi 2D ---")
    print("6. Terapkan Penskalaan (Scale)")
    print("7. Terapkan Pencerminan (Reflect)")
    print("8. Terapkan Rotasi (Rotate)")
    print("\n--- Lainnya ---")
    print("9. Hapus Semua Bentuk (Clear All)")
    print("10. Keluar (Exit)")
    print("-"*50)


def clear_all_shapes(ax):
    """Menghapus semua bentuk dari axes."""
    for p in ax.patches:
        p.remove()
    for txt in ax.texts:
        txt.remove()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(True)
    plt.title('Interactive Drawing and Transformation Application')
    print("Semua bentuk telah dihapus.")


def main():
    """Fungsi utama aplikasi."""
    print("\n" + "="*50)
    print("   SELAMAT DATANG DI APLIKASI GRAFIKA KOMPUTER")
    print("="*50)
    print("\nMenginisialisasi lingkungan grafis...")
    
    # Inisialisasi plot
    fig, ax = init_cartesian_plot(
        figsize=(8, 8),
        xlim=(-10, 10),
        ylim=(-10, 10),
        title='Interactive Drawing and Transformation Application'
    )
    
    # Enable interactive mode
    plt.ion()
    plt.show()
    
    # Variabel untuk menyimpan data bentuk terakhir
    current_shape_data = None
    
    while True:
        show_menu()
        choice = input("\nPilih opsi (1-10): ").strip()
        
        shape_data = None
        
        if choice == '1':
            shape_data = draw_square(ax)
            
        elif choice == '2':
            shape_data = draw_triangle(ax)
            
        elif choice == '3':
            shape_data = draw_rectangle(ax)
            
        elif choice == '4':
            shape_data = draw_circle(ax)
            
        elif choice == '5':
            shape_data = draw_trapezoid(ax)
            
        elif choice == '6':
            if current_shape_data is not None:
                new_data = apply_scaling(ax, current_shape_data)
                if new_data is not None:
                    current_shape_data = new_data
            else:
                print("Tidak ada bentuk yang tersedia. Gambar bentuk terlebih dahulu.")
                
        elif choice == '7':
            if current_shape_data is not None:
                new_data = apply_reflection(ax, current_shape_data)
                if new_data is not None:
                    current_shape_data = new_data
            else:
                print("Tidak ada bentuk yang tersedia. Gambar bentuk terlebih dahulu.")
                
        elif choice == '8':
            if current_shape_data is not None:
                new_data = apply_rotation(ax, current_shape_data)
                if new_data is not None:
                    current_shape_data = new_data
            else:
                print("Tidak ada bentuk yang tersedia. Gambar bentuk terlebih dahulu.")
                
        elif choice == '9':
            clear_all_shapes(ax)
            current_shape_data = None
            
        elif choice == '10':
            print("\nKeluar dari aplikasi. Sampai jumpa!")
            break
            
        else:
            print("Pilihan tidak valid. Harap masukkan angka antara 1 dan 10.")
        
        # Update current_shape_data jika menggambar bentuk baru
        if choice in ['1', '2', '3', '4', '5'] and shape_data is not None:
            current_shape_data = shape_data
            plot_shape_on_ax(ax, current_shape_data, clear_previous=True)
        
        # Redraw canvas
        plt.draw()
        plt.pause(0.1)
    
    # Cleanup
    plt.ioff()
    plt.close(fig)
    print("Aplikasi gambar telah ditutup.")


if __name__ == "__main__":
    main()
