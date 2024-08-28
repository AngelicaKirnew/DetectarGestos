#pip install opencv-python
#pip install cvzone
#pip install mediapipe

import cv2
from cvzone.HandTrackingModule import HandDetector
#from pynput.keyboard import Key, Controller

video = cv2.VideoCapture(0)

video.set(3,1280)
video.set(4,720)

#kb = Controller()

detector = HandDetector(detectionCon=0.8)
#por adrão se coloca todos os dedos dobrados
estadoAtual = [0,0,0,0,0]

imagem1 = cv2.imread('coracao.jpg')
imagem2 = cv2.imread('paz.jpg')
imagem3 = cv2.imread('joia.jpg')


while True:
    _,img = video.read()
    hands,img = detector.findHands(img)

    if hands:
        estado = detector.fingersUp(hands[0])
        #print(estado) #pra ver qual dedo ta levantado :)

        # Não importa qual mão você mostre na camera os valores são iguais
        # por exemplo o polegar é sempre o primeiro da esqueda pra direita [1,0,0,0,0]
        if estado!=estadoAtual and estado == [1,1,0,0,1]:
            print('imagem 1')


        if estado!=estadoAtual and estado == [0,1,1,0,0]:
            print('imagem 2')
            #identifica quando o dedo correspondente esta levantado e da um print com a mensagem

        if estado!=estadoAtual and estado == [1,0,0,0,0]:
            print('imagem 3')

        if estado == estadoAtual and estado == [1, 1, 0, 0, 1]:
            img[50:450, 50:450] = imagem1
            #ajustar a area que sera recortada na camera para encaixar a imagem dentro (220x220)
            #Até onde eu entendi só pegar o tamanho da imagem e somar 50 pra poder colocar ali :)

        if estado == estadoAtual and estado == [0, 1, 1, 0, 0]:
            img[50:700, 50:700] = imagem2

        if estado == estadoAtual and estado == [1, 0, 0, 0, 0]:
            img[50:410, 50:410] = imagem3

        estadoAtual = estado

    cv2.imshow('img',cv2.resize(img,(640,420)))
    cv2.waitKey(1)