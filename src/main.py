continua = True

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