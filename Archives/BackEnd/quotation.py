import requests


class CalculateValue():
    def clear_entrys(self):
        self.cep_source_get.clear()
        self.cep_destiny_get.clear()
        self.order_value_get.clear()
        self.order_weight_get.clear()
        self.lenght_get.clear()
        self.height_get.clear()
        self.width_get.clear()
        self.diameter_get.clear()

    def clear_radio_buttons(self):

        self.package_format_radio.isChecked(False)
        self.cylinder_format_radio.setCheckable(False)
        self.letter_format_radio.setCheckable(False)

        self.yes_radio_button.setCheckable(False)
        self.no_radio_button.setCheckable(False)

        self.yes_radio_buttonii.setCheckable(False)
        self.no_radio_buttonii.setCheckable(False)

    def handle_errors(self):
        self.entrys_style_ative = '''
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

        self.entrys_style_ii_ative = '''
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

        self.entrys_style_desative = '''
                    QLineEdit{
                        background-color: rgba(0, 0, 0, 0);
                        color: #707070;
                        border: 2px solid #808080;
                        border-radius: 10px;
                        font: 'Helvetica';
                        font-size: 18px;
                    }
                    QLineEdit:pressed{
                        color: #000000;
                    }
                '''

        self.entrys_style_ii_desative = '''
                    QLineEdit{
                        background-color: rgba(0, 0, 0, 0);
                        border: 2px solid;
                        border-top-color: none;
                        border-left-color: none;
                        border-right-color: none;
                        border-bottom-color: #808080;
                        font: 'Helvetica';
                        font-size: 18px;
                    }
                '''

        #### RADIO BUTTONS FORMAT ####
        def package():
            self.order_weight_get.setDisabled(False)
            self.order_weight_get.setStyleSheet(self.entrys_style_ative)

            self.diameter_get.setDisabled(False)
            self.diameter_get.setStyleSheet(self.entrys_style_ii_ative)

            self.height_get.setDisabled(False)
            self.height_get.setStyleSheet(self.entrys_style_ii_ative)

            self.diameter_get.setDisabled(True)
            self.diameter_get.setStyleSheet(self.entrys_style_ii_desative)

            self.width_get.setDisabled(False)
            self.width_get.setStyleSheet(self.entrys_style_ii_ative)

        def cylinder():
            self.order_weight_get.setDisabled(False)
            self.order_weight_get.setStyleSheet(self.entrys_style_ative)

            self.diameter_get.setDisabled(False)
            self.diameter_get.setStyleSheet(self.entrys_style_ii_ative)

            self.height_get.setDisabled(False)
            self.height_get.setStyleSheet(self.entrys_style_ii_ative)

            self.diameter_get.setDisabled(False)
            self.diameter_get.setStyleSheet(self.entrys_style_ii_ative)

            self.width_get.setDisabled(True)
            self.width_get.setStyleSheet(self.entrys_style_ii_desative)

            self.height_get.setDisabled(True)
            self.height_get.setStyleSheet(self.entrys_style_ii_desative)

        def letter():
            self.order_weight_get.setDisabled(True)
            self.order_weight_get.setStyleSheet(self.entrys_style_desative)

            self.diameter_get.setDisabled(True)
            self.diameter_get.setStyleSheet(self.entrys_style_ii_desative)

            self.height_get.setDisabled(True)
            self.height_get.setStyleSheet(self.entrys_style_ii_desative)

            self.width_get.setDisabled(False)
            self.width_get.setStyleSheet(self.entrys_style_ii_ative)

        self.package_format_radio.clicked.connect(package)
        self.cylinder_format_radio.clicked.connect(cylinder)
        self.letter_format_radio.clicked.connect(letter)

    def variables(self):
        #### ENTRYS ####
        self.cep_source = self.cep_source_get.text()
        self.cep_destiny = self.cep_destiny_get.text()
        self.order_value = self.order_value_get.text()
        self.order_weight = self.order_weight_get.text()
        self.lenght = self.lenght_get.text()
        self.height = self.height_get.text()
        self.width = self.width_get.text()
        self.diameter = self.diameter_get.text()

        if self.order_value == '':
            self.order_value = '0'

        #### COMBO BOX ####
        if self.service_box.currentText() == 'SEDEX':
            self.service = '04014'
        elif self.service_box.currentText() == 'SEDEX 10':
            self.service == '04782'
        elif self.service_box.currentText() == 'SEDEX 12':
            self.service = '04782'
        elif self.service_box.currentText() == 'SEDEX Hoje':
            self.service = '04804'
        elif self.service_box.currentText() == 'PAC':
            self.service = '04510'

        #### RADIO BUTTONS FORMAT ####
        if self.package_format_radio.isChecked():
            self.diameter = '0'
            self.format = '1'
        elif self.cylinder_format_radio.isChecked():
            self.width = '0'
            self.height = '0'
            self.format = '2'
        elif self.letter_format_radio.isChecked():
            self.order_weight = '1'
            self.diameter = '0'
            self.height = '0'
            self.format = '3'
        else:
            pass

        #### RADIO BUTTONS OWN HAND ####
        if self.yes_radio_button.isChecked():
            self.own_hand = 's'

        elif self.no_radio_button.isChecked():
            self.own_hand = 'n'
        else:
            pass

        #### RADIO BUTTONS EARLY WARNING ####
        if self.yes_radio_buttonii.isChecked():
            self.early_warning = 's'
        elif self.no_radio_buttonii.isChecked():
            self.early_warning = 'n'
        else:
            pass

    def send_data(self):
        try:
            self.variables()

            url = "http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?" \
                  "nCdEmpresa=&" \
                  "sDsSenha=&" \
                  f"sCepOrigem={self.cep_source}&" \
                  f"sCepDestino={self.cep_destiny}&" \
                  f"nVlPeso={self.order_weight}&" \
                  f"nCdFormato={self.format}&" \
                  f"nVlComprimento={self.lenght}&" \
                  f"nVlAltura={self.height}&" \
                  f"nVlLargura={self.width}&" \
                  f"sCdMaoPropria={self.own_hand}&" \
                  f"nVlValorDeclarado={self.order_value}&" \
                  f"sCdAvisoRecebimento={self.early_warning}&" \
                  f"nCdServico={self.service}&" \
                  f"nVlDiametro={self.diameter}&" \
                  "StrRetorno=xml&nIndicaCalculo=3"

            self.request = requests.post(url=url)
            self.values = self.request.text
        except:
            pass

    def receive_data(self):
        self.send_data()
        self.startAnimation()

        try:
            self.find_start_value = '<Valor>'
            self.find_end_value = '</Valor>'
            self.position_start = int(self.values.index(self.find_start_value) + len(self.find_start_value))
            self.position_end = int(self.values.index(self.find_end_value))
            self.value = self.values[self.position_start: self.position_end]

            self.find_start_deadline = '<PrazoEntrega>'
            self.find_end_deadline = '</PrazoEntrega>'
            self.position_start = int(self.values.index(self.find_start_deadline) + len(self.find_start_deadline))
            self.position_end = int(self.values.index(self.find_end_deadline))
            self.deadline = self.values[self.position_start: self.position_end]

            self.find_start_no_additional = '<ValorSemAdicionais>'
            self.find_end_no_additional = '</ValorSemAdicionais>'
            self.position_start = int(
                self.values.index(self.find_start_no_additional) + len(self.find_start_no_additional))
            self.position_end = int(self.values.index(self.find_end_no_additional))
            self.no_additional = self.values[self.position_start: self.position_end]

            self.find_start_own_hand = '<ValorMaoPropria>'
            self.find_end_own_hand = '</ValorMaoPropria>'
            self.position_start = int(self.values.index(self.find_start_own_hand) + len(self.find_start_own_hand))
            self.position_end = int(self.values.index(self.find_end_own_hand))
            self.own_hand = self.values[self.position_start: self.position_end]

            self.find_start_early_warning = '<ValorAvisoRecebimento>'
            self.find_end_early_warning = '</ValorAvisoRecebimento>'
            self.position_start = int(self.values.index(self.find_start_early_warning) + len(self.find_start_early_warning))
            self.position_end = int(self.values.index(self.find_end_early_warning))
            self.early_warning = self.values[self.position_start: self.position_end]

            self.find_start_declared_value = '<ValorValorDeclarado>'
            self.find_end_declared_value = '</ValorValorDeclarado>'
            self.position_start = int(self.values.index(self.find_start_declared_value) + len(self.find_start_declared_value))
            self.position_end = int(self.values.index(self.find_end_declared_value))
            self.declared_value = self.values[self.position_start: self.position_end]

            self.find_start_home_delivery = '<EntregaDomiciliar>'
            self.find_end_home_delivery = '</EntregaDomiciliar>'
            self.position_start = int(self.values.index(self.find_start_home_delivery) + len(self.find_start_home_delivery))
            self.position_end = int(self.values.index(self.find_end_home_delivery))
            self.home_delivery = self.values[self.position_start: self.position_end]

            self.find_start_weekend_delivery = '<EntregaSabado>'
            self.find_end_weekend_delivery = '</EntregaSabado>'
            self.position_start = int(self.values.index(self.find_start_weekend_delivery) + len(self.find_start_weekend_delivery))
            self.position_end = int(self.values.index(self.find_end_weekend_delivery))
            self.weekend_delivery = self.values[self.position_start: self.position_end]

            self.clear_entrys()

            if self.home_delivery == 'S':
                self.home_delivery = 'Sim'
            else:
                self.home_delivery = 'Não'

            if self.weekend_delivery == 'S':
                self.weekend_delivery = 'Sim'
            else:
                self.weekend_delivery = 'Não'

            self.value = f'R$ {self.value}'
            self.deadline = f'{self.deadline} dias'
            self.no_additional = f'R$ {self.no_additional}'
            self.own_hand = f'R$ {self.own_hand}'
            self.early_warning = f'R$ {self.early_warning}'
            self.declared_value = f'R$ {self.declared_value}'
            self.home_delivery = f'{self.home_delivery}'
            self.weekend_delivery = f'{self.weekend_delivery}'

            self.stopAnimation()
            self.result_frame()

        except:
            self.stopAnimation()
            self.error_frame()
