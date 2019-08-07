from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QListWidget, QWidget, QLabel
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QTimer, QDateTime
from PyQt5.QtGui import QPalette, QTextLine, QIcon
import sys, time
from Music import Music
from Home import Home

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
        dim = (height-bar_height)*0.11
        space = (height-bar_height)*0.035
        btnCenter = (width-dim)/2
        
        #space = 0
        #print (width, height)
        #print (dim, space)        

        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, bar_height, width, height-bar_height-dim))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet(r'background-color: #3f4042; border-radius: 10px;')
        #self.widget.setStyleSheet(r'background-color: #515254; border-radius: 10px;')
        #self.widget.setStyleSheet(r'background-color: white; border-radius: 10px;')
        self.widget.setStyleSheet(r'background-color: #71787a; border-radius: 10px;')

        #BARS
        self.bar = QWidget(self)
        self.bar.setGeometry(QRect(0,0, width, bar_height))
        self.bar.setStyleSheet("background-color: black;")

        self.buttonBar = QWidget(self)
        self.buttonBar.setGeometry(QRect(0,height-dim, width, dim))
        self.buttonBar.setStyleSheet("background-color: black;")

        #DATA
        self.date_time = QLabel(self.bar)
        self.date_time.setGeometry(QRect((width-width*0.3)/2, 0,width*0.3, bar_height))
        self.date_time.setAlignment(Qt.AlignCenter)
        self.date_time.setStyleSheet(r'background-color: grey;')
        self.date_time.setStyleSheet("font-size: 32px;")

        self.temperature = QLabel(self.buttonBar)
        self.temperature.setGeometry(QRect((width-dim)/2,0,dim,dim))
        self.temperature.setAlignment(Qt.AlignCenter)
        self.temperature.setStyleSheet(r'background-color: grey;')
        self.temperature.setStyleSheet("font-size: 38px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        
        #BUTTONS
        self.homeBtn = QPushButton(QIcon("src/home-pressed.png"), "", self.buttonBar)
        self.homeBtn.setGeometry(QRect((width-dim)/2-2*dim, 0, dim, dim))
        self.homeBtn.setIconSize(QSize(dim, dim))
        self.homeBtn.setObjectName("home")
        self.homeBtn.setStyleSheet(r'background-color: black; border-radius: 10px;')
        self.homeBtn.clicked.connect(self.onClickHome)

        self.musicBtn = QPushButton(QIcon("src/music.png"), "", self.buttonBar)
        self.musicBtn.setGeometry(QRect((width-dim)/2-dim, 0, dim, dim))
        self.musicBtn.setIconSize(QSize(dim, dim))
        self.musicBtn.setObjectName("music")
        self.musicBtn.setStyleSheet(r'background-color: black; border-radius: 10px;')
        self.musicBtn.clicked.connect(self.onClickMusic)

        #Qui è come se ci fosse la label dei gradi

        self.pushButton_3 = QPushButton(self.buttonBar)
        self.pushButton_3.setGeometry(QRect((width-dim)/2+dim, 0, dim, dim))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setText("")
        self.pushButton_3.setStyleSheet(r'background-color: black; border-radius: 10px;')

        self.settingsBtn = QPushButton(QIcon("src/settings.png"), "", self.buttonBar)
        self.settingsBtn.setGeometry(QRect((width-dim)/2+2*dim, 0, dim, dim))
        self.settingsBtn.setIconSize(QSize(dim, dim))
        self.settingsBtn.setObjectName("settings")
        self.settingsBtn.setStyleSheet(r'background-color: black ;border-radius: 10px;')
        self.settingsBtn.clicked.connect(self.onClickSettings)

        self.home = Home(self.widget)
        self.current = self.home
        self.currentBtn = self.homeBtn
        self.music = None
        self.radio = None

        #Posizionando qui questo comando invece che nel "main" non inserisce i pulsanti della SecondUi
        #self.showFullScreen()

    def updateTime(self):
        current = QDateTime.currentDateTime()
        date = current.date()
        time = current.time()
        self.date_time.setText(date.toString(Qt.ISODate) + " "+ time.toString())
        self.temperature.setText("22"+"°C")
        

    def onClickHome(self):

        self.changeTab()

        self.homeBtn.setIcon(QIcon("src/home-pressed.png"))

        if self.home == None:
            self.home = Home(self.widget)
        else:
            self.home.show()

        self.current = self.home
        self.currentBtn = self.homeBtn

    def onClickMusic(self):
        
        self.changeTab()

        self.musicBtn.setIcon(QIcon("src/music-pressed.png"))

        if self.music == None:
            self.music = Music(self.widget)
        else:
            self.music.show()

        self.current = self.music
        self.currentBtn = self.musicBtn

    def onClickNav(self):
        self.widget.close()
    
    def onClick(self):
        self.widget.close()
    
    def onClickSettings(self):

        self.changeTab()

        self.settingsBtn.setIcon(QIcon("src/settings-pressed.png"))
        """
        if self.settings == None:
            self.settings = Music(self.widget)
        else:
            self.settings.show()

        self.current = self.settings
        """
        self.currentBtn = self.settingsBtn

    def changeTab(self):

        self.current.hide()
        btnIconPath = "src/" + self.currentBtn.objectName() + ".png"
        self.currentBtn.setIcon(QIcon(btnIconPath))        



if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ui = MainWindow()
    
    ui.showFullScreen()
    sys.exit(app.exec_())
    
    
