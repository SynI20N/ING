import pymurapi as mur
import time
import multiprocessing as mlp
from multiprocessing import Process, Queue
import matplotlib.pyplot as plt
import threading as th

auv = mur.mur_init()
prev_time = 0
prev_error = 0.0
times = []
values = []
flag = False
prevDepth = 0.0
time_step = 0.03
speeds = []
    
start_time = time.time()
def clamp(v, max_v, min_v):
    if v > max_v:
        return max_v
    if v < min_v:
        return min_v
    return v
    
def show_plot(q):
    while True:
        point = q.get()
       # print (point)
        plt.plot(point[0], point[1], 'yo', markersize=1)
        plt.pause(0.05)
    
def keep_depth(value):
    global prev_time
    global prev_error
    global start_time
    
    global flag
    global prevDepth
    if flag == True:
        prevDepth = auv.get_depth()
        flag = not flag
    else:
        result = abs(prevDepth - auv.get_depth())/(time_step)
        speeds.append(result)
        prevDepth = auv.get_depth()
        
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
    times.append(time.time() - start_time)
    values.append(error)
    #print(error)
    
if __name__ == '__main__':
    q = Queue()
    mlp.freeze_support()
    p = Process(target = show_plot, args = (q,))
    p.start()
    while True:
        keep_depth(2)
        time.sleep(0.03)
        q.put((times[len(times)-1], speeds[len(speeds)-1]))
