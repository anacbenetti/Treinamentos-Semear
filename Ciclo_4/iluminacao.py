import cv2
import numpy as np

# Carregar a imagem
image_path = '/home/anabenetti/Semear_25/meuprojeto/filhote.jpg'
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    print("Erro ao abrir a imagem.")
else:
    # Ajuste de contraste e correção de iluminação usando correção gama
    gamma = 1.2  # Valor gama menor que 1 escurece a imagem, maior que 1 clareia a imagem
    adjusted_gamma = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

    # Aplicar a correção gama
    gamma_corrected = cv2.LUT(image, adjusted_gamma)

    # Equalização de histograma para melhorar o contraste
    # Convertendo para escala de cinza para equalização
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    equalized_image = cv2.equalizeHist(gray_image)

    # Exibir a imagem original
    cv2.imshow('Imagem Original', image)

    # Exibir a imagem após correção gama
    cv2.imshow('Gamma Correction', gamma_corrected)

    # Exibir a imagem após equalização de histograma
    cv2.imshow('Histogram Equalization', equalized_image)

    # Aguardar que uma tecla seja pressionada para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
