import sys
import os

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class ImageApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('Image')

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.col_layout = QVBoxLayout(self.container)
        self.container.setLayout(self.col_layout)

        self.title = QLabel('Football players')
        self.title.resize(self.width(), 25)
        self.title.setStyleSheet("font-size: 20px")
        self.title.setAlignment(Qt.AlignCenter)
        self.col_layout.addWidget(self.title)

        self.img_row_layout = QHBoxLayout(self.container)

        self.img_row_container = QWidget(self.container)
        self.img_row_container.setLayout(self.img_row_layout)

        for player in ['messi', 'ronaldo', 'dzuba']:
            image = QLabel(player, self.container)
            pixmap = QPixmap(f'./static/{player}.jpg').scaled(100, 300, Qt.KeepAspectRatio)

            image.setPixmap(pixmap)

            self.img_row_layout.addWidget(image)

        self.col_layout.addWidget(self.img_row_container)


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = ImageApp()
    ui.show()
    sys.exit(app.exec())
