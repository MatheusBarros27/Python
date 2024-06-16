'''
Um dos principais usos destinados aos operadores lógicos é a construção de expressões condicionais, que são utilizadas para (re)direcionar o fluxo de um programa. Isso é possível com as expressões if, elif e else em Python.

[CODIGO ABAIXO]

Pelo que o "XXX" deve ser substituído no código acima (ou seja, o que este código efetivamente faz?)

'''


a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

if a > b and a > c:

  resposta = a % 2 == 0

elif b > a and b > c:

  resposta = b % 2 == 0

else:

  resposta = c % 2 == 0

print("O maior número entre os três informados é par?", resposta)