import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 2\\images\\lena.jpg",1)
# cv2.imshow('image',img)

img = img[:,:,::-1]

plt.imshow(img)
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()