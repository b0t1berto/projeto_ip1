import gerenciador_arquivos
import visualizador
import ordenacao
import agrupamento

continua = True
pessoas = []

while continua:
    print("\n" + "="*20)
    print("      MENU")
    print("="*20)
    print("1 [CARREGAR]")
    print("2 [ADICIONAR]")
    print("3 [REMOVER]")
    print("4 [SALVAR]")
    print("5 [SAIR]")
    print("-"*20)
    
    escolha_menu = input("Digite a opção que você escolhe: ").upper().strip()
    
    if escolha_menu in ["5", "SAIR"]:
        continua = False
        print("Saindo do programa...")
        break
    elif escolha_menu in ["1", "CARREGAR"]:
        gerenciador_arquivos.limpar_tela()
        pessoas = gerenciador_arquivos.carregar_pessoas("rsc/pessoas_pequeno.csv")
        print("\033[32mPessoas carregadas com sucesso!\033[0m")
    elif escolha_menu in ["2", "ADICIONAR"]:
        gerenciador_arquivos.limpar_tela()
        nome = input("Digite o nome da pessoa que você quer adicionar: ")
        patrimonio = int(input("Digite o patrimônio da pessoa: "))
        salario = int(input("Digite o salário da pessoa: "))
        gerenciador_arquivos.adicionar_pessoas(nome, patrimonio, salario, pessoas)
        print("\033[32mPessoa adicionada com sucesso!\033[0m")
    elif escolha_menu in ["3", "REMOVER"]:
        gerenciador_arquivos.limpar_tela()
        nome = input("Digite o nome da pessoa que você quer remover: ")
        sucesso = gerenciador_arquivos.remover_pessoas(nome, pessoas)
        if sucesso:
            print("\033[32mPessoa removida com sucesso!\033[0m")
        else:    
            print("\033[31mNenhuma pessoa encontrada com esse nome.\033[0m")
    elif escolha_menu in ["4", "SALVAR"]:
        gerenciador_arquivos.limpar_tela()
        gerenciador_arquivos.salvar_pessoas("rsc/pessoas_pequeno.csv", pessoas)
        print("\033[32mPessoas salvas com sucesso!\033[0m")
    else:
        print("\033[31mOpção inválida! Tente digitar outra coisa.\033[0m")
        continue

    print("\nMENU DE VISUALIZAÇÃO")
    print("-" * 20)
    print("1 [TABELA]")
    print("2 [GRAFICO SALARIOS]")
    print("3 [GRAFICO PATRIMONIOS]")
    print("4 [GRAFICO DE MEDIAS]")
    print("5 [SAIR]")
    
    escolha_visualizacao = input("Digite como você quer visualizar os dados: ").upper().strip()
    
    if escolha_visualizacao in ["1", "TABELA"]:
        gerenciador_arquivos.limpar_tela()
        visualizador.visualizar_tabela(pessoas)
    elif escolha_visualizacao in ["2", "GRAFICO SALARIOS"]:
        gerenciador_arquivos.limpar_tela()
        salarios = []
        for pessoa in pessoas:
            salarios.append(float(pessoa["salario"]))
        if salarios:
            maior_salario = max(salarios)
            if maior_salario > 0:
                escala = maior_salario / 10
            else:
                escala = 1000
            visualizador.visualizar_grafico(salarios, True, True, True, escala, "34")
    elif escolha_visualizacao in ["3", "GRAFICO PATRIMONIOS"]:
        gerenciador_arquivos.limpar_tela()
        patrimonios = []
        for pessoa in pessoas:
            patrimonios.append(float(pessoa["patrimonio"]))
        if patrimonios:
            maior_patrimonio = max(patrimonios)
            if maior_patrimonio > 0:
                escala = maior_patrimonio / 10
            else:
                escala = 1000
            visualizador.visualizar_grafico(patrimonios, True, True, True, escala, "32")
    elif escolha_visualizacao in ["4", "GRAFICO DE MEDIAS"]:
        gerenciador_arquivos.limpar_tela()
        qtd = int(input("Deseja dividir em quantos grupos? "))
        while True:
            informacao = input("Você quer ver o gráfico de patrimonio ou de salarios? ")
            if informacao == "patrimonio":
                medias = agrupamento.agrupamento(pessoas, qtd)
                gerenciador_arquivos.limpar_tela()
                print("\n--- Gráfico de médias por patrimônio ---")
                visualizador.visualizar_grafico(medias, True, True, True, 1000, "32")
                break
            elif informacao == "salario":
                medias = agrupamento.agrupamento(pessoas, qtd)
                gerenciador_arquivos.limpar_tela()
                print("\n--- Gráfico de médias por salário ---")
                visualizador.visualizar_grafico(medias, True, True, True, 1000, "32")
                break
            else:
                print("\033[31mOpção inválida! Digite 'patrimonio' ou 'salario'.\033[m")
                continue
        patrimonios = []
        for pessoa in pessoas:
            patrimonios.append(float(pessoa["patrimonio"]))
        ordenacao.ordenacao_patrimonio(patrimonios)
        agrupamento.agrupamento(patrimonios, 5)
        visualizador.visualizar_grafico(agrupamento.lista_agrupamentos, True, True, True, None, "32")

    elif escolha_visualizacao in ["5", "SAIR"]:
        break
    else:
        print("\033[31mOpção de visualização inválida! Voltando ao menu principal.\033[0m")
        continue