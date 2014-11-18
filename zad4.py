# -*- coding: cp1250 -*-
import math
import random

class Postac:
    exp = 0
    wynik = {'wygrana':0,'przegrana':0,'remis':0}
    w = 0
    p = 0
    r = 0
    def __init__ (self, lvl, umiej1, umiej2):
        self.lvl = lvl
        self.umiej1 = umiej1
        self.umiej2 = umiej2
    def getExp(self):
        return self.exp 
    def walcz(self):
        for i in xrange (0,self.lvl):
            ja = random.random()*self.umiej1
            wrog = random.random()*0.05*self.lvl
            if ja > wrog:
                self.exp = self.exp+2*(self.lvl)**(-1)
                info = "Zwycięstwo"
                self.wynik['wygrana'] = self.wynik['wygrana'] + 1
            elif ja < wrog:
                self.exp = self.exp-1*(self.lvl)**(-1)
                info = "Przegrana"
                self.wynik['przegrana'] = self.wynik['przegrana'] + 1
            else:
                info = "Remis"
                self.wynik['remis'] = self.wynik['remis'] + 1
        return self.wynik
    def lvl_up(self):
        if self.wynik['wygrana']>self.wynik['przegrana']:
            return (self.lvl+self.wynik['wygrana']-self.wynik['przegrana'])
        else:
            return self.lvl
class Mag (Postac):
    cz = "Hokus pokus!"
    def setCzar(self, cz):
        self.cz = cz
    def setMoc(self, wynik, moc):
        self.moc=moc+round(1+wynik['wygrana']*random.uniform(0,0.2))
    def getMoc(self):
        return self.moc 
    def zucCzar(self):
        if (self.cz)=="":
            return(self.cz)
        else:
            return(self.cz)
class Wojownik (Postac):
    def setObrona(self, wynik, obrona):
        self.obrona=obrona+round(1+wynik['wygrana']*random.uniform(0,10))
    def bronSie(self):
        print("Obrona")
class Paladyn(Mag,Wojownik):
    def czarObronny(self):
        print("Zasłona czarami")

poziom = 10
moc = 1
obrona = 1
Gandalf = Paladyn(poziom, moc, obrona)
Gandalf.setCzar("Abrakadabra!")
print("Rzucony czar: " + Gandalf.zucCzar())
walka = Gandalf.walcz()
print("Wyniki walki: " + str(walka))
print("Zdobyte doświadczenie: " + str(Gandalf.getExp()))
Gandalf.setMoc(walka, moc)
print("Moc: "+str(Gandalf.getMoc()))
print("Poziom: "+str(Gandalf.lvl_up()))
