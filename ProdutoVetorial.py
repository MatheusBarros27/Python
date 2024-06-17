import numpy as np
import plotly.graph_objs as go

# Função para plotar vetores em 3D com Plotly
def plot_vectors_plotly(v1, v2, label1, label2):
    """
    Plota dois vetores em 3D usando Plotly.

    Parâmetros:
    v1 (array-like): O primeiro vetor, um array de 3 elementos [x, y, z].
    v2 (array-like): O segundo vetor, um array de 3 elementos [x, y, z].
    label1 (str): O rótulo para o primeiro vetor.
    label2 (str): O rótulo para o segundo vetor.
    """
    fig = go.Figure()
    
    # Adicionando o primeiro vetor ao gráfico
    fig.add_trace(go.Scatter3d(
        x=[0, v1[0]], y=[0, v1[1]], z=[0, v1[2]],
        mode='lines+markers', name=label1
    ))
    
    # Adicionando o segundo vetor ao gráfico
    fig.add_trace(go.Scatter3d(
        x=[0, v2[0]], y=[0, v2[1]], z=[0, v2[2]],
        mode='lines+markers', name=label2
    ))
    
    # Configurando o layout do gráfico
    fig.update_layout(scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z')
    ), margin=dict(l=0, r=0, b=0, t=0))
    
    # Exibindo o gráfico
    fig.show()

# Vetores de exemplo para visualização
a = np.array([4, 9, -6])
b = np.array([5, 0, -2])
plot_vectors_plotly(a, b, 'a', 'b')

c = np.array([2, -3, 1])
d = np.array([0, 1, 4])
plot_vectors_plotly(c, d, 'c', 'd')

e = np.array([1, 2, 3])
f = np.array([-2, 1, 0])
plot_vectors_plotly(e, f, 'e', 'f')

g = np.array([3, 4, 5])
h = np.array([1, -1, 2])
plot_vectors_plotly(g, h, 'g', 'h')

i = np.array([-4, -7, -3])
j = np.array([4, 9, -6])
plot_vectors_plotly(i, j, 'i', 'j')
