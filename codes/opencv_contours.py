import numpy as np
import cv2 as cv

im = cv. imread('C:\\Users\\Student\\PycharmProjects\\pythonProject3\\test.jpg')
assert im is not None, "file could not be read, check with os.path.exists()"
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret,thresh = cv.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
cnt = contours[4]
cnt_max_area = contours[0]
for cnt in contours:
    if cv.contourArea(cnt) > cv.contourArea(cnt_max_area):
        cnt_max_area = cnt
print(len(contours))
cnt_hull = cv.convexHull(cnt_max_area)
#epsilon = 0.01*cv.arcLength(cnt_max_area, True)
#approx = cv.approxPolyDP(cnt_max_area, epsilon, True)
cv.drawContours(im, [cnt_hull], 0, (0,255,0), 3)
cv.imshow("contours", im)
cv.waitKey(0)