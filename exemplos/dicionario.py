# Dicionario é uma representação desordenada de objetos representados na forma de chave e valor. São do tipo imutavel (inteiro, float ou string), não possuem noção de indices e não podem ser fatiados. 

# Dicionario de times e selecionando o valor apenas da chave 'brasil'
times = {'brasil':'palmeiras', 'inglaterra':'liverpool', 'italia':'milan'}
times['brasil']

# adicionando um valor em um dicionario
times['england']= 'tottenham'

# Pega um determinado valor
times.get('italia')

# Lista todas as keys de um dicionario
times.keys()

# Lista todos os valores de um dicionario
times.values()

# Lista todas as chaves e valores de um dicionario
times.items()
