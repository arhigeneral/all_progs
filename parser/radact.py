import pyperclip as pc

def folowers():
    all_info = pc.paste()
    water_marker = all_info[20:21]  #24:25
    marker = 'Фото профиля '
    count_of_folowers = int(all_info[74:78]) + 2 # Для меня 56:58
    folowers_name = []
    folower_name = ''
    print(marker)
    print(water_marker)
    print(count_of_folowers)
    i = 0
    j = 0
    while True:
        if all_info[i:i+13] == marker:
            i += 13
            while all_info[i] != water_marker:
                folower_name += all_info[i]
                i += 1
            j+=1
            folowers_name.append(folower_name)
            folower_name = ''
        i+=1
        if j == count_of_folowers:
            break


    folowers_name.sort()
    return folowers_name

def folowing():
    all_info = pc.paste()
    water_marker = all_info[20:21]
    marker = 'Фото профиля '
    count_of_folowing = int(all_info[92:94]) + 2 #для меня 72:74
    folowing_names = []
    print(count_of_folowing)
    folowing_name = ''
    i = 0
    j = 0
    while True:
        if all_info[i:i+13] == marker:
            i += 13
            while all_info[i] != water_marker:
                folowing_name += all_info[i]
                i += 1
            j+=1
            folowing_names.append(folowing_name)
            folowing_name = ''
        i+=1
        if j == count_of_folowing:
            break

    folowing_names.sort()
    return folowing_names


# all_info = pc.paste()
# water_marker = all_info[24:25]  #24:25
# print(water_marker)
# marker = all_info[0:13]
# print(marker)
# count_of_folowers = int(all_info[55:57]) + 2 # Для меня 56:58
# print(count_of_folowers)
# folowers_name = []
# folower_name = ''
# print(marker)
# i = 0
# j = 0
# while True:
#     if all_info[i:i+13] == marker:
#         i += 13
#         while all_info[i] != water_marker:
#             folower_name += all_info[i]
#             i += 1
#         j+=1
#         folowers_name.append(folower_name)
#         folower_name = ''
#     i+=1
#     if j == count_of_folowers:
#         break
#
# folowers_name.pop(0)
# folowers_name.pop(0)
# folowers_name.sort()
#
# print(folowers_name)
