def visualizar_tabela(pessoas):
    print(f"| {'nome':<15} | {'patrimonio':>12} | {'salario':>12}")
    print(f"|{'-'*17}|{"-"*14}|{'-'*14}")

    for pessoa in pessoas:
        print(
            f"| {pessoa['nome']:<15} |"
            f"R$ {pessoa['patrimonio']:>9.2f} |"
            f"R$ {pessoa['salario']:>9.2f}"
        )


def visualizar_grafico(valores, direcao_cima, linha_horizontal, rotulo_eixo_vertical, escala_valor, cor):
    maior_valor = max(valores)
    niveis = []
    nivel = escala_valor
    while nivel <= maior_valor:
        niveis.append(nivel)
        nivel += escala_valor
    if direcao_cima:
        niveis.reverse()
    for nivel in niveis:
        linha=""
        if rotulo_eixo_vertical:
            linha += f"R${nivel:8.2f}"
    for valor in valores:
        if valor >= nivel:
            linha += f"\033[{cor}m|\033[0m"
        else:
            linha += " "
        print(linha)
    if linha_horizontal:
        tamanho = len(valores)
    if rotulo_eixo_vertical:
        tamanho += 12
        print("-" * tamanho)
