import matplotlib.pyplot as plt

# Definindo os vetores na base canônica
vetor_x = [1, 0]  # Vetor unitário ao longo do eixo x
vetor_y = [0, 1]  # Vetor unitário ao longo do eixo y

# Plotando os vetores na base canônica
plt.figure()

# Vetor x
plt.quiver(0, 0, vetor_x[0], vetor_x[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vetor x')

# Vetor y
plt.quiver(0, 0, vetor_y[0], vetor_y[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vetor y')

# Adicionando o vetor (4,3)
plt.quiver(0, 0, 4, 3, angles='xy', scale_units='xy', scale=1, color='g', label='(4,3)')

# Configurações adicionais do gráfico
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.title("Combinações feitas com os vetores da base canônica")

# Exibindo o gráfico
plt.show()
