import pymurapi as mur
import time
import matplotlib.pyplot as plt
import threading as th

auv = mur.mur_init()
prev_time = 0
prev_time_while = 0
prev_depth = 0.0
prev_error = 0.0
times = []
velocities = []
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
    power_value = error * 70
    diff_value = 2 / (current_time - prev_time) * (error - prev_error)
    power_2 = clamp(power_value + diff_value, 100, -100)
    power_3 = clamp(power_value + diff_value, 100, -100)
    auv.set_motor_power(2, power_2)
    auv.set_motor_power(3, power_3)
    prev_time = current_time
    prev_error = error
   
    
start = time.time()
current = start
while current - start < 3:
    current = time.time()
    print(current - start)
    keep_depth(2)
    time.sleep(0.03)
start = time.time()
current = start
velocity = 0
while current - start < 5 or abs(auv.get_depth() - 1) > 0.01 or velocity > 1:
    current_time = int(round(time.time() * 1000))
    current_depth = auv.get_depth()
    current = time.time()
    print(str(current - start) + " " + str(velocity))
    velocity = (current_time - prev_time_while) * (current_depth - prev_depth)
    prev_time_while = current_time
    prev_depth = current_depth
    keep_depth(1)
    time.sleep(0.03)
    times.append(time.time())
    velocities.append(velocity)
    plt.plot(times, velocities)
    plt.ylim(-200, 200)
    plt.pause(0.5)
