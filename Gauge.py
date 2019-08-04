from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QRectF
import sys, random

class Gauge(QWidget):
    
    def __init__(self, widget):
        super(Gauge, self).__init__(widget)
        
        self.widget = widget
    

    def paintEvent(widget, event):

        qp = QPainter(widget)
 
        qp.setPen(QPen(Qt.darkGreen, 4)) 
        qp.drawEllipse(QPoint(10,10),10,10)  
        qp.drawRect(QRectF(10,0,100,30))
        qp.end() 

""" 
app = QApplication(sys.argv) 
 
window = Gauge() 
window.show() 
 
sys.exit(app.exec_())
"""