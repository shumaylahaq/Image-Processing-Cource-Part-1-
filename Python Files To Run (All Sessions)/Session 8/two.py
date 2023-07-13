import cv2
img = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\lena.jpg")
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA) # convert 3 channels to 4 channels images
print(img2.shape)


