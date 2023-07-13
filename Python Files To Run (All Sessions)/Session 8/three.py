import cv2
img1 = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\scene.jpg")
img2 = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\opencv.png")

img1 = cv2.resize(img1,(180,222))

img_np = img1+img2
img_cv = cv2.add(img1,img2)

cv2.imshow("image1",img_np)
cv2.imshow("image2",img_cv)

cv2.waitKey(0)
cv2.destroyAllWindows()