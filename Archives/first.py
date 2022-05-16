import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from requests import delete

class FrameHome():
    def execute_home(self):
        self.menu_frame_home()
        self.menu_label_home()
        self.menu_buttons_home()
        self.informations_frame()
        self.information_labels_home()
        self.information_buttons_home()

    def menu_frame_home(self):
        self.home_menu_frame = QFrame(self.first_window)
        self.horizontal_layout = QHBoxLayout(self.home_menu_frame)
        self.home_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.home_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.home_menu_frame.setMinimumSize(1080, 50)
        self.home_menu_frame.setMaximumSize(1920, 50)
        self.home_menu_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #000000;
                }
            '''
        )
        self.layout.addWidget(self.home_menu_frame)
        self.home_menu_frame.show()

    def menu_label_home(self):
        self.logo_white = QLabel(self.home_menu_frame)
        self.logo_white.setMinimumSize(200, 35)
        self.logo_white.setMaximumSize(200, 35)
        self.logo_white.setStyleSheet(
            '''
                QLabel{
                    background-color: none;
                    background-image: url(../Images/home_page/logo_white.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }    
            '''
        )
        self.horizontal_layout.addWidget(self.logo_white)
        self.logo_white.show()

        self.spacer_widgets = QSpacerItem(473, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontal_layout.addItem(self.spacer_widgets)

    def menu_buttons_home(self):
        self.register = QPushButton('Cadastre-se', self.home_menu_frame)
        self.register.setMinimumSize(170, 30)
        self.register.setMaximumSize(170, 30)
        self.register.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    color: #ffffff;
                    border-radius: 6px;
                    font: bold 'Verdana';
                    font-size: 18px;
                }
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.horizontal_layout.addWidget(self.register)
        self.register.show()

        self.spacer_buttons = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontal_layout.addItem(self.spacer_buttons)

        self.login = QPushButton('Entrar', self.home_menu_frame)
        self.login.setMinimumSize(150, 30)
        self.login.setMaximumSize(150, 30)
        self.login.setStyleSheet(
            '''
                QPushButton{
                    background-color: #ffffff;
                    color: #000000;
                    border-radius: 6px;
                    font: bold 'Verdana';
                    font-size: 18px;
                }
                QPushButton:hover{
                    background-color: #E6E6FA;
                }
                QPushButton:pressed{
                    background-color: #C1CDCD;
                }
            '''
        )
        self.horizontal_layout.addWidget(self.login)
        self.login.show()


    def informations_frame(self):
        self.body_frame = QFrame(self.first_window)
        self.body_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.body_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(../Images/home_page/background_frame_one.png);
                    background-position: center center;
                }
            '''
        )
        self.layout.addWidget(self.body_frame)
        self.body_frame.show()

        self.line = QFrame(self.body_frame)
        self.line.setGeometry(100, 250, 150, 2)
        self.line.setMinimumSize(150, 2)
        self.line.setMaximumSize(150, 2)
        self.line.setStyleSheet('background: none;')
        self.line.setLineWidth(1)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.show()

    def information_labels_home(self):
        self.title_text = QLabel('ECONOMIZE TEMPO E DINHEIRO\nCOM GESTÃO DE FRETES', self.body_frame)
        self.title_text.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: bold 'Helvetica';
                    font-size: 35px;
                }
            '''
        )
        self.title_text.setGeometry(100, 140, 700, 100)
        self.title_text.show()

        self.apresentation_text = QLabel( 
            'Faça a cotação das suas encomendas para\nconferir todas as taxas e\nprazos de entrega',
            self.body_frame)
        self.apresentation_text.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: 'Helvetica';
                    font-size: 25px;
                }
            '''
        )
        self.apresentation_text.setGeometry(100, 270, 500, 90)
        self.apresentation_text.show()

    def information_buttons_home(self):
        self.register_home = QPushButton('SAIBA MAIS', self.body_frame)
        self.register_home.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    color: #ffffff;
                    border-radius: 12px;
                    font: bold 'Verdana';
                    font-size: 19px;
                }
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.register_home.setGeometry(180, 420, 225, 60)
        self.register_home.show()
        
        

class Window(QMainWindow, FrameHome):
    def __init__(self):
        super(Window, self).__init__()
        self.definitions_window()
        self.execute_home()

    def definitions_window(self):
        self.setMinimumSize(1080, 720)
        self.setWindowTitle('TrazPRO')
        self.setWindowIcon(QIcon('../Images/home_page/icon.png'))
        self.setStyleSheet(
            '''
                QMainWindow{
                    background-color: black;
                }
            '''
        )
        
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
