import numpy as np
import matplotlib.pyplot as plt

# Definindo o vetor original
v = np.array([1, 1])

# a) Rotação
theta = np.pi / 4  # Ângulo de rotação em radianos
R = np.array([[np.cos(theta), -np.sin(theta)],
              [np.sin(theta), np.cos(theta)]])
rotated_v = np.dot(R, v)

# b) Escalonamento
S = np.array([[2, 0],
              [0, 0.5]])
scaled_v = np.dot(S, v)

# c) Reflexão
F = np.array([[1, 0],
              [0, -1]])
reflected_v = np.dot(F, v)

# d) Cisalhamento
H = np.array([[1, 0.5],
              [0, 1]])
sheared_v = np.dot(H, v)

# Exibindo os resultados
print("a) Rotação:")
print(rotated_v)

print("\nb) Escalonamento:")
print(scaled_v)

print("\nc) Reflexão:")
print(reflected_v)

print("\nd) Cisalhamento:")
print(sheared_v)

# Plotando os resultados
transformations = {
    'Rotação': R,
    'Escalonamento': S,
    'Reflexão': F,
    'Cisalhamento': H
}

plt.figure(figsize=(12, 10))

for i, (name, T) in enumerate(transformations.items(), start=1):
    transformed_v = np.dot(T, v)
    plt.subplot(2, 2, i)
    plt.title(name)
    plt.quiver([0, 0], [0, 0], [v[0], transformed_v[0]], [v[1], transformed_v[1]], angles='xy', scale_units='xy', scale=1, color=['r', 'b'])
    plt.xlim(-2, 3)
    plt.ylim(-2, 3)
    plt.grid(True)

plt.tight_layout()
plt.show()
