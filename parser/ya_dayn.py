folowing_names =['1dyomochkin', '4chan_tv', '4chantv2.0', '6ix9ine', '_.surovets._', '__apollinariya___', '__belangel._', '_aliliana_77',
 '_arozerova', '_belangel._', '_holynekk', '_krasilnikowa_', '_nails__for__you____', '_real_girl1', '_soevaya_', '_verona_',
 '_woem_', 'anastasia_galim_', 'anstyblya', 'anton_lapenko', 'arhigeneral', 'arkh_swan', 'arlovedbyyou', 'arriseup', 'artur_engo', 'ba.bitch_', 'blyaansty',
 'cherkasovpage', 'crybaby_mi', 'crybaby_mil', 'da_nil1', 'dautovmarsel23', 'dianochkaraim', 'dream_team_house', 'e_l_i_z_o_v',
 'ekaterina14.07', 'endless_noir', 'erik_djun', 'fanatichnaya', 'fucksusha', 'ge_jizn', 'gense_', 'ges5', 'hermantommeraas', 'holykakun', 'i_angelochek_',
 'icceeeberg', 'iceivan_2002', 'instasamka', 'iskrenochka_jizn', 'juliatsybina_', 'kizla_lis', 'kkkkirilova', 'kosman.v', 'krasnopeta', 'kurortniyroman1_',
 'lena_teplyashina', 'lera_fire_', 'liza_kuminova', 'lizakorchagina', 'lo_1ita', 'makefireup', 'makeup_bogdanova', 'manb1mbo', 'maranuha_nails', 'mari.gum_22',
 'mashukovsky', 'medvyedyeva', 'mentaldora', 'mirna_kaplan', 'missalina.21', 'msilotts', 'mysweet16beat', 'mysweet16live',
 'naarcissism', 'nasteppa', 'natalianikolaeva460', 'niallhoran', 'obschestvoznaika', 'off_fogel', 'onerov', 'polar_star__', 'rmv.smrt', 'sanyapopov23',
 'sarafan_video', 'senoritasaeva', 'shemetovatatiana_', 'shershavaya21', 'shershulya21', 'silaslov', 'svet1_1', 't_allboom', 'timabelorusskih', 'uduot_tv',
 'velvet.alina', 'veronikazolotova_', 'volodya.xxl', 'vtopaeva1', 'yuganski', 'yulechkasladost', 'zabi_vaka', 'zolotova._', 'zoolmu5ic']

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

print(len(old_folowing))
print(len(folowing_names))


def solution(number):
    sum = 0
    for i in range(0,number):
        if (i % 3 == 0) or (i % 5 == 0):
            sum += i

    return(sum)

print(solution(10))



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


print(unfolowing)
print(folowing_left)
print(folowing)
