import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QMessageBox
)
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt

class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Editor de Imagens - SIN392")
        self.setGeometry(100, 100, 800, 600)

        self.image = None  # Imagem carregada
        self.image_label = QLabel("Nenhuma imagem carregada")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.btn_open = QPushButton("Abrir Imagem")
        self.btn_open.clicked.connect(self.open_image)

        self.btn_save = QPushButton("Salvar Imagem")
        self.btn_save.clicked.connect(self.save_image)
        self.btn_save.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.btn_open)
        layout.addWidget(self.btn_save)

        self.setLayout(layout)

    def open_image(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Abrir Imagem", "", "Imagens (*.png *.jpg *.bmp)")
        if file_path:
            self.image = cv2.imread(file_path)
            if self.image is None:
                QMessageBox.critical(self, "Erro", "Não foi possível carregar a imagem.")
                return
            self.display_image(self.image)
            self.btn_save.setEnabled(True)

    def save_image(self):
        if self.image is not None:
            file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Imagem", "", "PNG (*.png);;JPG (*.jpg)")
            if file_path:
                cv2.imwrite(file_path, self.image)
                QMessageBox.information(self, "Imagem Salva", "Imagem salva com sucesso!")

    def display_image(self, img):
        """Converte imagem BGR para RGB e exibe no QLabel"""
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap.scaled(
            self.image_label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
        ))
