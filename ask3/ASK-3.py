
Agora = {
    "Item 1": 15,
    "Item 2": 20,
    "Item 3": 12,
    "item 4": 13,
    "Item 5": 5,
    "Item 6": 2,
    "Item 7": 3,
    "Item 8": 16,
    "Item 9": 28,
}

def poso_pliromis (lista, foros):
    i = 0
    poso = 0
    geniko_poso = 0.0
    temp = ""
    while i < len(lista):
        temp = lista[i]
        poso = poso + Agora.get(temp)
        i += 1
    poso_forou = poso * (foros/100)
    geniko_poso = poso + poso_forou
    print("Poso: " + str(poso) + "Poso Forou: " + str(poso_forou))
    print("Geniko Poso")
    print(geniko_poso)


list = []
x = False
temp = ""
while x == False:
    temp = input("Grapse Item Agoras: ")
    if temp == "Done":
        x = True
    else:
        list.append(temp)
foros = float(input("Dose pososto forou: "))
poso_pliromis(list, foros)


