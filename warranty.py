import numpy as np
a = [28435,43339,31211,10045,15932]
n = len(a)
def get_EV(a,n):
    prob = 1 / n
    sum = 0
    for i in range(0,n):
        sum += (a[i] * prob)
        return float(sum)
get_EV(a,n)
