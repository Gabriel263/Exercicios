def calcular_preco_final(preco_etiqueta, condicao_pagamento):
    if condicao_pagamento == 1:
        des10 = (preco_etiqueta * 10)/100
        return preco_etiqueta - des10  # desconto de 10%
    elif condicao_pagamento == 2:
        des15 = (preco_etiqueta * 15)/100
        return preco_etiqueta - des15  # desconto de 15%
    elif condicao_pagamento == 3:
        return preco_etiqueta  # sem juros
    elif condicao_pagamento == 4:
        juros = (preco_etiqueta * 10)/100
        return preco_etiqueta + juros # juros de 10%
    else:
        return None

preco_etiqueta = int(input("Digite o preço da etiqueta: "))
condicao_pagamento = int(input("Digite a opção de pagamaento: "))
preco_final = calcular_preco_final(preco_etiqueta, condicao_pagamento)
print(f'O preço final do produto é: {preco_final}')
