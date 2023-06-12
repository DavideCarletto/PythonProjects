''' Spesso i valori raccolti durante un esperimento vanno corretti, per togliere parte del
rumore di misura. Un approccio semplice a questo problema prevede di sostituire, in
una lista, ciascun valore con la media tra il valore stesso e i due valori adiacenti (o un
unico adiacente se il valore in esame si trova a una delle due estremità della lista).
Realizzate un programma che svolga tale operazione, senza creare un’altra lista.'''

lista  = [1,2,3,4,5,6,7,8,9]

for i in range(len(lista)):
    if(i == 0):
      lista[i] = (lista[i]+lista[i+1])/2
    elif(i == len(lista)-1):
        lista[i] = (lista[i] + lista[i - 1]) / 2
    else:
        lista[i] = (lista[i-1] + lista[i+1]) / 2

print(lista)