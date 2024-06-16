#DICIONARIOS

#Criando dicionarios

dicionario = {}
dicionario = dict()

dicionario = {'nome' : 'Matheus', 'idade' : 24, 'altura' : 1.68}

print(dicionario)
print(dicionario['idade'])

#Adicionando elementos em um dicionário

dicionario['Programador'] = True  #Caso não exista esta chave, ele adicionado no dicionario
print(dicionario)

dicionario['altura'] = 2.00          #Muda o valor da altura
print(dicionario)

#Iterando sobre um dicionário

for chave in dicionario:        #Percore as chaves do dicionario
    print(chave, "=", dicionario[chave]) 

#Testando a existencia de uma chave

print('peso' in dicionario)     # chave in dicionario
print('altura' in dicionario)