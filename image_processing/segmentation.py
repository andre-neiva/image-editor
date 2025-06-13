import cv2

def segmentar_otsu(img_gray):
    """Aplica segmentação automática de Otsu"""
    if img_gray is None:
        raise ValueError("Imagem não fornecida.")

    _, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return img_bin
