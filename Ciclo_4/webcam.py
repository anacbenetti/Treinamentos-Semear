import numpy as np
import cv2

#o zero significa o numero da sua webcam, caso voce tivesse mais que uma colocaria outro valor
cap = cv2.VideoCapture(0) #carregando uma imagem de video da webcam

while True:
    #o ret é responsavel para saber se sua camera esta disponivel para ser utilizada
    ret, frame = cap.read(); #forma que nossa imagem vai ser apresentada(frame)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #se o q for pressionado sai da janela
        break

cap.release() #libera o recurso da camera
cv2.destroyAllWindows() #desativando a webcam