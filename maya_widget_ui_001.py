
'''
import maya.cmds as cmds
from maya import OpenMayaUI as omui

# 'PySide' module provides access to the Qt APIs as its submodule, 
# & importing the following:
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

# Behave like a native maya window
# convert maya window pinter to pyside^ QWidget obj
mayaMainWindowPtr = omui.MQtUtil.mainWindow()
mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QWidget)
'''

from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random
import importlib


# Define a class: 

class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)
        self.initUI()
        '''
        # integrate the ui into masya's hiearchy - remain ontop
        self.setParent(mayaMainWindowPtr) 
        # makes it a standalone window
        self.setWindowFlags(Qt.Window)
        '''

        # can resize big or small
        self.resize(300, 150)
        self.setWindowTitle("Jmvs_widget_ui")
        
        '''
        # can't size any smaller
        self.setMinimumWidth(300)
        self.setMinimumHeight(150)
        
        # can't size at all
        self.setFixedWidth(300)
        self.setFixedHeight(150)
        '''

    def initUI(self):   
        version = "001"
        self.setWindowTitle(f"widget_ui_test_{version}")

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир", 
                      "Hello world"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World", 
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

        # Add the styleSheet

    # @QtCore.Slot()
    # the class has a function that randomly chooses an item from the list 
    # 'self.hello'. When the button is clicked, the function is called. 
    def magic(self):
        self.text.setText(random.choice(self.hello))

# Now add a main function to initiate the class 'MyWidget' and show it 

def main():
    # Check if the application already exists 
    app = QtWidgets.QApplication.instance()
    if not app: # If there is no 
        app = QtWidgets.QApplication([])# Use an empty list for maya
    
    ui = MyWidget()
    # widget.resize(300, 150)
    ui.show()
    
    app.exec()
    
    return ui


if __name__ == "__main__":
    # store the widget reference in a variable 
    # ('my_widget') to prevent garbage collection
    my_widget = main()


