valor1 = input("Digite o primeiro valor booleano (0 para FALSO, 1 para VERDADEIRO): ")
valor2 = input("Digite o segundo valor booleano (0 para FALSO, 1 para VERDADEIRO): ")

valor1 = bool(int(valor1))
valor2 = bool(int(valor2))

if valor1 and valor2:
    print("Ambos os valores são VERDADEIROS.")
elif not valor1 and not valor2:
    print("Ambos os valores são FALSOS.")
else:
    print("Os valores são diferentes.")