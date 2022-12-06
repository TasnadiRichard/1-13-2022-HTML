import sys
def teszt(sikeres_teszt):
    sorszam = sys._getframe(1).f_lineno
    if sikeres_teszt:
        msg = "A(z){0}. sorban álló teszt sikeres.".format(sorszam)
    else:
        msg = ("A(z){0}. sorban álló teszt SIKERTELEN.".format(sorszam))
    print(msg)

a=int(input("Óra"))*3600  
b=int(input("Perc"))*60
c=int(input("Másodperc"))
x=0
def masodpercre_valtas(a,b,c,):
    print(x)
    return x=a+b+c
teszt(masodpercre_valtas(a,b,c) == x)