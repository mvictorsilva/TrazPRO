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
                    background-color: blue;
                }
            '''
        )
        self.layout.addWidget(self.quotation_frame, 2, 0)
        self.quotation_frame.show()

        self.grid_layout_quotation = QGridLayout()
        self.quotation_frame.setLayout(self.grid_layout_quotation)


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
