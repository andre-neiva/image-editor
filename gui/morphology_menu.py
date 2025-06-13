from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from image_processing.morphology import erosao, dilatacao

def criar_menu_morfologia(parent):
    toggle_btn = QPushButton("▶ Morfologia Matemática")
    toggle_btn.setCheckable(True)
    toggle_btn.setChecked(False)

    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(15, 0, 0, 0)

    filtros = [
        ("Erosão", erosao),
        ("Dilatação", dilatacao)
    ]

    for nome, func in filtros:
        btn = QPushButton(nome)
        btn.clicked.connect(lambda _, f=func: parent.aplicar_filtro(f))
        layout.addWidget(btn)

    container.setVisible(False)

    def toggle_visibility():
        visible = toggle_btn.isChecked()
        container.setVisible(visible)
        toggle_btn.setText("▼ Morfologia Matemática" if visible else "▶ Morfologia Matemática")

    toggle_btn.clicked.connect(toggle_visibility)

    return toggle_btn, container
