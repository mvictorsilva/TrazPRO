from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *


class Clossed():
    def closed_main_frames(self):
        self.quotation_frame.hide()
        self.deadline_frame.hide()
        self.order_frame.hide()
        self.localization_frame.hide()
        self.user_frame.hide()
        self.notification_frame.hide()
        self.settings_frame.hide()


class Quotation():
    def frame_quotation(self):
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
        self.title_frame.setMinimumSize(500, 50)
        self.title_frame.setMaximumSize(500, 50)
        self.title_frame.setStyleSheet('''
            QLabel{
                background: none;
                color: #000000;
                font: Helvetica Neue Leve;
                font-size: 25px;
            }
        ''')
        self.title_frame.show()

        self.cep_source = QLabel('CEP de origem', self.quotation_frame)
        self.cep_source.setMinimumSize(100, 50)
        self.cep_source.setMaximumSize(100, 50)
        self.cep_source.setStyleSheet(self.font_style_subtitle)
        self.cep_source.show()

        self.cep_destiny = QLabel('CEP de destino', self.quotation_frame)
        self.cep_destiny.setMinimumSize(100, 50)
        self.cep_destiny.setMaximumSize(100, 50)
        self.cep_destiny.setStyleSheet(self.font_style_subtitle)
        self.cep_destiny.show()

        self.order_value = QLabel('Valor da encomenda', self.quotation_frame)
        self.order_value.setMinimumSize(100, 50)
        self.order_value.setMaximumSize(100, 50)
        self.order_value.setStyleSheet(self.font_style_subtitle)
        self.order_value.show()

        self.service = QLabel('Serviço', self.quotation_frame)
        self.service.setMinimumSize(100, 50)
        self.service.setMaximumSize(100, 50)
        self.service.setStyleSheet(self.font_style_subtitle)
        self.service.show()

        self.order_format = QLabel('Formato da encomenda', self.quotation_frame)
        self.order_format.setMinimumSize(100, 50)
        self.order_format.setMaximumSize(100, 50)
        self.order_format.setStyleSheet(self.font_style_subtitle)
        self.order_format.show()

        self.order_weight = QLabel('CEP de origem', self.quotation_frame)
        self.order_weight.setMinimumSize(100, 50)
        self.order_weight.setMaximumSize(100, 50)
        self.order_weight.setStyleSheet(self.font_style_subtitle)
        self.order_weight.show()

        self.subtitle_specifications = QLabel('Especificações da embalagem', self.quotation_frame)
        self.subtitle_specifications.setMinimumSize(500, 50)
        self.subtitle_specifications.setMaximumSize(500, 50)
        self.subtitle_specifications.setStyleSheet('''
            QLabel{
                background: none:
                color: #000000;
                font: Helvetica Neue Leve;
                font-size: 22;
            }
        ''')
        self.subtitle_specifications.show()

        self.lenght = QLabel('Comprimento:', self.quotation_frame)
        self.lenght.setMinimumSize(100, 50)
        self.lenght.setMaximumSize(100, 50)
        self.lenght.setStyleSheet(self.font_style_subtitle)
        self.lenght.show()

        self.height = QLabel('Altura:', self.quotation_frame)
        self.height.setMinimumSize(100, 50)
        self.height.setMaximumSize(100, 50)
        self.height.setStyleSheet(self.font_style_subtitle)
        self.height.show()

        self.width = QLabel('Largura:', self.quotation_frame)
        self.width.setMinimumSize(100, 50)
        self.width.setMaximumSize(100, 50)
        self.width.setStyleSheet(self.font_style_subtitle)
        self.width.show()

        self.diameter = QLabel('Diâmetro', self.quotation_frame)
        self.diameter.setMinimumSize(100, 50)
        self.diameter.setMaximumSize(100, 50)
        self.diameter.setStyleSheet(self.font_style_subtitle)
        self.diameter.show()

        self.question_ownhand = QLabel('Mão própria:', self.quotation_frame)
        self.question_ownhand.setMinimumSize(100, 50)
        self.question_ownhand.setMaximumSize(100, 50)
        self.question_ownhand.setStyleSheet(self.font_style_subtitle)
        self.question_ownhand.show()

        self.question_receivement = QLabel('Aviso de recebimento', self.quotation_frame)
        self.question_receivement.setMinimumSize(100, 50)
        self.question_receivement.setMaximumSize(100, 50)
        self.question_receivement.setStyleSheet(self.font_style_subtitle)
        self.question_receivement.show()

    def position_grid(self):
        #################### L A B E L S ####################
        self.grid_layout_quotation.addWidget(self.title_frame, 0, 0, Qt.AlignCenter)
        

class Deadline():
    def frame_deadline(self):
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


class Order():
    def frame_order(self):
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


class Localization():
    def frame_localization(self):
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


class User():
    def frame_user(self):
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


class Notification():
    def frame_notification(self):
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


class Settings():
    def frame_settings(self):
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
