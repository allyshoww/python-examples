# Função é uma sequencia de instruções que realiza uma operação. São blocos de códigos que realizam determinadas tarefas que precisam ser executadas diversas vezes.
# Tem que ser em letras minusculas e underline para espaçamento
# Palavra reservada: def
# Escopo Global: Pode ser acessada por todas as funções que estão presentes no modulo

#!/usr/bin/python3

# Função que printa alguma coisa


def python():
    print('Pythonzero')


python()

# Funçao que printa um nome digitado

# Ao se criar uma função, obrigatoriamente a função espera algum parametro. parametro é o valor que será substituido e que está dentro do parenteses na...
# ...primeira linha


def boa_vindas(nome):
    print("Seja bem vindo,{}".format(nome))


boa_vindas(input('Coloque seu nome aqui:'))

# Funcao que printa uma variavel (nome = anonimo)


def boa_vindas2(nome='anomimo'):
    print("Seja bem vindo, {}".format(nome))


boa_vindas2()

# Utiliza uma variavel para uma função
nome = 'Allyshow'


def welcome():
    print('Welcome {}'.format(nome))


welcome()

# Utiliza uma variavel global para uma função
nome = 'Allyshow'


def welcome():
    global nome
    nome = "Allyson Oliveira"
    print('Welcome {}'.format(nome))


welcome()
