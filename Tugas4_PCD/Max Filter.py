# Hairul Yasin
# F55121011

import cv2
import numpy as np

# Load citra digital
img = cv2.imread('IMG1.jpg')

# Tentukan ukuran kernel
kernel_size = 5

# Lakukan operasi Max Filter
img_max = cv2.dilate(img, np.ones((kernel_size, kernel_size), np.uint8))

# Tampilkan citra digital asli dan hasil operasi Max Filter
cv2.imshow('Citra Digital Asli', img)
cv2.imshow('Hasil Operasi Max Filter', img_max)
cv2.waitKey(0)
cv2.destroyAllWindows()
