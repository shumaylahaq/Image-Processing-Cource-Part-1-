import cv2
import numpy as np

# Load two images
img1 = cv2.imread('C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 9\\images\\home.jpg')
img2 = cv2.imread('C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 9\\images\\opencv.png')

rows,cols,channels = img2.shape
# I want to put logo on top-left corner, So I create a ROI
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)


# Now black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
# img1_bg = cv2.bitwise_and(roi,mask_inv,mask = mask_inv)


# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)


# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
# dst = cv2.bitwise_or(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

# cv2.imshow('res',mask_inv)
# cv2.imshow('res1',img1_bg)
# cv2.imshow('res2',img2_fg)
# cv2.imshow('res3',dst)
cv2.imshow('res4',img1)


cv2.waitKey(0)
cv2.destroyAllWindows()