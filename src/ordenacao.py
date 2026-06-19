def ordenacao_patrimonio(lista_entrada):
    lista_ordenada = []
    lista_ordenada.append(lista_entrada[0])
    for elemento in range(1, len(lista_entrada)):
        for item in range(len(lista_ordenada)):
            if lista_entrada[elemento]['patrimonio'] < lista_ordenada[item]['patrimonio']:
                lista_ordenada.insert(item, lista_entrada[elemento])
                break
            elif item == len(lista_ordenada) - 1:
                lista_ordenada.append(lista_entrada[elemento])
                break
    return lista_ordenada


def ordenacao_salario(lista_entrada):
    lista_ordenada = []
    lista_ordenada.append(lista_entrada[0])
    for elemento in range(1, len(lista_entrada)):
        for item in range(len(lista_ordenada)):
            if lista_entrada[elemento]['salario'] < lista_ordenada[item]['salario']:
                lista_ordenada.insert(item, lista_entrada[elemento])
                break
            elif item == len(lista_ordenada) - 1:
                lista_ordenada.append(lista_entrada[elemento])
                break
    return lista_ordenada