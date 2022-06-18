import sys
import os
from time import sleep
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class ProgressThread(QThread):
    progress = pyqtSignal(int)

    def run(self):
        count = 0

        while count < 100:
            count += 1
            sleep(0.1)
            self.progress.emit(count)


class ProgressApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('Progress')

        self.container = QWidget(self)
        self.setCentralWidget(self.container)

        self.col_layout = QVBoxLayout(self.container)
        self.container.setLayout(self.col_layout)

        self.title = QLabel('Progress bar')
        self.title.resize(self.width(), 25)
        self.title.setStyleSheet("font-size: 20px")
        self.title.setAlignment(Qt.AlignCenter)
        self.col_layout.addWidget(self.title)

        self.progress_bar = QProgressBar(self.container)
        self.progress_bar.setMaximum(100)
        self.col_layout.addWidget(self.progress_bar)

        self.progress_thread = ProgressThread()
        self.progress_thread.progress.connect(lambda val: self.progress_bar.setValue(val))
        self.progress_thread.start()


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = ProgressApp()
    ui.show()
    sys.exit(app.exec())
