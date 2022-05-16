import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400, 200)

        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.frame_1 = QFrame()
        self.frame_1.setStyleSheet('background-color: #000000')
        self.frame_1.setMinimumHeight(50)
        self.frame_1.setMaximumHeight(50)
        self.layout.addWidget(self.frame_1, 0, 0)

        self.frame_2 = QFrame()
        self.frame_2.setStyleSheet('background-color: red;')
        self.layout.addWidget(self.frame_2, 1, 0)

        self.frame_3 = QFrame()
        self.frame_3.setStyleSheet('background-color: #f7f7f7;')
        self.layout.addWidget(self.frame_3, 3, 0)

        self.frame_4 = QFrame()
        self.frame_4.setStyleSheet('background-color: blue;')
        self.layout.addWidget(self.frame_4, 2, 0)

        self.frame_5 = QFrame()
        self.frame_5.setStyleSheet('background-color: #808080;')
        self.layout.addWidget(self.frame_5, 2, 0)



        self.texting = QPushButton('Teste', self.frame_1)
        self.texting.setStyleSheet('''
            QPushButton{
                background-color: none;
                border-radius: 2px;
                color: #ffffff;
            }
            QPushButton:hover{
                background-color: #1C1C1C;
                color: #ffffff;
                border-radius: 2px;
                border-bottom: 4px solid blueviolet;
                
            }
        ''')
        self.texting.installEventFilter(self)
        self.texting.setGeometry(30, 0, 100, 50)

        self.texting2 = QPushButton('Teste2', self.frame_1)
        self.texting2.setStyleSheet('''
            QPushButton{
                background-color: none;
                border-radius: 2px;
                color: #ffffff;
            }
            QPushButton:hover{
                background-color: #1C1C1C;
                border-radius: 2px;
                border-bottom: 4px solid blueviolet;
                
            }
        ''')
        self.texting2.installEventFilter(self)
        self.texting2.setGeometry(150, 0, 100, 50)

        self.tex = QPushButton('teste', self.frame_2)
        self.tex.setGeometry(10, 10, 100, 50)
        self.tex.clicked.connect(lambda: self.frame_2.hide())

        self.texting3 = QPushButton('Teste3', self.frame_1)
        self.texting3.setStyleSheet('''
            QPushButton{
                background-color: none;
                border-radius: 2px;
                color: #ffffff;
            }
            QPushButton:hover{
                background-color: #1C1C1C;
                color: #ffffff;
                border-radius: 2px;
                border-bottom: 4px solid blueviolet;
                
            }
        ''')
        self.texting3.installEventFilter(self)
        self.texting3.setGeometry(270, 0, 100, 50)


        self.frame_2.hide()
        self.frame_4.hide()
        self.frame_5.hide()


    def eventFilter(self, source, event):
        if source == self.texting and event.type() == QEvent.Type.HoverMove:
            self.frame_4.hide()
            self.frame_5.hide()
            self.frame_2.show()
        elif source == self.texting2 and event.type() == QEvent.Type.HoverMove:
            self.frame_2.hide()
            self.frame_5.hide()
            self.frame_4.show()
        elif source == self.texting3 and event.type() == QEvent.Type.HoverMove:
            self.frame_4.hide()
            self.frame_2.hide()
            self.frame_5.show()

        return super().eventFilter(source, event)


if __name__ == '__main__':
    app = QApplication(sys.argv) 

    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
