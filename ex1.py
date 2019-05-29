#!/usr/bin/python3

nomes = ["Daniela", "Camila", "Gaspar", "Oliveira"]
busca = input('Digite um nome de uma pessoa: ')

for nome in nomes:
    if busca.lower().strip == nome:
        print("Convidado está na lista")
        break
else:
    print("Não está na lista")