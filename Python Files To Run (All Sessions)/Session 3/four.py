import numpy as np
import cv2

cap = cv2.VideoCapture("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 3\\videos\\test.avi")

w = cap.get(3)
h = cap.get(4)

print(w,'x',h)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 3\\videos\\test_gray1.avi",fourcc, 10.0, (int(w),int(h)))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()