import cv2
import numpy as np

img = np.zeros((500,500,3), np.uint8)

squ = np.full((50,50,3),127,np.uint8)

rep = np.zeros((50,1,3),np.uint8)

# img[450:,i:i+50,::] = squ

for i in range(1,450):
    
    img[450:,i-1:i,::] = rep
    img[450:,i:i+50,::] = squ
    cv2.imshow('image',img)

    k = cv2.waitKey(50) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()