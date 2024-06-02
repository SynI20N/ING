import cv2 as cv
import pymurapi as mur
import math
import time

cap = cv.VideoCapture(1)
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
        
    def process(self, error):
        timestamp = int(round(time.time()*1000))
        output = self._kp * error + self._kd / (timestamp - self._timestamp)*(error * self._prev_error)
        self._timestamp = timestamp
        self._prev_error = error
        return output
        
def keep_yaw(yaw_to_set):
    def clamp_to_180(angle):
        if angle > 180.0:
            return angle - 360.0
        if angle < -180.0:
            return angle + 360.0
        return angle
    try:
        error = auv.get_yaw() - yaw_to_set
        error = clamp_to_180(error)
        output = keep_yaw.regulator.process(error)
        output = clamp(output, -100, 100)
        auv.set_motor_power(0, -output)
        auv.set_motor_power(1, output)
    except AttributeError:
        keep_yaw.regulator = PD()
        keep_yaw.regulator.set_p_gain(0.0)
        keep_yaw.regulator.set_d_gain(0.5)
        
def keep_depth(depth_to_set):
    try:
        error = auv.get_depth() - depth_to_set
        output = keep_depth.regulator.process(error)
        output = clamp(output, -100, 100)
        auv.set_motor_power(2, output)
        auv.set_motor_power(3, output)
    except AttributeError:
        keep_depth.regulator = PD()
        keep_depth.regulator.set_p_gain(80)
        keep_depth.regulator.set_d_gain(50)    

def find_yellow_circle(image):
    #image_rgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    rgb_min = (0, 0, 0)
    rgb_max = (10, 10, 10)
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, image_bin = cv.threshold(image, 30, 65500, 0)
    #image_bin = cv.cvtColor(image_bin, cv.COLOR_GRAY2BGR)
    #cv.imwrite("initial.png", image)
    #cv.imwrite("result.png", image_bin)
    #exit(1)
    cnt, _ = cv.findContours(image_bin, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    if cnt:
        for c in cnt:
            area = cv.contourArea(c)
            if abs(area) < 300:
                continue
            hull = cv. convexHull(c)
            approx = cv.approxPolyDP(hull, cv.arcLength(c, True) * 0.02, True)
            
            if len(approx) < 7:
                continue
            print("found circle")
            moments = cv.moments(c)
            try:
                x = int(moments['m10'] / moments["m00"])
                y = int(moments['m01'] / moments["m00"])
            except ZeroDivisionError:
                return False, 0, 0, image_bin
            return True, x, y, image_bin
    return False, 0, 0, image_bin
    
def stab_on_yellow_circle(x, y):
        x_center = x - (image.shape[1]/2)
        y_center = (image.shape[0]/2) - y
        print(x_center)
        try:
            output_forward = stab_on_yellow_circle.regulator_forward.process(y_center)
            output_side = stab_on_yellow_circle.regulator_side.process(x_center)
            output_forward = clamp(output_forward, 50, -50)
            output_side = clamp(output_side, 50, -50)
            auv.set_motor_power(1, output_forward)
            auv.set_motor_power(2, output_forward)
            auv.set_motor_power(4, -output_side)
        except AttributeError:
            
            stab_on_yellow_circle.regulator_forward = PD()
            stab_on_yellow_circle.regulator_forward.set_p_gain(0.3)
            stab_on_yellow_circle.regulator_forward.set_d_gain(0.1)
            
            stab_on_yellow_circle.regulator_side = PD()
            stab_on_yellow_circle.regulator_side.set_p_gain(0.3)
            stab_on_yellow_circle.regulator_side.set_d_gain(0.1)
            #98 156 67
            #104 136 83
while True:
    ok, image = cap.read()
    if not ok:
        print('cam read error')
        break
    found, x, y, img = find_yellow_circle(image)
    time.sleep(0.05)
    if found:
        #img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
        #cv.circle(img, (x, y), 4, (255, 0, 255), 40)
        #cv.imwrite("center.png", img)
        print('x = ', x, "y = ", y)
        #exit(1)
        stab_on_yellow_circle(x, y)
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
