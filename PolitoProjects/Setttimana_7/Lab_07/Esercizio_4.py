'''Scrivete un programma che generi una sequenza di 20 valori casuali compresi tra 0 e
99, poi visualizzi la sequenza generata, la ordini e la visualizzi di nuovo, ordinata.
Usate il metodo sort.'''

import random

lista = []

for i in range (20):
    numero = random.randrange(100)
    lista.append(numero)

print(lista)
lista.sort()
print(lista)