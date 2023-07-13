import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

center = int(512/2)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.circle(img,(center,center),250,(0,255,0),3)
cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()