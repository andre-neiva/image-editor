import cv2
import numpy as np

def alargamento_contraste(img_gray):
    """Aplica alargamento de contraste à imagem em tons de cinza."""
    if img_gray is None:
        raise ValueError("Imagem não fornecida.")

    min_val = np.min(img_gray)
    max_val = np.max(img_gray)

    # Se a imagem tiver intensidade constante, retorna uma cópia
    if min_val == max_val:
        return img_gray.copy()

    # Normaliza os valores para a faixa [0, 255]
    normalized = cv2.normalize(img_gray, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    return normalized

def equalizar_histograma(img_gray):
    """Equaliza o histograma da imagem em tons de cinza"""
    if img_gray is None:
        raise ValueError("Imagem não fornecida.")

    return cv2.equalizeHist(img_gray)