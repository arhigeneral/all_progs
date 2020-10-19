import firs_window
import func_list
import perekrestok
import time

main_list = perekrestok.perekrestok()
print(main_list)
for i in range(0,len(main_list)):
    print(main_list[i])
    if i != 0:
        time.sleep(main_list[i][1] - main_list[i-1][1])
    else:
        time.sleep(main_list[i][1])
