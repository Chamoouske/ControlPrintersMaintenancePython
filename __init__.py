from menus import *
from controllerJSON import *

printers = getPrinters()

resp = ""
while resp != "0":
    resp = mainMenu(printers)

    if resp == "0":
        print("Obrigado por usar o Control Printer Maintenance!")
        menuBar()
        break
    elif resp == "1":
        registerPrinter(printers)
    elif (len(printers) > 0):
        if resp == "2":
            searchPrinter(printers)
        elif resp == "3":
            editPrinter(printers)
        elif resp == "4":
            deletePrinter(printers)
        elif resp == "5":
            showAllPrinters(printers)
        else:
            print("Opção inválida!")
    else:
        print("Opção inválida!")
