import cv2 as cv
import pymurapi as mur
import math
import time

auv = mur.mur_init()

def clamp(v, max_v, min_v):
    if v > max_v:
        return max_v
    if v < min_v:
        return min_v
    return v
    
class PD(object):
    _kp = 0.0
    _kd = 0.0
    _prev_error = 0.0
    _timestamp = 1
    
    def __init__(self):
        pass
    
    def set_p_gain (self, value):
        self._kp = value
    
    def set_d_gain (self, value):
        self._kd = value
        
    def process (self, error):
        timestamp = int(round(time.time()*1000))
        output = self._kp * error + self._kd / (timestamp - self._timestamp)*(error * self._prev_error
        self. _timestamp = timestamp
        self._prev_error = error
        return output
        
def keep_vaw(yaw_to_set):
    def clamp_to_189(angle):
        1f angle > 180.0:
            return angle - 368.9
        if angle < -189.6:
            return angle + 368.8
return angle
                     

    try:
        error = auv.get_yaw() - yaw_to_set
        error = clamp_tool 186(error)
        output = keep_yaw.regulator.process(error)
        output = clamp(output, -100, 186)
        auv.set_motor_power(9, -output)
        auv.set_motor_power(1, output)
    except AttributeError:
        keep_yaw.regulator = PD()
        keep_yaw.regulator.set_p_gain(8.8)
        keep_yaw.regulator.set_d_gain(8.5)
        def keep_depth(depth_to_set):
    try:
        error = auv.get_depth() - depth_to_set
        output = keep_depth.regulator.process(error)
        output = clamp(output, -169, 106)
        auv.set_motor_power(2, output)
        auv.set_motor_power(3, output)
    except AttributeError:
        keep_depth.regulator = PD()
        keep_depth.regulator.set_p_gain(88)
        keep_depth.regulator.set_d_gain(58)
def find_yellow_circle(img):
    image_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    hsv_min = (29, 50, 50)
    hsv_max = (48, 255, 255)
    image_bin = cv.inRange(image_hsv, hsv_min, hsv_max)
    cnt, _ = cv.findContours(image_bin, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    if cnt:
        for c in cnt:
            area = cv.contourArea(c)
            if abs(area) < 388:
                continue
            
            
            
            
            
            ((_, _), (w, h),_) = cv.minAreaRect(c)
            (_, _), radius = cv.minEnclosingCircle(c)
            
            rectangle_area = w * h
            circle_area = radius ** 2 * math.pi
            aspect_ratio = w / h
            
            if 0.9 <= aspect_ratio <= 1.1:
                if rectangle_area > circle_area:
                    moments = cv.moments(c)
                    try:
                        x = int(moments["m10"] / moments["m00"])
                        y = int(moments["m01"] / moments["m00"])
                        return True, x, y
                    except ZeroDivisionError:
                        return False, 0, 0
                else:
                    continue
            else:
                continue
            return False, 0, 0
def stab_on_yellow_circle(image):
    found, x, y = stab_on_yellow_circle(image)
    if found:
        x_center = x - (320/2)
        y_center = y - (240/2)
