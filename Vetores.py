import matplotlib.pyplot as plt

#Definindo o Vetor
vetor = [2,2]

#Definindo as origens para o vetor
origens = [(0,-1), (0, 1), (0,0), (0,2)]

#Extraindo as cordenadas x e y das origens

origensx = [origem[0] for origem in origens]
origensy = [origem[1] for origem in origens]

#Plotando o vetor (2,2) com as origens especificadas

plt.figure()
plt.quiver(origensx, origensy, [vetor[0]]*len(origensx), [vetor[1]]* len(origensy), angles='xy', scale_units='xy', scale=1, color='g')

#configurações adicionais do gráfico

plt.xlim(-1,5)
plt.ylim(-2,5)
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.axhline(0, color='black', linewidth = 0.5)
plt.axvline(0, color='black', linewidth = 0.5)
plt.grid(color='gray', linestyle = '--', linewidth = 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Um Vetor com diferentes pontos de origem")

# Exibir o gráfico
plt.show()
