# Classes definem caracteristicas e o comportamento dos seus objetos. Classe não é objeto.
# Cada caracteristica é representada por um atributo.
# Cada comportamento é estabelecido por um metodo.

# Exemplo:


class Dog():
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.energia = 10
        self.sede = 10
        self.fome = 10


dog1 = Dog('Nina', 'Shitzu', '6')


def latir(self):
    print('Latindo...')


def andar(self):
    self.energia -= 1
    self.fome -= 1
    self.sede -= 1
    print('Andando...')


def dormir(self):
    print('Dormindo ...')


print(dog1.nome, dog1.raca, dog1.idade, sep='\n')


def andar()


print(dog1.nome)
print(dog1.raca)
print(dog1.idade)


print(dog1.nome, '''
      energia {}
      fome {}
      sede {}
'''.format(dog1.energia, dog1.fome, dog1.sede), sep='\n')
