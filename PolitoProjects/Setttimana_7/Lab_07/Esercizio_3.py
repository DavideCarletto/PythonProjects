'''Scrivete la funzione def sameSet(a, b) che verifichi se due liste contengono gli
stessi elementi, indipendentemente dall’ordine e ignorando la presenza di duplicati.
Ad esempio, le due liste 1 4 9 16 9 7 4 9 11 e 11 11 7 9 16 4 1 devono essere
considerate uguali. La funzione non deve modificare le liste ricevute come parametri.'''

def sameSet(lista1,lista2):
    if lista1 == lista2:
        print("le due liste sono uguali")
    else:
        print("le due liste sono diverse")

lista1 = [1,2,3,4,5]
lista2 = [2,1,3,5,4]

sameSet(sorted(lista1),sorted(lista2))

print(lista1)
print(lista2)