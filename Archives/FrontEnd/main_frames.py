from calendar import day_abbr
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

from BackEnd.quotation import CalculateValue
from BackEnd.deadline import CalculateDeadline
from BackEnd.track_back import TrackBack
from BackEnd.employee import ImagePerfil

from BackEnd.db import DataBase


class Clossed:
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


class Quotation(Clossed, CalculateValue):
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

        self.order_value = QLabel('Valor declarado', self.quotation_frame)
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

        self.handle_errors()

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
        self.calculate.clicked.connect(self.receive_data)
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

    def result_frame(self):
        self.background = QFrame(self.quotation_frame)
        self.background.setStyleSheet('''
                    QFrame{
                        background-color: rgba(255, 255, 255, 0.3);
                    }
                ''')
        self.background.show()
        self.background.setGeometry(0, 0, 1080, 670)

        self.result = QFrame(self.background)
        self.result.setStyleSheet('''
            QFrame{
                background-color: #f8f8f8;
                border: 2px solid #909090;
                border-radius: 20px;
            }
        ''')
        self.result.show()
        self.result.setGeometry(290, 90, 500, 500)

        self.text_title = QLabel('Cotação', self.result)
        self.text_title.setStyleSheet('''
                    QLabel{
                        border: none;
                        background: none;
                        color: #000000;
                        font: bold 'Helvetica Neue Leve';
                        font-size: 25px;
                    }
                ''')
        self.text_title.setGeometry(200, 20, 200, 40)
        self.text_title.show()

        self.text_result = QLabel(self.result)
        self.text_result.setText(f'''
            Valor do frete: {self.value}\n
            Prazo de entrega: {self.deadline}\n
            Valor sem adicionais: {self.no_additional}\n
            Valor mão própria: {self.own_hand}\n
            Valor aviso de recebimento: {self.early_warning}\n
            Valor declarado: {self.declared_value}\n
            Entrega domiciliar: {self.home_delivery}\n
            Entrega no sábado: {self.weekend_delivery}\n
        ''')
        self.text_result.setStyleSheet('''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: 'Helvetica Neue Leve';
                font-size: 20px;
            }
        ''')
        self.text_result.setGeometry(10, 80, 480, 400)
        self.text_result.show()

        self.close = QToolButton(self.result)
        self.close.setIcon(QIcon('Images/main_frames/quotation/close.png'))
        self.close.setIconSize(QSize(20, 20))
        self.close.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.close.setStyleSheet(
            '''
                QToolButton{
                    border: none;
                    background-color: none;
                    border-radius: 4px
                }
                QToolButton:hover{
                    background-color: rgba(255, 255, 255, 0.5);
                }
            '''
        )
        self.close.clicked.connect(lambda: (self.result.deleteLater(),
                                            self.background.deleteLater()))
        self.close.setGeometry(450, 20, 22, 20)
        self.close.show()

    def error_frame(self):
        self.frame_error = QFrame(self.quotation_frame)
        self.frame_error.setMaximumSize(QSize(450, 35))
        self.frame_error.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.frame_error.setGeometry(330, 15, 450, 40)
        self.frame_error.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Dados incorretos', self.frame_error)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_error.deleteLater)


