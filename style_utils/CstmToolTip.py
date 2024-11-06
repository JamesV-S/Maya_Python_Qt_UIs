
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

class CustomToolTip(QWidget):
    def __init__(self, text, parent=None):
        super().__init__(parent, Qt.ToolTip)
        self.setWindowFlags(Qt.ToolTip)
        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel(text)
        
        # Set a custom styleSheet here!
        label.setStyleSheet("""
            QLabel {
                background-color: #2a2e32;
                color: #ffffff;
                border: 1px solid #ffffff;
                padding: 4px;
                border-radius: 4px;
            }
        """)
        layout.addWidget(label)
        self.setLayout(layout)

        # Add shadow effect
        shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        shadow.setBlurRadius(10)
        shadow.setColor(QtGui.QColor(0, 0, 0, 160))
        shadow.setOffset(4, 4)
        self.setGraphicsEffect(shadow)