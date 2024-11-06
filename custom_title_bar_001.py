
import maya.cmds as cmds
from maya import OpenMayaUI as omui

try:
    from PySide6 import QtCore, QtWidgets, QtGui
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QIcon
    from PySide6.QtWidgets import (QWidget)
    from shiboken6 import wrapInstance
except ModuleNotFoundError:
    from PySide2 import QtCore, QtWidgets, QtGui
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QIcon
    from PySide2.QtWidgets import (QWidget)
    from shiboken2 import wrapInstance

mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)

import sys
import random
import importlib
import os.path

'''
import sys
import importlib

from Maya_Python_Qt_UIs import custom_title_bar_001
importlib.reload(custom_title_bar_001)
custom_title_bar_001.main()
'''

class custom_bar(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(custom_bar, self).__init__(*args, **kwargs)
        self.initUI()
        self.setParent(mayaMainWindow) 
        #self.setWindowFlags(Qt.Window)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setWindowFlags(Qt.Window | Qt.Tool)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

    def initUI(self):
        # create title bar
        title_bar = QtWidgets.QWidget(self)
        title_bar_layout = QtWidgets.QHBoxLayout(title_bar)

        # add logo 
        logo = QtWidgets.QLabel("Logo", title_bar)
        title_bar_layout.addWidget(logo)

        # add title
        title = QtWidgets.QLabel("Custom title bar", title_bar)
        title_bar_layout.addWidget(title)

        # Add control buttons:
        minimize_button = QtWidgets.QPushButton("-", title_bar)
        maximise_button = QtWidgets.QPushButton("+", title_bar)
        exit_button = QtWidgets.QPushButton("x", title_bar)
        title_bar_layout.addWidget(minimize_button)
        title_bar_layout.addWidget(maximise_button)
        title_bar_layout.addWidget(exit_button)

        # Main layout
        main_layout = QtWidgets.QVBoxLayout(self)
        main_layout.addWidget(title_bar)
        # add other widgets here
        main_layout.addStretch()

        # Connect button signals
        minimize_button.clicked.connect(self.showMinimized)
        maximise_button.clicked.connect(self.toggleMaximize)
        exit_button.clicked.connect(self.close)

    def toggleMaximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.drag_position)
            event.accept()

def main():
    # Check if the application already exists 
    app = QtWidgets.QApplication.instance()
    if not app: # If there is no 
        app = QtWidgets.QApplication([])# Use an empty list for maya
    
    ui = custom_bar()
    ui.show()
    app.exec()
    return ui