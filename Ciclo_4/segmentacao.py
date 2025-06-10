import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg')
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Definir o intervalo de cor para segmentação
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# Criar uma máscara que isola os pixels dentro do intervalo de azul
mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

# Aplicar a máscara para obter o resultado
segmented_image = cv2.bitwise_and(image, image, mask=mask)

# Exibir a imagem
cv2.imshow('Original Image', image)
cv2.imshow('HSV Masked', mask)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
