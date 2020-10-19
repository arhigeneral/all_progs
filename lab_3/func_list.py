import random
import time

def way_time (index):
    name = []
    for i in range(0,index):
        name.append([i,random.randint(1,4)])

    return name
