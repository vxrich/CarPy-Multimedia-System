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

        self.innerWidget = QWidget(widget)
        self.innerWidget.setGeometry(QRect(100,100,400,400))
        self.innerWidget.setStyleSheet("background-color:white;")

        self.gauge = Gauge(widget)

        
        #self.elementList.append(self.gauge)
        self.elementList.append(self.innerWidget)

        self.show()

    