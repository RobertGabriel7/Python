import json
import requests
import inspect

""" Lista[] """

funcoes = [nome for nome in dir(inspect) if inspect.isfunction(getattr(requests, nome, None))]
funcoes = [nome for nome in dir(requests) if inspect.isfunction(getattr(requests, nome, None))]

print(funcoes)