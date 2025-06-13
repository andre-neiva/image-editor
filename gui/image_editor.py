import cv2
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QScrollArea, QFileDialog, QMessageBox, QGroupBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

from image_processing.histogram import exibir_histograma
from image_processing.intensity import alargamento_contraste, equalizar_histograma
from image_processing.filters.low_pass import (
    filtro_media, filtro_mediana, filtro_gaussiano,
    filtro_maximo, filtro_minimo
)
from image_processing.segmentation import segmentar_otsu

from gui.low_pass_menu import criar_menu_filtros_passabaixa
from gui.high_pass_menu import criar_menu_filtros_passaalta
from image_processing.fourier import exibir_espectro_fourier
from gui.morphology_menu import criar_menu_morfologia

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Imagens - SIN392")
        self.setGeometry(100, 100, 1000, 700)

        self.image_gray = None
        self.image_gray_original = None

        self.image_label = QLabel("Nenhuma imagem carregada")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # === MENU LATERAL ===
        side_menu = QVBoxLayout()

        self.btn_open = QPushButton("Abrir Imagem")
        self.btn_open.clicked.connect(self.open_image)
        side_menu.addWidget(self.btn_open)

        self.btn_save = QPushButton("Salvar Imagem")
        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setEnabled(False)
        side_menu.addWidget(self.btn_save)

        self.btn_reset = QPushButton("Reverter Imagem")
        self.btn_reset.clicked.connect(self.reset_image)
        self.btn_reset.setEnabled(False)
        side_menu.addWidget(self.btn_reset)


        side_menu.addSpacing(20)
        side_menu.addWidget(QLabel("Processamentos"))

        self.btn_histogram = QPushButton("Histograma")
        self.btn_histogram.clicked.connect(self.histogram_action)
        side_menu.addWidget(self.btn_histogram)

        self.btn_contrast = QPushButton("Alargamento de Contraste")
        self.btn_contrast.clicked.connect(self.contrast_action)
        side_menu.addWidget(self.btn_contrast)

        self.btn_equalize = QPushButton("Equalizar Histograma")
        self.btn_equalize.clicked.connect(self.equalize_action)
        side_menu.addWidget(self.btn_equalize)

        # === MENU COLAPSÁVEL DE FILTROS ===
        low_pass_menu, low_widget = criar_menu_filtros_passabaixa(self)
        side_menu.addWidget(low_pass_menu)
        side_menu.addWidget(low_widget)

        high_pass_menu, high_widget = criar_menu_filtros_passaalta(self)
        side_menu.addWidget(high_pass_menu)
        side_menu.addWidget(high_widget)

        self.btn_fourier = QPushButton("Exibir Espectro de Fourier")
        self.btn_fourier.clicked.connect(self.fourier_action)
        side_menu.addWidget(self.btn_fourier)
        
        morf_btn, morf_container = criar_menu_morfologia(self)
        side_menu.addWidget(morf_btn)
        side_menu.addWidget(morf_container)

        self.btn_otsu = QPushButton("Segmentação (Otsu)")
        self.btn_otsu.clicked.connect(self.otsu_action)
        side_menu.addWidget(self.btn_otsu)


        side_menu.addStretch(1)
        menu_group = QGroupBox("Menu")
        menu_group.setLayout(side_menu)


        # === VISUALIZAÇÃO DE IMAGEM ===
        image_scroll = QScrollArea()
        image_scroll.setWidgetResizable(True)
        image_scroll.setWidget(self.image_label)

        main_layout = QHBoxLayout()
        main_layout.addWidget(menu_group)
        main_layout.addWidget(image_scroll, 1)

        self.setLayout(main_layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Imagem", "", "Imagens (*.png *.jpg *.bmp)")
        if file_path:
            image_bgr = cv2.imread(file_path)
            if image_bgr is None:
                QMessageBox.critical(self, "Erro", "Não foi possível carregar a imagem.")
                return
            self.image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
            self.image_gray_original = self.image_gray.copy()
            self.display_image(self.image_gray)
            self.btn_save.setEnabled(True)
            self.btn_reset.setEnabled(True)

    def save_image(self):
        if self.image_gray is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem", "", "PNG (*.png);;JPG (*.jpg)")
            if file_path:
                cv2.imwrite(file_path, self.image_gray)
                QMessageBox.information(self, "Imagem Salva", "Imagem salva com sucesso!")

    def verificar_imagem(self):
        if self.image_gray is None:
            QMessageBox.warning(self, "Aviso", "Nenhuma imagem foi carregada.")
            return False
        return True

    def display_image(self, img):
        if len(img.shape) == 2:
            h, w = img.shape
            qt_image = QImage(img.data, w, h, w, QImage.Format_Grayscale8)
        else:
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            qt_image = QImage(rgb_image.data, w, h, ch * w, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))

    def aplicar_filtro(self, funcao_filtro):
        if not self.verificar_imagem():
            return
        try:
            resultado = funcao_filtro(self.image_gray)
            self.image_gray = resultado
            self.display_image(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao aplicar filtro:\n{str(e)}")

    def histogram_action(self):
        if not self.verificar_imagem():
            return
        exibir_histograma(self.image_gray)

    def contrast_action(self):
        if not self.verificar_imagem():
            return
        try:
            resultado = alargamento_contraste(self.image_gray)
            self.image_gray = resultado
            self.display_image(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao aplicar contraste:\n{str(e)}")

    def equalize_action(self):
        if not self.verificar_imagem():
            return
        try:
            resultado = equalizar_histograma(self.image_gray)
            self.image_gray = resultado
            self.display_image(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao aplicar equalização:\n{str(e)}")

    def fourier_action(self):
        if not self.verificar_imagem():
            return
        try:
            exibir_espectro_fourier(self.image_gray)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao calcular espectro de Fourier:\n{str(e)}")

    def otsu_action(self):
        if not self.verificar_imagem():
            return
        try:
            resultado = segmentar_otsu(self.image_gray)
            self.image_gray = resultado  # Atualiza para salvar
            self.display_image(resultado)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro na segmentação Otsu:\n{str(e)}")

    def reset_image(self):
        if self.image_gray_original is not None:
            self.image_gray = self.image_gray_original.copy()
            self.display_image(self.image_gray)
