from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDesktopWidget, QLabel


class GroupBox(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(QtCore.QRect(20, 20, 900, 700))
        self.setWindowTitle("InvoiceMee - Split Documents")
        layout = QtWidgets.QGridLayout(self)
        groupbox = QtWidgets.QGroupBox("Files to Convert", checkable=False)
        layout.addWidget(groupbox)

        hbox = QtWidgets.QHBoxLayout()
        groupbox.setLayout(hbox)
        label = QLabel()
        pixmap = QPixmap('images.jpg')
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        pathBox = QtWidgets.QLineEdit(self)
        pathBox.setPlaceholderText("Enter the Path Here")
        pathBox.setGeometry(QRect(160, 150, 201, 20))
        selectFileBtn = QtWidgets.QPushButton("Select")
        convertButton = QtWidgets.QPushButton("Convert")
        good_radiobutton = QtWidgets.QRadioButton("Invoices")
        naive_radiobutton = QtWidgets.QRadioButton("Credit Notes")
        hbox.addWidget(pathBox, alignment=QtCore.Qt.AlignCenter)
        hbox.addWidget(selectFileBtn, alignment=QtCore.Qt.AlignCenter)
        hbox.addWidget(convertButton, alignment=QtCore.Qt.AlignCenter)
        hbox.addWidget(good_radiobutton, alignment=QtCore.Qt.AlignCenter)
        hbox.addWidget(naive_radiobutton, alignment=QtCore.Qt.AlignCenter)
        hbox.addWidget(label,alignment=QtCore.Qt.AlignCenter)
        hbox.addStretch()
        self.center()


    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()
        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)
        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())