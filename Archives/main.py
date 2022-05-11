import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class FrameHome():
    def menu_frame_home(self):
        self.home_menu_window = QFrame(self.first_window)
        self.home_menu_window.setMinimumSize(1080, 50)
        self.home_menu_window.setMaximumSize(1920, 1080)
        self.home_menu_window.setStyleSheet('''
            QFrame{
                background-color: #000000;
                border-radius: 12px;
            }
        ''')
        self.layout.addWidget(self.home_menu_window, 0, 0)

    def menu_labels_home(self):
        self.title_text = QLabel('ECONOMIZE TEMPO E DINHEIRO\nCOM GESTÃO DE FRETES', self)
        self.title_text.setStyleSheet('''
            QLabel{
                background: none;
                color: #ffffff;
                font: bold 'Helvetica';
                font-size: 35px;
            }
        ''')
        self.apresentation_text = QLabel( 
            'Faça a cotação das suas encomendas para\nconferir todas as taxas e\nprazos de entrega',
            self)
        self.apresentation_text.setStyleSheet('''
            QLabel{
                background: none;
                color: #ffffff;
                font: 'Helvetica';
                font-size: 25px;
            }
        ''')

    
        self.layout.addWidget(self.title_text, 1, 0)
        self.layout.addWidget(self.apresentation_text, 2, 0)

    def menu_buttons_home(self):
        self.register_home = QPushButton('Cadastre-se', self)
        self.register_home.setStyleSheet('''
            QPushButton{
                background-color: #ffffff;
                color: #000000;
                border-radius: 4px;
                font: bold 'Verdana';
                font-size: 15px;
            }
        ''')

        self.layout.addWidget(self.register_home, 3, 0)


class Window(QMainWindow, FrameHome):
    def __init__(self):
        super(Window, self).__init__()
        self.definitions_window()
        self.menu_frame_home()

    def definitions_window(self):
        self.setMinimumSize(1080, 720)
        self.setWindowTitle('TrazPRO')

        self.setStyleSheet('''
            QMainWindow{
                background-color: black;
                background-image: url(../Images/home_page/background_frame_one.png);
                background-repeat: no-repeat; 
                background-position: center;
            }
        ''')
        
        self.first_window = QWidget(self)
        self.setCentralWidget(self.first_window)
        self.layout = QGridLayout()
        self.first_window.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)


if __name__ == '__main__':
    mainwindow = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(mainwindow.exec_())
