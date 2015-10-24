from PyQt4.QtGui import QApplication
from PyQt4.QtGui import QDialog
import threading
import sys

__author__ = 'girish'


import Ui


class MainWindow(QDialog,Ui.Ui_Dialog):

    def __init__(self,application):

        super(MainWindow, self).__init__()
        self.parent= application
        self.setupUi(self)
        self.setWindowTitle("Title Here") # add the title here
        self.closeButton.clicked.connect(lambda : sys.exit(1))







