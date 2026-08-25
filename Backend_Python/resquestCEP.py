import requests
import json 

cep = "02226010"
urlRequestCEP = f"https://mg-api.telefonicabigdata.com/consulta-cep-api/cep_lookup?cep={cep}"

try:
    requestTeste = {

        "bairro":"Jardim Brasil (Zona Norte)",
        "cep":"02226010",
        "complemento":"- Ate 1301/1302",
        "estado":"S\u00e3o Paulo",
        "ibge":"3550308","localidade":"Sao Paulo",
        "logradouro":"Rua Benfica",
        "regiao":"S\u00e3o Paulo",
        "uf":"SP","unidade":""}
    
    print(f"Rua : {requestTeste["logradouro"]}")

except:

    print("\nDeu algum erro.\n")