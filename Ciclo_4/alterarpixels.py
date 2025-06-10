import cv2 
import random

img = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg', -1)
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5)
cv2.imwrite('new_Gon.jpg', img)

for i in range(min(100, img.shape[0])):
    for j in range(img.shape[1]):
        #gera numeros aleatorios para preencher blue, green, red
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Adult_Gon', img)
cv2.waitKey(0) 
cv2.destroyAllWindows()