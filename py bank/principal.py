from funçoes import conta, criar_conta
from funçoes import fazer_login
import json

with open("usuarios.json", "r") as arquivo:
    usuarios = json.load(arquivo)

print("----seja bem vindo ao py bank----")
print("----escolha uma das opções abaixo----")
print("1 - criar conta")
print("2 - fazer login")
opcao = input("Digite a opção desejada: ")


    
if opcao == "1":
    criar_conta()

elif opcao == "2":
    usuario_logado = fazer_login()
    if usuario_logado:
        print(f"Bem-vindo, {usuario_logado}!")
        conta(usuario_logado)

