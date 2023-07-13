import cv2
import numpy as np 

image = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 2\\images\\lena.jpg",1)
cv2.imshow('image',image)
cv2.waitKey(5000) # after 5 seconds the window in which the image is being displayed gets closed automatically
cv2.destroyAllWindows()