import cv2
import numpy as np

def erosao(img, kernel_size=3):
    """Aplica erosão usando elemento estrutural quadrado"""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.erode(img, kernel, iterations=1)

def dilatacao(img, kernel_size=3):
    """Aplica dilatação usando elemento estrutural quadrado"""
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    return cv2.dilate(img, kernel, iterations=1)
