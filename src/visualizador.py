def visualizar_tabela(pessoas):
    print(f"| {'nome':<18} | {'patrimonio':>15} | {'salario':>14}")
    print(f"|{'-'*20}|{'-'*17}|{'-'*15}")

    for pessoa in pessoas:
        patrimonio_num = float(pessoa['patrimonio'])
        salario_num = float(pessoa['salario'])
        texto_patrimonio = f"R$ {patrimonio_num:.2f}"
        texto_salario = f"R$ {salario_num:.2f}"
        print(f"| {pessoa['nome']:<18} | {texto_patrimonio:>15} | {texto_salario:>14}")


def visualizar_grafico(valores, direcao_cima, linha_horizontal, rotulo_eixo_vertical, escala_valor, cor):
    if not valores:
        print("Sem valores para gerar o gráfico.")
        return

    maior_valor = max(valores)
    niveis = []
    nivel = escala_valor
    while nivel <= maior_valor:
        niveis.append(nivel)
        nivel += escala_valor
        
    if direcao_cima:
        niveis.reverse()
        
    for nivel in niveis:
        linha = ""
        if rotulo_eixo_vertical:
            texto_eixo = f"R${nivel:.2f}"
            linha += f"R${texto_eixo:>14} | "
        for valor in valores:
            if valor >= nivel:
                linha += f"\033[{cor}m █ \033[0m"  
            else:
                linha += "   " 
        print(linha)
        
    if linha_horizontal:
        tamanho_base = len(valores) * 3
        if rotulo_eixo_vertical:
            tamanho_base += 15
        print("-" * tamanho_base)
