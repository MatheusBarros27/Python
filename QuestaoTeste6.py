cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1
    if cont == n:
        print("CHEGOU NO 1000!")


print(resultado)
print(n)