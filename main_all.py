import integration
import detect_modifications as detect

import cv2

# i=0
# k=0
# for f in integration.adresses_des_fichiers_et_dossiers("data\\detecter_type_char\\images\\")[1]:
#     xx=f.split("\\")
#     o=xx[len(xx)-2]
#     # print(o,integration.bin(k,20))
    
#     i=0
#     for e in integration.adresses_des_fichiers_et_dossiers(f)[0]:
#         print(integration.bin(k,20)+"_"+integration.bin(i,20)+e.split(".")[1])
#         integration.ecrire_txt("adresses.txt",integration.bin(k,20)+"_"+integration.bin(i,20)+"."+e.split(".")[1]+","+str(k)+","+o+"\n")
#         i+=1
#         integration.copy_file(e,"oscar\\"+integration.bin(k,20)+"_"+integration.bin(i,20)+"."+e.split(".")[1])
#     k+=1

# detect.run(weights="C:\\Users\\Fujitsu\\Desktop\\med\\outils\\usage_model\\best.pt",imgsz=(640,640), conf_thres=0.25,source="C:\\Users\\Fujitsu\\Desktop\\med\\oscar\\")
###############################################
#     detect.run(weights="C:\\Users\\Fujitsu\\Desktop\\med\\outils\\usage_model\\best.pt",imgsz=(640,640), conf_thres=0.29,source="C:\\Users\\Fujitsu\\Desktop\\med\\"+f)


###############################################
#detection de char sur une video
# detect.run(weights="C:\\Users\\Fujitsu\\Desktop\\med\\outils\\usage_model\\detection_char.pt",imgsz=(640,640), conf_thres=0.3,source="C:\\Users\\Fujitsu\\Desktop\\med\\far.mp4")


###############################################
#detection de char sur un dossier d'images
# detect.run(weights="C:\\Users\\Fujitsu\\Desktop\\med\\outils\\usage_model\\detection_char.pt",imgsz=(640,640), conf_thres=0.3,source="C:\\Users\\Fujitsu\\Desktop\\med\\train\\oscar\\")



###############################################
# classes=['altay',
# 'al_khalid',
# 'amx_13',
# 'amx_30',
# 'amx_32',
# 'amx_40',
# 'anders',
# 'ariete',
# 'arjun',
# 'arjun_mk2',
# 'armata',
# 'bmpt',
# 'bmpt_72',
# 'bmt_72',
# 'btmp_84',
# 'challenger_1',
# 'challenger_2',
# 'chieftain',
# 'chieftain_untold_story',
# 'cv90105',
# 'cv90120t',
# 'drozd',
# 'expeditionary_tank',
# 'fv101_scorpion',
# 'gl5',
# 'ikv_91',
# 'jaguar',
# 'k1',
# 'k1a1',
# 'k21_105',
# 'k21_with_xc8',
# 'k2_black_panther_mbt',
# 'kaplan',
# 'karrar',
# 'leclerc',
# 'leopard',
# 'leopard_2',
# 'leopard_2a4m_can',
# 'leopard_2a5',
# 'leopard_2a6',
# 'leopard_2a7',
# 'leopard_2ng',
# 'leopard_2pl',
# 'leopard_c2',
# 'lince',
# 'm1985',
# 'm1a1_abrams',
# 'm1a2_abrams',
# 'm1a2_sep',
# 'm1_abrams',
# 'm2002',
# 'm551_sheridan',
# 'm60a2',
# 'm60a3',
# 'm60_patton',
# 'm60_phoenix',
# 'm84',
# 'm84ab1',
# 'm8_buford',
# 'm90_vihor',
# 'm95_degman',
# 'magach_7',
# 'marder_light_tank',
# 'mars_15',
# 'mb3_tamoyo',
# 'mbt_3000',
# 'merkava_mk1',
# 'merkava_mk2',
# 'merkava_mk3',
# 'merkava_mk4',
# 'merkava_mk4_meil_ruach',
# 'nkpz',
# 'of_40',
# 'olifant_mk1b',
# 'olifant_mk2',
# 'oplot',
# 'oplot_m',
# 'osorio',
# 'pl_01',
# 'pt76',
# 'pt91_twardy',
# 'pt_16',
# 'revolution',
# 'ruag_leopard_upgrade',
# 'sabalan',
# 'sabra',
# 'sk105_kurassier',
# 'sprut_sd',
# 'sprut_sdm1',
# 'st2',
# 'super_m48',
# 'super_m60',
# 't12_black_eagle',
# 't55',
# 't55_enigma',
# 't62',
# 't64',
# 't64b1m',
# 't64bm_bulat',
# 't64e',
# 't72',
# 't72b3',
# 't72b4',
# 't72m2_moderna',
# 't72m4',
# 't72ua1',
# 't80',
# 't80b',
# 't80bvm',
# 't80u',
# 't80ud',
# 't80um1_bars',
# 't84',
# 't84_yatagan',
# 't90',
# 't90m',
# 't90ms_tagil',
# 't95',
# 'tam',
# 'tank_ex',
# 'tank_technology_demonstrator',
# 'tk_x',
# 'tm_800',
# 'tosan',
# 'tr85m1',
# 'tusk',
# 'type_62',
# 'type_63',
# 'type_63a',
# 'type_74',
# 'type_80',
# 'type_90',
# 'type_90_II',
# 'type_96',
# 'type_98',
# 'type_99',
# 'type_99g',
# 'unidentified_north_korean_mbt',
# 'vfm_5',
# 'vickers_mk3',
# 'vickers_mk4',
# 'vickers_mk7',
# 'vt2',
# 'vt4',
# 'vt5',
# 'zbd_2000_light_tank',
# 'ztq_15',
# 'zulfiqar_1',
# 'zulfiqar_2',
# 'zulfiqar_3',
# ]
# detected=integration.adresses_des_fichiers_et_dossiers("C:\\Users\\Fujitsu\\Desktop\\med\\housni\\")[0]
# txt=integration.lire_txt('adresses.txt')
# for e in txt.split('\n'):
#     if len(e) >1:
#         rec=e.split(',')
#         file_source="C:\\Users\\Fujitsu\\Desktop\\med\\housni\\"+rec[0].split('.')[0]+".txt"
#         file_destin="C:\\Users\\Fujitsu\\Desktop\\med\\housni_2\\"+rec[0].split('.')[0]+".txt"
#         print(file_source, classes.index(rec[-1]))
#         if file_source in detected:
#             buf=integration.lire_txt(file_source).split('\n')
#             for el in buf:
#                 if len(el)>1:
#                     print('---',str(classes.index(rec[-1]))+" "+el)
#                     integration.ecrire_txt(file_destin,str(classes.index(rec[-1]))+" "+el+"\n")



####################################################################
def realTime(adresse_poids:str, adresse_image:str, seuil=0.6):
    # return detect.run_custom(weights="C:\\Users\\Fujitsu\\Desktop\\med\\outils\\usage_model\\detection_char.pt",imgsz=(256,256), conf_thres=seuil,source="C:\\Users\\Fujitsu\\Desktop\\med\\realTime\\housni.png")
    return detect.run_custom(weights=adresse_poids,imgsz=(256,256), conf_thres=seuil,source=adresse_image)




###################################################################
# folder_source='oscar\\'
# folder_distination='train\\'

# for f in integration.adresses_des_fichiers_et_dossiers(folder_source)[0]:
#     img=cv2.imread(f)
#     resized = cv2.resize(img, (640,640), interpolation = cv2.INTER_AREA)
#     cv2.imwrite(folder_distination+f,resized)
#     print(folder_distination+f)


####################################################################


