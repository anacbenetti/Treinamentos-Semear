import cv2 
import numpy as np

#o zero significa o numero da sua webcan, caso voce tivesse mais que uma colocaria outro valor
cap = cv2.VideoCapture(0) #carregando uma imagem de video da webcam

while True:
    #o ret é responsavel para saber se sua camera esta disponivel para ser utilizada
    ret, frame = cap.read(); #forma que nossa imagem vai ser apresentada(frame)
    width = int(cap.get(3)) #fornece a largura da imagem original
    height = int(cap.get(4))#fornece a altura da imagem original

    img = cv2.line(frame,(0,0), (width, height), (255,0,0), 10) #traçando a linha, os parametros sao(quadro onde vai desenhar, coordenada inicial, coordenada final, cor da linha, espessura)
    img = cv2.line(frame,(0,height), (width, 0), (255,0,0), 10) #traçando a linha, os parametros sao(quadro onde vai desenhar, coordenada inicial, coordenada final, cor da linha, espessura)
    img = cv2.rectangle(img, (100,100), (200,200), (128,128,128), -1) #desenhando retangulo (canto superior esquerdo, canto inferior direito, )
    img = cv2.circle(img, (300,300), 60, (0,0,255), -1) #desenhando circulo (posicao de onde esta centrado, valor do raio)
    font = cv2.FONT_HERSHEY_SIMPLEX #escolhendo a fonte
    img = cv2.putText(img, 'NREEEEEE', (200,height-10), font, 2, (255,255,255), cv2.LINE_AA)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): #se o q for pressionado sai da janela
        break

cap.release() #libera o recurso da camera
cv2.destroyAllWindows() #desativando a webcam