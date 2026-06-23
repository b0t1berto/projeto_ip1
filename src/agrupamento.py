import ordenacao

def agrupamento(lista, qtd_grupos, chave='patrimonio'):
    grupo = []
    lista_agrupamentos = []
    tamanho = len(lista)

    if qtd_grupos <= 0 or tamanho == 0:
        return []
    qtd_elementos_grupo = tamanho // qtd_grupos
    if qtd_elementos_grupo == 0:
        qtd_elementos_grupo = 1

    if chave == 'patrimonio':
        lista = ordenacao.ordenacao_patrimonio(lista)
    elif chave == 'salario':
        lista = ordenacao.ordenacao_salario(lista)
    else:
        chave == 'patrimonio'
    for elemento in lista:
        grupo.append(float(elemento[chave]))
        if len(grupo) == qtd_elementos_grupo:
            media = sum(grupo) / len(grupo)
            lista_agrupamentos.append(media)
            grupo = []
    if grupo:
        media = sum(grupo) / len(grupo)
        lista_agrupamentos.append(media)
    return lista_agrupamentos