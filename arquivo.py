def inicial():
    import arquivos

    while True:
        print("\033c", end="")  # Limpa a tela do terminal
        opcao = input("""
        --- Cadastro de usuários ---
        1. Adicionar
        2. Pesquisar
        3. Remover
        4. Listar todos
                    
        Selecione uma opção (0 para sair): """)

        
        if opcao == "0":
            break

        if opcao == "1":
            arquivos.adicionar_usuario()

        elif opcao == "2":
            arquivos.pesquisar_usuario()

        elif opcao == "3":
            arquivos.remover_usuario()

        elif opcao == "4":
            arquivos.listar_usuarios()