from msilib.schema import Error
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import *

import mysql.connector
from mysql.connector import Error

import secrets
import smtplib
import ssl
from email.message import EmailMessage


class DataBase:
    def connect_db(self):
        try:
            self.connect = mysql.connector.connect(
                user = 'root',
                host = '127.0.0.1',
                database = 'trazpro_db'
            )
            self.cursor = self.connect.cursor()
            print('MySQL Database connection successful')

        except Error as erro:
            print('Connection error...')

    def disconnect_db(self):
        self.connect.close()

    def variables_register(self):
        self.name_register_get = self.name.text()
        self.email__register_get = self.email_register.text()
        self.password_register_get = self.password_register.text()

    def clear_entrys_register(self):
        self.name.clear()
        self.email_register.clear()
        self.password_register.clear()

    def create_new_user(self):
        self.variables_register()
        self.connect_db()

        try:
            self.cursor.execute(
                '''
                    insert into gerente (nome, email, senha)
                    values (%s, %s, %s)
                ''',

                (
                    self.name_register_get,
                    self.email__register_get,
                    self.password_register_get
                )
            
            )

            self.connect.commit()
        except Error as erro:
            print(erro)

        self.clear_entrys_register()
        self.disconnect_db()

    def variables_login(self):
        self.email_login_get = self.email_login.text()
        self.password_login_get = self.password_login.text()

    def clear_entrys_login(self):
        self.email_login.clear()
        self.password_login.clear()

    def authorized_login_user(self):
        self.variables_login()
        self.connect_db()

        try:
            self.cursor.execute(
                f'''
                    select senha from gerente where email = '{self.email_login_get}'
                '''
            )
            self.password_db = self.cursor.fetchall()

            if self.password_login_get == self.password_db[0][0]:
                self.execute_navegation_bar()
            else:
                print('user incorrect')
        except:
            print('error')

        self.clear_entrys_login()
        self.disconnect_db()

    def send_new_password(self):
        email = self.email_question_get.text()
        new_password = secrets.token_urlsafe(4)

        try:
            email_sender = 'trazpro415@gmail.com'
            email_password = 'ajbaxqaqnihddxmq'
            email_receiver = f'{email}'

            subject = 'Mudança de senha TrazPRO'
            body = f'''
    Olá!\nSua nova senha do aplicativo é: {new_password}
            '''

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
        except:
            print('error...')

        self.connect_db()

        try:
            self.cursor.execute(
                '''
                    update gerente set senha = (%s) where email = (%s)
                ''',

                (
                    new_password,
                    email
                )
            )
        except:
            print('error...')

        self.disconnect_db()
        