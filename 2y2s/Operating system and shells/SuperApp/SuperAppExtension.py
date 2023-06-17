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
            self.showVirtMem()
        elif q == 3:
            self.showCurrentTime()

    def showUsers(self):
        a = pwd.getpwall()
        s = str(tabulate(a))
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)

    def showVirtMem(self):
        s = str(psutil.virtual_memory().percent)
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)

    def showCurrentTime(self):
        s = str(datetime.now().time())
        self.textEdit.clear()
        self.textEdit.insertPlainText(s)




def main():
    app = QApplication(sys.argv)
    window = SuperAppExtension()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
