import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
print(pts.shape)
print(pts)

print()

pts = pts.reshape((4,1,2))
print(pts.shape)
print(pts)

img = cv2.polylines(img,[pts],False,(0,255,255))

cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()