class Deadline(Clossed, CalculateDeadline):
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

        """self.post_date = QLabel('Data de postagem', self.deadline_frame)
        self.post_date.setMinimumSize(210, 50)
        self.post_date.setMaximumSize(210, 50)
        self.post_date.setStyleSheet(self.font_style_subtitle)
        self.post_date.show()"""

        self.title_cep = QLabel('Buscar CEP', self.deadline_frame)
        self.title_cep.setStyleSheet(self.font_style_title)
        self.title_cep.show()

        self.cep = QLabel('Digite o CEP:', self.deadline_frame)
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

        """self.post_date_get = QLineEdit(self.deadline_frame)
        self.post_date_get.setMinimumSize(200, 40)
        self.post_date_get.setMaximumSize(200, 40)
        self.post_date_get.setPlaceholderText('          /          /          ')
        self.post_date_get.setMaxLength(8)
        self.post_date_get.setStyleSheet(self.entrys_style)
        self.post_date_get.show()"""

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
        
        """self.question_i = QToolButton(self.deadline_frame)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setMinimumSize(30, 30)
        self.question_i.setIcon(QIcon('../Images/main_frames/deadline/question.png'))
        self.question_i.setIconSize(QSize(30, 30))
        self.question_i.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.question_i.setStyleSheet(self.question_style_button)
        self.question_i.show()"""

        self.calculate = QPushButton('CALCULAR', self.deadline_frame)
        self.calculate.setMinimumSize(150, 50)
        self.calculate.setMaximumSize(150, 50)
        self.calculate.setStyleSheet(self.style_buttons)
        self.calculate.clicked.connect(self.requests_deadline)
        self.calculate.show()

        self.cep_search = QPushButton('BUSCAR', self.deadline_frame)
        self.cep_search.setMinimumSize(150, 50)
        self.cep_search.setMaximumSize(150, 50)
        self.cep_search.setStyleSheet(self.style_buttons)
        self.cep_search.clicked.connect(self.requests_cep)
        self.cep_search.show()

    def positions_widgets_deadline(self):
        self.labels_deadline()
        self.entrys_deadline()
        self.buttons_deadline()

        ####################  L A B E L S  ####################
        self.title_frame.setGeometry(590, 150, 420, 50)
        self.cep_source.setGeometry(570, 220, 210, 50)
        self.cep_destiny.setGeometry(835, 220, 210, 50)
        """self.post_date.setGeometry(638, 350, 210, 50)"""
        self.title_cep.setGeometry(160, 200, 200, 50)
        self.cep.setGeometry(70, 305, 150, 30)
        self.line.setGeometry(470, 130, 2, 470)

        ####################  E N T R Y S  ####################
        self.cep_source_get.setGeometry(550, 270, 200, 40)
        self.cep_destiny_get.setGeometry(805, 270, 200, 40)
        """self.post_date_get.setGeometry(623, 400, 200, 40)"""
        self.cep_get.setGeometry(210, 300, 100, 30)

        #################### B U T T O N S ####################
        """self.question_i.setGeometry(823, 400, 40, 40)"""
        self.calculate.setGeometry(695, 400, 150, 50)
        self.cep_search.setGeometry(155, 400, 100, 30)

    def error_frameii(self):
        self.frame_errorii = QFrame(self.deadline_frame)
        self.frame_errorii.setMaximumSize(QSize(450, 35))
        self.frame_errorii.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_errorii.setFrameShape(QFrame.StyledPanel)
        self.frame_errorii.setFrameShadow(QFrame.Raised)
        self.frame_errorii.setGeometry(330, 15, 450, 40)
        self.frame_errorii.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_errorii)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Dados incorretos', self.frame_errorii)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_errorii)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_errorii.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_errorii.deleteLater)

    def result_frameii(self):
        self.background = QFrame(self.deadline_frame)
        self.background.setStyleSheet('''
            QFrame{
                background-color: rgba(255, 255, 255, 0.3);
            }
        ''')
        self.background.show()
        self.background.setGeometry(0, 0, 1080, 670)

        self.result = QFrame(self.background)
        self.result.setStyleSheet('''
            QFrame{
                background-color: #f8f8f8;
                border: 2px solid #909090;
                border-radius: 20px;
            }
        ''')
        self.result.show()
        self.result.setGeometry(380, 235, 320, 250)

        self.text_title = QLabel('Cotação', self.result)
        self.text_title.setStyleSheet('''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: bold 'Helvetica Neue Leve';
                font-size: 25px;
            }
        ''')
        self.text_title.setGeometry(100, 20, 200, 30)
        self.text_title.show()

        self.text_result = QLabel(self.result)
        self.text_result.setText(f'''
 CEP: {self.cep}
 Estado: {self.state}
 Cidade: {self.city}
 Logradouro: {self.road}
 Complemento: {self.complement}
        ''')
        self.text_result.setStyleSheet('''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: 'Helvetica Neue Leve';
                font-size: 20px;
            }
        ''')
        self.text_result.setGeometry(10, 10, 280, 280)
        self.text_result.show()

        self.close = QToolButton(self.result)
        self.close.setIcon(QIcon('Images/main_frames/quotation/close.png'))
        self.close.setIconSize(QSize(17, 17))
        self.close.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.close.setStyleSheet(
            '''
                QToolButton{
                    border: none;
                    background-color: none;
                    border-radius: 4px
                }
                QToolButton:hover{
                    background-color: rgba(255, 255, 255, 0.5);
                }
            '''
        )
        self.close.clicked.connect(lambda: (self.result.deleteLater(),
                                            self.background.deleteLater()))
        self.close.setGeometry(270, 27, 20, 20)
        self.close.show()

    def result_frameiii(self):
        self.background = QFrame(self.deadline_frame)
        self.background.setStyleSheet('''
            QFrame{
                background-color: rgba(255, 255, 255, 0.3);
            }
        ''')
        self.background.show()
        self.background.setGeometry(0, 0, 1080, 670)

        self.result = QFrame(self.background)
        self.result.setStyleSheet('''
            QFrame{
                background-color: #f8f8f8;
                border: 2px solid #909090;
                border-radius: 20px;
            }
        ''')
        self.result.show()
        self.result.setGeometry(235, 275, 610, 120)

        self.text_title = QLabel('Prazos', self.result)
        self.text_title.setStyleSheet('''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: bold 'Helvetica Neue Leve';
                font-size: 25px;
            }
        ''')
        self.text_title.setGeometry(265, 25, 100, 30)
        self.text_title.show()

        self.text_result = QLabel(self.result)
        self.text_result.setText(f'Sua encomenda chegará em {self.deadline} a partir da data de postagem')
        self.text_result.setStyleSheet('''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: 'Helvetica Neue Leve';
                font-size: 20px;
            }
        ''')
        self.text_result.setGeometry(10, 50, 600, 60)
        self.text_result.show()

        self.close = QToolButton(self.result)
        self.close.setIcon(QIcon('Images/main_frames/quotation/close.png'))
        self.close.setIconSize(QSize(17, 17))
        self.close.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.close.setStyleSheet(
            '''
                QToolButton{
                    border: none;
                    background-color: none;
                    border-radius: 4px
                }
                QToolButton:hover{
                    background-color: rgba(255, 255, 255, 0.5);
                }
            '''
        )
        self.close.clicked.connect(lambda: (self.result.deleteLater(),
                                            self.background.deleteLater()))
        self.close.setGeometry(550, 27, 20, 20)
        self.close.show()


