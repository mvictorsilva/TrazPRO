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

        except Error as erro:
            print('Connection error...')

    def disconnect_db(self):
        self.connect.close()


    def variables_register(self):
        self.name_register_get = self.name.text()
        self.email_register_get = self.email_register.text()
        self.password_register_get = self.password_register.text()

    def clear_entrys_register(self):
        self.name.clear()
        self.email_register.clear()
        self.password_register.clear()

    def create_new_user(self):
        self.variables_register()
        self.connect_db()

        try:
            if self.name_register_get  == '':
                self.error_frame()
            elif self.email_register_get == '':
                self.error_frame()
            elif self.password_register_get == '':
                self.error_frame()
            else:
                self.cursor.execute(
                    '''
                        insert into gerente (nome, email, senha)
                        values (%s, %s, %s)
                    ''',

                    (
                        self.name_register_get,
                        self.email_register_get,
                        self.password_register_get
                    )
                
                )

                self.connect.commit()
                self.confirmation_frame()
        except Error:
            self.error_frame()

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
            if self.email_login_get == '':
                self.error_frame()
            elif self.password_login_get == '':
                self.error_frame()
            else:
                self.cursor.execute(
                    f'''
                        select senha from gerente where email = '{self.email_login_get}'
                    '''
                )
                self.password_db = self.cursor.fetchall()

                self.cursor.execute(
                    f'''
                        select id_gerente from gerente where email = '{self.email_login_get}'
                    '''
                )
                self.id_gerente_db = self.cursor.fetchall()

                if self.password_login_get == self.password_db[0][0]:
                    self.id = self.id_gerente_db[0][0]
                    self.execute_navegation_bar()
                else:
                    print('user incorrect')
        except:
            pass

        self.clear_entrys_login()


    def send_new_password(self):
        email = self.email_question_get.text()
        new_password = secrets.token_urlsafe(4)

        try:
            email_sender = 'trazpro415@gmail.com'
            email_password = 'ajbaxqaqnihddxmq'
            email_receiver = f'{email}'

            subject = 'Mudança de senha TrazPRO'
            body = f'''
Olá!\n \nSua nova senha do aplicativo é: {new_password}
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
            self.background.deleteLater()
            self.question.deleteLater()
            self.password_change_notice()
        except:
            print('error...')

        self.disconnect_db()


    def variables_table_order(self):
        self.description_receive = self.description_get.text()
        self.amount_receive = int(self.amount_get.text())
        self.weight_receive = float(self.weight_get.text())
        self.arrival_receive = self.arrival_date_get.text()
        self.categor_receive = self.category_get.text()
        self.unitary_receive = float(self.unitary_get.text())

    def insert_values_table_order(self):
        self.variables_login()
        self.authorized_login_user()
        self.variables_table_order()

        if self.description_receive == '':
            self.error_frame()
        elif self.amount_receive == '':
            self.error_frame()
        elif self.weight_receive == '':
            self.error_frame()
        elif self.arrival_receive == '':
            self.error_frame()
        elif self.categor_receive == '':
            self.error_frame()
        elif self.unitary_receive == '':
            self.error_frame()
        else:
            self.cursor.execute(
                '''
                    insert into pacote (descrição, quantidade, peso, valor_unitario, data_chegada, nome_categoria)
                    values (%s, %s, %s, %s, %s, %s);
                ''',

                (
                    self.description_receive,
                    self.amount_receive,
                    self.weight_receive,
                    self.unitary_receive,
                    self.arrival_receive,
                    self.categor_receive
                )
            )
            self.connect.commit()

            self.cursor.execute(
                '''
                    select max(id_pacote) from pacote;
                '''
            )
            self.last_id_pacote = self.cursor.fetchall()

            self.cursor.execute(
                '''
                    insert into funcionario_pacote (id_funcionario, id_pacote)
                    values (%s, %s)
                ''',

                (
                    self.id,
                    self.last_id_pacote[0][0]
                )
            )
            self.connect.commit()

            self.add.deleteLater()
            self.confirmation_frame()
            self.fill_table_packages()

    def fill_table_packages(self):
        self.cursor.execute(
            f'''
                select * from pacote as p
                join funcionario_pacote as f on p.id_pacote = f.id_pacote
                where f.id_funcionario = '{self.id}';
            '''
        )
        self.packages = self.cursor.fetchall()

        self.table_order.setRowCount(len(self.packages))
        self.table_order.setColumnCount(8)

        for i in range(0, len(self.packages)):
            for j in range(0, 8):
                self.table_order.setItem(i, j, QTableWidgetItem(str(self.packages[i][j])))

        self.cursor.execute(
            '''
                select sum(quantidade) as total from pacote;
            '''
        )
        self.amount = self.cursor.fetchall()

        self.cursor.execute(
            '''
                select sum(valor_unitario) as total from pacote;
            '''
        )
        self.value = self.cursor.fetchall()

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

        self.quantity = QLabel(self.background)
        self.quantity.setText(f'{self.amount[0][0]}')
        self.quantity.setStyleSheet(self.style_results)
        self.quantity.show()

        self.stock = QLabel(self.background)
        self.stock.setText(f'{self.value[0][0]}')
        self.stock.setStyleSheet(self.style_results)
        self.stock.show()

        self.quantity.setGeometry(380, 30, 100, 30)
        self.stock.setGeometry(850, 30, 70, 30)
