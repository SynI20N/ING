import cv2 as cv
import pymurapi as mur



auv = mur.mur_init()

def binary_image():
    image = auv.get_image_bottom()
    
    imageHSV = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    
    low_hsv_blue = (105, 50, 50)
    max_hsv_blue = (135, 255, 255)
    
    blue_hsv_mask = cv.inRange(imageHSV, low_hsv_blue, max_hsv_blue)
    
    low_hsv_yellow = (20, 50, 50)
    max_hsv_yellow = (35, 255, 255)
    
    yellow_hsv_mask = cv.inRange(imageHSV, low_hsv_yellow, max_hsv_yellow)
    
    low_hsv_green = (45, 50, 50)
    max_hsv_green = (75, 255, 255)
    
    green_hsv_mask = cv.inRange(imageHSV, low_hsv_green, max_hsv_green)
    
    result_mask = blue_hsv_mask + yellow_hsv_mask + green_hsv_mask
    
    cv.imshow("ALL", result_mask)
    
    cv.waitKey(5)

while True:
    binary_image()
