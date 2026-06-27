def visualizar_tabela(pessoas):
    print(f"| {'nome':<18} | {'patrimonio':>15} | {'salario':>14}")
    print(f"|{'-'*20}|{'-'*17}|{'-'*15}")

    for pessoa in pessoas:
        patrimonio_num = float(pessoa['patrimonio'])
        salario_num = float(pessoa['salario'])
        texto_patrimonio = f"R$ {patrimonio_num:.2f}"
        texto_salario = f"R$ {salario_num:.2f}"
        print(f"| {pessoa['nome']:<18} | {texto_patrimonio:>15} | {texto_salario:>14}")


def visualizar_grafico(valores, direcao_cima, linha_horizontal, rotulo_eixo_vertical, escala_valor, cor, multiplicador_log = 0):
    if not valores:
        print("Sem valores para gerar o gráfico.")
        return
    while True:
        multiplicador_log = int(input("Qual multiplicador você usará na escala?(0 pra pular) "))
        if multiplicador_log < 0:
            print("\033[31mMultiplicador inválido. Digite um valor maior ou igual a 0.\033[0m")
            continue
        elif multiplicador_log == 1:
            multiplicador_log = 0
            break
        break

    maior_valor = max(valores)
    niveis = []
    nivel = escala_valor
    if nivel <= 0:
        nivel = 1
        
    while nivel <= maior_valor:
        if multiplicador_log == 0:
            niveis.append(nivel)
            nivel += escala_valor
        elif multiplicador_log > 1:
            niveis.append(nivel)
            nivel *= multiplicador_log
        
    if direcao_cima:
        niveis.reverse()
        
    for nivel in niveis:
        linha = ""
        if rotulo_eixo_vertical:
            texto_eixo = f"R$ {nivel:.2f}"
            linha += f"{texto_eixo:>15} | "
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
