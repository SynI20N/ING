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
    power_2 = 0
    power_3 = 0
    power_value = error * 200
    diff_value = 5 / (current_time - prev_time) * (error - prev_error)
    power_2 = clamp(power_value + diff_value, 100, -100)
    power_3 = clamp(power_value + diff_value, 100, -100)
    auv.set_motor_power(0, power_2)
    auv.set_motor_power(3, power_3)
    prev_time = current_time
    prev_error = error
    
def keep_depth_t (timeD, depth):
    prev_time_0 = time.time()
    while abs(time.time() - prev_time_0) < timeD:
        keep_depth(depth)
        print(depth)
        time.sleep(0.03)
        

commands = queue.Queue()
commands.put(lambda: keep_depth_t(5, -0.4))
commands.put(lambda: keep_depth_t(5, -0.2))
commands.put(lambda: keep_depth_t(5, 0))
times = [3, 4, 2]

n = 3
for i in range(n):
    cmd = commands.get(timeout=times[i])
    cmd()
