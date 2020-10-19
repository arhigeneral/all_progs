import random

print('Напишите количество циферек которое вы хотите угадывать!)')
main_numbers_int = int(input())
our_max_number = 0
our_min_number = 10**(main_numbers_int - 1)
for i in range(0,main_numbers_int):
    our_max_number += 9 * 10**i
main = str(random.randint(our_min_number,our_max_number))
len_main = len(main)


while True:

    main_points = [0,0,0,0,0,0,0,0,0,0]
    my_number_points = [0,0,0,0,0,0,0,0,0,0]
    position = 0
    numbers = 0

    print('Введи {} циферок!'.format(len_main))
    my_number = str(input())
    if my_number == 'dec':
        print(main)
    else:
        len_my_number = len(my_number)

        if len_my_number < len_main:

            my_number = my_number.rjust(len_main)
            my_number = my_number.replace(' ','0')
            len_my_number_zero = len(my_number)

            for i in range(0,len_my_number):
                if i == len_main:
                    break
                if my_number[len_my_number_zero - i - 1] == main[len_main - i - 1]:
                    position += 1
        else:
            for i in range(0,len_my_number):
                if i == len_main:
                    break
                if my_number[len_my_number - i - 1] == main[len_main - i - 1]:

                    position += 1

        for i in range (0,len_main):
            main_int = int(main[len_main - i - 1])
            main_points[main_int] += 1
            if i < len_my_number:
                my_number_int = int(my_number[len_my_number - i - 1])
                my_number_points[my_number_int] += 1

        for i in range(0,len(main_points)):
            if my_number_points[i] > main_points[i]:
                numbers += main_points[i]
            else:
                numbers += my_number_points[i]

        if my_number == main and numbers == len_main and position == len_main:
            print('Ура ты угадал число!')
            break
        else:
            print('Правильных позиций = {} правильных циферок =  {})))))'.format(position,numbers))
