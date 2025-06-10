import cv2
import numpy as np

# Carregar a imagem
image_path = '/home/anabenetti/Semear_25/meuprojeto/filhote.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Convertendo diretamente para escala de cinza

# Aplicar o detector de bordas Canny
edges = cv2.Canny(image, 100, 200)  # Os valores 100 e 200 são os limiares mínimo e máximo

# Encontrar contornos baseados nas bordas detectadas
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar contornos na imagem original (em cor)
image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
cv2.drawContours(image_color, contours, -1, (0, 255, 0), 2)

# Exibir a imagem
cv2.imshow('Detected Edges', edges)
cv2.imshow('Contours', image_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