class Order(Clossed, DataBase):
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

        self.quantity_products = QLabel(self.background)
        self.quantity_products.setText('Quantidade de produtos no estoque:')
        self.quantity_products.setStyleSheet(self.style_results)
        self.quantity_products.show()

        self.stock_value = QLabel(self.background)
        self.stock_value.setText('Valor em estoque: R$')
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
        self.new_order.clicked.connect(self.frame_new_order)
        self.new_order.show()

    def tables_order(self):
        self.table_order = QTableWidget(self.order_frame)
        self.table_order.setRowCount(1)
        self.table_order.setColumnCount(8)
        self.table_order.verticalHeader().setDefaultSectionSize(50)
        self.table_order.horizontalHeader().setDefaultSectionSize(130)

        self.titles = ['ID', 'DESCRIÇÃO', 'QUANTIDADE', 'PESO EM KG', 'VALOR UNITÁRIO', 'DATA DE CHEGADA', 'CATEGORIA', 'ID GERENTE']
        self.table_order.setHorizontalHeaderLabels(list(self.titles))

        # self.table_order.setStyleSheet(
        #     '''
        #         QTableWidget{
        #             border: 1px solid #cd6600;
        #             border-radius: 10px;
        #             selection-background-color: #cd6600;
        #         }
        #     '''
        # )
        self.table_order.setStyleSheet(
            '''
                QTableWidget{
                    gridline-color: #cd6600;
                    background-color: transparent;
                    outline: 0;
                    border-radius: 10px;
                    border: 1px solid #cd6600;
                    border-top: 0px
                }
                QTableWidget::item:selected{
                    background-color:#cd6600;;
                }
                QTableWidget::horizontalHeader{    
                    background-color: #cd6600;
                }
                QHeaderView::section:horizontal{
                    border: 1px solid #cd6600;
                    background-color: transparent;
                    border-left: 0px;
                    color: black;
                }
            '''
        )
        self.table_order.show()

    def positions_widgets_order(self):
        self.labels_order()
        self.buttons_order()
        self.tables_order()

        ####################  L A B E L S  ####################
        self.title.setGeometry(100, 20, 360, 50)
        self.logo_title.setGeometry(40, 20, 50, 50)
        self.background.setGeometry(10, 570, 1060, 90)
        self.quantity_products.setGeometry(30, 30, 350, 30)
        self.stock_value.setGeometry(650, 30, 200, 30)

        ####################  E N T R Y S  ####################
        # self.search.setGeometry(700, 25, 210, 40)

        #################### B U T T O N S ####################
        self.new_order.setGeometry(930, 25, 130, 40)
        
        ####################   T A B L E   #################### 
        self.table_order.setGeometry(10, 80, 1061, 480)

    def frame_new_order(self):
        self.add = QFrame(self.order_frame)
        self.add.setStyleSheet(
            '''
                QFrame{
                    background-color: #f8f8f8;
                    border: 2px solid;
                    border-color: #808080;
                    border-radius: 20px;
                }
            '''
        )
        self.add.setGeometry(130, 90, 800, 500)
        self.add.show()

        self.positions_widgets_add()

    def labels_add(self):
        self.style_subtitles = '''
            QLabel{
                border: none;
                background: none;
                color: #000000;
                font: Helvetica Neue Leve;
                font-size: 20px;
            }
        '''

        self.title = QLabel('Adicionar pacote', self.add)
        self.title.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 25px;
                }
            '''
        )
        self.title.show()

        self.description = QLabel('Descrição:', self.add)
        self.description.setStyleSheet(self.style_subtitles)
        self.description.show()

        self.amount = QLabel('Quantidade:', self.add)
        self.amount.setStyleSheet(self.style_subtitles)
        self.amount.show()

        self.weight = QLabel('Peso:', self.add)
        self.weight.setStyleSheet(self.style_subtitles)
        self.weight.show()

        self.arrival_date = QLabel('Chegada:', self.add)
        self.arrival_date.setStyleSheet(self.style_subtitles)
        self.arrival_date.show()

        self.category = QLabel('Categoria:', self.add)
        self.category.setStyleSheet(self.style_subtitles)
        self.category.show()

        self.unitary = QLabel('Valor unitário:', self.add)
        self.unitary.setStyleSheet(self.style_subtitles)
        self.unitary.show()

    def entrys_add(self):
        self.style_entrys = '''
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
        
        self.description_get = QLineEdit(self.add)
        self.description_get.setStyleSheet(self.style_entrys)
        self.description_get.show()

        self.amount_get = QLineEdit(self.add)
        self.amount_get.setStyleSheet(self.style_entrys)
        self.amount_get.show()

        self.weight_get = QLineEdit(self.add)
        self.weight_get.setStyleSheet(self.style_entrys)
        self.weight_get.show()

        self.arrival_date_get = QLineEdit(self.add)
        self.arrival_date_get.setStyleSheet(self.style_entrys)
        self.arrival_date_get.show()

        self.category_get = QLineEdit(self.add)
        self.category_get.setStyleSheet(self.style_entrys)
        self.category_get.show()

        self.unitary_get = QLineEdit(self.add)
        self.unitary_get.setStyleSheet(self.style_entrys)
        self.unitary_get.show()

    def button_add(self):
        self.add_button = QPushButton('ADICIONAR', self.add)
        self.add_button.setStyleSheet(
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
        self.add_button.clicked.connect(self.insert_values_table_order)
        self.add_button.show()

        self.question_style_button = '''
            QToolButton{
                background-color: none;
                border-radius: 4px
            }
            QToolButton:hover{
                background-color: rgba(255, 255, 255, 0.5);
            }
        '''
        
        self.close = QToolButton(self.add)
        self.close.setIcon(QIcon('Images/main_frames/order/close.png'))
        self.close.setIconSize(QSize(20, 20))
        self.close.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.close.setStyleSheet(
            '''
                QToolButton{
                    background-color: none;
                    border-radius: 4px
                }
                QToolButton:hover{
                    background-color: rgba(255, 255, 255, 0.5);
                }
            '''
        )
        self.close.clicked.connect(lambda: self.add.deleteLater())
        self.close.show()

    def positions_widgets_add(self):
        self.labels_add()
        self.entrys_add()
        self.button_add()

        #################### L A B E L S ####################
        self.title.setGeometry(300, 30, 350, 40)
        self.description.setGeometry(80, 100, 150, 40)
        self.amount.setGeometry(300, 100, 150, 40)
        self.weight.setGeometry(520, 100, 150, 40)
        self.arrival_date.setGeometry(80, 230, 150, 40)
        self.category.setGeometry(300, 230, 200, 40)
        self.unitary.setGeometry(520, 230, 200, 40)

        #################### E N T R Y S ####################
        self.description_get.setGeometry(80, 150, 200, 40)
        self.amount_get.setGeometry(300, 150, 200, 40)
        self.weight_get.setGeometry(520, 150, 200, 40)
        self.arrival_date_get.setGeometry(80, 280, 200, 40)
        self.category_get.setGeometry(300, 280, 200, 40)
        self.unitary_get.setGeometry(520, 280, 200, 40)

        #################### B U T T O N ####################
        self.add_button.setGeometry(310, 400, 180, 40)
        self.close.setGeometry(750, 20, 30, 30)

    def error_frame(self):
        self.frame_error = QFrame(self.order_frame)
        self.frame_error.setMaximumSize(QSize(450, 35))
        self.frame_error.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_error.setFrameShape(QFrame.StyledPanel)
        self.frame_error.setFrameShadow(QFrame.Raised)
        self.frame_error.setGeometry(330, 15, 450, 40)
        self.frame_error.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_error)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_error = QLabel('Dados incorretos', self.frame_error)
        self.label_error.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_error.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_error)

        self.pushButton_close_popup = QPushButton(self.frame_error)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_error.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_error.deleteLater)

    def confirmation_frame(self):
        self.frame_confirmation = QFrame(self.order_frame)
        self.frame_confirmation.setMaximumSize(QSize(450, 35))
        self.frame_confirmation.setStyleSheet('''
            QFrame{
                background-color: #cd6600; 
                border-radius: 5px;
            }
        ''')
        self.frame_confirmation.setFrameShape(QFrame.StyledPanel)
        self.frame_confirmation.setFrameShadow(QFrame.Raised)
        self.frame_confirmation.setGeometry(330, 15, 450, 40)
        self.frame_confirmation.show()

        self.horizontalLayout_3 = QHBoxLayout(self.frame_confirmation)
        self.horizontalLayout_3.setContentsMargins(10, 3, 10, 3)

        self.label_confirmation = QLabel('Cadastro concluído', self.frame_confirmation)
        self.label_confirmation.setStyleSheet('''
            QLabel{
                color: #ffffff; 
                font-size: 17px; 
                font: bold 'Verdana';
            }
        ''')
        self.label_confirmation.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_confirmation)

        self.pushButton_close_popup = QPushButton(self.frame_confirmation)
        self.pushButton_close_popup.setMaximumSize(QSize(20, 20))
        self.pushButton_close_popup.setStyleSheet('''
            QPushButton{
                border-radius: 4px;
                background-image: url('Images/main_frames/quotation/quit.png');
                background-position: center;
                background-color: none;
                background-color: #363636;
            }
        ''')
        self.pushButton_close_popup.clicked.connect(lambda: self.frame_confirmation.deleteLater())
        self.horizontalLayout_3.addWidget(self.pushButton_close_popup)

        QTimer.singleShot(3000, self.frame_confirmation.deleteLater)


