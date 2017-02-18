import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('watch.jpg', cv2.IMREAD_GRAYSCALE)
#IMREAD_COLOR = 1
#IMREAD_GRAYSCALE = 0
#IMREAD_UNCHANGED = -1

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Using matplot lib to display image
# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

# Save the image
cv2.imwrite('watchgray.png', img)

