import numpy as np
import cv2

image = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 2\\images\\lena.jpg",0)
cv2.imshow('image',image)

while True:
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        break
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 2\\images\\lena_copy.jpg",image)
        break
    else:
        pass
cv2.destroyAllWindows()