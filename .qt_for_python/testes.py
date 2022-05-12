from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from PyQt5.QtWidgets import *


def moveToBottomRight(msgBox):

    msgBox.addButton("重计", QMessageBox.ActionRole)
    msgBox.addButton("停计", QMessageBox.ActionRole)
    msgBox.addButton('继续', QMessageBox.ActionRole)

    screenGeometry = QApplication.desktop().availableGeometry()
    screenGeo = screenGeometry.bottomRight()

    msgGeo = msgBox.frameGeometry()

    msgGeo.moveBottomRight(screenGeo)

    msgBox.move(msgGeo.topLeft())


def main():

    app = QApplication(sys.argv)

    msgBox = QMessageBox()
    moveToBottomRight(msgBox)
    msgBox.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()