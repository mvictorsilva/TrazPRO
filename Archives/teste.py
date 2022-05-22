# from urllib.request import Request, urlopen
# from urllib.parse import urlencode

# url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?'
# post_fields = 'nCdEmpresa=&sDsSenha=&sCepOrigem=70002900&sCepDestino=04547000&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3'

# request = Request(url,urlencode(post_fields).encode())
# result2 = urlopen(request).read()
# result=str(result2)
# print(result)


import requests
informacoes = '''{
        'nCdEmpresa': '',
        'sDsSenha': '',
        'nCdServico': '040140',
        'sCepOrigem': '75910110',
        'sCepDestino': '07042090',
        'nVlPeso': '1',
        'nCdFormato':'3',
        'nVlComprimento': '3',
        'nVlAltura': '0',
        'nVlLargura': '2',
        'nVlDiametro': '1',
        'sCdMaoPropria': 'N',
        'nVlValorDeclarado': '0',
        'sCdAvisoRecebimento': 'N'
    }'''

informaçoes2 = 'nCdEmpresa=08082650&sDsSenha=564321&sCepOrigem=70002900&sCepDestino=04547000&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3'

requests = requests.post('http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?', params=informaçoes2)
print(requests.text())


link = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?nCdEmpresa=08082650&sDsSenha=564321&sCepOrigem=70002900&sCepDestino=04547000&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3'
test = '''http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?
    nCdEmpresa=08082650&
    sDsSenha=564321&
    sCepOrigem=70002900&
    sCepDestino=04547000&
    nVlPeso=1&nCdFormato=1&
    nVlComprimento=20&
    nVlAltura=20&
    nVlLargura=20&
    sCdMaoPropria=n&
    nVlValorDeclarado=0&
    sCdAvisoRecebimento=n&
    nCdServico=04510&
    nVlDiametro=0&
    StrRetorno=xml&
    nIndicaCalculo=3
'''
