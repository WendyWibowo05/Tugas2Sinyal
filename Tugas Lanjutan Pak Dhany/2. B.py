# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:22:31 2023

@author: Wendy Wibowo
"""

print("Nama: Wendy Anugerah Putra Wibowo")
print("NRP: 5009211115")

import cmath
import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    twiddle_factors = [cmath.exp(-2j * cmath.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even_k + twiddle_factors_k for even_k, twiddle_factors_k in zip(even, twiddle_factors)] + \
           [even_k - twiddle_factors_k for even_k, twiddle_factors_k in zip(even, twiddle_factors)]
def fft2d(matriks):
    baris, kolom = len(matriks), len(matriks[0])
    for i in range(baris):
        matriks[i] = fft(matriks[i])
    for j in range(kolom):
        kol = [matriks[i][j] for i in range(baris)]
        kol = fft(kol)
        for i in range(baris):
            matriks[i][j] = kol[i]
    return matriks

def hasil_matrix(matriks, judul):
    for baris in matriks:
        print(baris)
    print(judul + "\n")

matriks_input = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for i in range(len(matriks_input)):
    for j in range(len(matriks_input[0])):
        matriks_input[i][j] += i + j

hasil = fft2d(matriks_input)

np_hasil = np.fft.fft2(matriks_input)

def cetak_matriks(matriks, judul):
    print(judul)
    for baris in matriks:
        print(baris)
    print()

hasil_matrix(matriks_input, 'Matriks Input yang Diubah')
hasil_matrix(hasil, 'Implementasi FFT')
print("Perbandingan Hasil")

for baris1, baris2 in zip(hasil, np_hasil):
    print(np.round(baris1, decimals=2), "   ", np.round(baris2, decimals=2))

def plot_matrix(matrix, title):
    plt.imshow(np.abs(matrix), cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()

plot_matrix(matriks_input, 'Input Matrix')

plot_matrix(hasil, 'FFT Implementation')

plot_matrix(np_hasil, 'FFT with NumPy')