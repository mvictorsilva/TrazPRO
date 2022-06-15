from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

class ImagePerfil:
    def getImage(self):
        self.fname = QFileDialog.getOpenFileName(self.user_frame, 'Open file',
                                            'c:/', "Image files (*.png *.jpg *.jpeg)")
        self.imagePath = self.fname[0]
        self.pixmap = QPixmap(self.imagePath)


        self.image.setIcon(QIcon(self.pixmap))
        self.image.setIconSize(QSize(200, 200))
        self.image.setMinimumSize(200, 200)
        self.image.setMaximumSize(200, 200)


        self.image.setStyleSheet('''
            QToolButton{
                border: none;
                border-radius: 50px;
            }
        ''')
    
