altura = float(input("Digite a sua altura em metros: "))
sexo = input("Digite o seu sexo (M para masculino, F para feminino): ")

if sexo.upper() == "M":
    peso_ideal = (72.7 * altura) - 58
else:
    peso_ideal = (62.1 * altura) - 44.7

print("O seu peso ideal é: " + str(peso_ideal) + " kg")