class Localization(Clossed, TrackBack):
    def frame_localization(self):
        self.closed_main_frames()
        self.frame_screening.hide()
        self.localization_frame = QFrame(self.first_window)
        self.localization_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.localization_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.localization_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.localization_frame, 2, 0)
        self.localization_frame.show()

        self.position_widgets_localization()

    def labels_localization(self):
        self.title_track = QLabel('Deseja aconpanhar sua encomenda?', self.localization_frame)
        self.title_track.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 25px;
                }
            '''
        )
        self.title_track.show()

        self.subtitle_question = QLabel('Digite seu código de rastramento', self.localization_frame)
        self.subtitle_question.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: #000000;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            '''
        )
        self.subtitle_question.show()

    def entrys_localization(self):
        self.tracking_code = QLineEdit(self.localization_frame)
        self.tracking_code.setPlaceholderText('AA12345678BR')
        self.tracking_code.setStyleSheet(
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
        self.tracking_code.show()

    def button_localization(self):
        self.calculate = QPushButton('CALCULAR', self.localization_frame)
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
        self.calculate.clicked.connect(self.request_localization)
        self.calculate.show()

    def results_localization(self):
        self.background = QFrame(self.localization_frame)
        self.background.setStyleSheet(
            '''
                QFrame{
                    background-color: #f8f8f8;
                    border: 2px solid #909090;
                    border-radius: 20px;
                }
            '''
        )
        self.background.show()

        self.subtitle_result = QLabel('RESULTADO', self.background)
        self.subtitle_result.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: #000000;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            '''
        )
        self.subtitle_result.show()

        self.scroll_area = QScrollArea(self.background)
        self.horizontal_layout = QHBoxLayout(self.background)
        self.scroll_area.setGeometry(10, 70, 960, 320)

        self.label_result = QLabel(self.scroll_area)
        self.label_result.setMinimumSize(960, 320)
        self.label_result.setStyleSheet(
            '''
                QLabel{
                    border: none;
                    background: none;
                    color: #000000;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            ''')
        self.horizontal_layout.addWidget(self.label_result)

    def position_widgets_localization(self):
        self.labels_localization()
        self.entrys_localization()
        self.results_localization()
        self.button_localization()

        ####################  L A B E L S  ####################
        self.title_track.setGeometry(310, 20, 460, 50)
        self.subtitle_question.setGeometry(380, 80, 400, 50)

        ####################  E N T R Y S  ####################
        self.tracking_code.setGeometry(360, 125, 340, 40)

        #################### B U T T O N S ####################
        self.calculate.setGeometry(450, 175, 200, 40)

        #################### R E S U L T S ####################
        self.background.setGeometry(50, 240, 980, 400)
        self.subtitle_result.setGeometry(430, 20, 120, 40)


