# ESTRUTURAS CONDICIONAIS
# Verificar se uma pessoa é maior de idade ou não?

'''
Estrutura IF

if [CONDIÇÃO]:
    [comandos]
else
    [comandos Else]

OBS.:Não precisa abrir e fechar o comando
    pois o python utiliza a identação 
    do código como orientação das 
    estruturas de repetição e condição

'''


print("Vamos verificar se você é maior de idade!")

Nome = input("Digite seu Nome:")
Idade = int(input("Digite sua Idade:"))

if Idade >= 18:
    print(Nome, "Você é maior de idade!")
else:
    print(Nome, "Você Não é maior de idade!")
    

#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")
