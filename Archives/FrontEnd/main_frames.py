from ctypes import alignment
from logging.config import listen
from re import S
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Clossed():
    def closed_main_frames(self):
        try:
            self.quotation_frame.deleteLater()
        except:
            pass
        try:
            self.deadline_frame.deleteLater()
        except:
            pass
        try:
            self.order_frame.deleteLater()
        except:
            pass
        try:
            self.localization_frame.deleteLater()
        except:
            pass
        try:
            self.user_frame.deleteLater()
        except:
            pass
        try:
            self.notification_frame.deleteLater()
        except:
            pass
        try:
            self.settings_frame.deleteLater()
        except:
            pass


class Quotation(Clossed):
    def frame_quotation(self):
        self.closed_main_frames()
        
        self.frame_shipping.hide()
        self.quotation_frame = QFrame(self.first_window)
        self.quotation_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.quotation_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.quotation_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.quotation_frame, 2, 0)
        self.quotation_frame.show()

        self.position_widgets_quotation()


    def labels_quotation(self):
        self.font_style_subtitle = '''
            QLabel{
                background: none;
                color: #000000;
                font: Helvetica Neue Leve;
                font-size: 20px;
            }
        '''

        self.title_frame = QLabel('Cotação de envio de encomendas', self.quotation_frame)
        self.title_frame.setMinimumSize(420, 50)
        self.title_frame.setMaximumSize(420, 50)
        self.title_frame.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 25px;
                }
            '''
        )
        self.title_frame.show()

        self.cep_source = QLabel('CEP de origem', self.quotation_frame)
        self.cep_source.setMinimumSize(210, 50)
        self.cep_source.setMaximumSize(210, 50)
        self.cep_source.setStyleSheet(self.font_style_subtitle)
        self.cep_source.show()

        self.cep_destiny = QLabel('CEP de destino', self.quotation_frame)
        self.cep_destiny.setMinimumSize(210, 50)
        self.cep_destiny.setMaximumSize(210, 50)
        self.cep_destiny.setStyleSheet(self.font_style_subtitle)
        self.cep_destiny.show()

        self.order_value = QLabel('Valor da encomenda', self.quotation_frame)
        self.order_value.setMinimumSize(210, 50)
        self.order_value.setMaximumSize(210, 50)
        self.order_value.setStyleSheet(self.font_style_subtitle)
        self.order_value.show()

        self.service = QLabel('Serviço', self.quotation_frame)
        self.service.setMinimumSize(210, 50)
        self.service.setMaximumSize(210, 50)
        self.service.setStyleSheet(self.font_style_subtitle)
        self.service.show()

        self.order_weight = QLabel('Peso', self.quotation_frame)
        self.order_weight.setMinimumSize(210, 50)
        self.order_weight.setMaximumSize(210, 50)
        self.order_weight.setStyleSheet(self.font_style_subtitle)
        self.order_weight.show()
        
        self.subtitle_specifications = QLabel('Especificações da embalagem', self.quotation_frame)
        self.subtitle_specifications.setMinimumSize(300, 40)
        self.subtitle_specifications.setMaximumSize(300, 40)
        self.subtitle_specifications.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 20px;
                }
            '''
        )
        self.subtitle_specifications.show()

        self.lenght = QLabel('Comprimento:', self.quotation_frame)
        self.lenght.setMinimumSize(210, 50)
        self.lenght.setMaximumSize(210, 50)
        self.lenght.setStyleSheet(self.font_style_subtitle)
        self.lenght.show()

        self.cm_i = QLabel('cm', self.quotation_frame)
        self.cm_i.setMinimumSize(30, 50)
        self.cm_i.setMaximumSize(30, 50)
        self.cm_i.setStyleSheet(self.font_style_subtitle)
        self.cm_i.show()

        self.height = QLabel('Altura:', self.quotation_frame)
        self.height.setMinimumSize(210, 50)
        self.height.setMaximumSize(210, 50)
        self.height.setStyleSheet(self.font_style_subtitle)
        self.height.show()

        self.cm_ii = QLabel('cm', self.quotation_frame)
        self.cm_ii.setMinimumSize(30, 50)
        self.cm_ii.setMaximumSize(30, 50)
        self.cm_ii.setStyleSheet(self.font_style_subtitle)
        self.cm_ii.show()

        self.width = QLabel('Largura:', self.quotation_frame)
        self.width.setMinimumSize(210, 50)
        self.width.setMaximumSize(210, 50)
        self.width.setStyleSheet(self.font_style_subtitle)
        self.width.show()

        self.cm_iii = QLabel('cm', self.quotation_frame)
        self.cm_iii.setMinimumSize(30, 50)
        self.cm_iii.setMaximumSize(30, 50)
        self.cm_iii.setStyleSheet(self.font_style_subtitle)
        self.cm_iii.show()

        self.diameter = QLabel('Diâmetro', self.quotation_frame)
        self.diameter.setMinimumSize(210, 50)
        self.diameter.setMaximumSize(210, 50)
        self.diameter.setStyleSheet(self.font_style_subtitle)
        self.diameter.show()

        self.cm_iv = QLabel('cm', self.quotation_frame)
        self.cm_iv.setMinimumSize(30, 50)
        self.cm_iv.setMaximumSize(30, 50)
        self.cm_iv.setStyleSheet(self.font_style_subtitle)
        self.cm_iv.show()


    def entrys_quotation(self):
        self.entrys_style = '''
            QLineEdit{
                background-color: rgba(0, 0, 0, 0);
                color: #707070;
                border: 2px solid #cd6600;
                border-radius: 10px;
                font: 'Helvetica';
                font-size: 18px;
            }
            QLineEdit:pressed{
                color: #000000;
            }
        '''

        self.entrys_style_ii = '''
            QLineEdit{
                background-color: rgba(0, 0, 0, 0);
                border: 2px solid;
                border-top-color: none;
                border-left-color: none;
                border-right-color: none;
                border-bottom-color: #cd6600;
                font: 'Helvetica';
                font-size: 18px;
            }
        '''

        self.cep_source_get = QLineEdit(self.quotation_frame)
        self.cep_source_get.setMinimumSize(200, 40)
        self.cep_source_get.setMaximumSize(200, 40)
        self.cep_source_get.setPlaceholderText('Ex: 00000000')
        self.cep_source_get.setMaxLength(8)
        self.cep_source_get.setStyleSheet(self.entrys_style)
        self.cep_source_get.show()

        self.cep_destiny_get = QLineEdit(self.quotation_frame)
        self.cep_destiny_get.setMinimumSize(200, 40)
        self.cep_destiny_get.setMaximumSize(200, 40)
        self.cep_destiny_get.setPlaceholderText('Ex: 00000000')
        self.cep_destiny_get.setMaxLength(8)
        self.cep_destiny_get.setStyleSheet(self.entrys_style)
        self.cep_destiny_get.show()

        self.order_value_get = QLineEdit(self.quotation_frame)
        self.order_value_get.setMinimumSize(200, 40)
        self.order_value_get.setMaximumSize(200, 40)
        self.order_value_get.setPlaceholderText('R$ 000,00')
        self.order_value_get.setMaxLength(8)
        self.order_value_get.setStyleSheet(self.entrys_style)
        self.order_value_get.show()

        self.order_weight_get = QLineEdit(self.quotation_frame)
        self.order_weight_get.setMinimumSize(200, 40)
        self.order_weight_get.setMaximumSize(200, 40)
        self.order_weight_get.setPlaceholderText('Kg 00,00')
        self.order_weight_get.setMaxLength(8)
        self.order_weight_get.setStyleSheet(self.entrys_style)
        self.order_weight_get.show()

        self.lenght_get = QLineEdit(self.quotation_frame)
        self.lenght_get.setMinimumSize(150, 40)
        self.lenght_get.setMaximumSize(150, 40)
        self.lenght_get.setMaxLength(8)
        self.lenght_get.setStyleSheet(self.entrys_style_ii)
        self.lenght_get.show()

        self.height_get = QLineEdit(self.quotation_frame)
        self.height_get.setMinimumSize(150, 40)
        self.height_get.setMaximumSize(150, 40)
        self.height_get.setMaxLength(8)
        self.height_get.setStyleSheet(self.entrys_style_ii)
        self.height_get.show()

        self.width_get = QLineEdit(self.quotation_frame)
        self.width_get.setMinimumSize(150, 40)
        self.width_get.setMaximumSize(150, 40)
        self.width_get.setMaxLength(8)
        self.width_get.setStyleSheet(self.entrys_style_ii)
        self.width_get.show()

        self.diameter_get = QLineEdit(self.quotation_frame)
        self.diameter_get.setMinimumSize(150, 40)
        self.diameter_get.setMaximumSize(150, 40)
        self.diameter_get.setMaxLength(8)
        self.diameter_get.setStyleSheet(self.entrys_style_ii)
        self.diameter_get.show()


    def radio_buttons(self):
        self.radio_button_style = '''
            QRadioButton:indicator{
                width: 30px;
                height: 30px;
            }
            QRadioButton:indicator:unchecked{
                image: url('Images/main_frames/quotation/unchecked.png');

            }
            QRadioButton:indicator:checked{
                image: url('Images/main_frames/quotation/checked.png');
            }
        '''

        self.group_box_i = QGroupBox('Formato de encomenda', self.quotation_frame)
        self.group_box_i.setMinimumSize(300, 100)
        self.group_box_i.setMaximumSize(300, 100)
        self.group_box_i.setStyleSheet('font-size: 20px; font: Helvetica Neue Leve;')
        self.hboxi = QHBoxLayout(self.group_box_i)
        self.group_box_i.show()

        self.package_format_radio = QRadioButton(self.quotation_frame)
        self.package_format_radio.setMinimumSize(100, 50)
        self.package_format_radio.setMaximumSize(100, 50)
        self.package_format_radio.setIcon(QIcon('Images/main_frames/quotation/package.png'))
        self.package_format_radio.setIconSize(QSize(40, 40))
        self.package_format_radio.setStyleSheet(self.radio_button_style)
        self.hboxi.addWidget(self.package_format_radio)
        self.package_format_radio.show()

        self.cylinder_format_radio = QRadioButton(self.quotation_frame)
        self.cylinder_format_radio.setMinimumSize(100, 50)
        self.cylinder_format_radio.setMaximumSize(100, 50)
        self.cylinder_format_radio.setIcon(QIcon('Images/main_frames/quotation/cylinder.png'))
        self.cylinder_format_radio.setIconSize(QSize(40, 40))
        self.cylinder_format_radio.setStyleSheet(self.radio_button_style)
        self.hboxi.addWidget(self.cylinder_format_radio)
        self.cylinder_format_radio.show()

        self.letter_format_radio = QRadioButton(self.quotation_frame)
        self.letter_format_radio.setMinimumSize(100, 50)
        self.letter_format_radio.setMaximumSize(100, 50)
        self.letter_format_radio.setIcon(QIcon('Images/main_frames/quotation/letter.png'))
        self.letter_format_radio.setIconSize(QSize(40, 40))
        self.letter_format_radio.setStyleSheet(self.radio_button_style)
        self.hboxi.addWidget(self.letter_format_radio)
        self.letter_format_radio.show()

        self.radio_button_style_i = ''' 
            QRadioButton{
                font: 'Helvetica';
                font-size: 20px;
            }
            QRadioButton:indicator{
                width: 30px;
                height: 30px;
            }
            QRadioButton:indicator:unchecked{
                image: url('Images/main_frames/quotation/unchecked.png');

            }
            QRadioButton:indicator:checked{
                image: url('Images/main_frames/quotation/checked.png');
            }
        '''

        self.group_box_ii = QGroupBox('Mão própria', self.quotation_frame)
        self.group_box_ii.setMinimumSize(250, 80)
        self.group_box_ii.setMaximumSize(250, 80)
        self.group_box_ii.setStyleSheet('font-size: 20px; font: Helvetica Neue Leve;')
        self.hboxii = QHBoxLayout(self.group_box_ii)
        self.group_box_ii.show()

        self.yes_radio_button = QRadioButton('Sim', self.quotation_frame)
        self.yes_radio_button.setMinimumSize(100, 40)
        self.yes_radio_button.setMaximumSize(100, 40)
        self.yes_radio_button.setStyleSheet(self.radio_button_style_i)
        self.hboxii.addWidget(self.yes_radio_button)
        self.yes_radio_button.show()

        self.no_radio_button = QRadioButton('Não', self.quotation_frame)
        self.no_radio_button.setMinimumSize(100, 40)
        self.no_radio_button.setMaximumSize(100, 40)
        self.no_radio_button.setStyleSheet(self.radio_button_style_i)
        self.hboxii.addWidget(self.no_radio_button)
        self.no_radio_button.show()

        self.group_box_iii = QGroupBox('Aviso de recebimento', self.quotation_frame)
        self.group_box_iii.setMinimumSize(250, 80)
        self.group_box_iii.setMaximumSize(250, 80)
        self.group_box_iii.setStyleSheet('font-size: 20px; font: Helvetica Neue Leve;')
        self.hboxiii = QHBoxLayout(self.group_box_iii)
        self.group_box_iii.show()

        self.yes_radio_buttonii = QRadioButton('Sim', self.quotation_frame)
        self.yes_radio_buttonii.setMinimumSize(100, 40)
        self.yes_radio_buttonii.setMaximumSize(100, 40)
        self.yes_radio_buttonii.setStyleSheet(self.radio_button_style_i)
        self.hboxiii.addWidget(self.yes_radio_buttonii)
        self.yes_radio_buttonii.show()

        self.no_radio_buttonii = QRadioButton('Não', self.quotation_frame)
        self.no_radio_buttonii.setMinimumSize(100, 40)
        self.no_radio_buttonii.setMaximumSize(100, 40)
        self.no_radio_buttonii.setStyleSheet(self.radio_button_style_i)
        self.hboxiii.addWidget(self.no_radio_buttonii)
        self.no_radio_buttonii.show()


    def buttons_quotation(self):
        self.question_style_button = '''
            QToolButton{
                background-color: none;
                border-radius: 4px
            }
            QToolButton:hover{
                background-color: rgba(255, 255, 255, 0.5);
            }
        '''
        
        self.question_i = QToolButton(self.quotation_frame)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setIcon(QIcon('Images/main_frames/quotation/question.png'))
        self.question_i.setIconSize(QSize(30, 30))
        self.question_i.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.question_i.setStyleSheet(self.question_style_button)
        self.question_i.show()

        self.question_ii = QToolButton(self.quotation_frame)
        self.question_ii.setMinimumSize(30, 30)
        self.question_ii.setMinimumSize(30, 30)
        self.question_ii.setIcon(QIcon('Images/main_frames/quotation/question.png'))
        self.question_ii.setIconSize(QSize(30, 30))
        self.question_ii.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.question_ii.setStyleSheet(self.question_style_button)
        self.question_ii.show()

        self.calculate = QPushButton('CALCULAR', self.quotation_frame)
        self.calculate.setMinimumSize(150, 50)
        self.calculate.setMaximumSize(150, 50)
        self.calculate.setStyleSheet(
            '''
                QPushButton{
                    background-color: #cd6600;
                    color: #ffffff;
                    border-radius: 14px;
                    font: bold 'Verdana';
                    font-size: 19px;
                }
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.calculate.show()


    def combo_box_quotation(self):
        self.service_box = QComboBox(self.quotation_frame)
        self.service_box.setMinimumSize(200, 40)
        self.service_box.setMaximumSize(200, 40)
        list = ['SEDEX', 'SEDEX 10', 'SEDEX 12', 'SEDEX Hoje', 'PAC']
        self.service_box.setEditable(True)
        self.service_box.addItems(list)
        self.service_box.setStyleSheet(
            '''
                QComboBox{
                    background-color: rgba(0, 0, 0, 0);
                    color: #000000;
                    border: 2px solid #CD6600;
                    border-radius: 12px;
                    font: 'Helvetica';
                    font-size: 19px;
                }
            '''
        )
        self.service_box.show()


    def position_widgets_quotation(self):
        self.labels_quotation()
        self.entrys_quotation()
        self.radio_buttons()
        self.buttons_quotation()
        self.combo_box_quotation()

        ####################        L A B E L S       ####################
        self.title_frame.setGeometry(330, 10, 420, 50)
        self.cep_source.setGeometry(150, 80, 210, 50)
        self.cep_destiny.setGeometry(150, 200, 210, 50)
        self.order_value.setGeometry(450, 80, 210, 50)
        self.service.setGeometry(450, 200, 210, 50)
        self.order_weight.setGeometry(700, 200, 210, 50)
        self.subtitle_specifications.setGeometry(400, 310, 210, 50)
        self.lenght.setGeometry(150, 350, 210, 50)
        self.cm_i.setGeometry(480, 350, 30, 50)
        self.height.setGeometry(150, 400, 210, 50)
        self.cm_ii.setGeometry(480, 400, 30, 50)
        self.width.setGeometry(150, 450, 210, 50)
        self.cm_iii.setGeometry(480, 450, 30, 50)
        self.diameter.setGeometry(150, 500, 210, 50)
        self.cm_iv.setGeometry(480, 500, 30, 50)
        ####################       E N T R Y S       ####################
        self.cep_source_get.setGeometry(150, 130, 200, 40)
        self.cep_destiny_get.setGeometry(150, 250, 200, 40)
        self.order_value_get.setGeometry(450, 130, 200, 40)
        self.order_weight_get.setGeometry(700, 250, 200, 40)
        self.lenght_get.setGeometry(310, 350, 150, 40)
        self.height_get.setGeometry(310, 400, 150, 40)
        self.width_get.setGeometry(310, 450, 150, 40)
        self.diameter_get.setGeometry(310, 500, 150, 40)
        #################### R A D I O  B U T T O N S ####################
        self.group_box_i.setGeometry(700, 80, 300, 100)
        self.group_box_ii.setGeometry(650, 370, 250, 80)
        self.group_box_iii.setGeometry(650, 470, 250, 80)
        ####################       B U T T O N S      ###################
        self.question_i.setGeometry(360, 135, 30, 30)
        self.question_ii.setGeometry(360, 255, 30, 30)
        self.calculate.setGeometry(480, 590, 150, 50)
        ###################      C O M B O  B O X     ####################
        self.service_box.setGeometry(450, 250, 200, 40)


class Deadline(Clossed):
    def frame_deadline(self):
        self.closed_main_frames()
        self.frame_shipping.hide()
        self.deadline_frame = QFrame(self.first_window)
        self.deadline_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.deadline_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.deadline_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.deadline_frame, 2, 0)
        self.deadline_frame.show()

        self.positions_widgets_deadline()
        
    
    def labels_deadline(self):
        self.font_style_title = '''
            QLabel{
                background: none;
                color: #000000;
                font: bold 'Helvetica Neue Leve';
                font-size: 25px;
            }
        '''

        self.font_style_subtitle = '''
            QLabel{
                background: none;
                color: #000000;
                font: Helvetica Neue Leve;
                font-size: 20px;
            }
        '''

        self.title_frame = QLabel('Cálculo de prazos de entrega', self.deadline_frame)
        self.title_frame.setMinimumSize(420, 50)
        self.title_frame.setMaximumSize(420, 50)
        self.title_frame.setStyleSheet(self.font_style_title)
        self.title_frame.show()

        self.cep_source = QLabel('CEP de origem', self.deadline_frame)
        self.cep_source.setMinimumSize(210, 50)
        self.cep_source.setMaximumSize(210, 50)
        self.cep_source.setStyleSheet(self.font_style_subtitle)
        self.cep_source.show()

        self.cep_destiny = QLabel('CEP de destino', self.deadline_frame)
        self.cep_destiny.setMinimumSize(210, 50)
        self.cep_destiny.setMaximumSize(210, 50)
        self.cep_destiny.setStyleSheet(self.font_style_subtitle)
        self.cep_destiny.show()

        self.post_date = QLabel('Data de postagem', self.deadline_frame)
        self.post_date.setMinimumSize(210, 50)
        self.post_date.setMaximumSize(210, 50)
        self.post_date.setStyleSheet(self.font_style_subtitle)
        self.post_date.show()

        self.title_cep = QLabel('Buscar CEP', self.deadline_frame)
        self.title_cep.setStyleSheet(self.font_style_title)
        self.title_cep.show()

        self.cep = QLabel('CEP', self.deadline_frame)
        self.cep.setStyleSheet(self.font_style_subtitle)
        self.cep.show()

        self.line = QFrame(self.deadline_frame)
        self.line.setStyleSheet('background: none; background-color: #cd6600;')
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.line.show()


    def entrys_deadline(self):
        self.entrys_style = '''
            QLineEdit{
                background-color: rgba(0, 0, 0, 0);
                color: #707070;
                border: 2px solid #cd6600;
                border-radius: 10px;
                font: 'Helvetica';
                font-size: 18px;
            }
            QLineEdit:pressed{
                color: #000000;
            }
        '''

        self.cep_source_get = QLineEdit(self.deadline_frame)
        self.cep_source_get.setMinimumSize(200, 40)
        self.cep_source_get.setMaximumSize(200, 40)
        self.cep_source_get.setPlaceholderText('Ex: 00000000')
        self.cep_source_get.setMaxLength(8)
        self.cep_source_get.setStyleSheet(self.entrys_style)
        self.cep_source_get.show()

        self.cep_destiny_get = QLineEdit(self.deadline_frame)
        self.cep_destiny_get.setMinimumSize(200, 40)
        self.cep_destiny_get.setMaximumSize(200, 40)
        self.cep_destiny_get.setPlaceholderText('Ex: 00000000')
        self.cep_destiny_get.setMaxLength(8)
        self.cep_destiny_get.setStyleSheet(self.entrys_style)
        self.cep_destiny_get.show()

        self.post_date_get = QLineEdit(self.deadline_frame)
        self.post_date_get.setMinimumSize(200, 40)
        self.post_date_get.setMaximumSize(200, 40)
        self.post_date_get.setPlaceholderText('          /          /          ')
        self.post_date_get.setMaxLength(8)
        self.post_date_get.setStyleSheet(self.entrys_style)
        self.post_date_get.show()

        self.cep_get = QLineEdit(self.deadline_frame)
        self.cep_get.setMinimumSize(200, 40)
        self.cep_get.setMaximumSize(200, 40)
        self.cep_get.setPlaceholderText('Ex: 00000000')
        self.cep_get.setMaxLength(8)
        self.cep_get.setStyleSheet(self.entrys_style)
        self.cep_get.show()


    def buttons_deadline(self):
        self.question_style_button = '''
            QToolButton{
                background-color: none;
                border-radius: 4px
            }
            QToolButton:hover{
                background-color: rgba(255, 255, 255, 0.5);
            }
        '''

        self.style_buttons = '''
            QPushButton{
                background-color: #cd6600;
                color: #ffffff;
                border-radius: 14px;
                font: bold 'Verdana';
                font-size: 19px;
            }
            QPushButton:hover{
                background-color: #8B4500;
            }
            QPushButton:pressed{
                background-color: #EE7600;
            }
        '''
        
        self.question_i = QToolButton(self.deadline_frame)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setIcon(QIcon('Images/main_frames/deadline/question.png'))
        self.question_i.setIconSize(QSize(30, 30))
        self.question_i.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.question_i.setStyleSheet(self.question_style_button)
        self.question_i.show()

        self.calculate = QPushButton('CALCULAR', self.deadline_frame)
        self.calculate.setMinimumSize(150, 50)
        self.calculate.setMaximumSize(150, 50)
        self.calculate.setStyleSheet(self.style_buttons)
        self.calculate.show()

        self.cep_search = QPushButton('BUSCAR', self.deadline_frame)
        self.cep_search.setMinimumSize(150, 50)
        self.cep_search.setMaximumSize(150, 50)
        self.cep_search.setStyleSheet(self.style_buttons)
        self.cep_search.show()


    def positions_widgets_deadline(self):
        self.labels_deadline()
        self.entrys_deadline()
        self.buttons_deadline()

        ####################  L A B E L S  ####################
        self.title_frame.setGeometry(540, 150, 420, 50)
        self.cep_source.setGeometry(450, 220, 210, 50)
        self.cep_destiny.setGeometry(865, 220, 210, 50)
        self.post_date.setGeometry(638, 350, 210, 50)
        self.title_cep.setGeometry(100, 150, 200, 50)
        self.cep.setGeometry(150, 250, 100, 30)
        self.line.setGeometry(350, 130, 2, 470)

        ####################  E N T R Y S  ####################
        self.cep_source_get.setGeometry(420, 270, 200, 40)
        self.cep_destiny_get.setGeometry(835, 270, 200, 40)
        self.post_date_get.setGeometry(623, 400, 200, 40)
        self.cep_get.setGeometry(80, 300, 100, 30)

        #################### B U T T O N S ####################
        self.question_i.setGeometry(823, 400, 40, 40)
        self.calculate.setGeometry(645, 500, 150, 50)
        self.cep_search.setGeometry(105, 400, 100, 30)
      

class Order(Clossed):
    def frame_order(self):
        self.closed_main_frames()
        self.frame_packeges.hide()
        self.order_frame = QFrame(self.first_window)
        self.order_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.order_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.order_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.order_frame, 2, 0)
        self.order_frame.show()

        self.positions_widgets_order()

    
    def labels_order(self):
        self.style_results = (
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            '''
        )

        self.title = QLabel('Encomendas em estoque', self.order_frame)
        self.title.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #202020;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 25px;
                }
            '''
        )
        self.title.show()

        self.logo_title = QLabel(self.order_frame)
        self.image_logo_title = QPixmap('Images/main_frames/order/logo_title.png')
        self.logo_title.setStyleSheet(
            '''
                QLabel{
                    background: none;
                }
            '''
        )
        self.logo_title.setPixmap(self.image_logo_title)
        self.logo_title.show()

        self.background = QFrame(self.order_frame)
        self.background.setStyleSheet(
            '''
                QFrame{
                    background-color: #f7f7f7;
                    border-radius: 10px;
                }
            '''
        )
        self.background.show()

        self.quantity_products = QLabel('Quantidade de produtos no estoque:', self.background)
        self.quantity_products.setStyleSheet(self.style_results)
        self.quantity_products.show()

        self.stock_value = QLabel('Valor em estoque:', self.background)
        self.stock_value.setStyleSheet(self.style_results)
        self.stock_value.show()


    def entrys_order(self):
        self.search = QLineEdit(self.order_frame)
        self.search.setPlaceholderText('Buscar                    🔍')
        self.search.setStyleSheet(
            '''
                QLineEdit{
                    background-color: rgba(0, 0, 0, 0);
                    color: #707070;
                    border: 2px solid #cd6600;
                    border-radius: 10px;
                    font: 'Helvetica';
                    font-size: 18px;
                }
                QLineEdit:pressed{
                    color: #000000;
                }
            '''
        )
        self.search.show()


    def buttons_order(self):
        self.new_order = QPushButton(' Novo', self.order_frame)
        self.new_order.setIcon(QIcon('Images/main_frames/order/new.png'))
        self.new_order.setIconSize(QSize(18, 18))
        self.new_order.setStyleSheet(
            '''
                QPushButton{
                    background-color: #cd6600;
                    color: #ffffff;
                    border-radius: 14px;
                    font: bold 'Verdana';
                    font-size: 19px;
                }
                QPushButton:hover{
                    background-color: #8B4500;
                }
                QPushButton:pressed{
                    background-color: #EE7600;
                }
            '''
        )
        self.new_order.show()


    def tables_order(self):
        self.table_order = QTableWidget(self.order_frame)
        self.table_order.setRowCount(1)
        self.table_order.setColumnCount(8)
        self.table_order.verticalHeader().setDefaultSectionSize(50)
        self.table_order.horizontalHeader().setDefaultSectionSize(130)

        self.titles = ['ID', 'QUANTIDADE', 'DESCRIÇÃO', 'PESO EM KG', 'VALOR UNITÁRIO', 'DATA DE CHEGADA', 'CATEGORIA', 'TOTAL']
        self.table_order.setHorizontalHeaderLabels(list(self.titles))

        self.table_order.setStyleSheet(
            '''
                QTableWidget{
                    border: 1px solid #cd6600;
                    border-radius: 10px;
                    selection-background-color: #cd6600;
                }
            '''
        )
        self.table_order.show()


    def positions_widgets_order(self):
        self.labels_order()
        self.entrys_order()
        self.buttons_order()
        self.tables_order()

        ####################  L A B E L S  ####################
        self.title.setGeometry(100, 20, 360, 50)
        self.logo_title.setGeometry(40, 20, 50, 50)
        self.background.setGeometry(10, 570, 1060, 90)
        self.quantity_products.setGeometry(30, 30, 350, 30)
        self.stock_value.setGeometry(650, 30, 200, 30)

        ####################  E N T R Y S  ####################
        self.search.setGeometry(700, 25, 210, 40)

        #################### B U T T O N S ####################
        self.new_order.setGeometry(930, 25, 130, 40)
        
        ####################   T A B L E   #################### 
        self.table_order.setGeometry(10, 80, 1061, 480)


class Localization(Clossed):
    def frame_localization(self):
        self.closed_main_frames()
        self.frame_screening.hide()
        self.localization_frame = QFrame(self.first_window)
        self.localization_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.localization_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.localization_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: black;
                }
            '''
        )
        self.layout.addWidget(self.localization_frame, 2, 0)
        self.localization_frame.show()


class User(Clossed):
    def frame_user(self):
        self.closed_main_frames()
        self.frame_options.hide()
        self.user_frame = QFrame(self.first_window)
        self.user_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.user_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.user_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: white;
                }
            '''
        )
        self.layout.addWidget(self.user_frame, 2, 0)
        self.user_frame.show()


class Notification(Clossed):
    def frame_notification(self):
        self.closed_main_frames()
        self.frame_options.hide()
        self.notification_frame = QFrame(self.first_window)
        self.notification_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.notification_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.notification_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: brow;
                }
            '''
        )
        self.layout.addWidget(self.notification_frame, 2, 0)
        self.notification_frame.show()


class Settings(Clossed):
    def frame_settings(self):
        self.closed_main_frames()
        self.frame_options.hide()
        self.settings_frame = QFrame(self.first_window)
        self.settings_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.settings_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.settings_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: yellow;
                }
            '''
        )
        self.layout.addWidget(self.settings_frame, 2, 0)
        self.settings_frame.show()
