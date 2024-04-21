import cv2 as cv


image = cv.imread("C:/murIDE/codes/bottom_1.png")
    
imageHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)

low_hsv_blue = (105, 50, 50)
max_hsv_blue = (155, 255, 255)

blue_hsv_mask = cv.inRange(imageHSV, low_hsv_blue, max_hsv_blue)

cnt, _ = cv.findContours(blue_hsv_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

if cnt:
    for c in cnt:
        area = cv.contourArea(c)
        if abs(area) < 300:
            continue
        hull = cv.convexHull(c)
        approx = cv.approxPolyDP(hull, cv.arcLength(c, True) * 0.02, True)
        if len(approx) == 4:
            cv.drawContours(image, [c], 0, (9, 255,0), 3)
            ((x, y), (w, h), angle) = cv.minAreaRect(approx)
            aspect_ratio = w / float(h)
            if  0.9 <= aspect_ratio <= 1.1:
                cv.drawContours(image, [c], 0, (255, 0, 255), 3)
            else:
                cv.drawContours(image, [c], 0, (0, 255, 255), 3)
                                
            
        if len(approx) > 5:
            cv.drawContours(image, [c], 0, (255, 0, 0), 3)

#moments = cv.moments(cnt[0])

#x = moments['m10'] / moments["m00"]
#y = moments['m01'] / moments["m00"]

#cv.circle(image, (int(x), int(y)), 4, (0, 0, 255), 3)

cv.imshow("Cnt", image)

cv.waitKey()
    
    
