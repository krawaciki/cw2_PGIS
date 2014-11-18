# -*- coding: cp1250 -*-
import math
class Zespolona:
    r = 0
    u = 0
    def __init__ (self, a):
        self.a = a
    def setR(self, d):
        self.a = (d,self.a[1]) 
    def setU(self, d):
        self.a = (self.a[0],d)
    def getR(self):
        return self.a[0]
    def getU(self):
        return self.a[1] 
    def dodaj(self, b):
        return (self.a[0]+b[0], self.a[1]+b[1])
    def odejmij(self, b):
        return (self.a[0]-b[0], self.a[1]-b[1])
    def modul(self):
        return math.sqrt(self.a[0]**2+self.a[1]**2)
    def wyswietl (self):
        return (str(self.a[0])+" + "+str(self.a[1])+"i")

z1 = (4,2)
z2 = (3,4)
obiekt = Zespolona(z1)
print("z1: " + obiekt.wyswietl())
obiekt.setR(1)
obiekt.setU(2)
print("po ustawieniu ustawiaczem: " + obiekt.wyswietl())
print("pobranie pobieraczem: " + str(obiekt.getR()) + " + " + str(obiekt.getU()) +"i")
z3 = obiekt.dodaj(z2)
print("suma: " + str(z3[0])+" + "+str(z3[1])+"i")
z3 = obiekt.odejmij(z2)
print("roznica: " + str(z3[0])+" + "+str(z3[1])+"i")
z3 = obiekt.modul()
print("modul: " + str(z3))
