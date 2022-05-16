from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from initial_frames import FrameHome


class Window(QMainWindow, FrameHome):
    def __init__(self):
        super(Window, self).__init__()
        self.definitions_window()
        self.execute_home()

    def eventFilter(self, source, event):
        if source == self.shipping_menu and event.type() == QEvent.Type.HoverMove:
            self.frame_packeges.hide()
            self.frame_screening.hide()
            self.frame_options.hide()
            self.frame_shipping.show()
        elif source == self.packages_menu and event.type() == QEvent.Type.HoverMove:
            self.frame_packeges.hide()
            self.frame_screening.hide()
            self.frame_shipping.hide()
            self.frame_packeges.show()
        elif source == self.screening_menu and event.type() == QEvent.Type.HoverMove:
            self.frame_shipping.hide()
            self.frame_packeges.hide()
            self.frame_options.hide()
            self.frame_screening.show()
        elif source == self.options_menu and event.type() == QEvent.Type.HoverMove:
            self.frame_shipping.hide()
            self.frame_packeges.hide()
            self.frame_screening.hide()
            self.frame_options.show()

        return super().eventFilter(source, event)

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
