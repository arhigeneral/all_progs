import random
import func_list
import time

def wat_lists(cars_amount):

    first_way = random.randint(0,cars_amount) # 1 path
    up_to_down = func_list.way_time(first_way)
    if len(up_to_down) != 0:
        up_to_down_time = up_to_down[0][1]
    else:
        up_to_down_time = 0
    # print("Север - Юг")
    # print(str(up_to_down))

    if first_way != cars_amount:
        second_way = random.randint(first_way,cars_amount) - first_way  # 2 path
        memory = second_way + first_way
        down_to_up = func_list.way_time(second_way)
        # print("Юг - Север")
        # print(down_to_up)
        if len(down_to_up) != 0:
            down_to_up_time = down_to_up[0][1]
        else:
            down_to_up_time = 0

        if memory != cars_amount:
            third_way = random.randint(memory,cars_amount) - memory# 3 path
            memory_2 = third_way + memory
            left_to_right = func_list.way_time(third_way)
            if len(left_to_right) != 0:
                left_to_right_time = left_to_right[0][1]
            else:
                left_to_right_time = 0
            # print("Запад - Восток")
            # print(left_to_right)

            if memory_2 != cars_amount:
                fourth_way = cars_amount - memory_2 # 4 path
                memory_3 = memory_2 + fourth_way
                right_to_left = func_list.way_time(fourth_way)
                # print("Восток - Запад")
                # print(right_to_left)
                right_to_left_time = right_to_left[0][1]
            else:
                right_to_left = []
                right_to_left_time = 0
                # print("Восток - Запад")
                # print(right_to_left)

        else:
            left_to_right = []
            left_to_right_time = 0
            right_to_left = []
            right_to_left_time = 0
            # print("Запад - Восток")
            # print(left_to_right)
            # print("Восток - Запад")
            # print(right_to_left)

    else:
        left_to_right = []
        left_to_right_time = 0
        right_to_left = []
        right_to_left_time = 0
        down_to_up = []
        down_to_up_time = 0
        # print("Юг - Север")
        # print(down_to_up)
        # print("Запад - Восток")
        # print(left_to_right)
        # print("Восток - Запад")
        # print(right_to_left)

    return up_to_down, down_to_up, left_to_right, right_to_left


