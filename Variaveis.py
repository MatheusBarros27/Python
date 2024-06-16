#VARIÁVEIS

Nome = "MATHEUS"
Idade = 24
Altura = 1.68
Estudando = True

print("Olá ", Nome)
print("Sua idade é:", Idade)
print("Sua altura é:", Altura)
print("Situação de Estudo = ", Estudando)

Bairro = input("Você mora em qual bairro? ")

print("Você mora no bairro:", Bairro)

'''
Int - Numeros inteiros
Float - Numeros reais
str - String (Texto)
bool - Valores lógicos (TRUE e FALSE)

OBS.:   Todos os Inputs feitos no PYTHON 
        são lidos como String, portanto 
        temos que realizar as conversões 
        para trabalhar com os valores

Comandos para Converter Variaveis
int()           - Numeros inteiros
float()         - Numeros reais
str()           - String (Texto)
bool()          - Valores lógicos (TRUE e FALSE)

'''

Nome2 = input('Digite seu Nome Completo:')
print('Seu Nome completo é:', Nome2, type(Nome2))

Nota = float(input('Digite sua Nota:'))
print('Nota =', Nota, type(Nota))

#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")

