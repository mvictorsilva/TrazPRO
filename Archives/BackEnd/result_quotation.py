import requests

class Calculation():
    def variables(self):
        self.entrys_quotation()

        self.cep_source_get2 = self.cep_source_get.text()
        self.cep_destiny_get2 = self.cep_destiny_get.text()
        self.order_value_get2 = self.order_value_get.text()
        self.order_weight_get2 = self.order_weight_get.text()
        self.lenght_get2 = self.lenght_get.text()
        self.height_get2 = self.height_get.text()
        self.width_get2 = self.width_get.text()
        self.diameter_get2 = self.diameter_get.text()

    def teste(self):
        self.variables()

        print(self.cep_source_get2)
        print(self.cep_destiny_get2)
        print(self.order_value_get2)
        




# request = requests.post(f"""
# http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa=&sDsSenha=&sCepOrigem=70002900&sCepDestino=04547000&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3""")

# values = request.text

# find_start_value = '<Valor>'
# find_end_value = '</Valor>'
# position_start = int(values.index(find_start_value) + len(find_start_value))
# position_end = int(values.index(find_end_value))
# value = values[position_start : position_end]

# find_start_deadline = '<PrazoEntrega>'
# find_end_deadline = '</PrazoEntrega>'
# position_start = int(values.index(find_start_deadline) + len(find_start_deadline))
# position_end = int(values.index(find_end_deadline))
# deadline = values[position_start : position_end]

# find_start_deadline = '<PrazoEntrega>'
# find_end_deadline = '</PrazoEntrega>'
# position_start = int(values.index(find_start_deadline) + len(find_start_deadline))
# position_end = int(values.index(find_end_deadline))
# deadline = values[position_start : position_end]

# find_start_no_additional = '<ValorSemAdicionais>'
# find_end_no_additional = '</ValorSemAdicionais>'
# position_start = int(values.index(find_start_no_additional) + len(find_start_no_additional))
# position_end = int(values.index(find_end_no_additional))
# no_additional = values[position_start : position_end]

# find_start_own_hand = '<ValorMaoPropria>'
# find_end_own_hand = '</ValorMaoPropria>'
# position_start = int(values.index(find_start_own_hand) + len(find_start_own_hand))
# position_end = int(values.index(find_end_own_hand))
# own_hand = values[position_start : position_end]

# find_start_early_warning = '<ValorAvisoRecebimento>'
# find_end_early_warning = '</ValorAvisoRecebimento>'
# position_start = int(values.index(find_start_early_warning) + len(find_start_early_warning))
# position_end = int(values.index(find_end_early_warning))
# early_warning = values[position_start : position_end]

# find_start_declared_value = '<ValorValorDeclarado>'
# find_end_declared_value = '</ValorValorDeclarado>'
# position_start = int(values.index(find_start_declared_value) + len(find_start_declared_value))
# position_end = int(values.index(find_end_declared_value))
# declared_value = values[position_start : position_end]

# find_start_home_delivery = '<EntregaDomiciliar>'
# find_end_home_delivery = '</EntregaDomiciliar>'
# position_start = int(values.index(find_start_home_delivery) + len(find_start_home_delivery))
# position_end = int(values.index(find_end_home_delivery))
# home_delivery = values[position_start : position_end]

# find_start_weekend_delivery = '<EntregaSabado>'
# find_end_weekend_delivery = '</EntregaSabado>'
# position_start = int(values.index(find_start_weekend_delivery) + len(find_start_weekend_delivery))
# position_end = int(values.index(find_end_weekend_delivery))
# weekend_delivery = values[position_start : position_end]

# print(value)
# print(deadline)
# print(no_additional)
# print(own_hand)
# print(early_warning)
# print(declared_value)
# print(home_delivery)
# print(weekend_delivery)
