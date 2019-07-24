from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidget, QWidget
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize
from PyQt5.QtGui import QPalette, QTextLine, QIcon
import sys, time

class BasicFunc(object):
    def __init__(self,widget):

        self.widget = widget

        self.elementList = []

        self.width = widget.frameGeometry().width()
        self.height = widget.frameGeometry().height()

        self.btnDim = self.width*0.10
        self.space = self.height*0.05

    def delete(self):
        for element in self.elementList:
            element.hide()

    def show(self):
        for element in self.elementList:
            element.show()