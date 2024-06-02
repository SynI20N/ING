import cv2 as cv
import pymurapi as mur
from datetime import datetime

auv = mur.mur_init()
cap = cv.VideoCapture(1)


def find_yellow_circle(image):
    image_hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    hsv_min = (20, 200, 50)
    hsv_max = (48, 255, 255)
    image_bin = cv.inRange (image_hsv, hsv_min, hsv_max)
    cnt, _ = cv.findContours(image_bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    if cnt:
        for c in cnt:
            area = cv.contourArea(c)
            if abs(area) < 300:
                continue
            hull = cv. convexHull(c)
            approx = cv.approxPolyDP(hull, cv.arcLength(c, True) * 0.02, True)
            
            if len(approx) < 5:
                continue
            moments = cv.moments(c)
            try:
                x = int(moments["m10"] / moments["m00"])
                y = int(moments["m01"] / moments["m00"])
            except ZeroDivisionError:
                return False, 0, 0
            print('x = ', x, "y = ", y)
            return True, x, y
    return False, 0, 0
   

while True:
    ok, img = cap.read()
    if ok:
        cv.waitKey(1)
    else:
        print('cam read error')
        break
    found, x, y = find_yellow_circle(img)
    if found:
        cv.circle(img, (x, y), 4, (255, 0, 255), 4)
        cv.imwrite("cam.png", img)
        print('Found!')
        break
    #cv.imshow("window", image)
    cv.waitKey(5)
 
cap.release()
        
        
        
        
        
        
