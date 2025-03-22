op = input("Qual operacao deseja realizar + - * / ?")
num1 = int(input("Digite o primeiro numero para a operacao"))
num2 = int(input("Digite o segundo numero para a operacao"))
resultado = 0

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    op = "erro"

if op == "erro":
    print("Operacao invalida")
else:
    print(num1, op, num2, "=", result)
