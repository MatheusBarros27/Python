#CALCULO DE SISTEMAS LINEARES
#Calcular sistemas linerares através de Matrizes no NumPy
'''
EX.: Calcular as seguintes equações
    2x + 3y + 5z = 15
    6x - 1y + 3z = -10
    2x + 3y - 2z = 2 

'''

import numpy as np

#Ajustar as impressões de Matrizes para 2 digitos na casa decimal
np.set_printoptions(precision=2)

print("Vamos calcular as seguintes equações através do Método Matricial: \n")
print("2x + 3y + 5z = 15")
print("6x - 1y + 3z = -10")
print("2x + 3y - 2z = 2")

MatrizA = np.array([[2, 3, 5], [6, -1, 3], [2, 3, -2]])
print("\nMatriz A (Valores x, y e z) = \n", MatrizA) 

MatrizB = np.array([15, -10, 2])
print("\nMatriz B  (resultado das equações)= \n", MatrizB)

#Formula para Calcular as inconitas --> X = A-¹ . B 
#Calculando a Inversa de A

print("\nFormula para Calcular as inconitas --> X = A-¹ . B\n") 

MatrizInversaA = np.linalg.inv(MatrizA)
print("Matriz Inversa de A = \n", MatrizInversaA)

#Calculando a Matriz X
MatrizX = np.dot(MatrizInversaA, MatrizB)
print("\nMatriz X = \n", MatrizX)

#Imprimindo de forma mais clara
print(f"\nx = {MatrizX[0]:.2f}")
print(f"y = {MatrizX[1]:.2f}")
print(f"z = {MatrizX[2]:.2f}")

x = MatrizX[0]
y = MatrizX[1]
z = MatrizX[2]

#Calculo para checar se esta Certo
print("\nCalculo para checar se esta Certo: \n")

#Primeira Equação
print("Primeira Equação:")
print("2x + 3y + 5z = 15")
print(f"2.{x:.2f} + 3.{y:.2f} + 5.{z:.2f} = 15")
print(2*x + 3*y + 5*z, " = 15 \n")

#Segunda Equação
print("Segunda Equação:")
print("\n6x - 1y + 3z = -10")
print(f"6.{x:.2f} - 1.{y:.2f} + 3.{z:.2f} = -10")
print(6*x - 1*y + 3*z, " = -10\n")

#Terceira Equação
print("Terceira Equação:")
print("\n2x + 3y - 2z = 2")
print(f"2.{x:.2f} + 3.{y:.2f} - 2.{z:.2f} = 2")
print(2*x + 3*y - 2*z, " = 2 \n")                   

#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")