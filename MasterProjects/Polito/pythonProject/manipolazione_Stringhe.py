import math
from math import isclose

'''stringa = "questa è una stringa"

print (stringa.upper())
print (stringa.replace("una", "pota"))

num = "3,14"
print (float(num.replace("," , ".")))

piano = int (input("inserisci il piano in cui ti trovi:"))

if(piano > 13):
    print ("hai superato il piano fantasma")

else:
    if(piano == 13):
        print ("piano inesistente")

    print("non hai superato il piano fantasma")

a = 2<5
if(a == True):
    print("è minore di 5")


n = float (input("inserisci un numero:"))
v = math.sqrt(n);
print(n,v**2)

if(n == v**2):
    print (n, "e",v**2,"sono uguali")
else:
    print (n, "e",v**2,"sono diversi")

if(isclose(n,v**2,rel_tol=0.000000000005)):
    print(n, "e", v ** 2, "sono uguali")
else:
    print(n, "e", v ** 2, "sono diversi")

maggiore = 5>3
if maggiore:
    print("5 è maggiore di 3")
else:
    print("non è maggiore")
'''
print (f"Il mio valore è {2+5}")
print("Il mio magico valore è {2+5}")
print("Il mio %s numero magico è %d" % ('terzo',2+5))

a = 2.5
b = 4
c = 754
print ("Numero floaf con spazi inziali: ###%10.2f###"%(a))

print("%10.1f %10.1f %10.1f" % (a,b,c))
print(f"{a: 10.1f} {b: 10.1f} {c:10.1f}")
a = 24.54
b = 434
c = 75.34
print("%10.1f %10.1f %10.1f" % (a,b,c))

a = 2.3434
b = 400.34
c = 74
print("%10.1f %10.1f %10.1f" % (a,b,c))

saldoIniziale = 10000
TASSO_INTERESSE = 0.05
anno = 2021

while saldoIniziale<20000:
    interessi_maturati = saldoIniziale*TASSO_INTERESSE
    saldoIniziale= saldoIniziale+ interessi_maturati
    anno = anno +1

print(f"per raggiungere {saldoIniziale} euro dovrei aspettare al {anno}")