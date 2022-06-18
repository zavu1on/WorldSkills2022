import sys
import os
from PyQt5.QtWidgets import *
from layouts import LayoutsApp
from grid import GridApp
from progress import ProgressApp
from image import ImageApp


class MenuApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle('Menu')

        self.navigate_menu = self.menuBar().addMenu('Navigate')
        self.exit_menu = self.menuBar().addMenu('Exit')

        self.layouts_action = QAction('Layouts', self)
        self.layouts_action.triggered.connect(self.open_layouts_app)
        self.navigate_menu.addAction(self.layouts_action)

        self.grid_action = QAction('Grid', self)
        self.grid_action.triggered.connect(self.open_grid_app)
        self.navigate_menu.addAction(self.grid_action)

        self.progress_action = QAction('Progress', self)
        self.progress_action.triggered.connect(self.open_progress_app)
        self.navigate_menu.addAction(self.progress_action)

        self.image_action = QAction('Image', self)
        self.image_action.triggered.connect(self.open_image_app)
        self.navigate_menu.addAction(self.image_action)

        self.close_action = QAction('Close', self)
        self.close_action.triggered.connect(self.close)
        self.exit_menu.addAction(self.close_action)

    def open_layouts_app(self):
        self.app = LayoutsApp()
        self.setCentralWidget(self.app)

    def open_grid_app(self):
        self.app = GridApp()
        self.setCentralWidget(self.app)

    def open_progress_app(self):
        self.app = ProgressApp()
        self.setCentralWidget(self.app)

    def open_image_app(self):
        self.app = ImageApp()
        self.setCentralWidget(self.app)


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = MenuApp()
    ui.show()
    sys.exit(app.exec())
