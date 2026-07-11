import json

def criar_conta():
    with open("usuarios.json", "r") as arquivo:
        usuarios = json.load(arquivo)


    usuario = input("Digite o nome do usuário: ")
    if usuario in usuarios:
        print("desculpe,mas esse usuario ja existe,")
        return
    senha = input("Digite a senha do usuário: ")

    usuarios[usuario] = {
        "senha": senha,
        "saldo": 0
    }

    with open("usuarios.json", "w") as arquivo:
        json.dump(usuarios, arquivo, indent=4)
        
def fazer_login():
    
    for cont in range(1, 4):
        with open("usuarios.json", "r") as arquivo:
            usuarios = json.load(arquivo)

        
        usuario = input("Digite o nome do usuário: ")
        senha = input("Digite a senha do usuário: ")

        if usuario in usuarios and usuarios[usuario]["senha"] == senha:
            print("Login bem-sucedido!")
            return usuario
        else:
            print("Usuário ou senha incorretos.")
    print("voce tentou muita vezes, tente novamente mais tarde")
        

def conta(usuario):
    with open("usuarios.json", "r") as arquivo:
        usuarios = json.load(arquivo)

    while True:
        print("\n===== MENU =====")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Ver saldo")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            valor = float(input("Quanto deseja depositar? R$ "))
            usuarios[usuario]["saldo"] += valor

        elif opcao == "2":
            valor = float(input("Quanto deseja sacar? R$ "))

            if valor <= usuarios[usuario]["saldo"]:
                usuarios[usuario]["saldo"] -= valor
            else:
                print("Saldo insuficiente!")

        elif opcao == "3":
            print(f"Seu saldo é: R$ {usuarios[usuario]['saldo']}")

        elif opcao == "4":
            break

        else:
            print("Opção inválida!")

        with open("usuarios.json", "w") as arquivo:
            json.dump(usuarios, arquivo, indent=4)