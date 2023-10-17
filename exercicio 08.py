valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
valor3 = int(input("Digite o terceiro valor: "))

if valor1 != valor2 and valor1 != valor3 and valor2 != valor3:
    valores = [valor1, valor2, valor3]
    
    valores.sort(reverse=True)
    
    print("Os valores em ordem decrescente são: ", valores)
else:
    print("Por favor, insira três valores diferentes.")
