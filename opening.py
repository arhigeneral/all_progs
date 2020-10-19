massiv = [1.05, 1.4, 0.69, 1.41, 0.51, 1.49, 1.38, 2, 0.96, 1.31, 2.07, 1.02, 0.89, 1.51, 0.66, 1.16, 0.64, 1.07, 0.33, 1.59, 1.11, 1.33, 0.96, 1.4, 1.71, 0.75, 0.75, 0.92, 1.03, 0.78]
#massiv = [38, 60, 41, 51, 33, 42, 45, 21, 53, 60, 68, 52, 47, 46, 49, 49, 14, 57, 54, 59, 77, 47, 28, 48, 58, 32, 42, 58, 61, 30, 61, 35, 47, 72, 41, 45, 44, 55, 30, 40, 67, 65, 39, 48, 43, 60, 54, 42, 59, 50]
#print(len(massiv))
massiv.sort()

n = len(massiv)
sum = 0
D = 0
for i in range(0,len(massiv)):
    sum += massiv[i]

x = sum / len(massiv)

sum = 0

for i in range(0,len(massiv)):
    sum += ((massiv[i] - x) * (massiv[i] - x))
D = sum / (len(massiv) - 1)
#длина частичного интервала
h = (massiv[len(massiv) - 1] - massiv[0])/9
print('Длина частичного интервала = ',h)
#находим все интервалы
i = 0
bottom_border = massiv[0]
print('bottom_border = ',bottom_border)

while True:

    if len(massiv) == n + 8:
        break
    if bottom_border + h >= massiv[i + 1]:
        i += 1
    else:
        massiv.insert(i+1,'|')
        i += 1
        bottom_border += h
        print('bottom_border = ',bottom_border)

print('bottom_border = ',bottom_border + h)
#массив частот
frequency_mas = []
j = 0
#количество частот без учета последнего промежутка
nf = 0

for i in range(0,len(massiv)):
    if massiv[i] != '|':
        j += 1
    else:
        frequency_mas.append(j)
        nf += j
        j = 0
#для вычисления середины промежутка
j = (massiv[frequency_mas[0]-1] + massiv[0])/2
middle_mas = [j]

for i in range(0,8):
    middle_mas.append(j + h)
    j += h

print('середина интервала', middle_mas)
# print(nf)
frequency_mas.append(len(massiv) - len(frequency_mas)  - nf)
print('частота интервала', frequency_mas)

#выборочное среднее
x = 0
for i in range(0,len(middle_mas)):
    x += middle_mas[i]*frequency_mas[i]

x = x/n
print('Выборочное среднее = ',x)

#выборочное дисперсионное
D = 0
for i in range(0,len(middle_mas)):
    D += (middle_mas[i]**2)*frequency_mas[i]

D = D/n - x**2
print('Выборочное дисперсионное = ',D)
#массив относительной частоты
relative_frequency_mas = []
j = 0
for i in range (0,len(frequency_mas)):
    relative_frequency_mas.append(frequency_mas[i]/n)
    j += relative_frequency_mas[i]
    #print('вводим по очереди = ',j)

# print(j)
# print(relative_frequency_mas)

#коэффициент ассиметрии
koef_ass = 0
for i in range (0,len(frequency_mas)):
    koef_ass += frequency_mas[i]*((middle_mas[i] - x)**3)

koef_ass = (koef_ass/n)/D**(3/2)

print ('коэффициент ассиметрии = ',koef_ass)

#коэффициент эксцесса
koef_eks = 0
for i in range(0,len(frequency_mas)):
    koef_eks += frequency_mas[i]*((middle_mas[i] - x)**4)

koef_eks = ((koef_eks/n)/D**2) - 3
print ('коэффициент эксцесса = ',koef_eks)
#интерквантельный размах
print("интерквантельный размах = ",1.41-0.75)
print('медиана = ', 1.05)
print('первая мода = ',0.96)
print('вторая мода = ',1.4)
print(massiv)
