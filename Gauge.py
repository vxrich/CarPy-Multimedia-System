from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QRectF, QRect
import sys, random

class Gauge(QWidget):
    
    def __init__(self, widget):
        super(Gauge, self).__init__(widget)
        self.widget = widget

    def paintEvent(self, event):

        qp = QPainter(self.widget)
 
        qp.setPen(QPen(Qt.white, 4)) 
        qp.drawEllipse(QPoint(10,10),10,10)  
        qp.drawRect(QRectF(40,40,100,30))
        qp.end() 

"""
app = QApplication(sys.argv) 
 
window = Gauge() 
window.show() 
 
sys.exit(app.exec_())
"""