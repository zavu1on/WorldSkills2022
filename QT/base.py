import sys
import os
from PyQt5.QtWidgets import *


class BaseApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('Base')


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = BaseApp()
    ui.show()
    sys.exit(app.exec())
