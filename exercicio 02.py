nome = input("Digite o seu nome: ")
sexo = input("Digite o seu sexo (M para masculino, F para feminino): ")
estado_civil = input("Digite o seu estado civil (CASADO ou SOLTEIRO): ")

if sexo.upper() == "F" and estado_civil.upper() == "CASADA":
    tempo_casada = input("Digite o tempo de casada (em anos): ")
    print(nome + ", você é uma mulher casada há " + tempo_casada + " anos.")
else:
    print(nome + ", suas informações foram registradas.")
