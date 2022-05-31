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

        self.grid_layout_quotation = QGridLayout()
        self.quotation_frame.setLayout(self.grid_layout_quotation)

        self.labels_quotation()
        self.entrys_quotation()
        self.radio_buttons()
        self.buttons_quotation()
        self.combo_box_quotation()
        self.space_widgets_quotation()
        self.position_grid()

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
        self.order_value_get.setPlaceholderText('999,99')
        self.order_value_get.setMaxLength(8)
        self.order_value_get.setStyleSheet(self.entrys_style)
        self.order_value_get.show()

        self.order_weight_get = QLineEdit(self.quotation_frame)
        self.order_weight_get.setMinimumSize(200, 40)
        self.order_weight_get.setMaximumSize(200, 40)
        self.order_weight_get.setPlaceholderText('Kg')
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
        self.group_box_ii.setMinimumSize(220, 80)
        self.group_box_ii.setMaximumSize(220, 80)
        self.group_box_ii.setStyleSheet('font-size: 20px; font: Helvetica Neue Leve;')
        self.hboxii = QHBoxLayout(self.group_box_ii)

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
        self.group_box_iii.setMinimumSize(220, 80)
        self.group_box_iii.setMaximumSize(220, 80)
        self.group_box_iii.setStyleSheet('font-size: 20px; font: Helvetica Neue Leve;')
        self.hboxiii = QHBoxLayout(self.group_box_iii)

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

    def space_widgets_quotation(self):
        self.spacer_widgets_top = QSpacerItem(30, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.spacer_widgets_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # self.spacer_title = QSpacerItem(10, 30, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        # self.spacer_subtitle = QSpacerItem(30, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        # self.spacer_subtitle_ii = QSpacerItem(70, 70, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.spacer_widgets_right = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.spacer_widgets_botton = QSpacerItem(30, 30, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

    def position_grid(self):
        ####################        S P A C E R       ####################
        self.grid_layout_quotation.addItem(self.spacer_widgets_top, 0, 5)
        self.grid_layout_quotation.addItem(self.spacer_widgets_left, 0, 0, 1, 1)
        # self.grid_layout_quotation.addItem(self.spacer_title, 2, 5)
        # self.grid_layout_quotation.addItem(self.spacer_subtitle, 7, 5)
        self.grid_layout_quotation.addItem(self.spacer_widgets_right, 0, 6, 1, 1)
        self.grid_layout_quotation.addItem(self.spacer_widgets_botton, 16, 5)
        ####################        L A B E L S       ####################
        self.grid_layout_quotation.addWidget(self.title_frame, 1, 1, 1, 5, Qt.AlignCenter)
        self.grid_layout_quotation.addWidget(self.cep_source, 3, 2, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.cep_destiny, 5, 2, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.order_value, 3, 4, Qt.AlignCenter)
        self.grid_layout_quotation.addWidget(self.service, 5, 4, Qt.AlignCenter)
        self.grid_layout_quotation.addWidget(self.order_weight, 5, 5, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.subtitle_specifications, 5, 1, 8, 5, Qt.AlignCenter)
        self.grid_layout_quotation.addWidget(self.lenght, 10, 2, Qt.AlignRight)
        self.grid_layout_quotation.addWidget(self.cm_i, 10, 4, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.height, 11, 2, Qt.AlignRight)
        self.grid_layout_quotation.addWidget(self.cm_ii, 11, 4, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.width, 12, 2, Qt.AlignRight)
        self.grid_layout_quotation.addWidget(self.cm_iii, 12, 4, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.diameter, 13, 2, Qt.AlignRight)
        self.grid_layout_quotation.addWidget(self.cm_iv, 13, 4, Qt.AlignLeft)
        ####################       E N T R Y S       ####################
        self.grid_layout_quotation.addWidget(self.cep_source_get, 4, 2, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.cep_destiny_get, 6, 2, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.order_value_get, 4, 4, Qt.AlignCenter)
        self.grid_layout_quotation.addWidget(self.order_weight_get, 6, 5, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.lenght_get, 10, 3, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.height_get, 11, 3, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.width_get, 12, 3, Qt.AlignRight)
        self.grid_layout_quotation.addWidget(self.diameter_get, 13, 3, Qt.AlignLeft)
        #################### R A D I O  B U T T O N S ####################
        self.grid_layout_quotation.addWidget(self.group_box_i, 3, 5, 0, 0, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.group_box_ii, 10, 5, 11, 0, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.group_box_iii, 12, 5, 13, 0, Qt.AlignLeft)
        ####################       B U T T O N S      ###################
        self.grid_layout_quotation.addWidget(self.question_i, 4, 3,Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.question_ii, 6, 3, Qt.AlignLeft)
        self.grid_layout_quotation.addWidget(self.calculate, 15, 1, 15, 5, Qt.AlignCenter)
        ###################      C O M B O  B O X     ####################
        self.grid_layout_quotation.addWidget(self.service_box, 6, 4, Qt.AlignCenter)

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
                    background-color: red;
                }
            '''
        )
        self.layout.addWidget(self.deadline_frame, 2, 0)
        self.deadline_frame.show()

        self.grid_layout_quotation = QGridLayout()
        self.deadline_frame.setLayout(self.grid_layout_quotation)


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
                    background-color: green;
                }
            '''
        )
        self.layout.addWidget(self.order_frame, 2, 0)
        self.order_frame.show()

        self.grid_layout_order = QGridLayout()
        self.order_frame.setLayout(self.grid_layout_order)


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

        self.grid_layout_localization = QGridLayout()
        self.localization_frame.setLayout(self.grid_layout_localization)


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

        self.grid_layout_user = QGridLayout()
        self.user_frame.setLayout(self.grid_layout_user)


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

        self.grid_layout_notification = QGridLayout()
        self.notification_frame.setLayout(self.grid_layout_notification)


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

        self.grid_layout_settings = QGridLayout()
        self.settings_frame.setLayout(self.grid_layout_settings)
