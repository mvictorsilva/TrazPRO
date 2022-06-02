import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from window import Window


if __name__ == '__main__':
    mainwindow = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(mainwindow.exec_())
