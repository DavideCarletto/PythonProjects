'''Scrivete un programma che inizializzi una lista con dieci numeri interi casuali tra 1 e
100 e, poi, visualizzi quattro righe di informazioni, contenenti:
a. Tutti gli elementi di indice pari.
b. Tutti gli elementi di valore pari.
c. Tutti gli elementi in ordine inverso.
d. Il primo e l’ultimo elemento.'''

import random


listaNumeri = []

indicePari = []
numeriPari = []

for i in range (10):

    numero = random.randrange(100)
    listaNumeri.append(numero)

    if i %2 == 0:
        indicePari.append(numero)
    if numero %2 == 0:
        numeriPari.append(numero)

print(f"i tuoi numeri: {listaNumeri}")
print(f"numeri di indice pari:{indicePari}")
print(f"numeri pari:{numeriPari}")
listaInversa = list(reversed(listaNumeri))
print(f"ordine inverso:{listaInversa}")
print(f"primo e ultimo elemento:{listaNumeri[0]} e {listaNumeri[-1]}")