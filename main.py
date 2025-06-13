from PyQt5.QtWidgets import QApplication
# Update the import path if 'image_editor.py' is in the same directory as main.py
from gui.image_editor import ImageEditor
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec_())
