# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:35:10 2023

@author: Wendy Wibowo
"""
# ID
print("Nama: Wendy Anugerah Putra Wibowo")
print("NRP: 5009211115")

def convolution(signal1, signal2):
    # Panjang sinyal konvolusi
    result_length = len(signal1) + len(signal2) - 1
    result = [0] * result_length

    # Loop melalui setiap elemen dari sinyal hasil
    for i in range(result_length):
        # Batas bawah dan atas indeks untuk konvolusi
        lower_bound = max(0, i - len(signal2) + 1)
        upper_bound = min(len(signal1) - 1, i)

        # Hitung nilai konvolusi
        for j in range(lower_bound, upper_bound + 1):
            result[i] += signal1[j] * signal2[i - j]

    return result

# Fungsi untuk memvalidasi hasil menggunakan NumPy
def validate_with_numpy(signal1, signal2):
    import numpy as np
    numpy_result = np.convolve(signal1, signal2, mode='full')
    return numpy_result.tolist()

# Sinyal input
signal1 = [1, 2, 3, 4]
signal2 = [0.5, 1, 0.5]

# Hitung konvolusi menggunakan implementasi tanpa NumPy
result_without_numpy = convolution(signal1, signal2)

# Validasi hasil menggunakan NumPy
numpy_result = validate_with_numpy(signal1, signal2)

# Bandingkan hasil
if result_without_numpy == numpy_result:
    print("Hasil konvolusi sesuai!")
    print("Hasil konvolusi:", result_without_numpy)
else:
    print("Hasil konvolusi tidak sesuai.")
    print("Hasil konvolusi (tanpa NumPy):", result_without_numpy)
    print("Hasil konvolusi (NumPy):", numpy_result)
