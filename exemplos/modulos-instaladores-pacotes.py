# Modulo é um arquivo com várias funções utilizáveis em outra parte do código
# Repositorio oficial Python: https://pypi.python.org/pypi

# Importar o modulo. module é o nome do modulo que você quer importar

import csv
from module import somar
import module

# Criar um modulo


def mod():
    print("Modulo 1")


def mod2():
    print("Módulo 2")


# Ver informações sobre o modulo
dir(module)

# Chamar o modulo
module.mod()

# Instalar um modulo
pip install Modulo

# Procura um pacote
pip search nomeModulo

# Lista todos os modulos
pip list

# Desinstala pacotes
pip uninstall

# usar uma função especifica de um modulo

# Modulos nativos do python
# os: possibilita usar funcionalidades do sistema operacional
# sys: permite acessar parametros e funcoes especificas
# datetime: traz alguns tipos de data e hora
# json: codifica e decodifica no formato json
# CSV: le e escreve arquivos no formato CSV

# Modulo OS
# os.getlogin = pega o login do user atual
# saida = os.listdir('/home/allyson-oliveira') = Joga os arquivos que estão nesse caminho(path) para a variavel saida
# os.rename('/home/allyson-oliveira/teste', 'teste2')
# os.system('ls-lah') = Utiliza para enviar comandos linux


# MODULO SYS
# Fornece acesso a algumas variaveis ou funções executadas pelo Python
# Permite trabalhar com o interpretador conseguimos ver a versão do Python, em que sistema está em execução, passar parametros.

# MODULO DATETIME
# Mostra a data atual
# print(datetime.datetime.now())

# Pegar apenas a data
# print(datetime.datetime.now().strftime('%d')

#  Pegar data em um formato readable
# print(datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')

# Agendar um script para executar em 7 dias
# datetime.timedelta(7)

# Import csv
# Permite trabalhar com planilhas

with open('arquivo.csv', 'w') as csvfile:
    arquivo = csv.writer(csvfile, delimiter=',')
    arquivo.writerow(['Teste'] * 5)
    arquivo.writerow(['Teste2', 'Python'])
