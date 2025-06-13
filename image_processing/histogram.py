import cv2
import numpy as np
import matplotlib.pyplot as plt

def exibir_histograma(img_gray):
    """Exibe o histograma de uma imagem em tons de cinza"""
    if img_gray is None:
        raise ValueError("Imagem não fornecida.")

    # Calcular histograma
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])

    # Exibir histograma com matplotlib
    plt.figure("Histograma")
    plt.title("Histograma em Níveis de Cinza")
    plt.xlabel("Intensidade de Pixel")
    plt.ylabel("Frequência")
    plt.plot(hist, color='black')
    plt.xlim([0, 256])
    plt.grid(True)
    plt.show()
