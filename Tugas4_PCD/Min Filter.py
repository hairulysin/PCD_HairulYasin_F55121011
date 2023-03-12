# Hairul Yasin
# F55121011

import cv2
import numpy as np

# Load image
img = cv2.imread('lena.jpg')
img = cv2.resize(img, (362, 522))

# Define kernel size
ksize = 3

# Define kernel for min filter
kernel = np.ones((ksize,ksize),np.uint8)

# Apply min filter
filtered_img = cv2.erode(img,kernel)

# Display original and filtered image
cv2.imshow('Original Image', img)
cv2.imshow('Filtered Image', filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()