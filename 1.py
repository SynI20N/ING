import pymurapi as mur
import time
import matplotlib.pyplot as plt
auv = mur.mur_init()
prev_time = 0
prev_error = 0.0
times = []
values = []
points = []
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
    diff_value = 5 / (current_time - prev_time) * (error - prev_error)
    power_2 = clamp(power_value + diff_value, 100, -100)
    power_3 = clamp(power_value + diff_value, 100, -100)
    auv.set_motor_power(2, power_2)
    auv.set_motor_power(3, power_3)
    prev_time = current_time
    prev_error = error
    points.append((time.time(), error + value))
    times.append(time.time())
    values.append(error)
    plt.plot(times,values)
    #plt.show()
    plt.pause(0.5)
while True:
    keep_depth(2)
    time.sleep(0.03)
    
