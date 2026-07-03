
import arquivo
login = input("Digite o login: ")
senha = input("Digite a senha: ")

if login == "admin" and senha == "12345":
    arquivo.inicial()
    print("Login bem-sucedido!")
else:
    print("Login ou senha incorretos!")
