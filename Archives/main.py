import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class RegisterFrame():
    def execute_register(self):
        self.closed_frames()
        self.menu_frame_register()
        self.main_frame_register()

    def closed_frames(self):
        self.home_menu_frame.close()
        self.body_frame.close()

    def menu_frame_register(self):
        self.register_menu_frame = QFrame(self.first_window)
        self.horizontal_layout = QHBoxLayout(self.register_menu_frame)
        self.register_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.register_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.register_menu_frame.setMinimumSize(1080, 50)
        self.register_menu_frame.setMaximumSize(1920, 50)
        self.register_menu_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #000000;
                }
            '''
        )
        self.layout.addWidget(self.register_menu_frame)
        self.register_menu_frame.show()

    def main_frame_register(self):
        self.register_frame = QFrame(self.first_window)
        self.register_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.register_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.register_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(../Images/login_page/background_login.png);
                    background-position: center center;
                }
            '''
        )
        self.layout.addWidget(self.register_frame)
        self.register_frame.show()

class LoginFrame():
    def execute_login(self):
        self.closed_frames()
        self.menu_frame_login()
        self.menu_label_login()
        self.menu_buttons_login()

        self.main_frame_login()
        self.main_frame_labels()
        self.main_frame_entrys()
        self.main_frame_buttons()

    def closed_frames(self):
        self.home_menu_frame.close()
        self.body_frame.close()

    def menu_frame_login(self):
        self.login_menu_frame = QFrame(self.first_window)
        self.horizontal_layout_login = QHBoxLayout(self.login_menu_frame)
        self.login_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.login_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login_menu_frame.setMinimumSize(1080, 50)
        self.login_menu_frame.setMaximumSize(1920, 50)
        self.login_menu_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #000000;
                }
            '''
        )
        self.layout.addWidget(self.login_menu_frame)
        self.login_menu_frame.show()

    def menu_label_login(self):
        self.logo_black = QLabel(self.login_menu_frame)
        self.logo_black.setMinimumSize(200, 35)
        self.logo_black.setMaximumSize(200, 35)
        self.logo_black.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    background-image: url(../Images/home_page/logo_white.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.horizontal_layout_login.addWidget(self.logo_black)
        self.logo_black.show()

        self.spacer_widgets = QSpacerItem(473, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontal_layout_login.addItem(self.spacer_widgets)

    def menu_buttons_login(self):
        self.information = QPushButton('Sobre', self.login_menu_frame)
        self.information.setMinimumSize(120, 30)
        self.information.setMaximumSize(120, 30)
        self.information.setStyleSheet(
            '''
                QPushButton{
                    background-color: none;
                    border-radius: 6px;
                    color: #ffffff;
                    font: 'Verdana';
                    font-size: 18px;
                }
            '''
        )
        self.horizontal_layout_login.addWidget(self.information)
        self.information.show()
    
        self.spacer_buttons = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontal_layout_login.addItem(self.spacer_buttons)

        self.back_register = QPushButton('Cadastre-se', self.login_menu_frame)
        self.back_register.setMinimumSize(170, 30)
        self.back_register.setMaximumSize(170, 30)
        self.back_register.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    border-radius: 6px;
                    color: #ffffff;
                    font: bold 'Verdana';
                    font-size: 18px;
                }
                QPushButton:hover{
                    background-color: #201D2D;
                }
                QPushButton:pressed{
                    background-color: #4F4F4F;
                }
            '''
        )
        self.horizontal_layout_login.addWidget(self.back_register)
        self.back_register.show()


    def main_frame_login(self):
        self.main_frame = QFrame(self.first_window)
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(../Images/login_page/background_login.png);
                    background-position: center center;
                }
            '''
        )
        self.layout.addWidget(self.main_frame)
        self.main_frame.show()

        self.grid_layout_login = QGridLayout()
        self.main_frame.setLayout(self.grid_layout_login)

    def main_frame_labels(self):
        self.vertical_spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_login.addItem(self.vertical_spacer_item)

        self.question = QLabel('COMO QUER ACESSAR?', self.main_frame)
        self.question.setMinimumSize(360, 50)
        self.question.setMaximumSize(360, 50)
        self.question.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: bold 'Helvetica';
                    font-size: 30px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.question, 0, 0, Qt.AlignCenter)
        self.question.show()

        self.spacer_title = QSpacerItem(10, 50, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_login.addItem(self.spacer_title)

    def main_frame_entrys(self):
        self.email_login = QLineEdit(self.main_frame)
        self.email_login.setMinimumSize(350, 50)
        self.email_login.setMaximumSize(350, 50)
        self.email_login.setPlaceholderText('E-mail')
        self.email_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_login.setMaxLength(100)
        self.email_login.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    color: #CFCFCF;
                    border: 2px solid #CD6600;
                    border-radius: 25px;
                    font: 'Helvetica';
                    font-size: 19px;
                }
                QLineEdit:pressed{
                    color: #ffffff;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.email_login, 1, 0, Qt.AlignCenter)
        self.email_login.show()

        self.password_login = QLineEdit(self.main_frame)
        self.password_login.setMinimumSize(350, 50)
        self.password_login.setMaximumSize(350, 50)
        self.password_login.setPlaceholderText('Senha')
        self.password_login.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_login.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_login.setMaxLength(8)
        self.password_login.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    color: #CFCFCF;
                    border: 2px solid #CD6600;
                    border-radius: 25px;
                    font: 'Helvetica';
                    font-size: 19px;
                }
                QLineEdit:pressed{
                    color: #ffffff;

                }
            '''
        )
        self.grid_layout_login.addWidget(self.password_login, 3, 0, Qt.AlignCenter)
        self.password_login.show()

    def main_frame_buttons(self):
        self.remenber_user = QCheckBox('Lembrar usuário', self.main_frame)
        self.remenber_user.setMinimumSize(300, 40)
        self.remenber_user.setMaximumSize(300, 40)
        self.remenber_user.setChecked(False)
        self.remenber_user.setStyleSheet(
            '''
                QCheckBox{
                    color: #ffffff;
                    font: Helvetica;
                    font-size: 15px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.remenber_user, 4, 0, Qt.AlignCenter)
        self.remenber_user.show()

        self.login = QPushButton('Fazer login', self.remenber_user)
        self.login.setMinimumSize(350, 50)
        self.login.setMaximumSize(350, 50)
        self.login.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    color: #ffffff;
                    border-radius: 25px;
                    font: bold 'Verdana';
                    font-size: 20px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.login, 5, 0, Qt.AlignCenter)
        self.login.show()

        self.forgot_password = QPushButton('Esqueceu a senha?', self.main_frame)
        self.forgot_password.setMinimumSize(300, 40)
        self.forgot_password.setMaximumSize(300, 40)
        self.forgot_password.setStyleSheet(
            '''
                QPushButton{
                    text-align: right;
                    background: none;
                    color: #ffffff;
                    border-radius: 2px;
                    font: Helvetica;
                    font-size: 17px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.forgot_password, 6, 0, Qt.AlignCenter)
        self.forgot_password.show()

        self.spacer_button = QSpacerItem(10, 50, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_login.addItem(self.spacer_button)


        self.login_google = QPushButton('  Conecte-se com o Google', self.main_frame)
        self.login_google.setMinimumSize(350, 50)
        self.login_google.setMaximumSize(350, 50)
        self.login_google.setIcon(QIcon('../Images/login_page/google.png'))
        self.login_google.setStyleSheet(
            '''
                QPushButton{
                    background-color: #ffffff;
                    color: #000000;
                    border-radius: 25px;
                    font: bold 'Verdana';
                    font-size: 20px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.login_google, 7, 0, Qt.AlignHCenter)
        self.login_google.show()

        self.vertical_spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_login.addItem(self.vertical_spacer_item2)

class FrameHome(LoginFrame, RegisterFrame):
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
                    background-color: 	#201D2D;
                }
                QPushButton:pressed{
                    background-color: #4F4F4F;
                }
            '''
        )
        self.horizontal_layout.addWidget(self.register)
        self.register.clicked.connect(self.execute_register)
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
        self.login.clicked.connect(self.execute_login)
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
                    background-color: #201D2D;
                }
                QPushButton:pressed{
                    background-color: #4F4F4F;
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
