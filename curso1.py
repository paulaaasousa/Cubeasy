import cv2
import numpy as np
import matplotlib.pyplot
#Open CV = BGR
#print(imagem.shape[0]) #480 -- altura
#print(imagem.shape[1]) #640 -- largura
#print(imagem.shape[2]) #3 qtd de canais de cores

def media_fatias(a, b, c, d):
    soma = 0
    fatia = [0, 0, 0]
    imagem = cv2.imread("cubo1.jpeg")
    for i in range(a, b):
        for j in range(c, d):
            soma = soma + 1
            fatia = fatia + imagem[i, j]
    fatia = fatia/soma
    return fatia

def cor_fatia(fatia):
    if fatia[0]<90 and fatia[1]<90 and fatia[2]>190:
        return 1
    elif fatia[0]>200 and fatia[1]<100 and fatia[2]<100:
        return 2
    elif fatia[0]<130 and fatia[1]>200 and fatia[2]<100:
        return 3
    elif fatia[0]<165 and fatia[1]>220 and fatia[2]>220:
        return 4
    elif fatia[0]>200 and fatia[1]>200 and fatia[2]>200:
        return 5
    elif fatia[0]<125 and fatia[1]<150 and fatia[2]<230:
        return 6

def recebe_imagem (imagem):
    fatia11 = [0, 0, 0]
    fatia12 = [0, 0, 0]
    fatia13 = [0, 0, 0]
    fatia21 = [0, 0, 0]
    fatia22 = [0, 0, 0]
    fatia23 = [0, 0, 0]
    fatia31 = [0, 0, 0]
    fatia32 = [0, 0, 0]
    fatia33 = [0, 0, 0]

    fatia11 = media_fatias(123, 133, 215, 225)
    fatia12 = media_fatias(123, 133, 320, 330)
    fatia13 = media_fatias(115, 125, 440, 450)

    fatia21 = media_fatias(240, 250, 215, 225)
    fatia22 = media_fatias(240, 250, 320, 330)
    fatia23 = media_fatias(240, 250, 430, 440)

    fatia31 = media_fatias(340, 350, 215, 225)
    fatia32 = media_fatias(340, 350, 320, 330)
    fatia33 = media_fatias(340, 350, 430, 440)

    cor11 = cor_fatia(fatia11)
    cor12 = cor_fatia(fatia12)
    cor13 = cor_fatia(fatia13)

    cor21 = cor_fatia(fatia21)
    cor22 = cor_fatia(fatia22)
    cor23 = cor_fatia(fatia23)

    cor31 = cor_fatia(fatia31)
    cor32 = cor_fatia(fatia32)
    cor33 = cor_fatia(fatia33)

    if cor11 == cor12 == cor13 == cor21 == cor22 == cor23 == cor31 == cor32 == cor33:
        print(f'Face Resolvida')
    else:
        print(f'Face Embaralhada')



    # cv2.imshow("imagem", imagem)
    # cv2.waitKey(0)

imagem = cv2.imread("cubo1.jpeg")

recebe_imagem(imagem)





