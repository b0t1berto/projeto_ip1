import streamlit as st
import pandas as pd

def visualizar_tabela(pessoas):
    dados = []

    for pessoa in pessoas:
        patrimonio_num = float(pessoa['patrimonio'])
        salario_num = float(pessoa['salario'])

        dados.append({
            "Nome": pessoa["nome"],
            "Patrimônio": f"R$ {patrimonio_num:.2f}",
            "Salário": f"R$ {salario_num:.2f}"
        })

    df = pd.DataFrame(dados)
    st.dataframe(df, use_container_width=True)


def visualizar_grafico(valores, direcao_cima, linha_horizontal, rotulo_eixo_vertical, escala_valor, cor, multiplicador_log = 0):
    if not valores:
        st.write("Sem valores para gerar o gráfico.")
        return
    multiplicador_log = st.number_input(
        "Qual multiplicador você usará na escala? ",
        min_value=0,
        key=f"multiplicador_{escala_valor}_{cor}"
        )
    if multiplicador_log == 1:
        multiplicador_log = 0

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

    caractere_bloco = "🟩" if cor == "32" else "🟦" if cor == "34" else "⬛"

    conteudo_grafico = ""    
    for nivel in niveis:
        linha = ""
        if rotulo_eixo_vertical:
            texto_eixo = f"R$ {nivel:.2f}"
            linha += f"{texto_eixo:>15} | "
        for valor in valores:
            if valor >= nivel:
                linha += f"{caractere_bloco}"  
            else:
                linha += "    " 
        conteudo_grafico += linha + "\n"
        
    if linha_horizontal:
        tamanho_base = len(valores) * 4
        if rotulo_eixo_vertical:
            tamanho_base += 18
        conteudo_grafico += ("-" * tamanho_base) + "\n"

    st.code(conteudo_grafico, language="text")
