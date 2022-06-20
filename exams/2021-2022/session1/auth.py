import datetime
import os
import string
import sys
from random import choice
import mysql.connector as mysql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

conn = mysql.connect(
    user='worldskills',
    password='worldskills',
    port=3306,
    host='127.0.0.1',
    database='worldskills',
    autocommit=True
)
cur = conn.cursor()
code = ''
time = datetime.datetime.now()

class AuthApp(QMainWindow):
    def __init__(self):
        super(AuthApp, self).__init__()
        self.resize(500, 500)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('image.ico'))

        self.title = QLabel('Телеком Нева Связь', self)
        self.title.resize(500, 25)
        self.title.setStyleSheet("font-size: 25px")

        self.image = QLabel(self)
        self.image.resize(120, 100)
        self.image.setPixmap(QPixmap('Лого ТНС.jpg').scaled(120, 100))
        self.image.move(380, 0)

        QLabel('Номер', self).move(0, 100)
        QLabel('Пароль', self).move(0, 150)
        QLabel('Код', self).move(0, 200)

        self.num_input = QLineEdit(self)
        self.num_input.move(60, 100)

        self.pass_input = QLineEdit(self)
        self.pass_input.setVisible(False)
        self.pass_input.setEchoMode(QLineEdit.Password)
        self.pass_input.move(60, 150)

        self.code_input = QLineEdit(self)
        self.code_input.setVisible(False)
        self.code_input.setEchoMode(QLineEdit.Password)
        self.code_input.move(60, 200)

        self.reset_btn = QPushButton(self)
        self.reset_btn.setVisible(False)
        self.reset_btn.setIcon(QIcon('reset.png'))
        self.reset_btn.move(160, 200)
        self.reset_btn.clicked.connect(self.refresh_click_handler)

        self.cancel_btn = QPushButton('Отмена', self)
        self.cancel_btn.move(0, 250)

        self.enter_btn = QPushButton('Вход', self)
        self.enter_btn.move(100, 250)
        self.enter_btn.setVisible(False)
        self.enter_btn.clicked.connect(self.enter_click_handler)

    def keyPressEvent(self, *args, **kwargs):
        if args[0].key() == 16777220:
            cur.execute(f"SELECT * FROM User WHERE Number = {self.num_input.text()}")
            if resp := cur.fetchone():
                self.pass_input.setVisible(True)
                self.code_input.setVisible(True)
                self.pass_input.setVisible(True)
                self.enter_btn.setVisible(True)
                self.reset_btn.setVisible(True)
            elif resp[2] == self.pass_input.text() and self.code_input.text():
                if datetime.datetime.now() - time > datetime.timedelta(seconds=10):
                    QMessageBox.warning(self, "Ошибка!", 'Срок действия СМС истек!')
                else:
                    if self.code_input.text() == code:
                        QMessageBox.information(self, "Вы вошли в систему!", f"Ваша роль: {resp[3]}")
                    else:
                        QMessageBox.warning(self, "Ошибка!", 'Код не совпадает!')
            else:
                QMessageBox.warning(self, "Ошибка!", 'Такой номер не найден!')

    def enter_click_handler(self):
        cur.execute(f"SELECT * FROM User WHERE Number = {self.num_input.text()}")
        resp = cur.fetchone()

        if resp[2] == self.pass_input.text() and not self.code_input.text():
            global code, time

            code = ''
            time = datetime.datetime.now()

            code += choice(string.digits)
            code += choice(string.digits)
            code += choice(string.ascii_letters)
            code += choice(string.ascii_letters)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)

            print(code)
            QMessageBox.information(self, "СМС", code)
        elif resp[2] == self.pass_input.text() and self.code_input.text():
            if datetime.datetime.now() - time > datetime.timedelta(seconds=10):
                QMessageBox.warning(self, "Ошибка!", 'Срок действия СМС истек!')
            else:
                if self.code_input.text() == code:
                    QMessageBox.information(self, "Вы вошли в систему!", f"Ваша роль: {resp[3]}")
                else:
                    QMessageBox.warning(self, "Ошибка!", 'Код не совпадает!')
        else:
            QMessageBox.warning(self, "Ошибка!", 'Пароль не совпадает!')

    def refresh_click_handler(self):
        cur.execute(f"SELECT * FROM User WHERE Number = {self.num_input.text()}")

        if cur.fetchone()[2] == self.pass_input.text() and self.code_input.text():
            global code, time

            code = ''
            time = datetime.datetime.now()

            code += choice(string.digits)
            code += choice(string.digits)
            code += choice(string.ascii_letters)
            code += choice(string.ascii_letters)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)
            code += choice(string.ascii_uppercase)

            print(code)
            QMessageBox.information(self, "СМС", code)
        else:
            QMessageBox.warning(self, "Ошибка!", 'Пароль не совпадает!')


if __name__ == '__main__':
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)
    ui = AuthApp()
    ui.show()
    sys.exit(app.exec())
