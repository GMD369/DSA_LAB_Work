import sys
from PyQt5.QtWidgets import (QApplication , QMainWindow,QLabel,QWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QPushButton,QCheckBox,QRadioButton,QButtonGroup,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button1=QPushButton("#1")
        self.button2=QPushButton("#2")
        self.button3=QPushButton("#3")
        self.initUI()
     
        
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        hbox=QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)
        central_widget.setLayout(hbox)
        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                           background-color:blue;
                           color:white;

                        }
             QPushButton#button1{
                           background-color:red;}
                   """)   


if __name__=="__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
    
