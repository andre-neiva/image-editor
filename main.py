from PyQt5.QtWidgets import QApplication
from gui import ImageEditor
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageEditor()
    window.show()
    sys.exit(app.exec_())
