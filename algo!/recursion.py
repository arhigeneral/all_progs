import time

def countdown(i):
    print (i)
    if i <= 0:
        return
    else:
        countdown(i-1)
countdown(3)

def infinity():
    print("Ты здесь навсегда парень")
    time.sleep(0.01)
    infinity()

infinity()
