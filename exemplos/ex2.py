notas = [10, 9, 8, 7, 3]

soma_nota = sum(notas)
print(soma_nota)

divisao_nota = soma_nota/4
print(divisao_nota)

for nota in notas:
    if nota >= 7:
        print('aprovado')
    elif nota > 3:
        print('recuperacao')
    else:
        print('reprovado')