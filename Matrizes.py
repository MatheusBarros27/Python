# Matrizes

# Criando matrizes
Matriz = [[1, 2, 3], [4, 5, 6]]

#imprimindo a tabela
print(Matriz)

# Imprimindo a primeira linha
print(Matriz[0])  #Primeira linha Saída: [1, 2, 3]

# Imprimindo um elemento específico
print(Matriz[0][1])  # primeria linha segunda coluna; Saída: 2

# Adicionando uma nova linha
Matriz.append([7, 8, 9])
print(Matriz)

# Adicionando um novo elemento a uma linha específica
Matriz[0].append(4)
print(Matriz[0])

# Acessando o último elemento de cada linha
for linha in Matriz:
    print(linha[-1])

# Transpondo a matriz
MatrizTransposta = list(zip(*Matriz))
print(MatrizTransposta)
