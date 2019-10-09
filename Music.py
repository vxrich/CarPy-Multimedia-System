from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QEventLoop, QTimer
from PyQt5.QtGui import QIcon, QPalette
import sys, time, os, alsaaudio, re
from random import randint, sample
from BasicFunc import BasicFunc
from selenium import webdriver

import vlc

class Music(BasicFunc):
    def __init__(self,widget):
        super(Music, self).__init__(widget)

        self.mypath = "/home/vxrich/Documenti/CarPy-Multimedia-System/src/songs/"
        

        self.mixer = alsaaudio.Mixer()

        self.vol = self.mixer.getvolume()

        self.player = None
        self.random_status = 0
        self.playlist = [f for f in os.listdir(self.mypath) if os.path.isfile(os.path.join(self.mypath, f))]
        self.index = 0
        self.indexes = [i for i in range(0, len(self.playlist))]

        self.musicWidget = QWidget(widget)
        self.musicWidget.setGeometry(QRect(widget.width()/4,0, widget.width()/2, widget.height()))
        #self.musicWidget.setStyleSheet("background-color: white;")

        self.list = QListWidget(widget)
        self.list.setGeometry(QRect((self.width-self.btnDim*2.2)/2, self.height*0.04, self.btnDim*2.2, self.btnDim*2.2))
        self.list.setStyleSheet("background-color: white; color: black;")
        for p in self.playlist:
            self.list.addItem(re.sub('\.mp3$', '',p))
        self.list.clicked.connect(self.onClickList)
        
        self.album  = QPushButton(QIcon("src/music/album.png"), "", widget)
        self.album.setGeometry(QRect((self.width-self.btnDim*2.2)/2, self.height*0.04, self.btnDim*2.2, self.btnDim*2.2))
        self.album.setIconSize(QSize(self.btnDim*2.2,self.btnDim*2.2))
        self.album.clicked.connect(self.onClickAlbum)
        #self.album.setStyleSheet("background-color: white;")

        self.songTitle = QLabel(widget)
        self.songTitle.setGeometry(QRect((self.width-self.width*0.5)/2, self.height/2 - self.btnDim*0.3, self.width*0.5, self.btnDim/3))
        self.songTitle.setAlignment(Qt.AlignCenter)
        self.songTitle.setStyleSheet("font-size:" + str(int(self.btnDim/5)) + "px;")

        self.playPause = QPushButton(QIcon("src/music/play-button.png"),"",widget)
        self.playPause.setGeometry(QRect((self.width-self.btnDim)/2, self.height*0.6-self.btnDim/2, self.btnDim, self.btnDim))
        self.playPause.setIconSize(QSize(self.btnDim,self.btnDim))
        self.playPause.setObjectName("play")
        self.play_pause_status = 0
        self.playPause.clicked.connect(self.onClickPlayPause)

        self.next = QPushButton(QIcon("src/music/next.png"),"",widget)
        self.next.setGeometry(QRect((self.width-self.btnDim)/2 + (self.space + self.btnDim), self.height*0.6-self.btnDim/2, self.btnDim, self.btnDim))
        self.next.setIconSize(QSize(self.btnDim*0.7,self.btnDim*0.7))
        self.next.setObjectName("next")
        self.next.clicked.connect(self.onClickNext)

        self.previous = QPushButton(QIcon("src/music/back.png"),"",widget)
        self.previous.setGeometry(QRect((self.width-self.btnDim)/2 - (self.space + self.btnDim), self.height*0.6-self.btnDim/2, self.btnDim, self.btnDim))
        self.previous.setIconSize(QSize(self.btnDim*0.7,self.btnDim*0.7))
        self.previous.setObjectName("previous")
        self.previous.clicked.connect(self.onClickPrevious)
    
        self.random = QPushButton(QIcon("src/music/random.png"),"",widget)
        self.random.setGeometry(QRect((self.width-self.btnDim)/2, self.btnDim +(self.height*0.6-self.btnDim/2), self.btnDim, self.btnDim))
        self.random.setIconSize(QSize(self.btnDim*0.5,self.btnDim*0.5))
        self.random.setObjectName("random")
        self.random.clicked.connect(self.onClickRandom)

        self.volumeUp = QPushButton(QIcon("src/music/plus.png"),"",widget)
        self.volumeUp.setGeometry(QRect((self.width-self.btnDim)/2 + (self.space + self.btnDim), self.btnDim + (self.height*0.6-self.btnDim/2), self.btnDim, self.btnDim))
        self.volumeUp.setIconSize(QSize(self.btnDim*0.6,self.btnDim*0.6))
        self.volumeUp.setObjectName("volume_up")
        self.volumeUp.clicked.connect(self.onClickVolumeUp)

        self.volumeDown = QPushButton(QIcon("src/music/minus.png"),"",widget)
        self.volumeDown.setGeometry(QRect((self.width-self.btnDim)/2 - (self.space + self.btnDim), self.btnDim + (self.height*0.6-self.btnDim/2), self.btnDim, self.btnDim))
        self.volumeDown.setIconSize(QSize(self.btnDim*0.6,self.btnDim*0.6))
        self.volumeDown.setObjectName("volume_down")
        self.volumeDown.clicked.connect(self.onClickVolumeDown)

        """
        self.mute = QPushButton("src/music/mute.png", "", widget)
        self.mute.setGeometry(QRect((self.width-self.btnDim)/2, self.btnDim +(self.height*0.6-self.btnDim/2), self.btnDim, self.btnDim))
        self.mute.setIconSize(QSize(self.btnDim*0.6,self.btnDim*0.6))
        self.mute.setObjectName("mute")
        self.mute.clicked.connect(self.onClickMute)
        """

        self.spotify = QPushButton(QIcon("src/music/spotify.png"),"",widget)
        self.spotify.setGeometry(QRect(self.width*0.2, (self.height*0.75-self.btnDim/2), self.btnDim, self.btnDim))
        self.spotify.setIconSize(QSize(self.btnDim*0.4,self.btnDim*0.4))
        self.spotify.setObjectName("spotify")
        self.spotify.clicked.connect(self.onClickSpotify)

        self.progress = QProgressBar(widget)
        self.progress.setGeometry((self.width-self.width*0.4)/2,self.height/2 + self.btnDim*2.2, self.width*0.40, self.height*0.07)
        self.progress.setStyleSheet("background-color: #1f2021;")
        self.progress.setMaximum(100)
        self.progress.setMinimum(0)
        self.progress.setAlignment(Qt.AlignCenter)

        self.elementList.append(self.musicWidget)
        self.elementList.append(self.list)
        self.elementList.append(self.album)
        self.elementList.append(self.songTitle)
        self.elementList.append(self.playPause)
        self.elementList.append(self.next)
        self.elementList.append(self.previous)
        self.elementList.append(self.random)
        self.elementList.append(self.volumeDown)
        self.elementList.append(self.volumeUp)
        self.elementList.append(self.spotify)
        #self.elementList.append(self.mute)
        #self.elementList.append(self.list)
        #self.elementList.append(self.progress)
        
        self.show()
        self.list.hide()


    def onClickList(self):
        
        song = self.list.currentItem().text()
        self.album.show()
        self.list.hide()

        if self.player == None:

            self.player = vlc.MediaPlayer(self.mypath + song + ".mp3")
            self.songTitle.setText(song)
            self.play_pause_status = 1
            self.playPause.setIcon(QIcon("src/music/pause.png"))
            self.player.play()  

        else:

            self.player.stop()
            self.player = vlc.MediaPlayer(self.mypath + song + ".mp3")
            self.songTitle.setText(song)
            self.play_pause_status = 1
            self.playPause.setIcon(QIcon("src/music/pause.png"))
            self.player.play()        
     

    def onClickPlayPause(self):
    
        if self.player == None:

            if self.random == 1:    
                self.indexes = sample(range(0, len(self.playlist)), len(self.playlist))    
             
            self.player = vlc.MediaPlayer(self.mypath + self.playlist[self.indexes[self.index]])
            self.songTitle.setText(re.sub('\.mp3$', '', self.playlist[self.indexes[self.index]]))
            self.player.play()

        if self.play_pause_status == 0:
            self.play_pause_status = 1
            self.playPause.setIcon(QIcon("src/music/pause.png"))
            self.player.play()        
        else:
            self.play_pause_status = 0
            self.playPause.setIcon(QIcon("src/music/play-button.png"))
            self.player.pause()
        

    def onClickRandom(self):

        if self.random_status == 0:
            self.random_status = 1
            self.random.setIcon(QIcon("src/music/random-pressed.png"))
        else:
            self.random_status = 0
            self.random.setIcon(QIcon("src/music/random.png"))


    def onClickPrevious(self):

        if self.player == None:
            self.player = vlc.MediaPlayer(self.mypath + self.playlist[self.indexes[self.index]])
        
        try:
            self.index -= 1
            self.playlist[self.indexes[self.index]]
        except IndexError:
            self.index = 0

        self.player.stop()
        self.player = vlc.MediaPlayer(self.mypath + self.playlist[self.indexes[self.index]])
        self.songTitle.setText(re.sub('\.mp3$', '', self.playlist[self.indexes[self.index]]))
        self.player.play()


    def onClickNext(self):
    
        if self.player == None:
            self.player = vlc.MediaPlayer(self.mypath + self.playlist[self.indexes[self.index]])

        try:
            self.index += 1
            self.playlist[self.indexes[self.index]]
        except IndexError:
            self.index = 0

        self.player.stop()
        self.player = vlc.MediaPlayer(self.mypath + self.playlist[self.indexes[self.index]])
        self.songTitle.setText(re.sub('\.mp3$', '', self.playlist[self.indexes[self.index]]))
        self.player.play()


    def onClickVolumeDown(self):

        if self.mixer.getmute() == 1:
            self.mixer.setmute(0)

        if self.vol[0] > 0:
            self.vol[0] -= 1
            self.mixer.setvolume(self.vol[0])

        self.progress.setValue(self.vol[0])
        self.progress.show()
        
        loop = QEventLoop()
        QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        
        self.progress.hide()


    def onClickVolumeUp(self):

        if self.mixer.getmute() == 1:
            self.mixer.setmute(0)

        if self.vol[0] < 100:
            self.vol[0] += 1
            self.mixer.setvolume(self.vol[0])

        self.progress.setValue(self.vol[0])
        self.progress.show()
        
        loop = QEventLoop()
        QTimer.singleShot(3000, loop.quit)
        loop.exec_()
        
        self.progress.hide()

    def onClickMute(self):

        if self.mixer.getmute() == 0:
            self.mixer.setmute(1)
        else:
            self.mixer.setmute(0)


    def onClickSpotify(self):

        if self.player == None:
            pass
        else:
            self.player.stop()

        self.spotify.setIcon(QIcon("src/music/spotify-pressed.png"))

        driver = webdriver.Chrome()
        driver.fullscreen_window()
        driver.get('https://open.spotify.com')

        self.spotify.setIcon(QIcon("src/music/spotify.png"))

    def onClickAlbum(self):

        self.list.show()
        self.album.hide()
        
    
