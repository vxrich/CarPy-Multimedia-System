from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QEventLoop, QTimer, QPoint, QRectF
from PyQt5.QtGui import QIcon, QPalette, QPainter, QPen, QColor

import sys, time, os, alsaaudio, re
from random import randint, sample
from BasicFunc import BasicFunc
from Gauge import Gauge

class Home(BasicFunc):
    def __init__(self,widget):
        super(Home, self).__init__(widget)

        self.frame = QFrame(widget)
        self.frame.setStyleSheet("background-color: white;")
        self.frame.setGeometry(QRect(0,0,self.width, self.height))

        self.innerWidget = QWidget(widget)
        self.innerWidget.setGeometry(QRect(100,100,400,400))
        self.innerWidget.setStyleSheet("background-color:red;")

        self.button = QPushButton("ciao", self.widget)
        self.button.setGeometry(QRect(self.btnDim,self.btnDim,self.btnDim,self.btnDim))
        self.button.setStyleSheet("background-color: white; color: black;")

        self.gauge = Gauge(self.frame)

        self.elementList.append(self.button)
        self.elementList.append(self.gauge)
        self.elementList.append(self.innerWidget)
        self.elementList.append(self.frame)

        self.show()