import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title='I choose you! Abra!'
        self.left=100
        self.top=100
        self.width=320
        self.height=200
        self.window()
        
    def window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.label=QLabel('',self)
        self.label.move(100,20)
        self.abra=QLabel(self)
        self.abra.setPixmap(QPixmap('abra.png'))
        self.abra.move(130, 90)
        self.button=QPushButton('Go Abra!',self)
        self.button.move(110,150)
        self.button.clicked.connect(self.on_click)
        self.show()

    def part1(self):
        try:
            self.label.setText('')
            self.abra.setPixmap(QPixmap('abra.png'))
            self.button.setText('Go Abra!')
            self.button.clicked.connect(self.on_click)
        except:
            print('mmm')
  
    def on_click(self):
        try:
            self.label.setText('Abra used Teleport!')
            self.label.adjustSize()
            self.abra.setPixmap(QPixmap(''))
            self.button.setText('Try again!')
            self.button.clicked.connect(self.part1)
        except:
            print('nope')
        
        

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=App()
    sys.exit(app.exec_())
