# Nama : Hairul Yasin
# Stambuk : F55121011
import cv2 #import library yang dibuthkan
import numpy as np

# membaca gambar
img = cv2.imread('IMG2.jpg')

# menyamakan ukuran dari  gambar
img = cv2.resize(img, (326, 536))

# Define the kernel size for the filter (in this case, 5x5)
kernel_size = (5, 5)

# buat kernel untuk filter
kernel = np.ones(kernel_size, np.float32) / (kernel_size[0] * kernel_size[1])

# Aplikasikan filter ke gambar
filtered_img = cv2.filter2D(img, -1, kernel)

# Display the original and filtered images side by side
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
