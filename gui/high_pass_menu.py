from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from image_processing.filters.high_pass import (
    filtro_sobel, filtro_prewitt,
    filtro_roberts, filtro_laplaciano
)

def criar_menu_filtros_passaalta(parent):
    toggle_btn = QPushButton("▶ Filtros Passa-Alta")
    toggle_btn.setCheckable(True)
    toggle_btn.setChecked(False)

    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(15, 0, 0, 0)

    filtros = [
        ("Filtro Sobel", filtro_sobel),
        ("Filtro Prewitt", filtro_prewitt),
        ("Filtro Roberts", filtro_roberts),
        ("Filtro Laplaciano", filtro_laplaciano)
    ]

    for nome, func in filtros:
        btn = QPushButton(nome)
        btn.clicked.connect(lambda _, f=func: parent.aplicar_filtro(f))
        layout.addWidget(btn)

    container.setVisible(False)

    def toggle_visibility():
        visible = toggle_btn.isChecked()
        container.setVisible(visible)
        toggle_btn.setText("▼ Filtros Passa-Alta" if visible else "▶ Filtros Passa-Alta")

    toggle_btn.clicked.connect(toggle_visibility)

    return toggle_btn, container
