from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from FrontEnd.main_frames import Quotation, Deadline, Order, Localization, User, Employee, Settings


class FramesNavegationBar(Quotation, Deadline, Order, Localization, User, Employee, Settings):
    def execute_navegation_bar(self):
        self.home_menu_frame.deleteLater()
        self.body_frame.deleteLater()
        self.navegation_menu()
        self.label_navegation_menu()
        self.buttons_navegation_menu()

        self.sub_frames_navegation_menu()
        self.buttons_frames_navegation()
        self.frame_quotation()

    def navegation_menu(self):
        self.menu_bar = QFrame(self.first_window)
        self.layout_menu_navegation = QHBoxLayout(self.menu_bar)
        self.menu_bar.setFrameShape(QFrame.Shape.NoFrame)
        self.menu_bar.setFrameShadow(QFrame.Shadow.Raised)
        self.menu_bar.setMinimumHeight(50)
        self.menu_bar.setMaximumHeight(50)
        self.menu_bar.setStyleSheet('''
            QFrame{
                background-color: #CD6600;
            }
        ''')
        self.layout.addWidget(self.menu_bar, 0, 0)
        self.menu_bar.show()
    
    def label_navegation_menu(self):
        self.logo_black = QLabel(self.menu_bar)
        self.logo_black.setMinimumSize(150, 35)
        self.logo_black.setMaximumSize(150, 35)
        self.logo_black.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    background-image: url(Images/navegation_bar/logo_black.png);
                    background-repeat: no-repeat;
                    background-position: center;
                }
            '''
        )
        self.layout_menu_navegation.addWidget(self.logo_black)
        self.logo_black.show()

        self.spacer_widgets = QSpacerItem(350, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.layout_menu_navegation.addItem(self.spacer_widgets)

    def buttons_navegation_menu(self):

        self.futur_button_bar = '''
            QPushButton{
                background-color: none;
                border-radius: 15px;
                color: #ffffff;
                font: bold 'Helvetica';
                font-size: 17px;
            }
            QPushButton:hover{
                background-color: rgba(255, 255, 255, 0.2);
            }
        '''

        self.style_button_bar = '''
            QPushButton{
                background-color: none;
                border-radius: 15px;
                color: #ffffff;
                font: bold 'Helvetica';
                font-size: 17px;
            }
            QPushButton:hover{
                background-color: #ffffff;
                color: #CD6600
            }
        '''

        self.shipping_menu = QPushButton('Envio', self.menu_bar)
        self.shipping_menu.setMinimumSize(100, 30)
        self.shipping_menu.setMaximumSize(100, 30)
        self.shipping_menu.installEventFilter(self)
        self.shipping_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.shipping_menu)

        self.packages_menu = QPushButton('Meus pacotes', self.menu_bar)
        self.packages_menu.setMinimumSize(170, 30)
        self.packages_menu.setMaximumSize(170, 30)
        self.packages_menu.installEventFilter(self)
        self.packages_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.packages_menu)

        self.screening_menu = QPushButton('Rastrear', self.menu_bar)
        self.screening_menu.setMinimumSize(100, 30)
        self.screening_menu.setMaximumSize(100, 30)
        self.screening_menu.installEventFilter(self)
        self.screening_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.screening_menu)

        self.options_menu = QPushButton('Opções', self.menu_bar)
        self.options_menu.setMinimumSize(100 ,30)
        self.options_menu.setMaximumSize(100, 30)
        self.options_menu.installEventFilter(self)
        self.options_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.options_menu)

        self.spacer_buttons = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.layout_menu_navegation.addItem(self.spacer_buttons)

    def sub_frames_navegation_menu(self):
        self.frame_shipping = QFrame(self.first_window)
        self.layout_shipping = QHBoxLayout(self.frame_shipping)
        self.frame_shipping.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_shipping.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_shipping.setMinimumHeight(100)
        self.frame_shipping.setMaximumHeight(100)
        self.frame_shipping.setStyleSheet(
            '''
                QFrame{
                    background-color: 	#F7F7F7;
                }
            '''
        )
        self.layout.addWidget(self.frame_shipping, 1, 0)
        self.frame_shipping.hide()

        self.frame_packeges = QFrame(self.first_window)
        self.layout_packeges = QHBoxLayout(self.frame_packeges)
        self.frame_packeges.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_packeges.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_packeges.setMinimumHeight(100)
        self.frame_packeges.setMaximumHeight(100)
        self.frame_packeges.setStyleSheet(
            '''
                QFrame{
                    background-color: #F7F7F7;
                }
            '''
        )
        self.layout.addWidget(self.frame_packeges, 1, 0)
        self.frame_packeges.hide()

        self.frame_screening = QFrame(self.first_window)
        self.layout_screening = QHBoxLayout(self.frame_screening)
        self.frame_screening.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_screening.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_screening.setMinimumHeight(100)
        self.frame_screening.setMaximumHeight(100)
        self.frame_screening.setStyleSheet(
            '''
                QFrame{
                    background-color: #F7F7F7;
                }
            '''
        )
        self.layout.addWidget(self.frame_screening, 1, 0)
        self.frame_screening.hide()

        self.frame_options = QFrame(self.first_window)
        self.layout_options = QHBoxLayout(self.frame_options)
        self.frame_options.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_options.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_options.setMinimumHeight(100)
        self.frame_options.setMaximumHeight(100)
        self.frame_options.setStyleSheet(
            '''
                QFrame{
                    background-color: #F7F7F7;
                }
            '''
        )
        self.layout.addWidget(self.frame_options, 1, 0)
        self.frame_options.hide()

    def buttons_frames_navegation(self):
        self.button_style = '''
            QToolButton{
                background-color: none;
                border-radius: 4px;
                font: Helvetica;
                font-size: 17px;
            }
            QToolButton:hover{
                background-color: rgba(255, 255, 255, 0.5);
            }
        '''

        self.quotation = QToolButton(self.frame_shipping)
        self.quotation.setText('Cotação')
        self.quotation.setMinimumSize(100, 80)
        self.quotation.setMaximumSize(100, 80)
        self.quotation.setIcon(QIcon('Images/navegation_frame/quotation.png'))
        self.quotation.setIconSize(QSize(50, 50))
        self.quotation.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.quotation.setStyleSheet(self.button_style)
        self.quotation.clicked.connect(self.frame_quotation)
        self.layout_shipping.addWidget(self.quotation)
        self.quotation.show()

        self.deadline = QToolButton(self.frame_shipping)
        self.deadline.setText('Prazos de Entrega')
        self.deadline.setMinimumSize(150, 80)
        self.deadline.setMaximumSize(150, 80)
        self.deadline.setIcon(QIcon('Images/navegation_frame/deadline.png'))
        self.deadline.setIconSize(QSize(50, 50))
        self.deadline.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.deadline.setStyleSheet(self.button_style)
        self.deadline.clicked.connect(self.frame_deadline)
        self.layout_shipping.addWidget(self.deadline)
        self.deadline.show()

        self.order = QToolButton(self.frame_packeges)
        self.order.setText('Pedidos salvos')
        self.order.setMinimumSize(120, 80)
        self.order.setMaximumSize(120, 80)
        self.order.setIcon(QIcon('Images/navegation_frame/order.png'))
        self.order.setIconSize(QSize(50, 50))
        self.order.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.order.setStyleSheet(self.button_style)
        self.order.clicked.connect(self.frame_order)
        self.layout_packeges.addWidget(self.order)
        self.order.show()

        self.localization = QToolButton(self.frame_screening)
        self.localization.setText('Rastrear encomenda')
        self.localization.setMinimumSize(170, 80)
        self.localization.setMaximumSize(170, 80)
        self.localization.setIcon(QIcon('Images/navegation_frame/localization.png'))
        self.localization.setIconSize(QSize(50, 50))
        self.localization.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.localization.setStyleSheet(self.button_style)
        self.localization.clicked.connect(self.frame_localization)
        self.layout_screening.addWidget(self.localization)
        self.localization.show()

        self.user = QToolButton(self.frame_options)
        self.user.setText('Conta')
        self.user.setMinimumSize(100, 80)
        self.user.setMaximumSize(100, 80)
        self.user.setIcon(QIcon('Images/navegation_frame/user.png'))
        self.user.setIconSize(QSize(50, 50))
        self.user.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.user.setStyleSheet(self.button_style)
        self.user.clicked.connect(self.frame_user)
        self.layout_options.addWidget(self.user)
        self.user.show()

        self.notification = QToolButton(self.frame_options)
        self.notification.setText('Funcionários')
        self.notification.setMinimumSize(100, 80)
        self.notification.setMaximumSize(100, 80)
        self.notification.setIcon(QIcon('Images/navegation_frame/employee.png'))
        self.notification.setIconSize(QSize(50, 50))
        self.notification.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.notification.setStyleSheet(self.button_style)
        self.notification.clicked.connect(self.frame_employee)
        self.layout_options.addWidget(self.notification)
        self.notification.show()

        self.settings = QToolButton(self.frame_options)
        self.settings.setText('Sistema')
        self.settings.setMinimumSize(100, 80)
        self.settings.setMaximumSize(100, 80)
        self.settings.setIcon(QIcon('Images/navegation_frame/settings.png'))
        self.settings.setIconSize(QSize(50, 50))
        self.settings.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.settings.setStyleSheet(self.button_style)
        self.settings.clicked.connect(self.frame_settings)
        self.layout_options.addWidget(self.settings)
        self.settings.show()
