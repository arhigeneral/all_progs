
x = 1680
y = 640

def recursion(x,y):
    while x > y:
        x = x - y
    z = x
    x = y
    y = z
    if x / 2 == y:
        return print(x,y)
    else:
        recursion(x,y)

recursion(x,y)
