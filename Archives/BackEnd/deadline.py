import requests


class CalculateDeadline:
    def requests_cep(self):
        try:
            cep = self.cep_get.text()
            request = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

            result = request.json()

            self.cep = result['cep']
            self.road = result['logradouro']
            self.complement = result['complemento']
            self.district= result['bairro']
            self.city = result['localidade']
            self.state = result['uf']

            self.cep_get.clear()
            self.result_frameii()

        except:
            self.error_frameii()


    def requests_deadline(self):
        try:
            self.cep_source = self.cep_source_get.text()
            self.cep_destiny = self.cep_destiny_get.text()

            self.request = requests.post(f"""
                https://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?
                nCdEmpresa=&sDsSenha=&sCepOrigem={self.cep_source}&sCepDestino={self.cep_destiny}&nVlPeso=1&nCdFormato=10&nVlComprimento=10&nVlAltura=10&nVlLargura=10&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04014&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3""")
            self.values = self.request.text

            self.find_start_deadline = '<PrazoEntrega>'
            self.find_end_deadline = '</PrazoEntrega>'
            self.position_start = int(self.values.index(self.find_start_deadline) + len(self.find_start_deadline))
            self.position_end = int(self.values.index(self.find_end_deadline))
            self.deadline = self.values[self.position_start: self.position_end]
            self.deadline = f'{self.deadline} dias'

            self.cep_source_get.clear()
            self.cep_destiny_get.clear()

            self.result_frameiii()


        except:
            self.error_frame()
