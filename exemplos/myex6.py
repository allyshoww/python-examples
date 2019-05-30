#!/usr/bin/python
carrinho = []
produto1 = {"nome": "Tenis", "valor": 100}
produto2 = {"nome": "Meia", "valor": 100}
produto3 = {"nome": "Camiseta", "valor": 100}
produto4 = {"nome": "Calca", "valor": 100.00}
carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)


def totalCarrinho(carrinho):
    return sum(produto["valor"] for produto in carrinho)


def cupomDesconto(cupom=""):
    if cupom == 'xyzgratis':
        return 0.50
    else:
        return 1


print(" O total de sua compra é: ",
      (totalCarrinho(carrinho)*cupomDesconto()))
print(" Utilizando o cupom gratis 'xyzgratis' o valor será de: ",
      (totalCarrinho(carrinho)*cupomDesconto("xyzgratis")))
