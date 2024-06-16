#Listas ou ARRAY

#ANtes
Nota1 = 10.0
Nota2 = 5.3
nota3 = 2.7

#Com lista
Notas = [10.0, 5.3, 2.7]

#Criando Listas
Lista = []
Lista = list()
Lista = [3.14, 'Matheus', False]    #Permite qualquer tipo de dado juntos 
Lista_de_Lista = [10, [1, 2, 3]]

#Indexação Lista[numero] - para valores positivos pega do começo ao final e para valores negativos pega do final até o começo
Lista = [3.14, 'Matheus', False]    #Permite qualquer tipo de dado juntos 
qtd_elementos = len(Lista)          #Len() Calcula quantos elementos existe em uma lista 

i=0
for i in range(qtd_elementos):
    print("Elemento", i+1, "da Lista =", Lista[i])

print("")
#Slices (Fatiamento)

ListaSlice = [10, 20, 30, 40, 50 ,60 ,70,80 ,90 , 100]
LLL = len(ListaSlice)
print(ListaSlice)
print("Fatia = ", ListaSlice[2:6])
print("Fatia2 = ", ListaSlice[5:])      #vai até o final
print("Fatia3 = ", ListaSlice[0:LLL:2]) #Vai do início até o final, com PASSO = 2

#Exemplo 2 de uso do for para uma lista

for elemento in ListaSlice:
    print(elemento)
    
#METODOS DE LISTAS
#Append - Metodo que adiciona um valor ao final de uma lista
ListaAppend = [1,2,3,4,5,6,7,8,9]
print("Antes do Append:", ListaAppend)

ListaAppend.append(3)       #Pelo código
#Solicitando ao usuário
ListaAppend.append(int(input('Digite um número para adicionar ao final da lista:')))       
print("Depois do append:", ListaAppend)

#Insert - Metodo que adiciona um valor na lista em uma determinada posição
#ex: lista.insert(posição, elemento_adicionado)
ListaAppend.insert(2,10)
print("Depois do Insert:", ListaAppend)

#extend - metodo que adiciona todos os elementos de uma lista no final de outra lista
ListaExtend = [22,33,44]
ListaAppend.extend(ListaExtend)
print("Depois do extend: ", ListaAppend)

#pop - Metodo que remove um elemento de uma lista em uma determinada posição (Se não passar o valor ele remove o ultimo)
ListaAppend.pop(2)
print("Depois do pop:", ListaAppend)

#remove - metodo que remove um elemento baseado no valor passado a ele 
ListaAppend.remove(22)      #Pega o primeiro valor encontrado
print("Depois do remove:", ListaAppend)

#Count - metodo que conta quantas vezes um determinado valor aparece na lista
Valor_Count = 22
QTD_Count = ListaAppend.count(Valor_Count)
print(f"Quantidade de vezes que o valor {Valor_Count} aparece vezes na lista = {QTD_Count}")

#index - Metodod que retorna a posição de um determinado valor na lista
posicao = ListaAppend.index(Valor_Count)
print(f"A posição do valor {Valor_Count} é = ", posicao+1)

#sort - metodo que ordena os valores de uma lista (Se não passar parametros ele ordena de forma crescente)
ListaAppend.sort()
print("Ordem Crescente:", ListaAppend)

ListaAppend.sort(reverse=True) #Decrescente
print("Ordem Decrescente:",ListaAppend)

#FUNÇÕES

#len - Metodo que conta quantos elementos tem na lista

print("QTD de elementos = ", len(ListaAppend))

#sum - Metodo que Soma os elementos na lista

print("Soma dos elementos = ", sum(ListaAppend))

#max - Metodo que retorna o MAIOR valor da lista

print("Maior elemento = ", max(ListaAppend))

#min - Metodo que retorna o MENOR valor da lista

print("Menor elemento = ", min(ListaAppend))

#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")