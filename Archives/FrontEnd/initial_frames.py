from hmac import new
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import webbrowser

from FrontEnd.navegation_menus import FramesNavegationBar
from BackEnd.db import DataBase


class RegisterFrame(DataBase):
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
        url = "http://127.0.0.1:5500/Archives/Website/index.html"

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
        self.information.clicked.connect(lambda: webbrowser.open(url, new=new))
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
        def click():
            if (self.confirm_terms.isChecked()):
                self.register_user.setDisabled(False)
            else:
                self.register_user.setEnabled(False)

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
        self.confirm_terms.clicked.connect(click)
        self.confirm_terms.show()

        self.register_user = QPushButton('Cadastrar', self.register_frame)
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
        self.register_user.clicked.connect(self.create_new_user)
        self.register_user.setEnabled(False)
        self.register_user.show()

        # self.register_google = QPushButton('  Cadastre-se com o Google', self.register_frame)
        # self.register_google.setMinimumSize(350, 50)
        # self.register_google.setMaximumSize(350, 50)
        # self.register_google.setIcon(QIcon('Images/login_page/google.png'))
        # self.register_google.setStyleSheet(
        #     '''
        #         QPushButton{
        #             background-color: #ffffff;
        #             color: #000000;
        #             border-radius: 25px;
        #             font: bold 'Verdana';
        #             font-size: 20px;
        #         }
        #         QPushButton:hover{
        #             background-color: #E6E6FA;
        #         }
        #         QPushButton:pressed{
        #             background-color: #C1CDCD;
        #         }
        #     '''
        # )
        # self.grid_layout_register.addWidget(self.register_google, 12, 0, Qt.AlignHCenter)
        # self.register_google.show()

        self.vertical_spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_register.addItem(self.vertical_spacer_item2, 8, 0)

    def confirmation_frame_ii(self):
        self.frame_confirmation_ii = QFrame(self.register_frame)
        self.frame_confirmation_ii.setMaximumSize(QSize(450, 35))
        self.frame_confirmation_ii.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_confirmation_ii.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmation_ii.setFrameShadow(QFrame.Raised)
        self.frame_confirmation_ii.setGeometry(330, 15, 450, 40)
        self.frame_confirmation_ii.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_confirmation_ii)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_confirmation = QLabel('Cadastro concluído', self.frame_confirmation_ii)
        self.label_confirmation.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_confirmation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_confirmation)

        self.pushButton_close_popup = QPushButton(self.frame_confirmation_ii)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_confirmation_ii.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_confirmation_ii.deleteLater)

    def error_frame_ii(self):
        self.frame_error = QFrame(self.register_frame)
        self.frame_error.setMaximumSize(QSize(450, 35))
        self.frame_error.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.frame_error.setGeometry(330, 15, 450, 40)
        self.frame_error.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Dados incorretos', self.frame_error)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_error.deleteLater)


