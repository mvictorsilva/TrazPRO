import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.textEdit = QTextEdit()
        self.layout.addWidget(self.textEdit)

        self.menuBar = QMenu()
        self.filemenu = QMenu('File')
        self.filemenu.addAction(print('hello'))

        print('ok')
        
        self.menuBar.addMenu(self.filemenu)
        self.layout.setMenuBar(self.menuBar)

        qApp.installEventFilter(self)

        self.menuBar.hide()

    def eventFilter(self, source, event):
        if qApp.activePopupWidget() is None:
            if event.type() == QEvent.MouseMove:
                if self.menuBar.isHidden():
                    rect = self.geometry()
                    rect.setHeight(60)

                    if rect.contains(event.globalPos()):
                        self.menuBar.show()
                else:
                    rect = QRect(
                        self.menuBar.mapToGlobal(QPoint(0, 0)),
                        self.menuBar.size()
                    )
                    if not rect.contains(event.globalPos()):
                        self.menuBar.hide()
            elif event.type() == QEvent.Leave and source is self:
                self.menuBar.hide()
        return super().eventFilter(source, event)


if __name__ == '__main__':
    #don't auto scale when drag app toadifferent monitor.
    #QApplication.setAttribute(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv) 

    myApp = MyApp()
    myApp.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print('Closing Window...')
