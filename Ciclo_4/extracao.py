import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg')

# Inicializar o detector ORB
orb = cv2.ORB_create()

# Detectar pontos-chave e calcular descritores
keypoints, descriptors = orb.detectAndCompute(image, None)

# Desenhar os pontos-chave na imagem
image_keypoints = cv2.drawKeypoints(image, keypoints, None, color=(0, 255, 0), flags=0)

# Exibir a imagem com pontos-chave
cv2.imshow('ORB Key Points', image_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
