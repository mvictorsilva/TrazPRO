from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from navegation_menus import FramesNavegationBar


class RegisterFrame():
    def execute_register(self):
        self.closed_frames()
        self.menu_frame_register()
        self.menu_label_register()
        self.menu_buttons_register()

        self.main_frame_register()
        self.frame_register_labels()
        self.frame_register_entrys()
        self.frame_register_buttons()

    def login_register(self):
        self.login_menu_frame.deleteLater()
        self.main_frame.deleteLater()
        self.menu_frame_register()
        self.menu_label_register()
        self.menu_buttons_register()

        self.main_frame_register()
        self.frame_register_labels()
        self.frame_register_entrys()
        self.frame_register_buttons()

    def closed_frames(self):
        self.home_menu_frame.deleteLater()
        self.body_frame.deleteLater()

    def menu_frame_register(self):
        self.register_menu_frame = QFrame(self.first_window)
        self.horizontal_layout_register = QHBoxLayout(self.register_menu_frame)
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

    def menu_label_register(self):
        self.logo = QLabel(self.register_menu_frame)
        self.logo.setMinimumSize(200, 35)
        self.logo.setMaximumSize(200, 35)
        self.logo.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    background-image: url(Images/register_page/logo_white.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.horizontal_layout_register.addWidget(self.logo)
        self.logo.show()

        self.spacer_widgets = QSpacerItem(473, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.horizontal_layout_register.addItem(self.spacer_widgets)

    def menu_buttons_register(self):
        self.information = QPushButton('Sobre', self.register_menu_frame)
        self.information.setMinimumSize(120, 30)
        self.information.setMaximumSize(120, 30)
        self.information.setStyleSheet(
            '''
                QPushButton{
                    background-color: none;
                    border-radius: 6px;
                    color: #ffffff;
                    font: 'Verdana';
                    font-size: 17px;
                }
            '''
        )
        self.horizontal_layout_register.addWidget(self.information)
        self.information.show()
        
        self.spacer_buttons = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.horizontal_layout_register.addItem(self.spacer_buttons)

        self.back_login = QPushButton('Entrar', self.register_menu_frame)
        self.back_login.setMinimumSize(170, 30)
        self.back_login.setMaximumSize(170, 30)
        self.back_login.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    border-radius: 6px;
                    color: #ffffff;
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
        self.horizontal_layout_register.addWidget(self.back_login)
        self.back_login.clicked.connect(self.register_login)
        self.back_login.show()


    def main_frame_register(self):
        self.register_frame = QFrame(self.first_window)
        self.register_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.register_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.register_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(Images/login_page/background_login.png);
                    background-position: center center;
                }
            '''
        )
        self.layout.addWidget(self.register_frame)
        self.register_frame.show()

        self.grid_layout_register = QGridLayout()
        self.register_frame.setLayout(self.grid_layout_register)

    def frame_register_labels(self):
        self.vertical_spacer_item = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_register.addItem(self.vertical_spacer_item, 0, 0)

        self.title = QLabel('PRIMEIRO ACESSO?', self.register_frame)
        self.title.setMinimumSize(300, 50)
        self.title.setMaximumSize(350, 50)
        self.title.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: bold 'Helvetica';
                    font-size: 30px;
                }
            '''
        )
        self.grid_layout_register.addWidget(self.title, 1, 0, Qt.AlignCenter)
        self.title.show()

        self.spacer_title = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_register.addItem(self.spacer_title, 2, 0)

        self.option = QLabel('Ou', self.register_frame)
        self.option.setMaximumSize(350, 50)
        self.option.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: bold 'Helvetica';
                    font-size: 18px;
                }
            '''
        )
        self.grid_layout_register.addWidget(self.option, 9, 0, Qt.AlignCenter)
        self.option.show()

        self.spacer_button = QSpacerItem(10, 30, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_register.addItem(self.spacer_button, 11, 0)

    def frame_register_entrys(self):
        self.name = QLineEdit(self.register_frame)
        self.name.setMinimumSize(350, 50)
        self.name.setMaximumSize(350, 50)
        self.name.setPlaceholderText('Nome')
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name.setMaxLength(100)
        self.name.setStyleSheet(
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
        self.grid_layout_register.addWidget(self.name, 3, 0, Qt.AlignCenter)
        self.name.show()

        self.email_register = QLineEdit(self.register_frame)
        self.email_register.setMinimumSize(350, 50)
        self.email_register.setMaximumSize(350, 50)
        self.email_register.setPlaceholderText('E-mail')
        self.email_register.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_register.setMaxLength(100)
        self.email_register.setStyleSheet(
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
        self.grid_layout_register.addWidget(self.email_register, 4, 0, Qt.AlignCenter)
        self.email_register.show()

        self.password_register = QLineEdit(self.register_frame)
        self.password_register.setMinimumSize(350, 50)
        self.password_register.setMaximumSize(350, 50)
        self.password_register.setPlaceholderText('Senha')
        self.password_register.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.password_register.setMaxLength(8)
        self.password_register.setStyleSheet(
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
        self.grid_layout_register.addWidget(self.password_register, 5, 0, Qt.AlignCenter)
        self.password_register.show()

    def frame_register_buttons(self):
        self.confirm_terms = QCheckBox('Concordo com os termos de uso', self.register_frame)
        self.confirm_terms.setMinimumSize(300, 40)
        self.confirm_terms.setMaximumSize(300, 40)
        self.confirm_terms.setChecked(False)
        self.confirm_terms.setStyleSheet(
            '''
                QCheckBox{
                    color: #ffffff;
                    font: Helvetica;
                    font-size: 15px;
                }
            '''
        )
        self.grid_layout_register.addWidget(self.confirm_terms, 6, 0, Qt.AlignCenter)
        self.confirm_terms.show()

        self.register_user = QPushButton('Cadastar', self.register_frame)
        self.register_user.setMinimumSize(350, 50)
        self.register_user.setMaximumSize(350, 50)
        self.register_user.setStyleSheet(
            '''
                QPushButton{
                    background-color: #CD6600;
                    color: #ffffff;
                    border-radius: 25px;
                    font: bold 'Verdana';
                    font-size: 20px;
                }
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.grid_layout_register.addWidget(self.register_user, 7, 0, Qt.AlignCenter)
        self.register_user.show()

        self.spacer_button = QSpacerItem(10, 30, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_register.addItem(self.spacer_button, 8, 0)

        self.register_google = QPushButton('  Cadastre-se com o Google', self.register_frame)
        self.register_google.setMinimumSize(350, 50)
        self.register_google.setMaximumSize(350, 50)
        self.register_google.setIcon(QIcon('Images/login_page/google.png'))
        self.register_google.setStyleSheet(
            '''
                QPushButton{
                    background-color: #ffffff;
                    color: #000000;
                    border-radius: 25px;
                    font: bold 'Verdana';
                    font-size: 20px;
                }
                QPushButton:hover{
                    background-color: #E6E6FA;
                }
                QPushButton:pressed{
                    background-color: #C1CDCD;
                }
            '''
        )
        self.grid_layout_register.addWidget(self.register_google, 12, 0, Qt.AlignHCenter)
        self.register_google.show()

        self.vertical_spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_register.addItem(self.vertical_spacer_item2, 13, 0)


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

    def register_login(self):
        self.register_menu_frame.deleteLater()
        self.register_frame.deleteLater()
        self.menu_frame_login()
        self.menu_label_login()
        self.menu_buttons_login()

        self.main_frame_login()
        self.main_frame_labels()
        self.main_frame_entrys()
        self.main_frame_buttons()

    def closed_frames(self):
        self.home_menu_frame.deleteLater()
        self.body_frame.deleteLater()

    def menu_frame_login(self):
        self.login_menu_frame = QFrame(self.first_window)
        self.horizontal_layout_login = QHBoxLayout(self.login_menu_frame)
        self.login_menu_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.login_menu_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.login_menu_frame.setMinimumHeight(50)
        self.login_menu_frame.setMaximumHeight(50)
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
        self.logo_white = QLabel(self.login_menu_frame)
        self.logo_white.setMinimumSize(200, 35)
        self.logo_white.setMaximumSize(200, 35)
        self.logo_white.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    background-image: url(Images/login_page/logo_white.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.horizontal_layout_login.addWidget(self.logo_white)
        self.logo_white.show()

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
                    font-size: 17px;
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
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.horizontal_layout_login.addWidget(self.back_register)
        self.back_register.clicked.connect(self.login_register)
        self.back_register.show()


    def main_frame_login(self):
        self.main_frame = QFrame(self.first_window)
        self.main_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.main_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.main_frame.setStyleSheet(
            '''
                QFrame{
                    background-image: url(Images/login_page/background_login.png);
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
        self.grid_layout_login.addItem(self.vertical_spacer_item, 0, 0)

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
        self.grid_layout_login.addWidget(self.question, 1, 0, Qt.AlignCenter)
        self.question.show()

        self.spacer_title = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_login.addItem(self.spacer_title, 2, 0)

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
        self.grid_layout_login.addWidget(self.email_login, 3, 0, Qt.AlignCenter)
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
        self.grid_layout_login.addWidget(self.password_login, 4, 0, Qt.AlignCenter)
        self.password_login.show()

        self.option_login = QLabel('Ou', self.main_frame)
        self.option_login.setMaximumSize(350, 50)
        self.option_login.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #ffffff;
                    font: bold 'Helvetica';
                    font-size: 18px;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.option_login, 9, 0, Qt.AlignCenter)
        self.option_login.show()

        self.spacer_button = QSpacerItem(10, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_login.addItem(self.spacer_button, 10, 0)

    def main_frame_buttons(self):
        self.remenber_user = QCheckBox('Mostrar caracteres', self.main_frame)
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
        self.grid_layout_login.addWidget(self.remenber_user, 5, 0, Qt.AlignCenter)
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
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.login, 6, 0, Qt.AlignCenter)
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
        self.grid_layout_login.addWidget(self.forgot_password, 7, 0, Qt.AlignCenter)
        self.forgot_password.show()

        self.spacer_button = QSpacerItem(10, 15, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.grid_layout_login.addItem(self.spacer_button, 8, 0)


        self.login_google = QPushButton('  Conecte-se com o Google', self.main_frame)
        self.login_google.setMinimumSize(350, 50)
        self.login_google.setMaximumSize(350, 50)
        self.login_google.setIcon(QIcon('Images/login_page/google.png'))
        self.login_google.setStyleSheet(
            '''
                QPushButton{
                    background-color: #ffffff;
                    color: #000000;
                    border-radius: 25px;
                    font: bold 'Verdana';
                    font-size: 20px;
                }
                QPushButton:hover{
                    background-color: #E6E6FA;
                }
                QPushButton:pressed{
                    background-color: #C1CDCD;
                }
            '''
        )
        self.grid_layout_login.addWidget(self.login_google, 11, 0, Qt.AlignHCenter)
        self.login_google.show()

        self.vertical_spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_login.addItem(self.vertical_spacer_item2, 12, 0)


class FrameHome(LoginFrame, RegisterFrame, FramesNavegationBar):
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
                    background-image: url(Images/home_page/logo_white.png);
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
                    background-image: url(Images/home_page/background_frame_one.png);
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
        self.register_home.clicked.connect(self.execute_navegation_bar)
        self.register_home.show()
