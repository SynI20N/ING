import pymurapi as mur
import time
import queue
import threading as th

auv = mur.mur_init()
prev_time = 0
prev_error = 0.0

def clamp(v, max_v, min_v):
    if v > max_v:
        return max_v
    if v < min_v:
        return min_v
    return v
    
def keep_depth(value):
    global prev_time
    global prev_error
    current_time = int(round(time.time() * 1000))
    error = auv.get_depth() - value
    print(error)
    power_2 = 0
    power_3 = 0
    power_value = error * 500
    diff_value = 50 / (current_time - prev_time) * (error - prev_error)
    power_2 = clamp(power_value + diff_value, 100, -100)
    power_3 = clamp(power_value + diff_value, 100, -100)
    auv.set_motor_power(0, -power_2)
    auv.set_motor_power(3, -power_3)
    prev_time = current_time
    prev_error = error
    
def keep_depth_t (timeD, depth, pwr):
    prev_time_0 = time.time()
    while abs(time.time() - prev_time_0) < timeD:
        auv.set_motor_power(1, -pwr)
        auv.set_motor_power(2, -pwr)
        keep_depth(depth)
        time.sleep(0.01)
        

commands = queue.Queue()
commands.put(lambda: keep_depth_t(10, 0.25, 40))
commands.put(lambda: keep_depth_t(10, 0.15, -40))
commands.put(lambda: keep_depth_t(10, 0.20, 0))
times = [3, 4, 2]

n = 3
for i in range(n):
    cmd = commands.get(timeout=times[i])
    cmd()
    
    
