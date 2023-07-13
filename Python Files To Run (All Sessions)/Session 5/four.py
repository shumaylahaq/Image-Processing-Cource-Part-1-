import cv2
import numpy as np

drawing = 0 # true if mouse is pressed
crop = False 
x1,y1 = -1,-1
cc = []
img_crop = []

img = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 5\\images\\lena.jpg",1)
# img_org = np.copy(img)
img_copy = np.copy(img)

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global x1,y1,drawing,mode,cc,crop
    global img_copy
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = 1
        x1,y1 = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == 1 and drawing!=2:
            img_copy = np.copy(img)

            cv2.rectangle(img_copy,(x1,y1),(x,y),(0,255,0),2)
            

    elif event == cv2.EVENT_LBUTTONUP:
        if drawing == 1:
            drawing = 0
            cv2.rectangle(img_copy,(x1,y1),(x,y),(0,255,0),2)
            cc = [x1,y1,x,y]
            crop = True

cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img_copy)
    k = cv2.waitKey(1)
    if k == ord('m'):
        mode = not mode
    if k == ord('c'):
        if crop == True:
            crop = False
            img_crop = img_copy[cc[1]:cc[3],cc[0]:cc[2],::]
            print(type(img_crop))
            cv2.imshow('preview',img_crop)
    elif k == 27:
        break

cv2.destroyAllWindows()




