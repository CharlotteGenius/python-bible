#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:35:09 2019

@author: xiangyinyu
"""

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette

app = QApplication([])
app.setStyle('Macintosh')
# styles: 'Fusion', 'Windows', 'WindowsVista' (Windows only) and 'Macintosh' (Mac only

app.setStyleSheet("QPushButton { margin: 5ex; }")

window = QWidget()
layout = QVBoxLayout()
palette = QPalette()
palette.setColor(QPalette.ButtonText, Qt.red)
app.setPalette(palette)

button = QPushButton('Click')
layout.addWidget(button)
window.setLayout(layout)


def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    window.close()
    alert.exec_()
    

button.clicked.connect(on_button_clicked)

window.show()
app.exec_()
