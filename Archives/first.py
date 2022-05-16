

class FramesNavegationBar():
    def execute_navegation_bar(self):
        self.navegation_menu()
        self.label_navegation_menu()
        self.buttons_navegation_menu()

        self.main_frame()

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
                    background-image: url(../Images/navegation_bar/logo_black.png);
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
        self.shipping_menu.show()

        self.packages_menu = QPushButton('Meus pacotes', self.menu_bar)
        self.packages_menu.setMinimumSize(170, 30)
        self.packages_menu.setMaximumSize(170, 30)
        self.packages_menu.installEventFilter(self)
        self.packages_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.packages_menu)
        self.packages_menu.show()

        self.screening_menu = QPushButton('Rastrar', self.menu_bar)
        self.screening_menu.setMinimumSize(100, 30)
        self.screening_menu.setMaximumSize(100, 30)
        self.screening_menu.installEventFilter(self)
        self.screening_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.screening_menu)
        self.screening_menu.show()

        self.options_menu = QPushButton('Opções', self.menu_bar)
        self.options_menu.setMinimumSize(100 ,30)
        self.options_menu.setMaximumSize(100, 30)
        self.options_menu.installEventFilter(self)
        self.options_menu.setStyleSheet(self.style_button_bar)
        self.layout_menu_navegation.addWidget(self.options_menu)
        self.options_menu.show()

        self.spacer_buttons = QSpacerItem(50, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        self.layout_menu_navegation.addItem(self.spacer_buttons)

        # self.shipping_frame()
        # self.frame_shipping.hide()

    def eventFilter(self, source, event):
        if source == self.shipping_menu and event.type() == QEvent.Type.HoverMove:
            print('ok')
        elif source == self.packages_menu and event.type() == QEvent.Type.HoverMove:
            print('ok2')
        elif source == self.screening_menu and event.type() == QEvent.Type.HoverMove:
            print('ok3')
        elif source == self.options_menu and event.type() == QEvent.Type.HoverMove:
            print('ok4')

        return super().eventFilter(source, event)

    def shipping_frame(self):
        self.frame_shipping = QFrame(self.first_window)
        self.frame_shipping.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_shipping.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_shipping.setStyleSheet(
            '''
                QFrame{
                    background-color: #808080;
                }
            '''
        )
        self.layout.addWidget(self.frame_shipping, 1, 0)

    def main_frame(self):
        self.frame = QFrame(self.first_window)
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.frame, 2, 0)
        self.frame.show()

        self.grid_layout_login = QGridLayout()
        self.frame.setLayout(self.grid_layout_login)


class Window(QMainWindow, FramesNavegationBar):
    def __init__(self):
        super(Window, self).__init__()
        self.definitions_window()


    def definitions_window(self):
        self.resize(1080, 720)
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
        

# if __name__ == '__main__':
#     mainwindow = QApplication(sys.argv)
#     window = Window()
#     window.show()
#     sys.exit(mainwindow.exec_())
