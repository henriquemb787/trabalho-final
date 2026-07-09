def inicial():
    import arquivos

    while True:

        opcao = input("""
        --- Py Bank ---
        1. Sacar dinheiro
        2. Depositar dinheiro
        3. Pix

        Selecione uma opção (0 para sair): """)

        if opcao == "0":
            print("Obrigado por usar o Py Bank!")
            break

        elif opcao == "1":
            arquivos.retirar()

        elif opcao == "2":
            arquivos.depositar()

        
        

        else:
            print("Opção inválida.")
        