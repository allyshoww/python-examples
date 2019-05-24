#!/usr/bin/python3

idade = int(input("Digite sua idade: "))
habilitacao = input("Voce e habilitado?: ")

if habilitacao.lower().strip() =='sim':
    habilitacao = True
    
if idade >=18 and habilitacao == True:
    print('Voce pode dirigir')
else:
    print('voce nao pode dirigir')