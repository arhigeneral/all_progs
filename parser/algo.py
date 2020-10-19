import pyperclip as pc



all_info = pc.paste()
marker = all_info[0:13]
water_marker = all_info[27:28]
count_of_folowers = 1053
print(water_marker)
print(len(all_info))
folowers_name = []
folower_name = ''
i = 0
j = 0
print(marker)
while True:
    if all_info[i:i+13] == marker:
        i+=13
        while all_info[i] != water_marker:
            folower_name += all_info[i]
            i += 1
        j+=1
        print(j)
        folowers_name.append(folower_name)
        folower_name = ''
    i += 1
    if j == count_of_folowers:
        break

print(len(folowers_name))
