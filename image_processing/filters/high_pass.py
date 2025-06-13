import cv2
import numpy as np

def filtro_sobel(img):
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    sobel = np.hypot(sobelx, sobely)
    return np.clip(sobel, 0, 255).astype(np.uint8)

def filtro_prewitt(img):
    kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
    kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
    gx = cv2.filter2D(img, -1, kernelx)
    gy = cv2.filter2D(img, -1, kernely)
    prewitt = np.hypot(gx, gy)
    return np.clip(prewitt, 0, 255).astype(np.uint8)

def filtro_roberts(img):
    kernelx = np.array([[1, 0], [0, -1]])
    kernely = np.array([[0, 1], [-1, 0]])
    gx = cv2.filter2D(img, -1, kernelx)
    gy = cv2.filter2D(img, -1, kernely)
    roberts = np.hypot(gx, gy)
    return np.clip(roberts, 0, 255).astype(np.uint8)

def filtro_laplaciano(img):
    laplaciano = cv2.Laplacian(img, cv2.CV_64F)
    return np.clip(np.abs(laplaciano), 0, 255).astype(np.uint8)
