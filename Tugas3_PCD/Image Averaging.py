# Nama : Hairul Yasin
# Stambuk : F55121011
import cv2
import numpy as np

# Load the first image
img1 = cv2.imread('IMG3.1.png')

# Load the second image and resize it to match the size of the first image
img2 = cv2.imread('IMG3.2.png')
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Compute the weighted average of the two images
avg_img = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the result
cv2.imshow('Averaged Image', avg_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
