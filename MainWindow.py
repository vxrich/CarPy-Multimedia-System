from PyQt5.QtWidgets import QLineEdit, QMainWindow, QApplication, QPushButton, QListWidget, QWidget, QLabel
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QTimer, QDateTime, QPoint, QRectF
from PyQt5.QtGui import QPalette, QTextLine, QIcon, QPainter, QPen, QColor
import sys, time, os
from Music import Music
from Home import Home
from Note import Note

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("window")
        self.setGeometry(0,0,800, 480)
        self.setGeometry(0,0,1920,1080)
        #self.setStyleSheet(r'background-color: #1f2021; color: white;')
        self.setStyleSheet(r'background-color: #3f4042 ; color: white;')
    
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        bar_height = height*0.04
        
        
        #dim = height*0.2
        dim = (height-bar_height)*0.11
        icon_dim = dim*0.6
        space = (height-bar_height)*0.035
        btnCenter = (width-dim)/2


        self.widget = QWidget(self)
        self.widget.setGeometry(QRect(0, bar_height, width, height-bar_height-dim))
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("background-color: #3f4042; border-radius: 10px;")
        #self.widget.setStyleSheet("background-color: #515254; border-radius: 10px;")
        self.widget.setStyleSheet("background-color: #71787a; border-radius: 10px;")
        self.widget.setStyleSheet("background-color: #697b96; border-radius: 10px;")

        #-----------BARS-----------
        self.bar = QWidget(self)
        self.bar.setGeometry(QRect(0,0, width, bar_height))
        self.bar.setStyleSheet("background-color: black;")

        self.bottomBar = QWidget(self)
        self.bottomBar.setGeometry(QRect(0,height-dim, width, dim))
        self.bottomBar.setStyleSheet("background-color: black;")

        #-----------DATA-----------
        self.date_time = QLabel(self.bar)
        self.date_time.setGeometry(QRect((width-width*0.3)/2, 0,width*0.3, bar_height))
        self.date_time.setAlignment(Qt.AlignCenter)
        #self.date_time.setStyleSheet("font-size: 32px;")
        self.date_time.setStyleSheet('font-size: ' + str(int(bar_height*0.7)) + 'px;')
        

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._updateTime)
        self.timer.start(1000)
        
        #-----------BUTTONS-----------

        self.shutdownBtn = QPushButton(QIcon("src/menu/shutdown.png"), "", self.bottomBar)
        self.shutdownBtn.setGeometry(QRect(0, 0, dim, dim))
        self.shutdownBtn.setIconSize(QSize(icon_dim, icon_dim))
        self.shutdownBtn.setObjectName("shutdown")
        self.shutdownBtn.setStyleSheet("background-color: black; border-radius: 10px;")
        self.shutdownBtn.clicked.connect(self.onClickShutdown)

        self.homeBtn = QPushButton(QIcon("src/menu/home-pressed.png"), "", self.bottomBar)
        self.homeBtn.setGeometry(QRect((width-dim)/2-2*dim, 0, dim, dim))
        self.homeBtn.setIconSize(QSize(icon_dim, icon_dim))
        self.homeBtn.setObjectName("home")
        self.homeBtn.setStyleSheet("background-color: black; border-radius: 10px;")
        self.homeBtn.clicked.connect(self.onClickHome)

        self.musicBtn = QPushButton(QIcon("src/menu/music.png"), "", self.bottomBar)
        self.musicBtn.setGeometry(QRect((width-dim)/2-dim, 0, dim, dim))
        self.musicBtn.setIconSize(QSize(icon_dim, icon_dim))
        self.musicBtn.setObjectName("music")
        self.musicBtn.setStyleSheet("background-color: black; border-radius: 10px;")
        self.musicBtn.clicked.connect(self.onClickMusic)

        self.temperatureBtn = QPushButton(self.bottomBar)
        self.temperatureBtn.setGeometry(QRect((width-dim)/2,0,dim,dim))
        self.temperatureBtn.setObjectName("temperature")
        self.temperatureBtn.setStyleSheet("font-size:" + str(int(dim/3)) + "px;")

        self.noteBtn = QPushButton(QIcon("src/menu/note.png"), "", self.bottomBar)
        self.noteBtn.setGeometry(QRect((width-dim)/2+dim, 0, dim, dim))
        self.noteBtn.setIconSize(QSize(icon_dim,icon_dim))
        self.noteBtn.setObjectName("note")
        self.noteBtn.setStyleSheet("background-color: black; border-radius: 10px;")
        self.noteBtn.clicked.connect(self.onClickNotes)

        self.settingsBtn = QPushButton(QIcon("src/menu/settings.png"), "", self.bottomBar)
        self.settingsBtn.setGeometry(QRect((width-dim)/2+2*dim, 0, dim, dim))
        self.settingsBtn.setIconSize(QSize(icon_dim, icon_dim))
        self.settingsBtn.setObjectName("settings")
        self.settingsBtn.setStyleSheet("background-color: black ;border-radius: 10px;")
        self.settingsBtn.clicked.connect(self.onClickSettings)

        self.home = Home(self.widget)
        self.current = self.home
        self.currentBtn = self.homeBtn
        self.music = None
        self.radio = None
        self.note = None

        #Posizionando qui questo comando invece che nel "main" non inserisce i pulsanti della SecondUi
        #self.showFullScreen()

    def _updateTime(self):

        current = QDateTime.currentDateTime()
        date = current.date()
        time = current.time()
        self.date_time.setText(date.toString(Qt.ISODate) + " "+ time.toString())
        self.temperatureBtn.setText("22"+"°C")
        

    def onClickHome(self):

        self.changeTab()

        self.homeBtn.setIcon(QIcon("src/menu/home-pressed.png"))

        if self.home == None:
            self.home = Home(self.widget)
        else:
            self.home.show()

        self.current = self.home
        self.currentBtn = self.homeBtn

    def onClickMusic(self):
        
        self.changeTab()

        self.musicBtn.setIcon(QIcon("src/menu/music-pressed.png"))

        if self.music == None:
            self.music = Music(self.widget)
        else:
            self.music.show()

        self.current = self.music
        self.currentBtn = self.musicBtn

    def onClickNav(self):
        self.widget.close()
    
    def onClickNotes(self):

        self.changeTab()

        self.noteBtn.setIcon(QIcon("src/menu/note-pressed.png"))
        
        if self.note == None:
            self.note = Note(self.widget)
        else:
            self.note.show()

        self.current = self.note
        
        self.currentBtn = self.noteBtn
    
    def onClickSettings(self):

        self.changeTab()

        self.settingsBtn.setIcon(QIcon("src/menu/settings-pressed.png"))
        """
        if self.settings == None:
            self.settings = Settings(self.widget)
        else:
            self.settings.show()

        self.current = self.settings
        """
        self.currentBtn = self.settingsBtn

    def onClickShutdown(self):

        self.shutdownBtn.setIcon(QIcon("src/menu/shutdown-pressed.png"))

        os.system("shutdown now")

    def changeTab(self):

        self.current.hide()
        btnIconPath = "src/menu/" + self.currentBtn.objectName() + ".png"
        self.currentBtn.setIcon(QIcon(btnIconPath))        



if __name__ == "__main__":
    
    app = QApplication(sys.argv)

    ui = MainWindow()
    
    ui.showFullScreen()
    #ui.show()
    sys.exit(app.exec_())
    
    
