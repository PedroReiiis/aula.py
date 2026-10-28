contador = 1
while contador <= 10:
    print(contador)
    contador += 1

print("------------------------")

regressivo = int(input("Digite um número: "))
while regressivo >= 1:
    print(regressivo)
    regressivo -= 1

print("------------------------")

soma = 0 
n = int(input("0 sai? "))

while n != 0:
    soma += n
    n = int(input("0 sai? "))

print("A soma dos números digitados é:", soma)

print('------------------------')

senha = 1234
senha_digitada = int(input("Digite a senha: "))
while senha_digitada != senha:
    print("Senha incorreta!")
    senha_digitada = int(input("Digite a senha: "))
    print("pode entrar!")

print('------------------------')

escolha =  (input("Digite um número de 1 a 8: "))
match escolha:
    case "1":   
      print("Janeiro")
    case "2":   
     print("Fevereiro")
    case "3":   
     print("Março")
    case "4":   
     print("Abril") 
    case "5":
     print("Maio")
    case "6":
     print("Junho") 
    case "7":
     print("Julho") 
    case "8":
     print("Agosto")    
    case _ :
     print("Acabou o Mês")

print('------------------------')

calculadora = input("Digite a operação desejada (+, -, *, /): ")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
match calculadora:
    case "+":   
     print(num1 + num2)
    case "-":   
     print(num1 - num2)
    case "*":   
     print(num1 * num2)
    case "/":   
     print(num1 / num2)
    case _ :
     print("Operação inválida")

print('------------------------')

conceito = input("Digite o conceito (A, B, C, D ou E): ")
match conceito: 
    case "A":   
     print("Excelente")
    case "B":   
     print("Bom")
    case "C":   
     print("Regular")
    case "D":   
     print("Insuficiente") 
    case "E":
     print("Péssimo") 
    case _ :
     print("Conceito inválido")

