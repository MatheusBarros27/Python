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
    elif Operacao == "^1":
        return Num1 ** 2
    elif Operacao == "^2":
        return Num2 ** 2
    elif str.upper(Operacao) == "RESTO":
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
print(" ^1 = Eleva o primeriro número a 2")
print(" ^2 = Eleva o Segundo número a 2")
print(" Resto = Retorna se os números são pares ou não")
print("")

Sair = "S"

while Sair != "N":
    Num1 = float(input("Digite o Primeiro número: "))
    Num2 = float(input("Digite o Segundo número: "))
    Operacao = str.upper(input("Digite a operação desejada: "))
    print("")

    resultado = calculadora(Num1, Num2, Operacao)

    print(f"O resultado da Operação ({Operacao}) é:", resultado)
    print("")
    Sair = str.upper(input(f"Deseja realizar mais alguma operação (Digite S para Sim e N para Não: "))
    print("")
    
#Comando para executar Clicando no arquivo
print("Obrigado por usar esta calculadora!")
print("Criado por Matheus Barros.")
input("Pressione Enter para fechar...")