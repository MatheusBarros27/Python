#ESTRUTURAS DE REPETIÇÃO

'''
Não é necessario fechar o laço pois no PYTHON se utiliza a identação como referencia

While [CONDIÇÃO]:       (Cuidado com laços infinitos)
    [codigo while]

For i=0 in Range(10):   (Usar Range(Numero) para gerar uma lista com n Valores que quer repetir ou atribuir a uma lista)
    [codigo for]

OBS. FOR: o Range(Numero) vai até (Numero - 1)
     EX: Range(10) - Vai de 0 até 9
         Range(1, 10) - Vai de 1 até 9
         Range(1, 10, 2) - Vai de 1 a 9, pulando de 2 em 2. PASSO = 2
'''

#Exemplo 1: Acertar um número aleatório usando While
import random

print("Tente acertar o número sorteado!")

numero_sorteado = random.randint(1, 20)
print(numero_sorteado)
numero_escolhido = int(input('Digite um número entre 1 a 20:'))
print("")

while numero_escolhido != numero_sorteado:
    print("VOCÊ ERROU, TENTE NOVAMENTE!")
    numero_escolhido = int(input('Digite um número entre 1 a 20:'))
    print("")

#exemplo 2: Imprimir o parabens 10 vezes Usando For

i=1
for i in range(10):
    #f string para informar a variavel i dentro do print (Mais util para input, pois pelo print pode fazer print(i, "..."))
    print(f"{i} - PARABÉNS, VOCÊ ACERTOU!")
    print("O número sorteado era o", numero_sorteado)
    print("")


#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")

    