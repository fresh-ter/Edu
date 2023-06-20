import sys
import os
from multiprocessing import shared_memory, freeze_support
import subprocess
import re
import shutil
from datetime import datetime

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QLabel,
    QVBoxLayout,
    QMainWindow,
    QFileDialog,
    QMenu,
    QAction,
)
from PyQt5.QtCore import (
    QStringListModel,
    QProcess,
)
from PyQt5.QtGui import (
    QCursor
)

import UI.SuperAppUI as design


class SuperApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.openDirectory('..')

    def showAbout(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("About")
        dlg.resize(200, 100)

        message = QLabel("Операционные системы и оболочки\n\nPython 3.10\n\nName\nGroup")

        layout = QVBoxLayout()
        layout.addWidget(message)

        dlg.setLayout(layout)
        dlg.exec()

    def showHelp(self):
        dlg = QDialog(self)
        dlg.setWindowTitle("About")
        dlg.resize(200, 100)

        s = "Справка\n\n"
        s += 'Вывод информации о пользователях системы: Ctrl+1\n'
        s += 'Вывод информации о занятой виртуальной памяти: Ctrl+2\n'
        s += 'Вывод информации о текущем местном времени: Ctrl+3\n'
        s += 'Запуск Konsole: Ctrl+K\n'
        s += 'Запуск Dolphine: Ctrl+D\n'
        s += 'Запуск системного монитора: Ctrl+M\n'

        message = QLabel(s)

        layout = QVBoxLayout()
        layout.addWidget(message)

        dlg.setLayout(layout)
        dlg.exec()

    def showUsersList(self):
        a = shared_memory.SharedMemory(
            name='test',
            create=True,
            size=1
        )
        a.buf[0] = 1
        a.close()

        os.system("python3 SuperAppExtension.py &")

    def showVirtMem(self):
        a = shared_memory.SharedMemory(
            name='test',
            create=True,
            size=1
        )
        a.buf[0] = 2
        a.close()
        
        os.system("python3 SuperAppExtension.py &")

    def showCurrentTime(self):
        a = shared_memory.SharedMemory(
            name='test',
            create=True,
            size=1
        )
        a.buf[0] = 3
        a.close()
        
        os.system("python3 SuperAppExtension.py &")

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

    def getCurrentDirname(self):
        return self.lineEditCD.text()

    def changeDirectory(self):
        d = QFileDialog.getExistingDirectory(
                self,
                "Open Directory",
                self.getCurrentDirname(),
                QFileDialog.ShowDirsOnly
                | QFileDialog.DontResolveSymlinks
            )

        if d == '':
            return

        self.openDirectory(d)

    def openDirectory(self, dirname):
        self.lineEditCD.clear()
        self.lineEditCD.setText(dirname)

        l = os.listdir(dirname)
                                  
        self.listWidgetLS.clear()
        self.listWidgetLS.addItems(l)

    def getNameFromSelected(self):
        return self.listWidgetLS.currentItem().text()

    def getDataForCurrentItem(self):
        name = self.getNameFromSelected()
        dirname = self.getCurrentDirname()

        address = dirname + '/' + name

        t = ''
        if os.path.isfile(address):
            t = 'f'
        elif os.path.isdir(address):
            t = 'd'

        return t, address

    def actionMoveToTrash(self):
        d = self.getDataForCurrentItem()

        if 'SuperApp/System' in d[1]:
            return

        if d[0] == 'f':
            shutil.move(d[1], '../Trash/')
        elif d[0] == 'd':
            shutil.move(d[1]+'/', '../Trash/')

        self.openDirectory(self.getCurrentDirname())

    def actionDelete(self):
        d = self.getDataForCurrentItem()

        print(2, d)

        if 'SuperApp/System' in d[1]:
            return

        if d[0] == 'f':
            os.remove(d[1])
        elif d[0] == 'd':
            shutil.rmtree(d[1]+'/')

        self.openDirectory(self.getCurrentDirname())

    def customListMenu(self, point):
        action1 = QAction('Move to Trash', self)
        action1.triggered.connect(self.actionMoveToTrash)

        action2 = QAction('Delete', self)
        action2.triggered.connect(self.actionDelete)

        popMenu = QMenu()
        popMenu.addAction(action1)
        popMenu.addAction(action2)
        popMenu.exec_(QCursor.pos())

    def itemDClicked(self):
        print("Click")

    def dolphinRun(self):
        os.system("dolphin &")

    def monitorRun(self):
        os.system("plasma-systemmonitor &")

    def konsoleRun(self):
        os.system("konsole &")


def main():
    with open('superapp.log', 'a') as f:
        f.write(sys.argv[0] + ' ' + str(datetime.now()) + '\n')

    freeze_support()
    app = QApplication(sys.argv)
    window = SuperApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
