import sys
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()

def exibir():
    text = line_edit.text()
    if option_information.isChecked():
        messsage_box = QMessageBox.information(window,"Exemplo 1", 
                                                            text)
    elif option_warning.isChecked():
        messsage_box = QMessageBox.warning(window,"Exemplo 1", 
                                                        text)
    else:
        messsage_box = QMessageBox.critical(window,"Exemplo 1", 
                                                        text)

button = QPushButton('Exibir mensagem', window)
button.clicked.connect(exibir)
line_edit = QLineEdit()
# group box of widgets
groupbox = QGroupBox('Opções de Diálogo', window)
# options
option_information = QRadioButton('Information', window)
option_information.setChecked(True)
option_warning = QRadioButton('Warning', window)
option_critical = QRadioButton('Critical', window)
# layout of items of group box
layout_options = QVBoxLayout()
layout_options.addWidget(option_information)
layout_options.addWidget(option_critical)
layout_options.addWidget(option_warning)
groupbox.setLayout(layout_options)
# layout of QPushButton e QLineEdit
layout_first_widgets = QHBoxLayout()
layout_first_widgets.addWidget(line_edit)
layout_first_widgets.addWidget(button)
# main layout
layout_master = QVBoxLayout()
layout_master.addLayout(layout_first_widgets)
layout_master.addWidget(groupbox)
window.setLayout(layout_master)

window.show()
sys.exit(app.exec_())
