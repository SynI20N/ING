import random
import math

def hoare_partition(arr, lo, hi):
    x = arr[random.randint(lo, hi - 1)]
    i = lo - 1
    j = hi + 1
    while True:
        i += 1
        j -= 1
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_select(arr, lo, hi, i):
    if(lo == hi):
        return arr[lo]
    q = hoare_partition(arr, lo, hi)
    k = q - lo + 1
    if(k == i):
        return arr[q]
    elif(i < k):
        return quick_select(arr, lo, q, i)
    else:
        return quick_select(arr, q + 1, hi, i - k)

tests = [[-10, -5, -60, 14, 28, 3, 12, -25],
        [-8, 4, 10, 14, 8, -10, 7, -12, -15],
        [-69, -37, -11, 42, 62, -46, -35, 9, 61, 66],
        [-1000],
        [10, 10, 10, 10, 10, 10, 10]]
for test in tests:
    n = len(test)
    order = math.ceil(n / 2) if n % 2 else n / 2
    result = quick_select(test, 0, len(test) - 1, order)
    print(f"n = {n}, order = {order}, result = {result}")


