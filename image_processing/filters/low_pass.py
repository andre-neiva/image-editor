import cv2
import numpy as np

def filtro_media(img):
    return cv2.blur(img, (3, 3))

def filtro_mediana(img):
    return cv2.medianBlur(img, 3)

def filtro_gaussiano(img):
    return cv2.GaussianBlur(img, (3, 3), 0)

def filtro_maximo(img, mask_size=3):
    pad_size = (mask_size - 1) // 2
    img_pad = pad_image(img, pad_size)
    img_out = np.zeros_like(img, dtype=np.uint8)

    for i in range(pad_size, img_pad.shape[0] - pad_size):
        for j in range(pad_size, img_pad.shape[1] - pad_size):
            n = get_neigh(img_pad, i, j, mask_size)
            img_out[i - pad_size, j - pad_size] = np.max(n)

    return img_out

def filtro_minimo(img, mask_size=3):
    pad_size = (mask_size - 1) // 2
    img_pad = pad_image(img, pad_size)
    img_out = np.zeros_like(img, dtype=np.uint8)

    for i in range(pad_size, img_pad.shape[0] - pad_size):
        for j in range(pad_size, img_pad.shape[1] - pad_size):
            n = get_neigh(img_pad, i, j, mask_size)
            img_out[i - pad_size, j - pad_size] = np.min(n)

    return img_out
        ####### img_out[i, j] = n.min()

def pad_image(img, pad_size):
    """Aplica padding zero ao redor da imagem."""
    return np.pad(img, pad_size, mode='constant', constant_values=0)

def get_neigh(img, i, j, size):
    """Extrai a vizinhança (janela) centrada em (i, j)."""
    half = size // 2
    return img[i - half:i + half + 1, j - half:j + half + 1]