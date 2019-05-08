#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:35:11 2019

@author: xiangyinyu
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit
from PyQt5.QtWidgets import QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = '-- 测试你是不是沙皮（超准！） --'
        self.left = 10
        self.top = 10
        self.width = 300
        self.height = 100
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.getText()
        self.getInteger()
        self.getChoice()
        self.window()
        self.show()
    
    def getText(self):
        name, okPressed = QInputDialog.getText(self, "输入您的名字","Your name:", QLineEdit.Normal, "")
        if okPressed and name != '':
            print(name)      
        
    def getInteger(self):
        age, okPressed = QInputDialog.getInt(self, "输入您的年龄","Your age:", 28, 0, 100, 1)
        if okPressed:
            print(age)
        
    def getChoice(self):
        colors = ("Red","Blue","Green","Pink","Black","None of above")
        color, okPressed = QInputDialog.getItem(self, "选择一个您喜欢的颜色","Pick a color:", colors, 0, False)
        if okPressed and color:
            print(color)

    def window(self):
        self.label = QLabel('Is Charlotte beautiful?')
        self.button1 = QPushButton("Yes!")
        self.button2 = QPushButton("Definitely yes!")
        self.button3 = QPushButton("If you dare to choose No.")
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)
        self.setLayout(self.layout)

        self.button1.clicked.connect(self.result2)
        self.button2.clicked.connect(self.result2)
        self.button3.clicked.connect(self.result1)
        
    @pyqtSlot()
    def result1(self):
        alert = QMessageBox()
        alert.setText('你的沙皮指数10000%! 还真是完全的大沙皮呢~')
        alert.exec_()
    
    @pyqtSlot()
    def result2(self):
        alert = QMessageBox()
        alert.setText('你的沙皮指数0%! 完全是宇宙大智慧！')
        alert.exec_()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

