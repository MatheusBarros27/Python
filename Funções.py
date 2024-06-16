#FUNÇÕES

#Exemplos de funções

'''

print() #Imprime valores e variaveis na tela
input() #le algum valor digitado pelo usuario
len()   #Retorna a qtd de elementos de uma lista
max()   #Retorna o maior valor de uma lista

'''

#CRIAÇÃO DE FUNÇÕES

#Função inicial

def saudacao():         
    print("Seja bem vindo(a)!")
    print("É um prazer ter você fazendo parte deste curso!")
    print("")

saudacao()
saudacao()

#Função com parametros

def saudacao(nome, curso):         
    print("Seja bem vindo(a), ", nome, "!!!")
    print("É um prazer ter você fazendo parte do curso de ", curso, "!")
    print("")

nome = input("Digite seu nome:")
curso = input("Digite seu curso:")

saudacao(nome, curso)

#Função com parametro default

def saudacao(nome, curso = "PYTHON"):         
    print("Seja bem vindo(a), ", nome, "!!!")
    print("É um prazer ter você fazendo parte do curso de ", curso, "!")
    print("")

saudacao("Matheus") #Se não passar nenhum valor para o default, ele assume o que foi escrito na função

#Funções com retorno

def soma(Num1, Num2):
    return Num1 + Num2 #retorna o valor da soma dos 2 parametros que foram passados
                       # Depois do return a função para de executar
    
resultado = soma(4893, 2938)

print("O resultado da Soma é:", resultado)

#CALCULADORA por função

def calculadora(Num1=1, Num2=1, Operacao = "+"):
    if Operacao == "+":
        return Num1 + Num2
    elif Operacao == "-":
        return Num1 - Num2
    elif Operacao == "*":
        return Num1 * Num2
    elif Operacao == "/":
        return Num1 / Num2
    elif Operacao == "^":
        return Num1 ** Num2
    elif Operacao == "Resto":
        if Num1 % 2 == 0 and Num2 % 2 ==0:
            return "Os dois números digitados são Pares!"
        elif Num1 % 2 == 0 and Num2 % 2 != 0:
            return "O primeiro número digitado é Par e segundo é Impar!"
        elif Num1 % 2 != 0 and Num2 % 2 == 0:
            return "O primeiro número digitado é Impar e segundo é Par!"
        else:
            return "O dois números digitados são Impares!"

print("Seja bem vindo a Calculadora, digite 2 números e a operação que deseja realizar:")
print("Operações disponiveis:")
print(" + = Adição")
print(" - = Subtração")
print(" * = Multiplicação")
print(" / = Divisão")
print(" ^ = Potencia")
print(" Resto = Retorna se os números são pares ou não")

Num1 = float(input("Digite o Primeiro número: "))
Num2 = float(input("Digite o Segundo número: "))
Operacao = input("Digite a operação desejada: ")

resultado = calculadora(Num1, Num2, Operacao)

print(f"O resultado da Operação ({Operacao}) é:", resultado)


#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")

