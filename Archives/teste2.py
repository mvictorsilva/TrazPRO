import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QFrame
from PyQt5.QtCore import QRect, QPropertyAnimation, pyqtSignal
from PyQt5 import uic

class MyFrame(QFrame):    
    mouseHover = pyqtSignal(bool)

    def enterEvent(self, event):
        self.mouseHover.emit(True)

    def leaveEvent(self, event):
        self.mouseHover.emit(False)



class Principal(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.frame = MyFrame(self)
        self.frame.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.frame.setGeometry(100, 100, 30, 50)
        self.frame.mouseHover.connect(self.hover_anim)


    def hover_anim(self, hovering):
        anim = QPropertyAnimation(self.frame, b"geometry")
        anim.setDuration(100)
        if hovering:
            anim.setStartValue(QRect(100,100,90,50))
            anim.setEndValue(QRect(100,100,30,50))
        else:
            anim.setStartValue(QRect(100,100,30,50))
            anim.setEndValue(QRect(100,100,30,50))
        anim.start() 



app = QApplication([])
p = Principal()
p.resize(300,300)
p.show()
app.exec_()