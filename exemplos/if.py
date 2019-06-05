#! /usr/bin/python3
idade = 18
if idade == 18:
    print('Voce e maior de idade')
else:
    print('Voce e menor de idade')

notas = [10, 9, 8, 7, 3, 10, 8, 1, 1, 5]

soma_nota = sum(notas)
print("Soma da nota: " , soma_nota)

divisao_nota = soma_nota/10
print(divisao_nota)

if divisao_nota >= 7:
    print('aprovado')
elif divisao_nota >=3:
    print('recuperacao')
else:
    print('reprovado')
