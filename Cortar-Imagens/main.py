import cv2
from os import listdir
from os.path import isfile, join

# Caminho das imagens
path = 'img/'
files = [f for f in listdir(path) if isfile(join(path, f))]


# Recorta a área em que está a forma de onda longa.
def ecg_crop_img(y, yo, x, xo, path_save, save_name):
    i = 0
    for each in files:
        image = ("img/" + each)
        img = cv2.imread(image)
        crop_img = img[y:yo, x:xo]
        # cv2.imshow("cropped", crop_img) # MOSTRA A IMAGEM CORTADA
        cv2.imwrite('newImg/' + path_save + '/' + save_name + each, crop_img)
        cv2.waitKey(0)
    print('Finalizado.')


# SÃO 2 FORMATOS DIFERENTES DE ELETROCARDIOGRAMA COM INFARTO DO MIOCÁRDIO,
# DEVIDO A ISSO FOI NECESSÁRIO FAZER O PROCESSO DUAS VEZES,
# UMA PARA AS IMAGENS DE 1 A 37 E OUTRA PARA AS IMAGENS DE 38 A 77.


ecg_crop_img(1250, 1500, 70, 2150, path_save='longo', save_name='longo') # CORTA A ONDA LONGA

ecg_crop_img(300, 600, 70, 642, path_save='D1', save_name='D1') # CORTA A ONDA D1 1-37
ecg_crop_img(600, 900, 70, 642, path_save='D2', save_name='D2') # CORTA A ONDA D2 1-37
ecg_crop_img(900, 1200, 70, 642, path_save='D3', save_name='D3')  # CORTA A ONDA D3 1-37
ecg_crop_img(300, 600, 646, 1133, path_save='AVR', save_name='AVR') # CORTA A ONDA aVR 1-37
ecg_crop_img(600, 900, 646, 1133, path_save='AVL', save_name='AVL') # CORTA A ONDA aVL 1-37
ecg_crop_img(900, 1200, 646, 1133, path_save='AVF', save_name='AVF')  # CORTA A ONDA aVF 1-37
ecg_crop_img(300, 600, 1140, 1625, path_save='V1', save_name='V1') # CORTA A ONDA V1 1-37
ecg_crop_img(600, 900, 1140, 1625, path_save='V2', save_name='V2') # CORTA A ONDA V2 1-37
ecg_crop_img(900, 1200, 1140, 1625, path_save='V3', save_name='V3') # CORTA A ONDA V3 1-37
ecg_crop_img(300, 600, 1630, 2124, path_save='V4', save_name='V4') # CORTA A ONDA V4 1-37
ecg_crop_img(600, 900, 1630, 2124, path_save='V5', save_name='V5') # CORTA A ONDA V5 1-37
ecg_crop_img(900, 1200, 1630, 2124, path_save='V6', save_name='V6') # CORTA A ONDA V6 1-37

# ecg_crop_img(270, 450, 70, 1130, path_save='D1', save_name='D1') # CORTA A ONDA D1 38-77
# ecg_crop_img(450, 630, 70, 1130, path_save='D2', save_name='D2') # CORTA A ONDA D2 38-77
# ecg_crop_img(630, 810, 70, 1130, path_save='D3', save_name='D3')  # CORTA A ONDA D3 38-77
# ecg_crop_img(826, 980, 70, 1133, path_save='AVR', save_name='AVR') # CORTA A ONDA aVR 1-38
# ecg_crop_img(980, 1150, 70, 1133, path_save='AVL', save_name='AVL') # CORTA A ONDA aVL 1-38
# ecg_crop_img(1150, 1330, 70, 1133, path_save='AVF', save_name='AVF')  # CORTA A ONDA aVF 1-38
# ecg_crop_img(290, 517, 1140, 2123, path_save='V1', save_name='V1') # CORTA A ONDA V1 38-77
# ecg_crop_img(517, 675, 1140, 2123, path_save='V2', save_name='V2') # CORTA A ONDA V2 38-77
# ecg_crop_img(675, 843, 1140, 2123, path_save='V3', save_name='V3')  # CORTA A ONDA V3 38-77
# ecg_crop_img(826, 980, 1140, 2123, path_save='V4', save_name='V4') # CORTA A ONDA V4 1-38
# ecg_crop_img(980, 1150, 1140, 2123, path_save='V5', save_name='V5') # CORTA A ONDA V5 1-38
# ecg_crop_img(1150, 1330, 1140, 2123, path_save='V6', save_name='V6')  # CORTA A ONDA V6 1-38
