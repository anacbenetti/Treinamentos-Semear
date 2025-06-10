import cv2

# Carregar a imagem em escala de cinza
image = cv2.imread('/home/anabenetti/Semear_25/meuprojeto/filhote.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar thresholding
_, thresholded_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

# Exibir a imagem
cv2.imshow('Original Image', image)
cv2.imshow('Thresholded Image', thresholded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
