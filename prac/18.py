p = [75,(95,64),(17,47,82),(18,35,87,10),(20,04,82,47,65),(19,01,23,75,03,34),(88,02,77,73,07,63,67),(99,65,04,28,06,16,70,92),(41,41,26,56,83,40,80,70,33)]
sum = p[0]
max = 0
index = 0
for i in range(1,4):
    if p[i][index] > p[i][index+1]:
        max = p[i][index]
    else:
        max = p[i][index+1]
        index+=1

    print(max)
    sum+=max

print(sum)
