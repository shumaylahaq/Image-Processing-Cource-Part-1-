import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,400), font, 1,(255,255,255),2)

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()