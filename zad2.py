# -*- coding: cp1250 -*-
def rachunek(zamowienie):
    menu = {}
    tekst = ""
    i = 0
    plik = open("menu.txt")
    for tekst in plik:
        tekst = tekst.split()
        menu[tekst[0]] = (tekst[1])
        i = i+1
    cena = 0
    cenaK = 0
    for i in zamowienie:
        if i in menu:
            cena = cena + int(menu[i])
#napiwek
        if cena > 5 : cenaK = cena + 5
        elif cena > 10 : cenaK = cena + 10
        elif cena > 15 : cenaK = cena + 15
        else : cenaK = cena + 20
    return cenaK

print("Warto�� 1. zam�wienia: " + str(rachunek(["wodzionka", "szpajza"])))
print("Warto�� 2. zam�wienia: " + str(rachunek(["karbinadle", "kluski","�urek"])))
print("Warto�� 3. zam�wienia: " + str(rachunek(["ciapkapusta", "krewetki"])))
