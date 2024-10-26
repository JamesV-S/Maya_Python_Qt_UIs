import sys
import random
import importlib
# 'PySide' module provides access to the Qt APIs as its submodule, 
# & importing the following:
from PySide6 import QtCore, QtWidgets, QtGui

# Define a class: 

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
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

    @QtCore.Slot()
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
    
    widget = MyWidget()
    widget.resize(300, 150)
    widget.show()
    
    app.exec()
    
    return widget


if __name__ == "__main__":
    # store the widget reference in a variable 
    # ('my_widget') to prevent garbage collection
    my_widget = main()


