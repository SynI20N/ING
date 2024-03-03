import cv2 as cv


image = cv.imread ("C:/Users/Student/Desktop/image.png")

imageHCV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

low_hsv_blue = (210/2, 50, 50)
max_hsv_blue = (270/2, 255, 255)

low_hsv_cyan = (150/2, 50, 50)
max_hsv_cyan = (210/2, 255, 255)

low_hsv_yel = (30/2, 50, 50)
max_hsv_yel = (90/2, 255, 255)


blue_hsv_mask = cv.inRange(imageHCV, low_hsv_blue, max_hsv_blue)

cyan_hsv_mask = cv.inRange(imageHCV, low_hsv_cyan, max_hsv_cyan)

yel_hsv_mask = cv.inRange(imageHCV, low_hsv_yel, max_hsv_yel)


cv.imshow("blue", blue_hsv_mask)
cv.imshow("syan", cyan_hsv_mask)
cv.imshow("yel", yel_hsv_mask)
cv.waitKey()
