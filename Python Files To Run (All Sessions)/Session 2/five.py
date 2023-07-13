
import cv2
import numpy as np 

image = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 2\\images\\lena.jpg",1)
cv2.imshow('image',image)
k = cv2.waitKey(0)
if k == ord('esc'): # the window can now be closed by pressing the escape key
    cv2.destroyAllWindows()