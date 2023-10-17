peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    condicao = "Abaixo do peso"
elif imc < 25:
    condicao = "Peso normal"
elif imc < 30:
    condicao = "Acima do peso"
else:
    condicao = "Obeso"

print("O seu IMC é: " + str(imc) + ", e a sua condição é: " + condicao)
