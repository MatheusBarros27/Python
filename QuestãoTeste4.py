'''
Enunciado

Utilizamos listas para armazenar em um único objeto uma coleção de valores. Muitas vezes, desejamos criar uma nova lista a partir de uma lista original. Observe o código abaixo:


Qual deve ser o valor de A, B, C e D, respectivamente, para que o código acima gere a seguinte lista_final: [10, 10, 14, 6, 42, 126, 8, 10, 26]?


'''

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]

lista_final1 = []
lista_final2 = []
lista_final3 = []
lista_final4 = []
lista_final5 = []


for item in lista_inicial:

    if item % 2 == 0:

        if item < 0:
            
            A1 = -2*item
            A2 = -item
            A3 = 2*item
            A4 = item
            A5 = -item
            lista_final1.append(A1)
            lista_final2.append(A2)
            lista_final3.append(A3)
            lista_final4.append(A4)
            lista_final5.append(A5)
    
        else:
            B1 = 2*item
            B2 = item
            B3 = -2*item
            B4 = -item
            B5 = 2*item
            lista_final1.append(B1)
            lista_final2.append(B2)
            lista_final3.append(B3)
            lista_final4.append(B4)
            lista_final5.append(B5)
    else:

        if item < 0:
            C1 = -item
            C2 = -2*item
            C3 = item
            C4 = 2*item
            C5 = -2*item
            lista_final1.append(C1)
            lista_final2.append(C2)
            lista_final3.append(C3)
            lista_final4.append(C4)
            lista_final5.append(C5)
    
        else:
            D1 = item
            D2 = 2*item
            D3 = -item
            D4 = -2*item
            D5 = item
            lista_final1.append(D1)
            lista_final2.append(D2)
            lista_final3.append(D3)
            lista_final4.append(D4)
            lista_final5.append(D5)

print("a) ", lista_final1)
print("b) ", lista_final2)
print("c) ", lista_final3)
print("d) ", lista_final4)
print("e) ", lista_final5)