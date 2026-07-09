def retirar():
    senha_correta = "1234"
    valor = float(input("Digite o valor do saque: "))

    if valor <= 0:
        print("O valor do saque deve ser maior que zero.")
    else:
        senha = input("Digite sua senha para confirmar: ")

        if senha == senha_correta:
            print("Saque realizado com sucesso!")
        else:
            print("Senha incorreta.")


def depositar():
    senha_correta = "1234"
    valor = float(input("Digite o valor do depósito: "))

    if valor <= 0:
        print("O valor do depósito deve ser maior que zero.")
    else:
        senha = input("Digite sua senha para confirmar: ")

        if senha == senha_correta:
            print("Depósito realizado com sucesso!")
        else:
            print("Senha incorreta.")