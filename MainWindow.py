from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidget, QWidget, QLabel
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QTimer, QDateTime
from PyQt5.QtGui import QPalette, QTextLine, QIcon
import sys, time
from Music import Music

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("window")
        self.setGeometry(0,0,1920,1080)
        #self.setStyleSheet(r'background-color: #1f2021; color: white;')
        self.setStyleSheet(r'background-color: #3f4042 ; color: white;')
    
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        bar_height = height*0.04
        
        
        #dim = height*0.2
        dim = (height-bar_height)*0.16
        space = (height-bar_height)*0.035
        
        #space = 0
        #print (width, height)
        #print (dim, space)

        self.music = None
        self.radio = None
        

        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(dim+space*2, bar_height, width-dim-space*2, height-bar_height))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet(r'background-color: #3f4042; border-radius: 10px;')
        #self.widget.setStyleSheet(r'background-color: #515254; border-radius: 10px;')
        #self.widget.setStyleSheet(r'background-color: white; border-radius: 10px;')
        #self.widget.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')

        self.bar = QWidget(self)
        self.bar.setGeometry(QRect(0,0, width, bar_height))
        self.bar.setStyleSheet("background-color: black;")

        self.date_time = QLabel(self.bar)
        self.date_time.setGeometry(QRect((width-width*0.3)/2, 0,width*0.3, bar_height))
        self.date_time.setAlignment(Qt.AlignCenter)
        self.date_time.setStyleSheet(r'background-color: grey;')
        self.date_time.setStyleSheet("font-size: 32px;")
        
        self.home = QPushButton(self)
        self.home.setGeometry(QRect(space, bar_height+space, dim, dim))
        self.home.setObjectName("home")
        self.home.setText("Home")
        self.home.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')
        self.home.clicked.connect(self.onClickHome)

        self.musicBtn = QPushButton(self)
        self.musicBtn.setGeometry(QRect(space, bar_height+space*2+dim, dim, dim))
        self.musicBtn.setObjectName("music")
        self.musicBtn.setText("Music")
        self.musicBtn.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')
        self.musicBtn.clicked.connect(self.onClickMusic)

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setGeometry(QRect(space, bar_height+space*3+dim*2, dim, dim))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("")
        self.pushButton_3.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')

        self.pushButton_4 = QPushButton(self)
        self.pushButton_4.setGeometry(QRect(space, bar_height+space*4+dim*3, dim, dim))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setText("")
        self.pushButton_4.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')

        self.settings = QPushButton(self)
        self.settings.setGeometry(QRect(space, bar_height+space*5+dim*4, dim, dim))
        self.settings.setObjectName("settings")
        self.settings.setText("")
        self.settings.setStyleSheet(r'background-color: #71787a;border-radius: 10px;')

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        #Posizionando qui questo comando invece che nel "main" non inserisce i pulsanti della SecondUi
        #self.showFullScreen()

    def updateTime(self):
        current = QDateTime.currentDateTime()
        date = current.date()
        time = current.time()
        self.date_time.setText(date.toString(Qt.ISODate) + " "+ time.toString())
        

    def onClickHome(self):
        self.music.delete()

    def onClickMusic(self):
        if self.music == None:
            self.music = Music(self.widget)
        else:
            self.music.show()


    def onClickNav(self):
        self.widget.close()
    
    def onClick(self):
        self.widget.close()
    
    def onClickSettings(self):
        self.widget.close()
        


if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ui = MainWindow()
    
    ui.showFullScreen()
    sys.exit(app.exec_())
    
    
