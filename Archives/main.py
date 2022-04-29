import sys
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.definitions_window()
        self.labels_and_buttons_login()

    def definitions_window(self):
        self.setMinimumSize(1080, 720)
        self.setWindowTitle('TrazPRO')
        self.background = """
            QMainWindow{
                background-color: black;
                background-image: url(C:/Users/Victor/Downloads/testmain.png);
                background-repeat: no-repeat; 
                background-position: center;}
        """

        self.setStyleSheet(self.background)
        
        self.first_window = QWidget(self)
        self.setCentralWidget(self.first_window)
        self.layout = QGridLayout()
        
        self.first_window.setLayout(self.layout)

    def labels_and_buttons_login(self):
        self.menu_frame = QFrame(self)
        self.menu_frame.setStyleSheet('QFrame{background-color: black;}')
        self.menu_frame.setMinimumSize(1080,50)
        self.menu_frame.setMaximumSize(1080, 50)

        self.button = QPushButton('teste', self.first_window)
        self.button.setStyleSheet('QPushButton{background-color: none; color: white; background-color: none;}')
        self.button.setMinimumSize(70, 50)
        self.button.setMaximumSize(70, 50)

        self.label = QLabel('title', self.menu_frame)
        self.label.setPixmap(QPixmap(
        'C:/Users/Victor/Pictures/Imgs_project/logo_white.png'))
        

        self.layout.addWidget(self.menu_frame, 0, 0)
        self.layout.addWidget(self.button, 2, 2)
if __name__ == '__main__':
    mainwindow = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(mainwindow.exec())
