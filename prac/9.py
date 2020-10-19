

for a in range (0,1000):
    for b in range (0,1000 - a):
        if ((a**2 + b**2 == (1000 - a - b)**2) and (a < b) and (b < (1000 - a - b))):
            c = (1000 - a - b)
            print("это а = ", a)
            print("это b = ", b)
            print("это c = ", c)
            break
