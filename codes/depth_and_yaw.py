import threading as th

auv = mur.mur_init()
prev_time = 0
prev_error = 0.0
times = []
values = []
def clamp(v, max_v, min_v):
    if v > max_v:
        return max_v
    if v < min_v:
        return min_v
    return v
    
def show_plot():
    while True:
        plt.plot(times,values)
        plt.pause(0.05)
    
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
    times.append(time.time())
    values.append(error)
    
th.Thread(target=show_plot, args=(), daemon=True).start()
while True:
    keep_depth(2)
    time.sleep(0.03)
