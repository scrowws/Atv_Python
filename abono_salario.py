salario = float(input("Informe o seu salario:"))
if salario >= 5000:
    percentual = salario * 0.15
    abono = salario + percentual
    print(f"Seu abono vai ser de 15%: {percentual:.2f}")
else:
    percentual = salario * 0.1
    print(f"Seu abono vai ser de 10%: {percentual:.2f}")
