import numpy as np
import matplotlib.pyplot as plt

# Definindo a matriz A
A = np.array([[6, -1],
              [2, 3]])

# Calculando os autovalores e autovetores
autovalores, autovetores = np.linalg.eig(A)

# Criando a matriz diagonal com os autovalores
matriz_diagonal = np.diag(autovalores)

# Imprimindo os autovalores e autovetores
print("Autovalores:")
print(autovalores)
print("\nAutovetores:")
print(autovetores)

# Imprimindo os autovetores como colunas
print("\nAutovetores como colunas:")
for i in range(len(autovalores)):
    print(f"Autovetor {i+1}: {autovetores[:, i]}")

# Bonus - reconstruindo a matriz A
A_reconstruida = autovetores @ matriz_diagonal @ np.linalg.inv(autovetores)
print("\nA reconstruída:\n", A_reconstruida)

# Representação geométrica dos autovetores
origin = [0, 0]  # Origem do vetor

plt.figure()
plt.quiver(*origin, autovetores[0, 0], autovetores[1, 0], color='r', scale=8,
           label=f"Autovetor 1: {autovetores[:, 0]}")
plt.quiver(*origin, autovetores[0, 1], autovetores[1, 1], color='b', scale=8,
           label=f"Autovetor 2: {autovetores[:, 1]}")
plt.xlim(-3, 3)
plt.ylim(-3, 3)
plt.axvline(x=0, color='grey', lw=1)
plt.axhline(y=0, color='grey', lw=1)
plt.grid(True)
plt.legend()
plt.title('Representação Geométrica dos Autovetores')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.show()
