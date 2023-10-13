# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 00:23:18 2023

@author: Wendy Wibowo
"""

print("Nama: Wendy Anugerah Putra Wibowo")
print("NRP: 5009211115")

import numpy as np
import cmath
import matplotlib.pyplot as plt


Pengali = 1/2
PanjangGrafik = 4 * Pengali
N = 1024  

t = np.linspace(-PanjangGrafik / 2, PanjangGrafik / 2, N, endpoint=False)

def f(t):
    return 1.0 if abs(t) <= Pengali else 0.0

F_manual = [sum(f(t[j]) * cmath.exp(-2j * cmath.pi * k * j / N) for j in range(N)) for k in range(N)]

F_numpy = np.fft.fft([f(tj) for tj in t])

hasil_validasi = np.allclose(F_manual, F_numpy, rtol=1e-10, atol=1e-10)
if hasil_validasi:
    print("Hasil Sudah Sesuai")
else:
    print("Hasil TIDAK Sesuai")

freqs = [k / PanjangGrafik for k in range(N)]

# Plotting
plt.figure(figsize=(10, 6))

plt.subplot(311)
plt.plot(t, [f(tj) for tj in t])
plt.title('Sinyal Asli')
plt.grid()

plt.subplot(312)
plt.plot(freqs, np.abs(F_manual))
plt.title('Spektrum Frekuensi (FFT Manual)')
plt.grid()

plt.subplot(313)
plt.plot(freqs, np.abs(F_numpy))
plt.title('Spektrum Frekuensi (FFT NumPy)')
plt.grid()

plt.tight_layout()
plt.show()
