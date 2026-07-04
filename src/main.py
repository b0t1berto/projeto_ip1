import gerenciador_arquivos
import visualizador
import ordenacao
import agrupamento
import streamlit as st

st.title("Gerenciador de Pessoas")

if "pessoas" not in st.session_state:
    st.session_state.pessoas = []

escolha_menu = st.selectbox(
    "Menu",
    ["CARREGAR", "ADICIONAR", "REMOVER", "SALVAR"],
    key="menu_principal"
)
if escolha_menu == "CARREGAR":
    st.session_state.pessoas = gerenciador_arquivos.carregar_pessoas("rsc/pessoas_pequeno.csv")
    st.success("Pessoas carregadas com sucesso!")
elif escolha_menu == "ADICIONAR":
    with st.form("form_adicionar"):
        nome = st.text_input("Digite o nome da pessoa que você quer adicionar: ")
        patrimonio = st.number_input("Digite o patrimônio da pessoa: ", min_value=0)
        salario = st.number_input("Digite o salário da pessoa: ", min_value=0)
        botao_add = st.form_submit_button("Adicionar pessoa")

        if botao_add:
            gerenciador_arquivos.adicionar_pessoas(nome, patrimonio, salario, st.session_state.pessoas)
            st.success("Pessoa adicionada com sucesso!")
elif escolha_menu == "REMOVER":
    with st.form("form_remover"):
        nome = st.text_input("Digite o nome da pessoa que você quer remover: ")
        botao_rem = st.form_submit_button("Remover pessoa")

        if botao_rem:
            sucesso = gerenciador_arquivos.remover_pessoas(nome, st.session_state.pessoas)
            if sucesso:
                st.success("Pessoa removida com sucesso!")
            else:
                st.error("Nenhuma pessoa encontrada com esse nome.")
elif escolha_menu == "SALVAR":
    gerenciador_arquivos.salvar_pessoas("rsc/pessoas_pequeno.csv", st.session_state.pessoas)
    st.success("Pessoas salvas com sucesso!")

st.divider()

escolha_visualizacao = st.selectbox(
    "Escolha uma opção de visualização:",
    ["NENHUM", "TABELA", "GRAFICO SALARIOS", "GRAFICO PATRIMONIOS", "GRAFICO DE MEDIAS"],
    key="menu_visualizacao"
)

if escolha_visualizacao != "NENHUM":
    if escolha_visualizacao == "TABELA":
        visualizador.visualizar_tabela(st.session_state.pessoas)

    elif escolha_visualizacao == "GRAFICO SALARIOS":
        salarios = []
        for pessoa in st.session_state.pessoas:
            salarios.append(float(pessoa["salario"]))
        if salarios:
            maior_salario = max(salarios)
            if maior_salario > 0:
                escala = maior_salario / 10
            else:
                escala = 1000
            visualizador.visualizar_grafico(salarios, True, True, True, escala, "34")

    elif escolha_visualizacao == "GRAFICO PATRIMONIOS":
        patrimonios = []
        for pessoa in st.session_state.pessoas:
            patrimonios.append(float(pessoa["patrimonio"]))
        if patrimonios:
            maior_patrimonio = max(patrimonios)
            if maior_patrimonio > 0:
                escala = maior_patrimonio / 10
            else:
                escala = 1000
            visualizador.visualizar_grafico(patrimonios, True, True, True, escala, "32")

    elif escolha_visualizacao == "GRAFICO DE MEDIAS":
        qtd = st.number_input("Deseja dividir em quantos grupos? ", min_value=1, step=1)
        informacao = st.selectbox(
            "Você quer ver o gráfico de patrimonio ou de salários?",
            ["patrimônio", "salários"],
            key="qtd_grupos"
        )
        if informacao == "patrimônio":
            medias = agrupamento.agrupamento(st.session_state.pessoas, qtd)
            st.write("\n--- Gráfico de médias por patrimônio ---")
            visualizador.visualizar_grafico(medias, True, True, True, 1000, "32")
        elif informacao == "salários":
            medias = agrupamento.agrupamento(st.session_state.pessoas, qtd)
            st.write("\n--- Gráfico de médias por salário ---")
            visualizador.visualizar_grafico(medias, True, True, True, 1000, "32")