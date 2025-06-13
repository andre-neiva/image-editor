import numpy as np
import matplotlib.pyplot as plt

def exibir_espectro_fourier(img_gray):
    """Exibe o espectro de magnitude da transformada de Fourier"""
    if img_gray is None:
        raise ValueError("Imagem não fornecida.")

    # Calcula a FFT e centraliza o espectro
    f = np.fft.fft2(img_gray)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20 * np.log(1 + np.abs(fshift))

    # Exibe o espectro com matplotlib
    plt.figure("Espectro de Fourier")
    plt.title("Espectro de Magnitude (Fourier)")
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.axis('off')
    plt.show()
