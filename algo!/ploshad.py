def ploshad(x,y):
    i = 0
    j = 0
    while (x>y):
        x-=y
        i+=1
        print("Our", i ,"x = ", x)
    while (y>x):
        y-=x
        j+=1
        print("Our", j ,"y = ", y)
    if (x != y):
        ploshad(x,y)
        print("хуй")
    else:
        print("хуй хуй")
        return print("this is our x =",x,"and y =",y)

ploshad(1680,640)
