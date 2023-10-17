def calcular_media_aproveitamento(id_aluno, nota1, nota2, nota3, ME):
    MA = (nota1 + nota2 * 2 + nota3 * 3 + ME) / 7
    if MA >= 90:
        conceito = 'A'
    elif MA >= 75:
        conceito = 'B'
    elif MA >= 60:
        conceito = 'C'
    elif MA >= 40:
        conceito = 'D'
    else:
        conceito = 'E'

    if conceito in ['A', 'B', 'C']:
        status = 'Aprovado'
    else:
        status = 'Reprovado'

    print(f'Número do aluno: {id_aluno}')
    print(f'Notas: {nota1}, {nota2}, {nota3}')
    print(f'Média dos exercícios: {ME}')
    print(f'Média de aproveitamento: {MA}')
    print(f'Conceito: {conceito}')
    print(f'Status: {status}')

id_aluno = float(input("Digite a id do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
ME =  float(input("Digite a média de exercicios: "))
calcular_media_aproveitamento(id_aluno, nota1, nota2, nota3, ME)