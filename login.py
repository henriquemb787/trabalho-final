import arquivo

print("Bem-vindo ao Py Bank!")

login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "12345":
    print("Login bem-sucedido!")
    arquivo.inicial()
else:
    print("Login ou senha incorretos!")