import func_list


left_to_right = func_list.way_time(90)
right_to_left = func_list.way_time(30)
sum = len(left_to_right) + len(right_to_left)
main_list = []

print(left_to_right)
print(right_to_left)

i = 0
left_to_right_time = 0
right_to_left_time = 0
len_right_to_left = len(right_to_left)
len_left_to_right = len(left_to_right)
left_to_right_index = 0
right_to_left_index = 0

while True:


    if (right_to_left_time + right_to_left[right_to_left_index][1]) > (left_to_right_time + left_to_right[left_to_right_index][1]) and len(left_to_right) != 0:
        left_to_right_time += left_to_right[left_to_right_index][1]
        main_list.append((i,left_to_right_time))
        if len(left_to_right) - 1 != left_to_right_index:
            left_to_right_index += 1
        else:
            left_to_right[left_to_right_index][1] = 10000000
        #print("1 if")
    elif (left_to_right_time + left_to_right[left_to_right_index][1]) > (right_to_left_time + right_to_left[right_to_left_index][1]) and len(right_to_left) != 0:
        right_to_left_time += right_to_left[right_to_left_index][1]
        main_list.append((i,right_to_left_time))
        if len(right_to_left) - 1 != right_to_left_index:
            right_to_left_index += 1
        else:
            right_to_left[right_to_left_index][1] = 10000000
        #print('2 if')
    elif len(right_to_left) != 0 and len(left_to_right) != 0:
        # нужно добавить проверку чтобы первым добавлялся наименьший эллемент
        if left_to_right[left_to_right_index][1] == right_to_left[right_to_left_index][1]:
            left_to_right_time += left_to_right[left_to_right_index][1]
            main_list.append((i,left_to_right_time))
            if len(left_to_right) - 1 != left_to_right_index:
                left_to_right_index += 1
            else:
                left_to_right[left_to_right_index][1] = 10000000
            #print('3 if')
            i += 1
            right_to_left_time += right_to_left[right_to_left_index][1]
            main_list.append((i,right_to_left_time))
            if len(right_to_left) - 1 != right_to_left_index:
                right_to_left_index += 1
            else:
                right_to_left[right_to_left_index][1] = 10000000
        elif left_to_right[left_to_right_index][1] > right_to_left[right_to_left_index][1]:
            right_to_left_time += right_to_left[right_to_left_index][1]
            main_list.append((i,right_to_left_time))
            if len(right_to_left) - 1 != right_to_left_index:
                right_to_left_index += 1
            else:
                right_to_left[right_to_left_index][1] = 10000000
            #print('4 if')
        else:
            left_to_right_time += left_to_right[left_to_right_index][1]
            main_list.append((i,left_to_right_time))
            if len(left_to_right) - 1 != left_to_right_index:
                left_to_right_index += 1
            else:
                left_to_right[left_to_right_index][1] = 10000000
            #print('else')
    elif len(right_to_left) != 0:
        right_to_left_time += right_to_left[right_to_left_index][1]
        main_list.append((i,right_to_left_time))
        if len(right_to_left) - 1 != right_to_left_index:
            right_to_left_index += 1
        else:
            right_to_left[right_to_left_index] = 10000000
        #print('5 if')
    elif len(left_to_right)   != 0:
        left_to_right_time += left_to_right[left_to_right_index][1]
        main_list.append((i,left_to_right_time))
        if len(left_to_right) - 1 != left_to_right_index:
            left_to_right_index += 1
        else:
            left_to_right[left_to_right_index][1] = 10000000
        #print('6 if')

    i += 1

    


    if len(main_list) == sum:
        break




print(main_list)
