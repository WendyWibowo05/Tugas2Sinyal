# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 18:26:05 2023

@author: Wendy Wibowo
"""
print("Nama: Wendy Anugerah Putra Wibowo")
print("NRP: 5009211115")

import numpy as np
import matplotlib.pyplot as plt

def fft(x):
    N = len(x)
    if N <= 1:
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    faktor_twiddle = [np.exp(-2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, faktor_twiddle)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, faktor_twiddle)]

def ifft(x):
    N = len(x)
    if N <= 1:
        return x
    even = ifft(x[0::2])
    odd = ifft(x[1::2])
    faktor_twiddle = [np.exp(2j * np.pi * k / N) * odd_k for k, odd_k in enumerate(odd)]
    return [even_k + twiddle_k for even_k, twiddle_k in zip(even, faktor_twiddle)] + \
           [even_k - twiddle_k for even_k, twiddle_k in zip(even, faktor_twiddle)]

def fft2d(matrix):
    baris, kolom = len(matrix), len(matrix[0])

    for i in range(baris):
        matrix[i] = fft(matrix[i])

    for j in range(kolom):
        kolom = [matrix[i][j] for i in range(baris)]
        kolom = fft(kolom)
        for i in range(baris):
            matrix[i][j] = kolom[i]

    return matrix

def mfcc(matrix):
    fft_matrix = fft2d(matrix)
    log_spektrogram = np.log(np.abs(fft_matrix) ** 2 + 1e-10)
    cepstrum = ifft2d(log_spektrogram)

    return cepstrum

def ifft2d(matrix):
    baris, kolom = len(matrix), len(matrix[0])

    for i in range(baris):
        matrix[i] = ifft(matrix[i])

    for j in range(kolom):
        kolom = [matrix[i][j] for i in range(baris)]
        kolom = ifft(kolom)
        for i in range(baris):
            matrix[i][j] = kolom[i]

    return matrix

def display_matrix(matrix, title):
    plt.imshow(np.abs(matrix), cmap='viridis')
    plt.colorbar()
    plt.title(title)
    plt.show()

input_matrix = [
    [0, 1, 2, 3],
    [4, 5, 6, 7],
    [8, 9, 10, 11],
    [12, 13, 14, 15]
]

for i in range(len(input_matrix)):
    for j in range(len(input_matrix[0])):
        input_matrix[i][j] += i + j  

hasil_mfcc = mfcc(input_matrix)
display_matrix(input_matrix, 'Matriks Input yang Diubah')
display_matrix(hasil_mfcc, 'Implementasi MFCC')
