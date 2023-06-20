import sys
import pwd
from multiprocessing import shared_memory
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QVBoxLayout,
    QMainWindow,
)
from PyQt5.QtCore import (
    QTimer,
)

import UI.SuperAppExtensionUI as design

from tabulate import tabulate
import psutil


class SuperAppExtension(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.processMem()

    def processMem(self):
        a = shared_memory.SharedMemory(name='test')
        q = a.buf[0]
        a.unlink()
        a.close()

        if q == 1:
            self.showUsers()
        elif q == 2:
            timer = QTimer(self)
            timer.timeout.connect(self.showVirtMem)
            timer.start(1000)
        elif q == 3:
            timer = QTimer(self)
            timer.timeout.connect(self.showCurrentTime)
            timer.start(1000)

    def showUsers(self):
        a = pwd.getpwall()
        s = str(tabulate(a))
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)

        with open('superapp.log', 'a') as f:
            f.write('users: ' + s + '\n')


    def showVirtMem(self):
        s = str(psutil.virtual_memory().percent)
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)

        with open('superapp.log', 'a') as f:
            f.write('virtmem: ' + s + '\n')

    def showCurrentTime(self):
        s = str(datetime.now().time())
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)

        with open('superapp.log', 'a') as f:
            f.write('currenttime: ' + s + '\n')




def main():
    with open('superapp.log', 'a') as f:
        f.write(sys.argv[0] + ' ' + str(datetime.now()) + '\n')

    app = QApplication(sys.argv)
    window = SuperAppExtension()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
