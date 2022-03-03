def mainMenu(printers):
    menuBar()
    print("Informe a opção de acordo com o número ao lado dela: ")
    print("1 -> Cadastrar nova impressora")

    if (len(printers) > 0):
        print("2 -> Buscar impressora")
        print("3 -> Editar impressora")
        print("4 -> Excluir impressora")
        print("5 -> Listar impressoras")
    else:
        print("Não existe impressoras cadastradas!")
        print("Cadastre uma nova para aparecer novas opções no menu!")

    print("0 -> Sair")
    resp = input("Informe a sua escolha: ")

    return resp


def menuSearchPrinter():
    menuBar()
    print("Informe a opção de acordo com o número ao lado dela: ")
    print("1 -> Buscar pelo MAC")
    print("2 -> Buscar pelo modelo")
    print("3 -> Buscar pelo setor")

    print("0 -> Voltar")
    resp = input("Informe a sua escolha: ")
    menuBar()

    return resp


def menuEditPrinter(printer):
    resp = "S"
    while resp == "S":
        print("Informe a opção da informação da impressora " +
              printer["MAC"]+" que deseja editar: ")
        print("1 -> Modelo")
        print("2 -> Setor")
        print("3 -> Data da Compra")
        print("4 -> Manutenções")
        print("0 -> Voltar")
        try:
            opc = int(input("Informe a sua escolha: "))
            menuBar()
            return (opc)
        except:
            print("Opção inválida")
            menuBar()


def menuBar():
    print("\n==================================================================================================\n")
