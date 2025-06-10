import cv2

# Carregar a imagem
image_path = '/home/anabenetti/Semear_25/meuprojeto/filhote.jpg'
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    print("Erro ao abrir a imagem.")
else:
    # Aplicar Gaussian Blur
    gaussian_blur = cv2.GaussianBlur(image, (5, 5), 0)  # O segundo parâmetro é o tamanho do kernel, que deve ser positivo e ímpar. O terceiro é o desvio padrão.

    # Aplicar Median Blur
    median_blur = cv2.medianBlur(image, 5)  # O parâmetro é o tamanho do kernel, que deve ser um número ímpar maior que 1.

    # Exibir a imagem original
    cv2.imshow('Imagem Original', image)

    # Exibir a imagem com Gaussian Blur
    cv2.imshow('Gaussian Blur', gaussian_blur)

    # Exibir a imagem com Median Blur
    cv2.imshow('Median Blur', median_blur)

    # Aguardar que uma tecla seja pressionada para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()
