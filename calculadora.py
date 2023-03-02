from time import sleep

while True:

    valor1 = 0
    valor2 = 0
    resultado = 0

    print("\n\n::::::::::::::::::: MENU PRINCIPAL :::::::::::::::::::")
    print("\n ::::::::::::::::::: Calculadora :::::::::::::::::::")
    print("\nPossíveis códigos de operações: \n")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    operacao = int(input("\nInforme o código da operação desejada: "))

    if operacao == 1:
        print("\n::::::::::::::::::: SOMA :::::::::::::::::::")

        valor1 = int(input("\nInforme o primeiro valor da soma: "))
        valor2 = int(input("Informe o segundo valor da soma: "))

        resultado = valor1 + valor2

        print(f"\nO resultado da soma dos dois valores descritos é de: {resultado}.")

        sleep(2.5)

        while True:

            print("\n::::::::::::::::::: OPÇÕES :::::::::::::::::::")
            print("\n1 - Realizar outra operação de soma com outros valores.")
            print("\n2 - Voltar para o Menu Principal.")

            opcao = int(input("\nInforme a opção desejada: "))
            
            if opcao == 1:
                
                print("\n::::::::::::::::::: SOMA :::::::::::::::::::")

                valor1 = int(input("\nInforme o primeiro valor da soma: "))
                valor2 = int(input("Informe o segundo valor da soma: "))

                resultado = valor1 + valor2

                print(f"\nO resultado da soma dos dois valores descritos é de: {resultado}.")
                
                sleep(2.5)

            elif opcao == 2:
                print("\nRetornando ao Menu Principal.")
                sleep(2.5)
                break

            else:
                (print("\nValor inválido, voltando para o Menu Principal."))
                sleep(2.5)
                break
            
    elif operacao == 2:
        print("\n::::::::::::::::::: SUBTRAÇÃO :::::::::::::::::::")

        valor1 = int(input("\nInforme o primeiro valor da subtração: "))
        valor2 = int(input("Informe o segundo valor da subtração: "))

        resultado = valor1 - valor2

        print(f"\nO resultado da subtração dos dois valores descritos é de: {resultado}.")

        sleep(2.5)

        while True:

            print("\n::::::::::::::::::: OPÇÕES :::::::::::::::::::")
            print("\n1 - Realizar outra operação de subtração com outros valores.")
            print("\n2 - Voltar para o Menu Principal.")

            opcao = int(input("\nInforme a opção desejada: "))
            
            if opcao == 1:

                print("\n::::::::::::::::::: SUBTRAÇÃO :::::::::::::::::::")

                valor1 = int(input("\nInforme o primeiro valor da subtração: "))
                valor2 = int(input("Informe o segundo valor da subtração: "))

                resultado = valor1 - valor2

                print(f"\nO resultado da subtração dos dois valores descritos é de: {resultado}.")
                
                sleep(2.5)

            elif opcao == 2:
                print("\nRetornando ao Menu Principal.")
                sleep(2.5)
                break

            else:
                (print("\nValor inválido, voltando para o Menu Principal."))
                sleep(2.5)
                break

    elif operacao == 3:
        print("\n::::::::::::::::::: MULTIPLICAÇÃO :::::::::::::::::::")

        valor1 = int(input("\nInforme o primeiro valor da multiplicação: "))
        valor2 = int(input("Informe o segundo valor da multiplicação: "))

        resultado = valor1 * valor2

        print(f"\nO resultado da multiplicação dos dois valores descritos é de: {resultado}.")

        sleep(2.5)

        while True:

            print("\n::::::::::::::::::: OPÇÕES :::::::::::::::::::")
            print("\n1 - Realizar outra operação de multiplicação com outros valores.")
            print("\n2 - Voltar para o Menu Principal.")

            opcao = int(input("\nInforme a opção desejada: "))
            
            if opcao == 1:

                print("\n::::::::::::::::::: MULTIPLICAÇÃO :::::::::::::::::::")

                valor1 = int(input("\nInforme o primeiro valor da multiplicação: "))
                valor2 = int(input("Informe o segundo valor da multiplicação: "))

                resultado = valor1 * valor2

                print(f"\nO resultado da multiplicação dos dois valores descritos é de: {resultado}.")
                
                sleep(2.5)

            elif opcao == 2:
                print("\nRetornando ao Menu Principal.")
                sleep(2.5)
                break

            else:
                (print("\nValor inválido, voltando para o Menu Principal."))
                sleep(2.5)
                break

    elif operacao == 4:
        print("\n::::::::::::::::::: DIVISÃO :::::::::::::::::::")

        valor1 = int(input("\nInforme o primeiro valor da divisão: "))
        valor2 = int(input("Informe o segundo valor da divisão: "))

        resultado = valor1 / valor2

        print(f"O resultado da divisão dos valores descritos é  de: {resultado}")

        sleep(2.5)

        while True:

            print("\n::::::::::::::::::: OPÇÕES :::::::::::::::::::")
            print("\n1 - Realizar outra operação de divisão com outros valores.")
            print("\n2 - Voltar para o Menu Principal.")

            opcao = int(input("\nInforme a opção desejada: "))
            
            if opcao == 1:

                print("\n::::::::::::::::::: DIVISÃO :::::::::::::::::::")

                valor1 = int(input("\nInforme o primeiro valor da divisão: "))
                valor2 = int(input("Informe o segundo valor da divisão: "))

                resultado = valor1 / valor2

                print(f"O resultado da divisão dos valores descritos é  de: {resultado}")
                
                sleep(2.5)

            elif opcao == 2:
                print("\nRetornando ao Menu Principal.")
                sleep(2.5)
                break

            else:
                (print("\nValor inválido, voltando para o Menu Principal."))
                sleep(2.5)
                break
    
    elif operacao == 5:
        print("\nSaindo.")
        sleep(2.5)
        break