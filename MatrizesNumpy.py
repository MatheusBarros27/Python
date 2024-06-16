import numpy as np

# Definir a precisão de exibição para duas casas decimais
np.set_printoptions(precision=2, suppress=True)

# Criando matrizes como listas de listas
Matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Imprimindo a matriz inicial (lista de listas)
print("\nMatriz inicial (lista de listas):")
print(Matriz)

# Convertendo a matriz para um array numpy com tipo de dado inteiro
MatrizA = np.array(Matriz, dtype=int)

# Imprimindo a matriz convertida (array numpy)
print("\nMatriz convertida (array numpy):")
print(MatrizA)

#acessando a primeira linha

print("\nPrimeira linha = ", MatrizA[0])

#Acessando segunda linha, primeira coluna
print("\nSegunda linha, Primeira coluna = ", MatrizA[1][0])

#transpondo a matriz

MatrizTransposta = MatrizA.transpose()
print("\nMatriz Transposta = \n", MatrizTransposta)

# Criando uma segunda matriz para operações
MatrizB = np.array([[7, 8, 9], [10, 11, 12], [12, 13, 14]])

# Adição de matrizes
#adição da estrutura Try para exibir se conseguir realizar a operação e se não conseguir, apenas mostrar o erro na tela
try:
    MatrizAdicao = MatrizA + MatrizB                #Soma
    print("\nSoma das matrizes:\n", MatrizAdicao)
except ValueError as e:
    print("\nErro na soma das matrizes:", e)

# Subtração de matrizes
try:
    MatrizSubtracao = MatrizA - MatrizB             #Subtração
    print("\nSubtração das matrizes:\n", MatrizSubtracao)
except ValueError as e:
    print("\nErro na subtração das matrizes:", e)

# Multiplicação de matrizes (elemento a elemento - NÃO É A DIVISÃO DO CONCEITO DE ALGEBRA)
try:
    MatrizMultiplicacao = MatrizA * MatrizB         #Multiplicação
    print("\nMultiplicação elemento a elemento das matrizes:\n", MatrizMultiplicacao)
except ValueError as e:
    print("\nErro na multiplicação elemento a elemento das matrizes:", e)

# Divisão de matrizes (elemento a elemento - NÃO É A DIVISÃO DO CONCEITO DE ALGEBRA)
try:
    MatrizDivisao = MatrizA / MatrizB               #Divisão
    print("\nDivisão elemento a elemento das matrizes:\n", MatrizDivisao)
except ValueError as e:
    print("\nErro na divisão elemento a elemento das matrizes:", e)

# Multiplicação de matrizes (produto matricial)
try:
    MatrizProdutoMatricial = np.dot(MatrizA, MatrizB)
    print("\nProduto matricial:\n", MatrizProdutoMatricial)
except ValueError as e:
    print("\nErro no produto matricial:", e)

# Para calcular o determinante, precisamos de uma matriz quadrada
MatrizQuadrada = np.array([[1, 2], [3, 4]])

# Determinante da matriz quadrada
try:
    Determinante = np.linalg.det(MatrizQuadrada)
    print("\nDeterminante da matriz quadrada:\n", Determinante)
except ValueError as e:
    print("\nErro ao calcular o determinante:", e)
