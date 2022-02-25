import json
from menus import *
from functions import *


def getPrinters():
    with open("./controlPrinters.json", "r") as arquivo:
        dicionario = json.load(arquivo)
        return dicionario



def saveData(printers):
    with open("./controlPrinters.json", "w") as json_file:
        json.dump(printers, json_file)



def registerPrinter(printers):
    mac = input("Informe o MAC da impressora: ").upper()
    if (validateEmptyFields(mac) == False):
        return
    model = input("Informe o modelo (MODEL) da impressora: ").upper()
    if (validateEmptyFields(model) == False):
        return
    sector = input("Informe o setor (SECTOR) que a impressora fica: ").upper()
    if (validateEmptyFields(sector) == False):
        return

    try:
        countMaintenance = int(input("Informe a quantidade de manutenções que a impressora já teve: "))

        if (countMaintenance) >= 0:
            maintenance = {}
            for index in range(0, countMaintenance):
                date = input("Informe a " + str(index + 1) + "ª data da manutenção (dd/mm/aaaa): ").upper()
                date = validateDate(date)
                maintenance[date] = input("Informe o motivo da manutenção: ")

            printers[mac] = {
                "MAC": mac,
                "MODEL": model,
                "SECTOR": sector,
                "MAINTENANCE": maintenance
            }

            saveData(printers)
            menuBar()
            print("Impressora salva com sucesso!")

        else:
            print("A quantidade de manutenções não pode ser menor do que 0 (zero)!")
    except:
        print("Valor inválido")


def searchPrinter(printers):
    resp = menuSearchPrinter()

    if resp == "0":
        return

    if resp == "1":
        field = "MAC"
        searchedPrinter = {}
    elif resp == "2":
        field = "MODEL"
    elif resp == "3":
        field = "SECTOR"
    else:
        print("Opção inválida!")
        return

    search = input("Informe o " + field + " da impressora que deseja encontrar: ").upper()
    menuBar()
    for printer in printers:
        if printers[printer][field] == search:
            print(printers[printer])
            if field == "MAC":
                searchedPrinter = printers[printer]
                return searchedPrinter


def editPrinter(printers):
    mac = input("Informe o MAC da impressora que deseja editar: ").upper()
    if (validateEmptyFields(mac) == False):
        return

    menuBar()
    for printer in printers:
        if printers[printer]["MAC"] == mac:
            print(printers[printer])
            resp = input("\nEssa é a impressora que deseja alterar? <S> Sim / <N> Não: ").upper()
            menuBar()

            if resp == "S":
                opc = menuEditPrinter(printers[printer])
            else:
                return

            if opc == 0:
                return
            elif opc == 1:
                printers[printer]["MAC"] = input("Informe o novo MAC: ")
            elif opc == 2:
                printers[printer]["SECTOR"] = input("Informe o novo SETOR: ")
            elif opc == 3:
                resp = input("Adicionar uma nova manutenção? <S> Sim / <N> Não: ").upper()
                menuBar()
                
                if resp == "N":
                    print(printers[printer]["MAINTENANCE"])
                    date = input("\nDigite a data da manutenção que deseja alterar: ").upper()
                    date = validateDate(date)
                    printers[printer]["MAINTENANCE"][date] = input("Informe a manutenção que a impressora teve na data " + date + ": ")
                elif resp == "S":
                    try:
                        countMaintenance = int(input("Informe a quantidade de manutenções serão adicionadas: "))

                        if (countMaintenance) >= 0:
                            for index in range(0, countMaintenance):
                                date = input("Informe a " + str(index + 1) + "ª data a ser inserida (dd/mm/aaaa): ")
                                date = validateDate(date)
                                printers[printer]["MAINTENANCE"][date] = input("Informe o motivo da manutenção: ")
                                menuBar()
                        else:
                            print("A quantidade de manutenções não pode ser menor do que 0 (zero)!")
                    except:
                        print("Valor inválido")

                else:
                    print("Opção inválida!")
            else:
                print("Opção inválida!")
            saveData(printers)
            menuBar()
            print("Impressora salva com sucesso!")


def showAllPrinters(printers):
    for printer in printers:
        print(printers[printer])


def deletePrinter(printers):
    mac = input("Informe o MAC da impressora que deseja excluir: ").upper()
    if (validateEmptyFields(mac) == False):
        return

    menuBar()
    for printer in printers:
        if printers[printer]["MAC"] == mac:
            print(printers[printer])
            resp = input("\nEssa é a impressora que deseja excluir? <S> Sim / <N> Não: ").upper()
            if resp == "S":
                printers.pop(printer)
                saveData(printers)

                menuBar()
                print("Impressora apagada com sucesso!")
                return
            else:
                return
