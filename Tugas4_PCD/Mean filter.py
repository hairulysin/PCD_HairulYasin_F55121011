# Hairul Yasin
# F55121011

import cv2
import numpy as np

# Load citra digital
img = cv2.imread('IMG1.jpg')

# Tentukan ukuran kernel
kernel_size = 3

# Lakukan operasi Mean Filter
img_mean = cv2.blur(img, (kernel_size, kernel_size))

# Tampilkan citra digital asli dan hasil operasi Mean Filter
cv2.imshow('Citra Digital Asli', img)
cv2.imshow('Hasil Operasi Mean Filter', img_mean)
cv2.waitKey(0)
cv2.destroyAllWindows()

