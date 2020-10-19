fibon = []
i = 2
fibon.append(1)
fibon.append(1)

while (fibon[i-1]+fibon[i-2]) < 4000000:
    fibon.append(fibon[i-1] + fibon[i - 2])
    i+=1
j = 0
sum = 0
for j in range (0,i):
    if (fibon[j] % 2 == 0):
        sum+=fibon[j]
print(fibon)
print(sum)
