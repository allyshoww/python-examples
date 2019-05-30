# Quando não sabemos quantos argumentos são passados em uma função, utilizamos *args ou **kwargs.
# *args transforma argumentos em tupla
# **kwargs transforma argumentos em um dicionário.


def classe(**kwargs):
    print('O ip do servidor atual é: ', kwargs["ip"])
    print('O novo ip é: ', kwargs["novo"])


# Essa é um dicionario, com informações chave e valor. Chave = "ip", valor = "192.168.0.1.". Nesse caso, veja que utilizamos o kwargs acima.
classe(ip="192.168.0.1", novo="10.1.1.1")


def alterarServidor(*args):
    print('O ip do servidor atual é: ', args[0])
    print('O novo ip é: ', args[1])


# Essa é uma tupla, com valores imutáveis. Veja que utilziamos o args no exemplo acima.
alterarServidor("192.168.0.10", "10.0.0.1")


def cadastro(**pessoa):
    print(type(pessoa))


cadastro(nome='allyson', sobrenome='oliveira')
exit()


def cadastro1(*pessoa1):
    print(type(pessoa1))


cadastro1('allyson', 'de_souza')
