import sys
import os
from PyQt5.QtWidgets import *


class LayoutsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)

        self.setWindowTitle('Layouts')

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.col_layout = QVBoxLayout(self.container)
        self.container.setLayout(self.col_layout)

        self.title = QLabel('Choose your favorite sport', self.container)
        self.title.resize(self.width(), 25)
        self.title.setStyleSheet("font-size: 20px")
        self.col_layout.addWidget(self.title)

        self.btn_row_container = QWidget(self.container)
        self.btn_row_layout = QHBoxLayout(self.container)
        self.btn_row_container.setLayout(self.btn_row_layout)

        self.football_btn = QPushButton('Football', self.container)
        self.football_btn.clicked.connect(self.get_btn_click_handler(self.football_btn))
        self.basketball_btn = QPushButton('Basketball', self.container)
        self.basketball_btn.clicked.connect(self.get_btn_click_handler(self.basketball_btn))
        self.tennis_btn = QPushButton('Tennis', self.container)
        self.tennis_btn.clicked.connect(self.get_btn_click_handler(self.tennis_btn))

        self.btn_row_layout.addWidget(self.football_btn)
        self.btn_row_layout.addWidget(self.basketball_btn)
        self.btn_row_layout.addWidget(self.tennis_btn)

        self.col_layout.addWidget(self.btn_row_container)

    def get_btn_click_handler(self, button: QPushButton):
        def btn_click_handler():
            answer = QMessageBox.question(self, 'Commit your choice!', f'Yor favorite sport is {button.text()}?',
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if answer == QMessageBox.StandardButton.Yes:
                QMessageBox.information(self, 'Success!', 'Your answer has been saved!')

        return btn_click_handler


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = LayoutsApp()
    ui.show()
    sys.exit(app.exec())
