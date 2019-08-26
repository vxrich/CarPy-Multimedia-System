from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon, QPalette
import sys, time, os, alsaaudio, re
from random import randint, sample
from BasicFunc import BasicFunc

class Note(BasicFunc):
    def __init__(self,widget):
        super(Note, self).__init__(widget)

        self.textbox = QLineEdit(self.widget)
        self.textbox.move(20, 20)
        self.textbox.resize(280,40)

        self.elementList.append(self.textbox)
        
        self.show()