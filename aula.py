nome = ["Pedro", "Maria", "João", "Ana"]
print(nome)

print("O Primeiro nome é", nome[0], "O ultimo nome é" ,nome[-1])

n = [10, 15, 5, 40, 7]
print(len(n))

nota = [7.5, 8.0, 9.5, 6.0]
print(nota[1])

nota[1] = 9.0

print(nota[1])

idade = [20, 25, 30, 35]
print(idade)
print("A soma da idade é", idade[0]+idade[1]+idade[2])
print( sum(idade) / 2 )
print("------------------------")
numeral = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
            11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numeral:
    print(number)
print("------------------------")
for number in range(1, 11):
    print(number)
print("------------------------")
for number in range(0, 21, 2):
    print(number)

print("------------------------")

for number in range(9, 0, -1):
    print(number)
    if number == 9:
        print("Vai Explodir")

    elif number == 6:
        print("Corre")

    elif number == 1:
        print("BOOOM")


print("-----------------------")
#Tabuada

tabuada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for tabu in range(0,11):
 print(tabuada[1],"X" ,tabu, "=" ,2 * tabu )

print("---------------------------")

cores = ["azul","Vermelho","amarelo"]
for i in cores:
     print(i)

print("---------------------------")

valor = [1, 2, 3, 4, 5, 6]
for val in range(len(valor)):
    print(valor[val], "->" ,val)
    
print("---------------------------")

nt = [ 5.0, 10.0, 7.0, 8.0]
media = sum(nt) / len(nt)
print( media )

print("---------------------------")

nums = [1, 2, 3, 4, 5, 6, 7, 8]
for n in range(0,9,2):
    print(n)

print("--------------------")

n = int(input("Quantos números deseja digitar? "))

lista = []

for i in range(n):
    numero = int(input("Digite um número: "))
    lista.append(numero)

soma = 0

for numero in lista:
    soma = soma + numero

print("A soma dos números é:", soma)

media = soma / numero

print("A Media dos numeros é: ", media)

 