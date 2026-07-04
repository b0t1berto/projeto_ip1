import csv


def carregar_pessoas(caminho_arquivo):
    pessoas = []
    with open(caminho_arquivo, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for linha in reader:
            if not linha:
                continue
            if "nome" in linha[0].lower():
                continue
            pessoa = {
                "nome": linha[0].strip(),
                "patrimonio": linha[1].strip(),
                "salario": linha[2].strip()
            }
            pessoas.append(pessoa)
    return pessoas


def adicionar_pessoas(nome, patrimonio, salario, lista):
    nova_pessoa = {
        "nome": (nome).strip(),
        "patrimonio": float(patrimonio),
        "salario": float(salario)
    }
    lista.append(nova_pessoa)


def remover_pessoas(nome, lista):
    nome_desejado = nome.strip().lower()
    for pessoa in lista:
        if pessoa["nome"].lower() == nome_desejado:
            lista.remove(pessoa)
            return True
    return False

def salvar_pessoas(caminho_arquivo, lista):
    with open(caminho_arquivo, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        for pessoa in lista:
            writer.writerow(
                [
                pessoa["nome"], 
                pessoa["patrimonio"], 
                pessoa["salario"]
                ]
                )
