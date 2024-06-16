import numpy as np

# Solicita ao usuário a quantidade de alunos
QtdAlunos = int(input("Quantos alunos você vai digitar as notas? "))

# Cria um array vazio para armazenar os nomes dos alunos
Nomes = np.empty(QtdAlunos, dtype=object)

# Cria um array de zeros para armazenar as notas dos alunos
Notas = np.zeros(QtdAlunos)

# Loop para inserção dos nomes e notas dos alunos
for i in range(QtdAlunos):
    Nomes[i] = input(f"Nome do aluno {i+1}: ")
    Notas[i] = float(input(f"Nota do aluno {Nomes[i]}: "))
    
print("Array Numpy contendo os Nomes: \n", Nomes)
print("Array Numpy contendo as Notas: \n", Notas)


# Utiliza uma máscara para selecionar os alunos que ficaram de recuperação (nota <= 7) e que foram aprovados
mask = Notas < 7
print("\nAlunos que ficaram de Recuperação:")
for nome, nota in zip(Nomes[mask], Notas[mask]):
    print(f"Nome: {nome}, Nota: {nota:.2f}")

mask2 = Notas >= 7
print("\nAlunos que foram Aprovados:")
for nome, nota in zip(Nomes[mask2], Notas[mask2]):
    print(f"Nome: {nome}, Nota: {nota:.2f}")

# Exemplo adicional de seleção de elementos usando NumPy
numeros = np.array([2, 6, 8, 12, 4, 7, 10])
mascara = (numeros > 5) & (numeros < 10)
elementos_selecionados = numeros[mascara]
print("\nExemplo de seleção de elementos:")
print("Elementos selecionados:", elementos_selecionados)
