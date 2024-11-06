

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

# from PySide6 import QtCore, QtWidgets, QtGui
import sys
import random
import importlib
import os.path

'''
import sys
import importlib

from Maya_Python_Qt_UIs import maya_widget_ui_001
importlib.reload(maya_widget_ui_001)
maya_widget_ui_001.main()
'''
 
def delete_existing_ui(ui_name):
    if cmds.window(ui_name, exists=True):
        cmds.deleteUI(ui_name, window=True)

class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super(MyWidget, self).__init__(*args, **kwargs)
        version = "001"
        delete_existing_ui(f"JmvsWidgetUI{version}")
        self.setObjectName(f"JmvsWidgetUI{version}")
        self.initUI()
        # integrate the ui into masya's hiearchy - remain ontop
        self.setParent(mayaMainWindow) 
        # makes it a standalone window
        self.setWindowFlags(Qt.Window)
        self.setWindowTitle(f"Jmvs_widget_ui_{version}")
        # can resize big or small
        self.resize(300, 150)
        # self.setWindowTitle("Jmvs_widget_ui")
        
        # call the stylesheet
        stylesheet_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                       "CSS", "style_sheet_ui_001.css")
        with open(stylesheet_path, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)
        
        '''
        # can't size any smaller
        self.setMinimumWidth(300)
        self.setMinimumHeight(150)
        
        # can't size at all
        self.setFixedWidth(300)
        self.setFixedHeight(150)
        '''

    def initUI(self):   
        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир", 
                      "Hello world"]        
        # Add the buttons
        self.button_01 = QtWidgets.QPushButton("Click me!")
        self.button_02 = QtWidgets.QPushButton("Second Button")
        self.text = QtWidgets.QLabel("Hello World", 
                                     alignment=QtCore.Qt.AlignCenter)        
        self.button_03 = QtWidgets.QPushButton("Third Button")
        self.check_box = QtWidgets.QCheckBox()
        self.combo_box = QtWidgets.QComboBox()
     
        #---------------------------------------------------------------------
        # Applying differtent styles to same type of widget
        '''
        self.button_01.setObjectName("button_01")
        self.button_02.setObjectName("button_02")
        '''
        # OR
        # assign a common class to apply a single style to multiple buttons
        '''
        self.button_01.setProperty("specialButton", True)
        self.button_02.setProperty("specialButton", True)
        self.button_03.setProperty("specialButton", False)
        '''

        # Create lists ot make it easier 
        special_true = [self.button_01, self.button_02]
        special_false = [self.button_03]

        for item in special_true:
            item.setProperty("specialButton", True)
        for item in special_false:
            item.setProperty("specialButton", False)
        
        #----------------------------------------------------------------------
        '''
        # basic vertical layout
        #self.layout = QtWidgets.QVBoxLayout(self)
        
        # basic horizontal layout
        self.layout = QtWidgets.QHBoxLayout(self)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_01)
        self.layout.addWidget(self.button_02)
        '''        
        # grid layout:
        self.grid_layout = QtWidgets.QGridLayout(self)
        # First 2: addWidget(widget, row, column)
        # Optional 3rd & 4th: addWidget(widget, row, column, rowSpan, columnSpan)

        self.grid_layout.addWidget(self.button_01, 1, 0)
        # first row, first column 
        self.grid_layout.addWidget(self.button_02, 1, 1)
        # first row, second column
        self.grid_layout.addWidget(self.button_03, 1, 2)
        # first row, third column
        
        self.grid_layout.addWidget(self.text, 0, 1, 1, 1)
        # first row, first column, Spans 1 row, span 3 columns 

        self.grid_layout.addWidget(self.check_box, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.combo_box, 0, 2, 1, 1)
        
        # Connections:
        self.button_01.clicked.connect(self.magic_func)
        self.button_02.clicked.connect(self.second_btn_func)
        self.button_03.clicked.connect(self.third_btn_func)

    def magic_func(self):
        self.text.setText(random.choice(self.hello))

    def second_btn_func(self):
        print("2nd btn clicked!")

    def third_btn_func(self):
        print("3rd btn clicked!")

# Now add a main function to initiate the class 'MyWidget' and show it 

def main():
    # Check if the application already exists 
    app = QtWidgets.QApplication.instance()
    if not app: # If there is no 
        app = QtWidgets.QApplication([])# Use an empty list for maya
    
    ui = MyWidget()
    ui.show()
    app.exec()
    return ui

# my_widget = main()

if __name__ == '__main__':
    print("RUN IF")
else:
    print("DIDN'T RUN IF")
    # store the widget reference in a variable 
    # ('my_widget') to prevent garbage collection
    #my_widget = main()
    # main()


