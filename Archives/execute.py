import sys
from PySide2.QtWidgets import *

from FrontEnd.window import Window


if __name__ == '__main__':
    mainwindow = QApplication()
    window = Window()
    window.show()
    sys.exit(mainwindow.exec_())
