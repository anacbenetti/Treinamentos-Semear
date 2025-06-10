import cv2 
import random

img = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg', -1)
if img is None:
    print("Erro: imagem não carregada.")
    exit()

img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# Verifica se a imagem tem tamanho suficiente
h, w = img.shape[:2]
if h >= 150 and w >= 150:
    tag = img[50:100, 100:150]
    img[100:150, 50:100] = tag
else:
    print(f"A imagem ({w}x{h}) é pequena demais para recortes de 150 pixels.")

cv2.imshow('Ace', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
