import cv2 
import numpy as np

#o zero significa o numero da sua webcan, caso voce tivesse mais que uma colocaria outro valor
cap = cv2.VideoCapture(0) #carregando uma imagem de video da webcam

while True:
    #o ret é responsavel para saber se sua camera esta disponivel para ser utilizada
    ret, frame = cap.read(); #forma que nossa imagem vai ser apresentada(frame)
    width = int(cap.get(3)) #fornece a largura da imagem original
    height = int(cap.get(4))#fornece a altura da imagem original

    image = np.zeros(frame.shape, np.uint8) #cria uma matriz de zeros (tipo inteiro de 8 bits)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy = 0.5) #redimensionando minha imagem como metade do tamanho original
    
    #alocando as imagens nos quadrantes
    image[:height//2, :width//2] = smaller_frame 
    image[height//2:, :width//2] = smaller_frame
    image[:height//2, width//2:] = smaller_frame
    image[height//2:, width//2:] = smaller_frame

    
    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #se o q for pressionado sai da janela
        break

cap.release() #libera o recurso da camera
cv2.destroyAllWindows() #desativando a webcam