class LoginFrame(DataBase):
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
        url = "http://127.0.0.1:5500/Archives/Website/index.html"

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
        self.information.clicked.connect(lambda: webbrowser.open(url, new=new))
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
        self.password_login.setMaxLength(6)
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

    def main_frame_buttons(self):
        def click():
            if (self.remenber_user.isChecked()):
                self.password_login.setEchoMode(QLineEdit.Normal)
            else:
                self.password_login.setEchoMode(QLineEdit.EchoMode.Password)


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
        self.remenber_user.clicked.connect(click)
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
        self.login.clicked.connect(self.authorized_login_user)
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
        self.forgot_password.clicked.connect(self.update_password)
        self.forgot_password.show()

        self.vertical_spacer_item2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.grid_layout_login.addItem(self.vertical_spacer_item2, 8, 0)

    def update_password(self):
        self.background = QFrame(self.main_frame)
        self.background.setStyleSheet(
            '''
                QFrame{
                    background-color: rgba(255, 255, 255, 0.3);
                }
            '''
        )
        self.background.show()
        self.background.setGeometry(0, 0, 1080, 670)

        self.question = QFrame(self.background)
        self.question.setStyleSheet(
            '''
                QFrame{
                    background-color: #f8f8f8;
                    border: 2px solid #f8f8f8;
                    border-radius: 20px;
                }
            '''
        )
        self.question.show()
        self.question.setGeometry(290, 170, 500, 300)

        self.email_question = QLabel('Digite o seu E-mail:', self.question)
        self.email_question.setStyleSheet('''
            QLabel{
                background: none;
                border: none;
                color: #ffffff;
                font: Helvetica Neue Leve;
                font-size: 25px;
            }
        ''')
        self.email_question.setGeometry(140, 50, 270, 50)
        self.email_question.show()

        self.email_question_get = QLineEdit(self.question)
        self.email_question_get.setPlaceholderText('@gmail.com')
        self.email_question_get.setMaxLength(100)
        self.email_question_get.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.email_question_get.setStyleSheet('''
            QLineEdit{
                background-color: rgba(0, 0, 0, 0);
                color: #707070;
                border: 2px solid #cd6600;
                border-radius: 20px;
                font: 'Helvetica';
                font-size: 18px;
            }
            QLineEdit:pressed{
                color: #ffffff;
            }
        ''')
        self.email_question_get.setGeometry(100, 120, 280, 40)
        self.email_question_get.show()

        self.send_email = QPushButton('Mudar senha', self.question)
        self.send_email.setStyleSheet(
            '''
                QPushButton{
                    background-color: #cd6600;
                    color: #ffffff;
                    border-radius: 14px;
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
        self.send_email.setGeometry(165, 200, 170, 50)
        self.send_email.clicked.connect(self.send_new_password)
        self.send_email.show()

        self.close = QToolButton(self.question)
        self.close.setIcon(QIcon('Images/main_frames/quotation/close.png'))
        self.close.setIconSize(QSize(20, 20))
        self.close.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.close.setStyleSheet(
            '''
                QToolButton{
                    border: none;
                    background-color: none;
                    border-radius: 4px
                }
            '''
        )
        self.close.clicked.connect(lambda: (self.question.deleteLater(),
                                            self.background.deleteLater()))
        self.close.setGeometry(450, 20, 22, 20)
        self.close.show()

    def password_change_notice(self):
        self.frame_alert = QFrame(self.main_frame)
        self.frame_alert.setMaximumSize(QSize(450, 35))
        self.frame_alert.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_alert.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_alert.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_alert.setFrameShape(QFrame.StyledPanel)
        self.frame_alert.setFrameShadow(QFrame.Raised)
        self.frame_alert.setGeometry(330, 15, 450, 40)
        self.frame_alert.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_alert)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Senha alterada! Verifique o seu E-mail', self.frame_alert)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 16px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_alert)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_alert.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(6000, self.frame_alert.deleteLater)

    def confirmation_frame(self):
        self.frame_confirmation = QFrame(self.main_frame)
        self.frame_confirmation.setMaximumSize(QSize(450, 35))
        self.frame_confirmation.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_confirmation.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmation.setFrameShadow(QFrame.Raised)
        self.frame_confirmation.setGeometry(330, 15, 450, 40)
        self.frame_confirmation.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_confirmation)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_confirmation = QLabel('Cadastro concluído', self.frame_confirmation)
        self.label_confirmation.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_confirmation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_confirmation)

        self.pushButton_close_popup = QPushButton(self.frame_confirmation)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_confirmation.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_confirmation.deleteLater)

    def error_frame(self):
        self.frame_error = QFrame(self.main_frame)
        self.frame_error.setMaximumSize(QSize(450, 35))
        self.frame_error.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.frame_error.setGeometry(330, 15, 450, 40)
        self.frame_error.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Dados incorretos', self.frame_error)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_error.deleteLater)


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
        url = "http://127.0.0.1:5500/Archives/Website/index.html"
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
        # self.register_home.clicked.connect(self.execute_navegation_bar)
        self.register_home.clicked.connect(lambda: webbrowser.open(url, new=new))
        self.register_home.show()
