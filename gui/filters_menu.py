from PyQt5.QtWidgets import QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from image_processing.filters.low_pass import (
    filtro_media, filtro_mediana, filtro_gaussiano,
    filtro_maximo, filtro_minimo
)


def criar_menu_filtros_passabaixa(parent):
    """Cria o botão colapsável e o widget com os botões de filtros"""

    # Botão de colapsar
    toggle_btn = QPushButton("▶ Filtros Passa-Baixa")
    toggle_btn.setCheckable(True)
    toggle_btn.setChecked(False)

    # Widget de botões de filtros
    container = QWidget()
    layout = QVBoxLayout(container)
    layout.setContentsMargins(15, 0, 0, 0)

    filtros = [
        ("Filtro de Média", filtro_media),
        ("Filtro de Mediana", filtro_mediana),
        ("Filtro Gaussiano", filtro_gaussiano),
        ("Filtro Máximo", filtro_maximo),
        ("Filtro Mínimo", filtro_minimo)
    ]

    for label, func in filtros:
        btn = QPushButton(label)
        btn.clicked.connect(lambda _, f=func: parent.aplicar_filtro(f))
        layout.addWidget(btn)

    container.setVisible(False)

    def toggle_visibility():
        visible = toggle_btn.isChecked()
        container.setVisible(visible)
        toggle_btn.setText("▼ Filtros Passa-Baixa" if visible else "▶ Filtros Passa-Baixa")

    toggle_btn.clicked.connect(toggle_visibility)

    return toggle_btn, container
