#Operadores em PYTHON

#Operadores Aritiméticos
'''
Soma: +                 (Para Variaveis String funciona como concatenar)
Subtração: -            
Multiplicação: *
Divisão: /
Divisão inteira: //     (Descarta aparte decimal da divisão)
Resto da divisão: %
Potencia: **

'''

numero1 = 10
numero2 = 20

print('Operadores Aritiméticos:')
print('numero1 + numero2 =',numero1 + numero2)
print('numero1 - numero2 =', numero1 - numero2)
print('numero1 * numero2 =', numero1 * numero2)
print('numero1 / numero2 =', numero1 / numero2)
print('numero1 // numero2 =', numero1 // numero2)
print("Resto = 20 % 3 =", 20 % 3)
print("2^3 = 2**3 =", 2**3)


#Operadores Boleanos
'''
Igual: ==
Maior: >
Maior ou Igual: >=
Menor: <
Menor ou Igual: <=
Diferente: !=
Negação: Not()
E: and
OU: or

'''

Idade1 = 22
Idade2 = 24
Altura1 = 1.68
Altura2 =  1.60

print('Operadores Boleanos')
print(Idade1, " == ", Idade2, "?", Idade1 == Idade2)
print(Idade1, " >= ", Idade2, "?", Idade1 >= Idade2)
print(Idade1, " <= ", Idade2, "?", Idade1 <= Idade2)
print(Idade1, " != ", Idade2, "?", Idade1 != Idade2)
print("Python == Python?", "Python" == "Python")
print("Banana != Python?", "Banana" == "Python")
print("Banana + Python?", "Banana" + "Python")


#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")
