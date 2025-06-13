import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QFileDialog, QMessageBox, QSizePolicy, QScrollArea, QGroupBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Imagens - SIN392")
        self.setGeometry(100, 100, 1000, 700)

        self.image = None
        self.image_label = QLabel("Nenhuma imagem carregada")
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Botões de menu
        self.btn_open = QPushButton("Abrir Imagem")
        self.btn_open.clicked.connect(self.open_image)

        self.btn_save = QPushButton("Salvar Imagem")
        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setEnabled(False)

        # Botões de funcionalidades (placeholders)
        self.btn_histogram = QPushButton("Histograma")
        self.btn_histogram.clicked.connect(self.histogram_action)

        self.btn_contrast = QPushButton("Alargamento de Contraste")
        self.btn_contrast.clicked.connect(self.contrast_action)

        self.btn_equalize = QPushButton("Equalizar Histograma")
        self.btn_equalize.clicked.connect(self.equalize_action)

        # Menu lateral (layout vertical)
        side_menu = QVBoxLayout()
        side_menu.addWidget(self.btn_open)
        side_menu.addWidget(self.btn_save)
        side_menu.addSpacing(20)
        side_menu.addWidget(QLabel("Processamentos"))
        side_menu.addWidget(self.btn_histogram)
        side_menu.addWidget(self.btn_contrast)
        side_menu.addWidget(self.btn_equalize)
        side_menu.addStretch(1)

        # Agrupar o menu lateral (opcional)
        menu_group = QGroupBox("Menu")
        menu_group.setLayout(side_menu)

        # Área de imagem com scroll (caso seja grande)
        image_scroll = QScrollArea()
        image_scroll.setWidgetResizable(True)
        image_scroll.setWidget(self.image_label)

        # Layout principal com dois blocos lado a lado
        main_layout = QHBoxLayout()
        main_layout.addWidget(menu_group)
        main_layout.addWidget(image_scroll, 1)

        self.setLayout(main_layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Imagem", "", "Imagens (*.png *.jpg *.bmp)")
        if file_path:
            # Carregar imagem (em BGR)
            image_bgr = cv2.imread(file_path)
            if image_bgr is None:
                QMessageBox.critical(self, "Erro", "Não foi possível carregar a imagem.")
                return

            # Converter para tons de cinza
            self.image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

            # Exibir a imagem em tons de cinza
            self.display_image(self.image_gray)

            # Ativar botão de salvar
            self.btn_save.setEnabled(True)



    def save_image(self):
        if self.image_gray is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem", "", "PNG (*.png);;JPG (*.jpg)")
            if file_path:
                cv2.imwrite(file_path, self.image_gray)
                QMessageBox.information(self, "Imagem Salva", "Imagem salva com sucesso!")


    def display_image(self, img):
        """Exibe imagem no QLabel — suporta RGB e grayscale"""
        if len(img.shape) == 2:  # Grayscale
            h, w = img.shape
            bytes_per_line = w
            qt_image = QImage(img.data, w, h, bytes_per_line, QImage.Format_Grayscale8)
        else:  # RGB
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))


    # Ações placeholders (por enquanto só mensagens)
    def histogram_action(self):
        QMessageBox.information(self, "Histograma", "Função de histograma será implementada.")

    def contrast_action(self):
        QMessageBox.information(self, "Contraste", "Função de alargamento de contraste será implementada.")

    def equalize_action(self):
        QMessageBox.information(self, "Equalizar", "Função de equalização será implementada.")
