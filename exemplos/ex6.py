#!/usr/bin/python
carrinho = []
produto1 = {"nome": "Tenis", "valor": 21.70}
produto2 = {"nome": "Meia", "valor": 10}
produto3 = {"nome": "Camiseta", "valor": 17.30}
produto4 = {"nome": "Calca", "valor": 100.00}
carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)


def totalCarrinho(carrinho):
    return sum(produto["valor"] for produto in carrinho)


def cupomDesconto(cupom=""):
    if cupom == "xyzgratis":
        return 0.50
    else:
        return 1


print("o total da sua compra e: ",
      (totalCarrinho(carrinho)*cupomDesconto()))
print("utilizando o cupom xyzgratis o valor sera de ",
      (totalCarrinho(carrinho)*cupomDesconto("xyzgratis")))
