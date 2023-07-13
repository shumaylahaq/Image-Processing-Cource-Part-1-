import cv2
import numpy as np

img = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\butter.png",-1)  # Reading the image with the fourth alpha channel. 
                                           # This just makes the task easier
# img_copy = np.copy(img)
drawing = False

# Create a black image, a window
# img = np.zeros((250,512,3), np.uint8)
# img_copy = np.copy(img)
cv2.namedWindow('image')


def nothing(x):
    pass

def mouse_call(event,x,y,flag,s):
    global drawing,rad
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
    
    if event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.circle(img,(x,y),rad,(0,0,0,0),-1)
            
    if event == cv2.EVENT_LBUTTONUP:
        drawing = False

cv2.setMouseCallback('image',mouse_call)

# create trackbars for color change
# cv2.createTrackbar('R','image',0,255,nothing)
# cv2.createTrackbar('G','image',0,255,nothing)
# cv2.createTrackbar('B','image',0,255,nothing)
# cv2.createTrackbar('A','image',0,255,nothing)

cv2.createTrackbar('Radius','image',5,50,nothing)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    if k == ord('s'):
        cv2.imwrite("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\butter_copy.png",img)
    # get current positions of four trackbars
#     r = cv2.getTrackbarPos('R','image')
#     g = cv2.getTrackbarPos('G','image')
#     b = cv2.getTrackbarPos('B','image')
#     a = cv2.getTrackbarPos('A','image')

    rad = cv2.getTrackbarPos('Radius','image')

cv2.destroyAllWindows()