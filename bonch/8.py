import random

print('Введите число!')
n = int(input())
n_list = []
sum = 0
max = 0
max_i = 0
proizv = 1

for i in range(0,n):
    print('это наш {} заход'.format(i))
    n_list.append(random.randint(-10,10))
    if n_list[i] > 0:
        sum += n_list[i]
        if n_list[i] > max:
            max = n_list[i]
            proizv = 1
    elif -1 * n_list[i] > max:
        max = -1 * n_list[i]
        proizv = 1
    proizv *= n_list[i]

print(n_list)

proizv /= max

if proizv == 1 or proizv == -1:
    proizv = 0

print('Сумма чисел = {}, Произведение чисел = {}'.format(sum,proizv))
