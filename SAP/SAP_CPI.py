import requests
from requests.auth import HTTPBasicAuth

# URL do endpoint SOAP
url = "https://4beecdb1trial.it-cpitrial06-rt.cfapps.us10-001.hana.ondemand.com/cxf/aula03/soap"

# Cabeçalhos HTTP
headers = {
    "Content-Type": "text/xml; charset=utf-8",
    "SOAPAction": "http://tempuri.org/Add"  # Esse SOAPAction pode variar dependendo do serviço
}

# Corpo da requisição (XML)
soap_body = """<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
   <soapenv:Header/>
   <soapenv:Body>
      <tem:Add>
         <tem:intA>10</tem:intA>
         <tem:intB>55</tem:intB>
      </tem:Add>
   </soapenv:Body>
</soapenv:Envelope>"""

# Usuário e senha para autenticação básica
username = "sb-159a1d85-33fd-46dc-9e93-58887314dde2!b432831|it-rt-4beecdb1trial!b55215"
password = "b314fd75-c82a-42c8-89da-f7a5cff95723$k27lOt6KOFMyONZfOyHc4deYQaA7pllbNDeDpQVZ2-s="

# Fazendo a requisição POST
response = requests.post(
    url,
    data=soap_body,
    headers=headers,
    auth=HTTPBasicAuth(username, password)
)

# Verificando a resposta
if response.status_code == 200:
    print("Resposta do servidor:")
    print(response.text)
else:
    print(f"Erro: {response.status_code}")
    print(response.text)
