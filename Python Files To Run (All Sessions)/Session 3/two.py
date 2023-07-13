import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 3\\videos\\test.avi")

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        cv2.imshow('frame',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()