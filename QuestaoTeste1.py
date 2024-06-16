'''
Questão 3
Para a construção de programas flexíveis e mais complexos, é necessário que haja a realização de comparações. Isso é possível com o uso de operadores lógicos de comparação (em python: ==, !=, <, <=, >, >=), como mostra o código:

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print(num > x*y, num <= x + y, num*y != x*y)
Suponha que na execução do script acima, o usuário digitou o valor 10, quando solicitado pelo input. Qual das alternativas a seguir produz o mesmo output que o script acima?


'''

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))

print("num > x*y, num <= x + y, num*y != x*y")

print("a)")
print(num > x*y, num <= x + y, num*y != x*y)
print(num == x, num == y, num == x + y)


print("b)")
print(num > x*y, num <= x + y, num*y != x*y)
print(2 == "2", False, 2.0 == 2)


print("c)")
print(num > x*y, num <= x + y, num*y != x*y)
print(True, False, False)


print("d)")
print(num > x*y, num <= x + y, num*y != x*y)
print(num == x*y, num*y == x*y, y > x + num)

print("e)")
print(num > x*y, num <= x + y, num*y != x*y)
print(False, True, True)


#Comando para executar Clicando no arquivo
input("Pressione Enter para fechar...")
