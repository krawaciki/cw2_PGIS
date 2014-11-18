# -*- coding: cp1250 -*-
def wczytywanie(lokalizacja):
    lista=[]
    plik=open(lokalizacja,'r')
    plik1=open('statystyki.txt','w')
    tekst=str(plik.read())
    tekst=tekst.replace('.', '')
    tekst=tekst.replace('*', '')
    tekst=tekst.replace('?', '')
    tekst=tekst.replace('(', '')
    tekst=tekst.replace(')', '')
    tekst=tekst.replace('!', '')
    tekst=tekst.replace(',', '')
    tekst=tekst.replace(';', '')
    tekst=tekst.replace(':', '')
    tekst=tekst.replace('”', '')
    tekst=tekst.replace('„', '')
    tekst=tekst.replace('', '')
    tekst=tekst.replace('-', '')
    tekst=tekst.replace('~', '')
    tekst=tekst.replace('«', '')
    tekst=tekst.replace('»', '')
    tekst=tekst.split()
    unik_slowa=list(set(tekst))
    for i in xrange(0,len(unik_slowa)):
        k=0
        for j in xrange(0,len(tekst)):
            if unik_slowa[i]==tekst[j]:
                k+=1
        lista.append([k, unik_slowa[i]])
    lista=sorted(lista, reverse=True)
    plik1.writelines("słowo \t|liczba wystąpień\n")
    plik1.writelines("____________________________\n")
    for i in xrange(0,len(lista)):
        plik1.writelines(str(lista[i][1])+"\t|\t"+str(lista[i][0])+"\n")
    plik.close
    plik1.close
    return True
wczytywanie("tekst.txt")
