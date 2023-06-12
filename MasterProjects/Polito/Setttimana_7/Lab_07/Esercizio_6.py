'''Scrivete la funzione sum_without_smallest che calcoli la somma di tutti i valori di
una lista, escludendo il valore minimo.'''

def sum_without_smallest(lista):
    somma = 0
    lista.remove(min(lista))
    for i in range(len(lista)):
        somma += lista[i]
    return somma

lista = [1,2,3,4,5,6,7,8,9]

print(sum_without_smallest(lista))