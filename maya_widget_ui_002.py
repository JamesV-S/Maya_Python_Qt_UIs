

import maya.cmds as cmds
from maya import OpenMayaUI as omui

# 'PySide' module provides access to the Qt APIs as its submodule, 
# & importing the following:
try:
    from PySide6 import QtCore, QtWidgets, QtGui
    from PySide6.QtCore import Qt
    from PySide6.QtGui import QIcon, QFont
    from PySide6.QtWidgets import (QWidget)
    from shiboken6 import wrapInstance
except ModuleNotFoundError:
    from PySide2 import QtCore, QtWidgets, QtGui
    from PySide2.QtCore import Qt
    from PySide2.QtGui import QIcon, QFont
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
        # self.create_radio_button()
        

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

        self.button_01.clicked.connect(self.magic_func)
        self.button_02.clicked.connect(self.second_btn_func)
        self.button_03.clicked.connect(self.third_btn_func)
    
    def create_radio_button(self):
        self.grp_box = QtWidgets.QGroupBox("GroupBoxTitle_001", self)
        font = QFont("Times New Roman",  12)
        font.setBold(True)
        self.grp_box.setFont(font)
        

        hbox_layout = QtWidgets.QHBoxLayout()
        rad1 = QtWidgets.QRadioButton("Rd_button")
        rad1.setChecked(False)
        hbox_layout.addWidget(rad1)
        self.grp_box.setLayout(hbox_layout)

        vbox = QtWidgets.QHBoxLayout()
        vbox.addWidget(self.grp_box)
        

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
        
        #---------------------------------------------------------------------
        # Group box:
        
        self.grp_box = QtWidgets.QGroupBox("GroupBoxTitle_002", self)
        font = QFont("Times New Roman",  12)
        font.setBold(True)
        self.grp_box.setFont(font)
        #layout = QtWidgets.QVBoxLayout(self)
        #layout.addWidget(self.button_01)
        #layout.addWidget(QtWidgets.QLabel("Inside GroupBox"))
        # group_box.setLayout(layout)
        hbox_layout = QtWidgets.QHBoxLayout()
        rad1 = QtWidgets.QRadioButton("Rd_button")
        rad1.setChecked(False)
        hbox_layout.addWidget(rad1)
        self.grp_box.setLayout(hbox_layout)
        

        # ComboBox
        combo_box = QtWidgets.QComboBox()
        combo_box.addItems(["Uno", "Dos", "Tres"])

        # QHeaderView - (typically used in conjunction with QtableView or 
        # QTreeView). Let's me customise headers. 
        tree_view = QtWidgets.QTreeView()
        header = tree_view.header()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        
        #---------------------------------------------------------------------
        # TreeView
        obj_list = ["clavicle", "shoulder", "elbow", "wrist"]
        pref = "jnt"
        types = ["rig", "skn", "geo"]
        type_1 = "rig"
        type_2 = "skn"
        id = "0"

        model = QtGui.QStandardItemModel()
        ''' WIP - type on different colmns and try get dedicated hierarchy's 
        underthem correctly!

        parent_item = model.invisibleRootItem()
        
        parent_type = []
        for type_index, item_type in enumerate(types):
            # Parent for the type, placed in separate top-level rows
            parent_type.append(QtGui.QStandardItem(item_type))
        print("parent type: ", str(parent_type))
        parent_item.appendRow(parent_type)
        
        
        for type_index, item_type in enumerate(types):
            # Create the nested hierarchy for each type
            previous_item = None
            current_item = []
            for item in obj_list:
                item_name = f"{pref}_{item_type}_{id}_{item}"
                current_item.append(QtGui.QStandardItem(item_name))
                
            parent_item.appendRow(current_item[0])
                #if previous_item is None:
                 #   parent_type.appendRow(current_item)  # First item under the type
                #else:
                #    previous_item.appendRow(current_item) # Child of previous item

                #previous_item = current_item  # Update for the next iteration
        '''

        ''' - placing a list of items into grp's
        parent_item = model.invisibleRootItem()

        # Create the hierarchies for type_1 and type_2
        for type_index, item_type in enumerate([type_1, type_2]):
            parent_type = QtGui.QStandardItem(item_type)
            parent_item.appendRow(parent_type)

            for i, item in enumerate(obj_list):
                item_name = f"{pref}_{type_1}_{id}_{item}"
                item_col = QtGui.QStandardItem(item_name)

                # Append to the correct parent based on type_index
                if type_index == 0:
                    parent_type.appendRow(item_col)
                else:
                    parent_type.appendRow(item_col)
        '''  

        # - Gives 2 different hieracrhy's on same row:
        parent_item = model.invisibleRootItem()
        parent_item = model.invisibleRootItem()

        standard_item_1 = []
        standard_item_2 = []
        for item in obj_list:
            standard_item_1.append(QtGui.QStandardItem(f"{pref}_{type_1}_{id}_{item}"))
            standard_item_2.append(QtGui.QStandardItem(f"{pref}_{type_2}_{id}_{item}"))
        parent_item.appendRow(standard_item_1[0])
        parent_item.appendRow(standard_item_2[0])
        # standard_item_1 = standard_item_1[1:]
        for x in range(len(standard_item_1)-1):
            standard_item_1[x].appendRow(standard_item_1[x+1])
            standard_item_2[x].appendRow(standard_item_2[x+1])

        #standard_item_1.appendRow()
        print(f"qt tree veiw item list: {standard_item_1}") # doesn't priont the string
        
        '''
        item1 = QtGui.QStandardItem("parent_item_1")
        chil_item1 = QtGui.QStandardItem("child_item_1")
        item1.appendRow(chil_item1)
        parent_item.appendRow(item1)
        '''

        tree_view.setModel(model)

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
        
        tree_view.setObjectName("treeView")
        
        # Create lists ot make it easier 
        special_true = [self.button_01, self.button_03]
        special_false = []
        
        for item in special_true:
            item.setProperty("specialButton", True)
        for item in special_false:
            item.setProperty("specialButton", False)
        
        #----------------------------------------------------------------------
        
        # basic vertical layout
        #self.layout = QtWidgets.QVBoxLayout(self)
            
        # basic horizontal layout
        self.layout = QtWidgets.QVBoxLayout(self)

        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button_01)
        #self.layout.addWidget(self.button_02)
        self.layout.addWidget(self.button_03)
        self.layout.addWidget(combo_box)
        self.layout.addWidget(self.grp_box) # tree_view  
        self.layout.addWidget(tree_view)
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
        ''' 
        # Connections:
        
        
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


