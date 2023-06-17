import sys
import os
from multiprocessing import shared_memory, freeze_support
import subprocess
import re

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QVBoxLayout,
    QMainWindow,
)

import UI.SuperAppUI as design


class SuperApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def showAbout(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("About")
        dlg.resize(200, 100)
        message = QLabel("Операционные системы и оболочки\n\nPython 3.10\n\nName\nGroup")
        layout = QVBoxLayout()
        layout.addWidget(message)
        dlg.setLayout(layout)
        dlg.exec()

    def showUsersList(self):
        a = shared_memory.SharedMemory(name='test', create=True, size=1)
        a.buf[0] = 1
        a.close()

        os.system("xterm -e './SuperAppExtension' &")

    def showVirtMem(self):
        a = shared_memory.SharedMemory(name='test', create=True, size=1)
        a.buf[0] = 2
        a.close()
        
        os.system("xterm -e './SuperAppExtension' &")

    def showCurrentTime(self):
        a = shared_memory.SharedMemory(name='test', create=True, size=1)
        a.buf[0] = 3
        a.close()
        
        os.system("xterm -e './SuperAppExtension' &")

    def termInput(self):
        sIn = self.lineEdit_termIn.text()
        self.lineEdit_termIn.clear()

        self.textEdit_termOut.insertPlainText('> ' + sIn + '\n')

        try:
            p = subprocess.Popen(re.split(r'\s+', sIn), stdout=subprocess.PIPE)
            sOut = p.stdout.read().decode('utf-8')

        except OSError:
            sOut = 'Invalid command'

        
        self.textEdit_termOut.insertPlainText(sOut+'\n\n')


def main():
    freeze_support()
    app = QApplication(sys.argv)
    window = SuperApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
