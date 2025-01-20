#Crie um código em python que teste se o site PUDIM está acessivel pelo computador usado


import urllib.error
import urllib.request

try: 
    site = urllib.request.urlopen('https://www.pudim.com.br/')
except urllib.error.URLError:
    print('DEU MUITO RUIM!')
else:
    print('Deu bom!')
    print(site.read())