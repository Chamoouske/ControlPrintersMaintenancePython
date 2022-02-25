def validateEmptyFields(field):
    if field == '':
        print("Valor inválido")
        return False

def validateDate(date):
    if date[2] != "/":
        day = date[0] + date[1]
        month = date[2]+date[3]
        year = date[4]+date[5]

        date = day + "/" + month + "/" + year

    return date

