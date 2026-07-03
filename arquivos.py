
usuarios = {"admin": 12345}

def adicionar_usuario():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- ADICIONAR USUÁRIOS ---")
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")
    usuarios[usuario] = senha

def pesquisar_usuario():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- PESQUISAR USUÁRIOS ---")
    usuario = input("Digite o usuário para pesquisar: ")
    if usuario in usuarios:
        print(f"Usuário encontrado: {usuario}")
        input("Pressione Enter para continuar...")
    else:
        print("Usuário não encontrado!")

def remover_usuario():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- REMOVER USUÁRIO ---")
    usuario = input("Digite o usuário para remover: ")
    if usuario in usuarios:
        del usuarios[usuario]
        print("Usuário removido com sucesso!")
    else:
        print("Usuário não encontrado!")

def listar_usuarios():
    print("\033c", end="")  # Limpa a tela do terminal
    print("-- LISTA DE USUÁRIOS CADASTRADOS ---")
    if usuarios:
        for usuario in usuarios:
            print(usuario)
    else:
        print("Nenhum usuário cadastrado!")