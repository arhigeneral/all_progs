import pyautogui as pg
import time
import radact

pg.hotkey('winleft')
time.sleep(1)
pg.typewrite('chrome\n',0.5)
time.sleep(1)
pg.typewrite('https://www.instagram.com/arhigeneral/\n',)
time.sleep(4)
pg.click(689,257)
time.sleep(2)

for i in range(0,90):
    pg.click(876,605)
time.sleep(4)
pg.hotkey('ctrl','a')
pg.hotkey('ctrl','c')
time.sleep(1)
folowers_names = radact.folowers()

pg.click(959,288)
pg.click(888,260)

time.sleep(2)
print(folowers_names)
for i in range(0,80):
    pg.click(876,605)
time.sleep(4)
pg.hotkey('ctrl','a')
pg.hotkey('ctrl','c')

time.sleep(1)
folowing_names = radact.folowing()
print(folowing_names)
yebani = []
for i in range(0,len(folowing_names)):
    for j in range(0,len(folowers_names)):
        if folowing_names[i] == folowers_names[j]:
            break
        elif j == len(folowers_names) - 1:
            yebani.append(folowing_names[i])

print('Oт этих ублюдков стоит отписаться! -',yebani)

pg.click(1350,10)
