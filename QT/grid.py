import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class GridApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)

        self.setWindowTitle('Grid Layout')

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.col_layout = QVBoxLayout(self.container)
        self.container.setLayout(self.col_layout)

        self.phone = QLabel("", self.container)
        self.phone.resize(300, 20)
        self.phone.setStyleSheet("font-size: 20px")
        self.phone.setAlignment(Qt.AlignCenter)
        self.col_layout.addWidget(self.phone)

        self.grd_container = QWidget(self.container)
        self.grid_layout = QGridLayout(self.grd_container)
        self.grd_container.setLayout(self.grid_layout)

        self.btn_9 = QPushButton('9', self.container)
        self.btn_8 = QPushButton('8', self.container)
        self.btn_7 = QPushButton('7', self.container)
        self.btn_6 = QPushButton('6', self.container)
        self.btn_5 = QPushButton('5', self.container)
        self.btn_4 = QPushButton('4', self.container)
        self.btn_3 = QPushButton('3', self.container)
        self.btn_2 = QPushButton('2', self.container)
        self.btn_1 = QPushButton('1', self.container)
        self.btn_0 = QPushButton('0', self.container)

        self.btn_9.clicked.connect(self.get_btn_click_handler(self.btn_9))
        self.btn_8.clicked.connect(self.get_btn_click_handler(self.btn_8))
        self.btn_7.clicked.connect(self.get_btn_click_handler(self.btn_7))
        self.btn_6.clicked.connect(self.get_btn_click_handler(self.btn_6))
        self.btn_5.clicked.connect(self.get_btn_click_handler(self.btn_5))
        self.btn_4.clicked.connect(self.get_btn_click_handler(self.btn_4))
        self.btn_3.clicked.connect(self.get_btn_click_handler(self.btn_3))
        self.btn_2.clicked.connect(self.get_btn_click_handler(self.btn_2))
        self.btn_1.clicked.connect(self.get_btn_click_handler(self.btn_1))
        self.btn_0.clicked.connect(self.get_btn_click_handler(self.btn_0))

        self.grid_layout.addWidget(self.btn_9, 0, 2)
        self.grid_layout.addWidget(self.btn_8, 0, 1)
        self.grid_layout.addWidget(self.btn_7, 0, 0)
        self.grid_layout.addWidget(self.btn_6, 1, 2)
        self.grid_layout.addWidget(self.btn_5, 1, 1)
        self.grid_layout.addWidget(self.btn_4, 1, 0)
        self.grid_layout.addWidget(self.btn_3, 2, 2)
        self.grid_layout.addWidget(self.btn_2, 2, 1)
        self.grid_layout.addWidget(self.btn_1, 2, 0)
        self.grid_layout.addWidget(self.btn_0, 3, 1)

        self.col_layout.addWidget(self.grd_container)

    def get_btn_click_handler(self, button: QPushButton):
        def btn_click_handler():
            self.phone.setText(
                self.phone.text() + button.text()
            )

        return btn_click_handler


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = GridApp()
    ui.show()
    sys.exit(app.exec())
