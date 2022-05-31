import requests

jac = int(input('dsdfsd:  '))

requests = requests.post(f"""
http://ws.correios.com.br/calculador/CalcPrecoPrazo.aspx?
nCdEmpresa=&
sDsSenha=&
sCepOrigem={jac}&
sCepDestino=04547000&nVlPeso=1&nCdFormato=1&nVlComprimento=20&nVlAltura=20&nVlLargura=20&sCdMaoPropria=n&nVlValorDeclarado=0&sCdAvisoRecebimento=n&nCdServico=04510&nVlDiametro=0&StrRetorno=xml&nIndicaCalculo=3""").json()

print(requests.text)
