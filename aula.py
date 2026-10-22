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