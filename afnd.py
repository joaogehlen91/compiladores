entrada = ['se', 'entao', 'senao']
entrada = ['se', 'entao']

lista_simbolos = ['$']
estados_finais = []

x = 'x'

matriz = []


estado = 0

for token in entrada:
    for simbolo in token:
        linha = [[estado]]
        estado += 1
        if simbolo not in lista_simbolos:
            lista_simbolos.append(simbolo)
            linha.append([estado])
            matriz.append(linha)
        else:
            linha.append()

    # escreve em uma lista os estados finais #
    estados_finais.append([estado])


        


print(matriz)
print(lista_simbolos)


linha = [[3], ]
lista_simbolos = ['$', 's', 'e']

matriz = 
[
 0   [[0], [1]],
 1   [[1], [2]]
 2   [[2], [3]]
]