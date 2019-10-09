from PyQt5.QtWidgets import *
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication, Qt, QSize, QEventLoop, QTimer, QDateTime
from PyQt5.QtGui import QIcon, QPalette 
import sys, time, os, alsaaudio, re
from random import randint, sample
from BasicFunc import BasicFunc
from Spreadsheet import Spreadsheet
import httplib2

from config import SHEET, FUEL_COL, COST_COL, TRAVEL_COL

class Note(BasicFunc):
    def __init__(self,widget):
        super(Note, self).__init__(widget)

        self.keyLayout = QGridLayout()
        self.textLayout = QGridLayout()
        
        self.keyboardWidget = QWidget(widget)
        self.keyboardWidget.setGeometry(QRect(self.height*0.05, self.height*0.05, self.width/3, self.height*0.9))
        #self.keyboardWidget.setStyleSheet("background-color: #71787a; color: white;")
        self.keyboardWidget.setLayout(self.keyLayout)
        
        self.textWidget = QWidget(widget)
        self.textWidget.setGeometry(QRect(2*self.height*0.05 + self.width/3, self.height*0.05, 2*self.width/3 - self.height*0.15, self.height*0.9))
        #self.textWidget.setStyleSheet("background-color: #71787a;")
        self.textWidget.setLayout(self.textLayout)
        

        #----------BUTTONS--------------

        self.buttonGroup = QButtonGroup()
        self.buttonGroup.setExclusive(True)

        self.lineGroup = []

        
        btnDim = int(self.keyboardWidget.width()/5)
        btnSize = QSize(btnDim, btnDim)

        btnStyle = "background-color: black; font-size:" + str(int(btnDim*0.5)) + "px;"

        uploadBtnStyle = "background-color: black; font-size:" + str(int(btnDim*0.2)) + "px;"
        uploadGreenBtnStyle = "background-color: #17fc03; color: black; font-size:" + str(int(btnDim*0.2)) + "px;"
        
        self.buttons = [QPushButton(str(i)) for i in range(10)]
        position = [ [i,j] for i in range(3) for j in range(3)]
        position.insert(0,[3,1])

        for i in range(10):
            self.buttons[i].setStyleSheet(btnStyle)
            self.buttons[i].setFixedSize(btnSize)
            self.keyLayout.addWidget(self.buttons[i], (position[i])[0], (position[i])[1])
            self.buttonGroup.addButton(self.buttons[i])

        self.cancel = QPushButton("C", self.keyboardWidget)
        self.cancel.setFixedSize(btnSize)
        self.cancel.setObjectName("cancel")
        self.cancel.setStyleSheet(btnStyle)
        self.keyLayout.addWidget(self.cancel, 3,0)
        self.cancel.clicked.connect(self.onClickCancel)

        self.comma = QPushButton(",", self.keyboardWidget)
        self.comma.setFixedSize(btnSize)
        self.comma.setObjectName("comma")
        self.comma.setStyleSheet(btnStyle)
        self.keyLayout.addWidget(self.comma, 3,2)
        self.buttonGroup.addButton(self.comma)

        self.next = QPushButton(QIcon("src/note/next.png"), "",self.keyboardWidget)
        self.next.setFixedSize(btnSize)
        self.next.setIconSize(btnSize)
        self.next.setObjectName("next")
        self.next.setStyleSheet(btnStyle)
        self.keyLayout.addWidget(self.next,4,2)
        self.buttonGroup.addButton(self.next)

        self.previous = QPushButton(QIcon("src/note/back.png"), "",self.keyboardWidget)
        self.previous.setFixedSize(btnSize)
        self.previous.setIconSize(btnSize)
        self.previous.setObjectName("previous")
        self.previous.setStyleSheet(btnStyle)
        self.keyLayout.addWidget(self.previous,4,0)
        self.buttonGroup.addButton(self.previous)

        self.upload = QPushButton("UPLOAD", self.keyboardWidget)
        self.upload.setFixedSize(btnSize)
        self.upload.setObjectName("upload")
        self.upload.setStyleSheet(uploadBtnStyle)
        self.keyLayout.addWidget(self.upload, 4,1)
        self.upload.clicked.connect(self.onClickUpload)
        
        self.buttonGroup.buttonClicked.connect(self.onClickButton)
        
        #----------TEXTBOX------------

        textWidth = self.textWidget.width()/3
        textHeight = textWidth/4
        fontSize = str(int(textHeight/1.5))

        textStyle = "background-color: black; font-size:" + fontSize + "px;"

        self.date = QDateEdit(self.textWidget)
        self.date.setObjectName("date")
        self.date.setStyleSheet(textStyle)
        self.date.setDate(QDateTime.currentDateTime().date())
        self.textLayout.addWidget(self.date, 0,0)
        #self.lineGroup.append(self.date)

        self.fuel = QLineEdit(self.textWidget)
        self.fuel.setFixedSize(textWidth,textHeight)
        self.fuel.setStyleSheet(textStyle)
        self.textLayout.addWidget(self.fuel, 1,0)
        self.lineGroup.append(self.fuel)

        self.cost = QLineEdit(self.textWidget)
        self.cost.setFixedSize(textWidth,textHeight)
        self.cost.setStyleSheet(textStyle)
        self.textLayout.addWidget(self.cost, 2,0)
        self.lineGroup.append(self.cost)

        self.kilometers = QLineEdit(self.textWidget)
        self.kilometers.setFixedSize(textWidth,textHeight)
        self.kilometers.setStyleSheet(textStyle)
        self.textLayout.addWidget(self.kilometers, 3,0)
        self.lineGroup.append(self.kilometers)

        #----------LABEL-------------

        labelStyle = "color: black; font-size:" +str(int(self.keyboardWidget.width()/12))+ "px;"

        self.dateLabel = QLabel(self.textWidget)
        self.dateLabel.setText("DATE")
        self.dateLabel.setStyleSheet(labelStyle)
        self.textLayout.addWidget(self.dateLabel,0,1)

        self.fuelLabel = QLabel(self.textWidget)
        self.fuelLabel.setText("FUEL")
        self.fuelLabel.setStyleSheet(labelStyle)
        self.textLayout.addWidget(self.fuelLabel, 1,1)

        self.costLabel = QLabel(self.textWidget)
        self.costLabel.setText("COST")
        self.costLabel.setStyleSheet(labelStyle)
        self.textLayout.addWidget(self.costLabel, 2,1)

        self.kilometersLabel = QLabel(self.textWidget)
        self.kilometersLabel.setText("KILOMETERS")
        self.kilometersLabel.setStyleSheet(labelStyle)
        self.textLayout.addWidget(self.kilometersLabel,3,1)



        self.elementList.append(self.keyboardWidget)
        self.elementList.append(self.textWidget)

        self.index = 0
        self.lineGroup[self.index].setFocus()

        self.show()
        
        try:
            self.spreadSheet = Spreadsheet()
        except httplib2.ServerNotFoundError:
            print("errore")  

    def onClickButton(self, btn):

        currentLine = self.lineGroup[self.index]

        if btn.objectName() != "next" and currentLine.objectName() != "date":
            currentLine.setText(currentLine.text() + btn.text())
        else:
            try:
                self.index += 1
                self.lineGroup[self.index].setFocus()
            except IndexError:
                self.index = 0
                self.lineGroup[self.index].setFocus()

        #self.fuel.setText(self.fuel.text() + btn.text())

    def onClickCancel(self):

        if self.lineGroup[self.index].objectName() == "date":
            pass
        else:
            self.lineGroup[self.index].setText("")

    def onClickUpload(self):

        try:
            inizio = time.time()
            self.spreadSheet.setNewRecord(self.date.text(), self.fuel.text(), self.cost.text(), self.kilometers.text())
            fine = time.time()
            print(fine-inizio)
            self.cleanAllText()
            #self.upload.setStyleSheet(uploadGreenBtnStyle)
            #time.sleep(2)
            #self.upload.setStyleSheet(uploadBtnStyle)
        except httplib2.ServerNotFoundError:
            print("errore")            

    def cleanAllText(self):

        for line in self.lineGroup:
            line.setText("")


    def initializeButton(self, i):

        self.button = QPushButton(str())
        self.button.setStyleSheet("background-color: black;")
        self.button.setFixedSize(QSize(int(self.keyboardWidget.width()/4),int(self.keyboardWidget.width()/4)))
        self.gridLayout.addWidget(self.button, x, y)
        self.button.clicked.connect(self.onClickButton)

        return self.button
