# ESTRUTURAS CONDICIONAIS
# Verificar se uma pessoa é maior de idade ou não?

'''
Estrutura IF

if [CONDIÇÃO]:
    [comandos]
elif [CONDIÇÃO2]:
    [comandos Else if ou elif]
else:
    [comandos else]

OBS.:Não precisa abrir e fechar o comando
    pois o python utiliza a identação 
    do código como orientação das 
    estruturas de repetição e condição

'''

#Verificar Nome e Idade (Maior ou Menor de idade)
print("Vamos verificar se você é maior de idade!")

Nome = input("Digite seu Nome:")
Idade = int(input("Digite sua Idade:"))

if Idade >= 18:
    print(Nome, "Você é maior de idade!")
else:
    print(Nome, "Você Não é maior de idade!")
    

#Verificar Situação das Notas (Aprovado, Recuperação ou Reprovado)
print("Vamos agora verificar se você reprovou", Nome, "?")

Nota1 = float(input("Digite sua primeira Nota:"))
Nota2 = float(input("Digite sua segunda Nota:"))
Media = (Nota1 + Nota2) / 2

if Media >= 7:
    print(Nome, "Você está APROVADO!")
    print("PARABÉNS")
elif Media >= 5:
    print(Nome, "Você está de RECUPERAÇÃO!")
    print("Não se preocupe você ainda tem mais uma chance, ESTUDE!")
else:
    print(Nome, "Você está REPROVADO!")
    print("Só ano que vem agora! :( ")

#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")
