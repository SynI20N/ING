import numpy as np
import cv2 as cv
import time

img1 = cv.imread('C:\murIDE\codes\img1.jpg')
img2 = cv.imread('C:\murIDE\codes\img2.jpg')
for i in range (0,100):
    assert img1 is not None, "file could not be read"
    imgf = cv.addWeighted (img1, i/100, img2, 1-i/100,0)
    cv.imshow('imgf', imgf)
    cv.waitKey (100)
    cv.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    #time.sleep(0)
    #cv.destroyAllWindows()
