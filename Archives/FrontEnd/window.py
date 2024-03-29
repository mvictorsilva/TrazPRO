from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from FrontEnd.initial_frames import FrameHome

class LoadingProcess():
    def Animation(self):
        self.animation = QWidget()
        self.animation.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.animation.setWindowFlags(Qt.FramelessWindowHint)
        self.animation.setAttribute(Qt.WA_TranslucentBackground)

        self.gif = QMovie('Images/home_page/loading.gif')

        self.loading = QLabel(self)
        self.loading.setMovie(self.gif)
        self.loading.setGeometry(330, 250, 200, 200)
        self.loading.setMinimumSize(QSize(300, 250)) 
        self.loading.setMaximumSize(QSize(250, 250)) 
        self.loading.setObjectName("lb1")

        self.animation.show()

    def startAnimation(self): 
        self.Animation()
        self.gif.start() 
  
    def stopAnimation(self):
        self.gif.stop()
        self.animation.close()

class Window(QMainWindow, FrameHome, LoadingProcess):
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

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirmação', 'Tem certeza que deseja fechar a janela?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def definitions_window(self):
        self.setMinimumSize(1080, 720)
        self.setMaximumSize(1080, 720)
        self.setWindowTitle('TrazPRO')
        self.setWindowIcon(QIcon('Images/home_page/icon.png'))
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
