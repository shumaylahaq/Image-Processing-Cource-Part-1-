import cv2
import numpy as np

arr = np.zeros((500,500,3),dtype = 'uint8')

# changing the B channel value of the numpy array to 255
# this causes the image to be blue in color
arr[:,:] = [255,0,0]

cv2.imshow('image',arr)
cv2.waitKey(0)
cv2.destroyAllWindows()