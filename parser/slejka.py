import pyautogui as pg
import time
import pyperclip as pc

def folowing():
    all_info = pc.paste()
    water_marker = all_info[26:27]
    marker = all_info[0:13]
    count_of_folowing = int(all_info[76:79]) + 2
    print('это вот маркер - {} а это вот подпе - {}'.format(water_marker,count_of_folowing))
    folowing_names = []
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
    folowing_names.pop(0)
    folowing_names.pop(0)
    folowing_names.sort()
    return folowing_names


old_folowing =['1dyomochkin', '4chan_tv', '4chantv2.0', '6ix9ine', '_.surovets._', '__apollinariya___', '__belangel._', '_aliliana_77',
'_arozerova', '_belangel._', '_holynekk', '_krasilnikowa_', '_nails__for__you____', '_real_girl1', '_soevaya_', '_verona_', '_woem_',
 'anastasia_galim_', 'anstyblya', 'anton_lapenko', 'arhigeneral', 'arkh_swan', 'arlovedbyyou', 'arriseup', 'artur_engo', 'ba.bitch_', 'blyaansty',
  'cherkasovpage', 'crybaby_mi', 'crybaby_mil', 'da_nil1', 'daria_andreevna01', 'dautovmarsel23', 'dianochkaraim', 'dream_team_house', 'e_l_i_z_o_v',
  'ekaterina14.07', 'endless_noir', 'erik_djun', 'fanatichnaya', 'fucksusha', 'ge_jizn', 'gense_', 'ges5', 'hermantommeraas', 'holykakun', 'i_angelochek_',
  'icceeeberg', 'iceivan_2002', 'instasamka', 'iskrenochka_jizn', 'juliatsybina_', 'kizla_lis', 'kkkkirilova', 'kosman.v', 'krasnopeta', 'kurortniyroman1_',
  'lena_teplyashina', 'lera_fire_', 'liza_kuminova', 'lizakorchagina', 'lo_1ita', 'makefireup', 'makeup_bogdanova', 'manb1mbo', 'maranuha_nails', 'mari.gum_22',
  'mashazdesss', 'mashkeroy', 'mashukovsky', 'medvyedyeva', 'mentaldora', 'mirna_kaplan', 'missalina.21', 'msilotts', 'mysweet16beat', 'mysweet16live', 'n__gladkih',
  'naarcissism', 'nasteppa', 'natalianikolaeva460', 'nepolna', 'niallhoran', 'obschestvoznaika', 'off_fogel', 'onerov', 'polar_star__', 'rmv.smrt', 'sanyapopov23',
  'sarafan_video', 'senoritasaeva', 'shemetovatatiana_', 'shershavaya21', 'shershulya21', 'silaslov', 'svet1_1', 't_allboom', 'timabelorusskih', 'uduot_tv',
  'velvet.alina', 'veronikazolotova_', 'volodya.xxl', 'vtopaeva1', 'yuganski', 'yulechkasladost', 'zabi_vaka', 'zolotova._', 'zoolmu5ic']

pg.hotkey('winleft')
time.sleep(1)
pg.typewrite('chrome\n',0.5)
time.sleep(1)
pg.typewrite('https://www.instagram.com/fuckingidolll/\n',)
time.sleep(4)
time.sleep(2)

pg.click(959,288)
pg.click(888,260)

time.sleep(2)

for i in range(0,60):
    pg.click(876,605)

pg.hotkey('ctrl','a')
pg.hotkey('ctrl','c')

time.sleep(1)
folowing_names = folowing()

pg.click(1350,10)

# for i in range (0,len(old_folowing)):
#     for j in range (0, len(folowing_names)):
#         if old_folowing[i] == folowing_names[j]:
#             k += 1
#             break
# i = 1
# while  (old_folowing_i != len(old_folowing) - 1) and (folowing_names_i != len(folowing_names) - 1):
#     # первы if не работает так как там больше человек(106) всегда захдит во 2 нужна другая проверка
#     if len(old_folowing) - 1 == old_folowing_i + i:
#         print('bbbbbbbbbbbbbbbbbbbbbbbbbb')
#         old_folowing_i += 1
#         i = 1
#         unfolowing.append(old_folowing[old_folowing_i])
#     if len(folowing_names) - 1 == folowing_names_i + i:
#         print('aaaaaaaaaaaaaaaaaaaaaaaaaa')
#         folowing_names_i +=1
#         i = 1
#         unfolowing.append(folowing_names[folowing_names_i])
#     if old_folowing[old_folowing_i] == folowing_names[folowing_names_i]:
#         old_folowing_i += 1
#         folowing_names_i += 1
#         folowing_left.append(old_folowing[old_folowing_i - 1])
#     if folowing_names[folowing_names_i + i] == old_folowing[old_folowing_i]:
#         folowing_names_i += i
#         old_folowing_i += 1
#         i = 1
#         folowing_left.append(old_folowing[old_folowing_i - 1])
#     if old_folowing[old_folowing_i + i] == folowing_names[folowing_names_i]:
#         old_folowing_i += i
#         folowing_names_i += 1
#         i = 1
#         folowing_left.append(old_folowing[old_folowing_i - 2])
#
#     i += 1
#     print(i)
i = 1
old_folowing_i = 0
folowing_names_i = 0
folowing_left = []
unfolowing = []
folowing = []
i = 0

while (len(old_folowing) != 0) or (len(folowing_names) != 0):
    if folowing_names[0] == old_folowing[0]:
        folowing_left.append(folowing_names[0])
        old_folowing.pop(0)
        folowing_names.pop(0)
        i = 0
    elif  (i != 0) and (folowing_names[i] == old_folowing[0]):
        for j in range(0,i+1):
            if j < i:
                folowing.append(folowing_names[0])
            folowing_names.pop(0)
        folowing_left.append(old_folowing[0])
        i = 0
        old_folowing.pop(0)
    elif (old_folowing[i] == folowing_names[0]) and (i != 0):
        for j in range(0,i+1):
            if j < i:
                unfolowing.append(old_folowing[0])
            old_folowing.pop(0)
        folowing_left.append(folowing_names[0])
        i = 0
        folowing_names.pop(0)
    i += 1


print('От них отписалась -',unfolowing)
print('На них подписалась -',folowing)
print('Вот они остались -',folowing_left)
