import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 3\\videos\\test.avi")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# creating the video capture object
out = cv2.VideoWriter("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 3\\videos\\test_gray1.avi",fourcc, 10.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()