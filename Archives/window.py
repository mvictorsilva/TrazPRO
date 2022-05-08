from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1080, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1080, 720))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMinimumSize(QtCore.QSize(1080, 50))
        self.frame_2.setMaximumSize(QtCore.QSize(1920, 50))
        self.frame_2.setStyleSheet('''
                QFrame{
                        background-color: black;
                }
        ''')
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setMinimumSize(QtCore.QSize(200, 35))
        self.label.setMaximumSize(QtCore.QSize(200, 35))
        self.label.setStyleSheet('''
                QLabel{
                        background-color: none;
                        background-image: url(../Images/home_page/logo_white.png);
                        background-repeat: no-repeat;
                        background-position: center;
                }    
        ''')
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(473, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton_2.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('''
                QPushButton{
                        background-color: #ffffff;
                        border-radius: 4px;
                        color: #000000;
                }
        ''')
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(10, 30, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('''
                QPushButton{
                        background-color: #262D3D;
                        color: #ffffff;
                        border-radius: 4px;
                }
        ''')
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet('''
            QFrame{
                background-image: url(../Images/home_page/background_frame_one.png);
                background-position: center center;
            }
        ''')
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(180, 420, 225, 60))
        self.pushButton_3.setMinimumSize(QtCore.QSize(225, 60))
        self.pushButton_3.setMaximumSize(QtCore.QSize(225, 60))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet('''
                QPushButton{
                        background-color: #262D3D;
                        color: #ffffff;
                        border-radius: 12px;
                }
        ''')
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(100, 270, 500, 90))
        self.label_2.setMinimumSize(QtCore.QSize(500, 90))
        self.label_2.setMaximumSize(QtCore.QSize(500, 90))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('''
                QLabel{
                        background: none;
                        color: white;
                }
        ''')
        self.label_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(100, 140, 700, 100))
        self.label_3.setMinimumSize(QtCore.QSize(700, 100))
        self.label_3.setMaximumSize(QtCore.QSize(700, 100))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('''
            QLabel{
                background: none;
                color: white;
            }       
        ''')
        self.label_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setGeometry(QtCore.QRect(100, 250, 150, 2))
        self.line.setMinimumSize(QtCore.QSize(150, 2))
        self.line.setMaximumSize(QtCore.QSize(150, 2))
        self.line.setStyleSheet("background: none;")
        self.line.setLineWidth(1)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TrazPRO"))
        MainWindow.setWindowIcon(QIcon('../Images/home_page/icon.png'))
        # MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.pushButton_2.setText(_translate("MainWindow", "Cadastre-se"))
        self.pushButton.setText(_translate("MainWindow", "Entrar"))
        self.pushButton_3.setText(_translate("MainWindow", "SAIBA MAIS"))
        self.label_2.setText(_translate("MainWindow", "Faça a cotação das suas encomendas para\n"
                "conferir todas as taxas e\n"
                "prazos de entrega"))
        self.label_3.setText(_translate("MainWindow", "ECONOMIZE TEMPO E DINHEIRO \n"
                "NA GESTÃO DE FRETES"))


if __name__ == "__main__":
    import sys
    import main
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
