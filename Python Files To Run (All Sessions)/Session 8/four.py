import cv2
img1 = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\scene.jpg")
img2 = cv2.imread("C:\\Users\\Admin\\Downloads\\image processing - 1\\Python Files\\Session 8\\images\\opencv.png")

img1 = cv2.resize(img1,(180,222))

dst = cv2.addWeighted(img1,0.9,img2,0.1,0)

cv2.imshow("image1",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()