class User(Clossed, ImagePerfil):
    def frame_user(self):
        self.closed_main_frames()
        self.frame_options.hide()
        self.user_frame = QFrame(self.first_window)
        self.user_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.user_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.user_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.user_frame, 2, 0)
        self.user_frame.show()

        self.position_widgets_user()

    def labels_user(self):
        self.style_informations = '''
            QLabel{
                background: none;
                color: #000000;
                font: bold 'Helvetica Neue Leve';
                font-size: 20px;
            }
        '''

        self.title_information_user = QLabel('Informações da conta', self.user_frame)
        self.title_information_user.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 30px;
                }
            '''
        )
        self.title_information_user.show()

        self.name = QLabel('Nome:', self.user_frame)
        self.name.setStyleSheet(self.style_informations)
        self.name.show()

        self.date = QLabel('Data de nascimento:', self.user_frame)
        self.date.setStyleSheet(self.style_informations)
        self.date.show()

        self.id = QLabel('Identificador:', self.user_frame)
        self.id.setStyleSheet(self.style_informations)
        self.id.show()

        self.phone = QLabel('Telefone celular:', self.user_frame)
        self.phone.setStyleSheet(self.style_informations)
        self.phone.show()

        self.email = QLabel('E-mail para login:', self.user_frame)
        self.email.setStyleSheet(self.style_informations)
        self.email.show()
        
        self.office = QLabel('Cargo:', self.user_frame)
        self.office.setStyleSheet(self.style_informations)
        self.office.show()

        self.admission = QLabel('Admissão:', self.user_frame)
        self.admission.setStyleSheet(self.style_informations)
        self.admission.show()

    def image_perfil(self):
        self.image = QToolButton(self.user_frame)
        self.image.setToolTip('Mudar foto de perfil')
        self.image.setStyleSheet(
            '''
               QToolButton{
                    background-image: url(Images/main_frames/user/adicionar.png);
                    background-repeat: no-repeat;
                    background-position: center center;
                    border: 1px solid #f7f7f7;
                    border-radius: 100px;
                }
            '''
        )
        self.image.clicked.connect(self.getImage)
        self.image.show()

    def position_widgets_user(self):
        self.labels_user()
        self.image_perfil()

        #################### L A B E L S ####################
        self.title_information_user.setGeometry(370, 20, 350, 40)
        self.name.setGeometry(520, 130, 200, 40)
        self.date.setGeometry(520, 200, 210, 40)
        self.id.setGeometry(520, 270, 200, 40)
        self.phone.setGeometry(300, 360, 200, 40)
        self.email.setGeometry(300, 430, 200, 40)
        self.office.setGeometry(300, 500, 200, 40)
        self.admission.setGeometry(300, 570, 200, 40)

        ####################   I M A G E   ####################
        self.image.setGeometry(250, 115, 200, 200)


class Employee(Clossed):
    def frame_employee(self):
        self.closed_main_frames()
        self.frame_options.hide()
        self.employee_frame = QFrame(self.first_window)
        self.employee_frame.setFrameShape(QFrame.Shape.NoFrame)
        self.employee_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.employee_frame.setStyleSheet(
            '''
                QFrame{
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.employee_frame, 2, 0)
        self.employee_frame.show()

        self.positions_widgets_emplyee()

    def labels_employee(self):
        self.title_frame = QLabel('Funcionários', self.employee_frame)
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

        self.logo_title = QLabel(self.employee_frame)
        self.image_logo_title = QPixmap('Images/main_frames/empoyee/empoyee.png')
        self.logo_title.setStyleSheet(
            '''
                QLabel{
                    background: none;
                }
            '''
        )
        self.logo_title.setPixmap(self.image_logo_title)
        self.logo_title.show()

    def buttons_and_entrys_employee(self):
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

        self.search = QLineEdit(self.employee_frame)
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

        self.new = QPushButton('Novo', self.employee_frame)
        self.new.setStyleSheet(self.style_buttons)
        self.new.show()

        self.delete = QPushButton('Deletar', self.employee_frame)
        self.delete.setStyleSheet(self.style_buttons)
        self.delete.show()

        self.edit = QPushButton('Editar', self.employee_frame)
        self.edit.setStyleSheet(self.style_buttons)
        self.edit.show()

    def table_employee(self):
        self.employee_table = QTableWidget(self.employee_frame)
        self.employee_table.setRowCount(1)
        self.employee_table.setColumnCount(7)
        self.employee_table.verticalHeader().setDefaultSectionSize(50)
        self.employee_table.horizontalHeader().setDefaultSectionSize(130)

        self.titles = ['ID', 'NOME', 'DATA DE\nNASCIMENTO', 'CARGO', 'E-MAIL', 'TELEFONE', 'ADMISSÃO']
        self.employee_table.setHorizontalHeaderLabels(list(self.titles))

        self.employee_table.setStyleSheet(
            '''
                QTableWidget{
                    gridline-color: #cd6600;
                    background-color: transparent;
                    outline: 0;
                    border: 1px solid #cd6600;
                    border-top: 1px
                }
                QTableWidget::item:selected{
                    background-color:#cd6600;;
                }
                QTableWidget::horizontalHeader{    
                    background-color: #cd6600;
                }
                QHeaderView::section:horizontal{
                    border: 1px solid #cd6600;
                    background-color: transparent;
                    border-left: 0px;
                    color: black;
                }
            '''
        )
        self.employee_table.show()

    def positions_widgets_emplyee(self):
        self.labels_employee()
        self.buttons_and_entrys_employee()
        self.table_employee()

        ####################      L A B E L S     ####################
        self.title_frame.setGeometry(150, 20, 400, 50)
        self.logo_title.setGeometry(80, 20, 50, 50)

        ####################  BUTTONS AND ENTRYS  ####################
        self.search.setGeometry(790, 25, 210, 40)
        self.new.setGeometry(190, 600, 200, 40)
        self.delete.setGeometry(440, 600, 200, 40)
        self.edit.setGeometry(690, 600, 200, 40)

        ####################      T A B L E       ####################
        self.employee_table.setGeometry(70, 80, 931, 470)


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
                    background-color: #ffffff;
                }
            '''
        )
        self.layout.addWidget(self.settings_frame, 2, 0)
        self.settings_frame.show()

        self.labels_system()

    def labels_system(self):
        self.title_name = QLabel('TrazPRO', self.settings_frame)
        self.title_name.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: bold 'Helvetica Neue Leve';
                    font-size: 30px
                }
            '''
        )
        self.title_name.setGeometry(470, 170, 200, 50)
        self.title_name.show()

        self.logo = QLabel(self.settings_frame)
        self.logo.setStyleSheet(
            '''
                QLabel{
                    background-image: url('Images/main_frames/system/logo.png');
                    background-repeat: no-repeat;
                    background-position: center center;
                }
            '''
        )
        self.logo.setGeometry(460, 250, 150, 150)
        self.logo.show()

        self.version = QLabel('Versão Beta', self.settings_frame)
        self.version.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #000000;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            '''
        )
        self.version.setGeometry(480, 430, 150, 50)
        self.version.show()

        self.creator = QLabel('Create by MVictor', self.settings_frame)
        self.creator.setStyleSheet(
            '''
                QLabel{
                    background: none;
                    color: #808080;
                    font: Helvetica Neue Leve;
                    font-size: 20px;
                }
            '''
        )
        self.creator.setGeometry(880, 610, 200, 50)
        self.creator.show()
