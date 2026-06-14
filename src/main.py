import gerenciador_arquivos
import visualizador

continua = True
pessoas =[]

while continua:
    entrada = input().upper()
    if entrada == "SAIR":
        continua = False
    print("MENU")
    print("-"*10)
    print("[CARREGAR]")
    print("[ADICIONAR]")
    print("[REMOVER]")
    print("[SALVAR]")
    escolha_menu = input("Digite a opção que você escolhe(ENTRE[]): ").upper()
    if escolha_menu == "[CARREGAR]":
        gerenciador_arquivos.carregar_pessoas("rsc/pessoas_pequeno.csv")
        print("Pessoas carregadas com sucesso!")
    elif escolha_menu == "[ADICIONAR]":
        nome = input("Digite o nome da pessoa que você quer adicionar: ")
        patrimonio = input("Digite o patrimônio da pessoa: ")
        salario = input("Digite o salário da pessoa: ")
        gerenciador_arquivos.adicionar_pessoas(nome, patrimonio, salario, pessoas)
        print("Pessoa adicionada com sucesso!")
    elif escolha_menu == "[REMOVER]":
        nome = input("Digite o nome da pessoa que você quer remover: ")
        gerenciador_arquivos.remover_pessoas(nome, pessoas)
        print("Pessoa removida com sucesso!")
    elif escolha_menu == "[SALVAR]":
        gerenciador_arquivos.salvar_pessoas("rsc/pessoas_pequeno.csv", pessoas)
        print("Pessoas salvas com sucesso!")
    else:
        print("Opção inválida! Tente digitar outra coisa.")
        continue
    print("MENU DE VISUALIZAÇÃO")
    print("-" * 20)
    print("[TABELA]")
    print("[GRAFICO SALARIOS]")
    print("[GRAFICO PATRIMONIOS]")
    escolha_visualizacao = input("Digite como você quer visualizar os dados(entre []): ").upper()
    if escolha_visualizacao == "[TABELA]":
        visualizador.visualizar_tabela(pessoas)
    elif escolha_visualizacao == "[GRAFICO SALARIOS]":
        salarios = []
        for pessoa in pessoas:
            salarios.append(pessoa["salario"])
        visualizador.visualizar_grafico(salarios, True, True, True, 1000, "34")
    elif escolha_visualizacao == "[GRAFICO PATRIMONIOS]":
        patrimonios = []
        for pessoa in pessoas:
            patrimonios.append(pessoa["patrimonio"])
        visualizador.visualizar_grafico(patrimonios, True, True, True, 10000, "32")