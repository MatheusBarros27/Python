#DATAFRAMES EM PYTHON PELA BIBLIOTECA PANDAS

import pandas as pd

# Criando um dicionário com os dados.
dicionario = {
    'Autores': ['Rick Riordan', 'J. R. R. Tolkien', 'Rick Riordan', 'Machado de Assis'],
    'Titulos': ['O Ladrão de Raios', 'A Sociedade do Anel', 'Mar de Monstros', 'Memórias Póstumas de Brás Cubas'],
    'Preços': [63.5, 58.6, 47.34, 89.26],
    'Qtd Vendidos': [50, 60, 80, 90]
}
print("Dicionário original:")
print(dicionario)

# Convertendo o dicionário para um DataFrame.
df = pd.DataFrame(dicionario)
print("\nDataFrame inicial:")
print(df)

# Criando uma máscara para selecionar linhas com o autor 'Rick Riordan'.
mask = df['Autores'] == "Rick Riordan"
print("\nLinhas com 'Rick Riordan':")
print(df[mask])

# Adicionando novos dados para 'Rick Riordan'.
dicionario_add = {
    'Autores': ['Rick Riordan'],
    'Titulos': ['O Cálice dos Deuses'],
    'Preços': [100],
    'Qtd Vendidos': [58]
}
print("\nDicionário adicional:")
print(dicionario_add)

# Convertendo o dicionário adicional para um DataFrame.
df2 = pd.DataFrame(dicionario_add)

# Concatenando os dois DataFrames.
df = pd.concat([df, df2], ignore_index=True)
print("\nDataFrame após concatenação:")
print(df)

# Aplicando desconto de 10% nos preços acima de 50.
mask_acima_50 = df['Preços'] >= 50
df.loc[mask_acima_50, 'Preços'] *= 0.9

print("\nDataFrame após aplicação de desconto:")
print(df)

# Selecionando os títulos de 'Rick Riordan'.
titulos_rick_riordan = df[df['Autores'] == 'Rick Riordan']['Titulos']
print("\nTítulos de 'Rick Riordan':")
print(titulos_rick_riordan.tolist())

# Calculando a média, mediana e máximo dos preços por autor.
precos_por_autor = df.groupby('Autores')['Preços'].agg(['mean', 'median', 'max'])
print("\nEstatísticas dos preços por autor:")
print(precos_por_autor)