def perekrestok(up_to_down,down_to_up,left_to_right,right_to_left):

    main_list = []
    j = 1
    i = 1

    len_up_to_down = len(up_to_down)
    len_down_to_up = len(down_to_up)
    len_left_to_right = len(left_to_right)
    len_right_to_left = len(right_to_left)
    up_to_down_time = 0
    down_to_up_time = 0
    left_to_right_time = 0
    right_to_left_time = 0
    up_to_down_index = 0
    down_to_up_index = 0
    left_to_right_index = 0
    right_to_left_index = 0

    if len(up_to_down) == 0:
        up_to_down = [[0,10000000]]
    if len(down_to_up) == 0:
        down_to_up = [[0,10000000]]
    if len(left_to_right) == 0:
        left_to_right = [[0,10000000]]
    if len(right_to_left) == 0:
        right_to_left = [[0,10000000]]

    while True:

        while True:


            if (down_to_up_time + down_to_up[down_to_up_index][1]) > (up_to_down_time + up_to_down[up_to_down_index][1]) and len(up_to_down) != 0:
                up_to_down_time += up_to_down[up_to_down_index][1]
                main_list.append((i,up_to_down_time,'Север - Юг'))
                i += 1
                if len(up_to_down) - 1 != up_to_down_index:
                    up_to_down_index += 1
                else:
                    up_to_down[up_to_down_index][1] = 10000000
                #print("1 if")
            elif (up_to_down_time + up_to_down[up_to_down_index][1]) > (down_to_up_time + down_to_up[down_to_up_index][1]) and len(down_to_up) != 0:
                down_to_up_time += down_to_up[down_to_up_index][1]
                main_list.append((i,down_to_up_time,'Юг - Север'))
                i += 1
                if len(down_to_up) - 1 != down_to_up_index:
                    down_to_up_index += 1
                else:
                    down_to_up[down_to_up_index][1] = 10000000
                #print('2 if')
            elif down_to_up[down_to_up_index][1] != 10000000 and up_to_down[up_to_down_index][1] != 10000000:
                # нужно добавить проверку чтобы первым добавлялся наименьший эллемент
                if up_to_down[up_to_down_index][1] == down_to_up[down_to_up_index][1]:
                    up_to_down_time += up_to_down[up_to_down_index][1]
                    main_list.append((i,up_to_down_time,'Север - Юг'))
                    if len(up_to_down) - 1 != up_to_down_index:
                        up_to_down_index += 1
                    else:
                        up_to_down[up_to_down_index][1] = 10000000
                    #print('3 if')
                    i += 1
                    down_to_up_time += down_to_up[down_to_up_index][1]
                    main_list.append((i,down_to_up_time,'Юг - Север'))
                    i += 1
                    if len(down_to_up) - 1 != down_to_up_index:
                        down_to_up_index += 1
                    else:
                        down_to_up[down_to_up_index][1] = 10000000
                elif up_to_down[up_to_down_index][1] > down_to_up[down_to_up_index][1]:
                    down_to_up_time += down_to_up[down_to_up_index][1]
                    main_list.append((i,down_to_up_time,'Юг - Север'))
                    i += 1
                    if len(down_to_up) - 1 != down_to_up_index:
                        down_to_up_index += 1
                    else:
                        down_to_up[down_to_up_index][1] = 10000000
                    #print('4 if')
                else:
                    up_to_down_time += up_to_down[up_to_down_index][1]
                    main_list.append((i,up_to_down_time,'Север - Юг'))
                    i += 1
                    if len(up_to_down) - 1 != up_to_down_index:
                        up_to_down_index += 1
                    else:
                        up_to_down[up_to_down_index][1] = 10000000
                    #print('else')
            elif down_to_up[down_to_up_index][1] != 10000000:
                down_to_up_time += down_to_up[down_to_up_index][1]
                main_list.append((i,down_to_up_time,'Юг - Север'))
                i += 1
                if len(down_to_up) - 1 != down_to_up_index:
                    down_to_up_index += 1
                else:
                    down_to_up[down_to_up_index][1] = 10000000
                #print('5 if')
            elif up_to_down[up_to_down_index][1] != 10000000:
                up_to_down_time += up_to_down[up_to_down_index][1]
                main_list.append((i,up_to_down_time,'Север - Юг'))
                i += 1
                if len(up_to_down) - 1 != up_to_down_index:
                    up_to_down_index += 1
                else:
                    up_to_down[up_to_down_index][1] = 10000000
                #print('6 if')

            # print('zzzzzzzzzzzzzzzzzzzzzzzz')
            # print(len(main_list))
            # if len_down_to_up - 1 == down_to_up_index:
            #     print('syka')
            # if len_up_to_down - 1 == up_to_down_index:
            #     print('aaaaaaaaaaaaaaaaaa blya')


            # if (len_main_list + 1 == len(main_list)):
            #     i += 1
            # print('this is our i' ,i)
            # print('up_to_down_time = ',up_to_down_time)
            # print('down_to_up_time = ',down_to_up_time)
            # print('down_to_up[down_to_up_index][1] = ',down_to_up[down_to_up_index][1])
            # print('up_to_down[up_to_down_index][1] = ',up_to_down[up_to_down_index][1])
            # print('asjfgsadfgsadfgjkasd = ',j)
            if (up_to_down_time // 15 == j and down_to_up_time // 15 == j) or (up_to_down_time // 15 == j and down_to_up[down_to_up_index][1] == 10000000) or (down_to_up_time // 15 == j and up_to_down[up_to_down_index][1] == 10000000) or (up_to_down[up_to_down_index][1] == 10000000 and down_to_up[down_to_up_index][1] == 10000000):
                if up_to_down[up_to_down_index][1] == 10000000 and down_to_up[down_to_up_index][1] != 10000000:
                    left_to_right_time = max(down_to_up_time,15 * j)
                    right_to_left_time = max(down_to_up_time,15 * j)
                elif down_to_up[down_to_up_index][1] == 10000000 and up_to_down[up_to_down_index][1] != 10000000:
                    left_to_right_time = max(up_to_down_time,15 * j)
                    right_to_left_time = max(up_to_down_time,15 * j)
                elif up_to_down[up_to_down_index][1] == 10000000  and down_to_up[down_to_up_index][1] == 10000000:
                    left_to_right_time = 15 * j
                    right_to_left_time = 15 * j
                else:
                    left_to_right_time = max(up_to_down_time,15 * j,down_to_up_time)
                    right_to_left_time = max(up_to_down_time,15 * j,down_to_up_time)
                j += 1
                break

        while True:

            len_main_list = len(main_list)

            if (right_to_left_time + right_to_left[right_to_left_index][1]) > (left_to_right_time + left_to_right[left_to_right_index][1]) and len(left_to_right) != 0:
                left_to_right_time += left_to_right[left_to_right_index][1]
                main_list.append((i,left_to_right_time,'Запад - Восток'))
                i += 1
                if len(left_to_right) - 1 != left_to_right_index:
                    left_to_right_index += 1
                else:
                    left_to_right[left_to_right_index][1] = 10000000
                #print("1 if")
            elif (left_to_right_time + left_to_right[left_to_right_index][1]) > (right_to_left_time + right_to_left[right_to_left_index][1]) and len(right_to_left) != 0:
                right_to_left_time += right_to_left[right_to_left_index][1]
                main_list.append((i,right_to_left_time,'Восток - Запад'))
                i += 1
                if len(right_to_left) - 1 != right_to_left_index:
                    right_to_left_index += 1
                else:
                    right_to_left[right_to_left_index][1] = 10000000
                #print('2 if')
            elif left_to_right[left_to_right_index][1] != 10000000 and right_to_left[right_to_left_index][1] != 10000000:
                # нужно добавить проверку чтобы первым добавлялся наименьший эллемент
                if left_to_right[left_to_right_index][1] == right_to_left[right_to_left_index][1]:
                    left_to_right_time += left_to_right[left_to_right_index][1]
                    main_list.append((i,left_to_right_time,'Запад - Восток'))
                    if len(left_to_right) - 1 != left_to_right_index:
                        left_to_right_index += 1
                    else:
                        left_to_right[left_to_right_index][1] = 10000000
                    #print('3 if')
                    i += 1
                    right_to_left_time += right_to_left[right_to_left_index][1]
                    main_list.append((i,right_to_left_time,'Восток - Запад'))
                    i += 1
                    if len(right_to_left) - 1 != right_to_left_index:
                        right_to_left_index += 1
                    else:
                        right_to_left[right_to_left_index][1] = 10000000
                elif left_to_right[left_to_right_index][1] > right_to_left[right_to_left_index][1]:
                    right_to_left_time += right_to_left[right_to_left_index][1]
                    main_list.append((i,right_to_left_time,'Восток - Запад'))
                    i += 1
                    if len(right_to_left) - 1 != right_to_left_index:
                        right_to_left_index += 1
                    else:
                        right_to_left[right_to_left_index][1] = 10000000
                    #print('4 if')
                else:
                    left_to_right_time += left_to_right[left_to_right_index][1]
                    main_list.append((i,left_to_right_time,'Запад - Восток'))
                    i += 1
                    if len(left_to_right) - 1 != left_to_right_index:
                        left_to_right_index += 1
                    else:
                        left_to_right[left_to_right_index][1] = 10000000
                    #print('else')
            elif right_to_left[right_to_left_index][1] != 10000000:
                right_to_left_time += right_to_left[right_to_left_index][1]
                main_list.append((i,right_to_left_time,'Восток - Запад'))
                i += 1
                if len(right_to_left) - 1 != right_to_left_index:
                    right_to_left_index += 1
                else:
                    right_to_left[right_to_left_index][1] = 10000000
                #print('5 if')
            elif left_to_right[left_to_right_index][1] != 10000000:
                left_to_right_time += left_to_right[left_to_right_index][1]
                main_list.append((i,left_to_right_time,'Запад - Восток'))
                i += 1
                if len(left_to_right) - 1 != left_to_right_index:
                    left_to_right_index += 1
                else:
                    left_to_right[left_to_right_index][1] = 10000000
                #print('6 if')

            #
            # if (len_main_list + 1 == len(main_list)):
            #     i += 1

            if (left_to_right_time // 15 == j and right_to_left_time // 15 == j) or (left_to_right_time // 15 == j and right_to_left[right_to_left_index][1] == 10000000) or (right_to_left_time // 15 == j and left_to_right[left_to_right_index][1] == 10000000) or (right_to_left[right_to_left_index][1] == 10000000 and left_to_right[left_to_right_index][1] == 10000000):
                if left_to_right[left_to_right_index][1] == 10000000 and right_to_left[right_to_left_index][1] != 10000000:
                    up_to_down_time = max(left_to_right_time,15 * j,right_to_left_time)
                    down_to_up_time = max(left_to_right_time,15 * j,right_to_left_time)
                elif right_to_left[right_to_left_index][1] == 10000000 and left_to_right[left_to_right_index][1] != 10000000:
                    up_to_down_time = max(left_to_right_time,15 * j,right_to_left_time)
                    down_to_up_time = max(left_to_right_time,15 * j,right_to_left_time)
                elif left_to_right[left_to_right_index][1] == 10000000  and right_to_left[right_to_left_index][1] == 10000000:
                    up_to_down_time = 15 * j
                    down_to_up_time = 15 * j
                else:
                    up_to_down_time = max(left_to_right_time,15 * j,right_to_left_time)
                    down_to_up_time = max(left_to_right_time,15 * j,right_to_left_time)
                j += 1
                # print('hhhhhhhhhhhhhhhhhhhhhhhhhhhh = ',j)
                # print('leelelelellelelellelelele = ',len(main_list))
                break

        # print('55555555555555555555555555555555555555555555555555555555555555')
        # print(len(main_list))
        # print(len(up_to_down) + len(down_to_up) + len(left_to_right) + len(right_to_left))
        # print('это наши тачки {} raz {} dva {} tri {} chetire'.format(up_to_down, down_to_up, left_to_right, right_to_left))
        # print('Это наши длины один {} два {} три {} четыре {}'.format(len(up_to_down) , len(down_to_up) , len(left_to_right) , len(right_to_left)))
        if len(main_list) == len_down_to_up + len_up_to_down + len_right_to_left + len_left_to_right:
            break

    # print(main_list)
    # print(len(main_list))
    return main_list


# print("Input amount of cars!")
# cars_amount = int(input())
# up_to_down, down_to_up, left_to_right, right_to_left = wat_lists(cars_amount)
# main_list = perekrestok(up_to_down,down_to_up,left_to_right,right_to_left)
# #
# #
# # # for i in range(0,len(main_list)):
# # #     if i != 0:
# # #         time.sleep(main_list[i][1] - main_list[i-1][1])
# # #     else:
# # #         time.sleep(main_list[i][1])
# # #     print(main_list[i])
# #
# #
# for i in range(0,len(main_list)):
#     if main_list[i][1] - main_list[i-1][1] >= 0:
#         print(main_list[i])
#     else:
#         print('dsahfsjdkafdfhjdsssssssssssssssssssssыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыыsss')
#         print(main_list[i])
