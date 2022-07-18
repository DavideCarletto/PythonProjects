'''Scrivete un programma che acquisisca da tastiera una sequenza di numeri interi
(terminata da una riga vuota), calcoli la somma alternata degli elementi di una lista.
Ad esempio, se il programma legge i dati 1 4 9 16 9 7 4 9 11, deve calcolare e
visualizzare 1 – 4 + 9 – 16 + 9 – 7 + 4 – 9 + 11 = –2. '''

def calcolaSomma (lista):
    somma = 0
    stringaVisualizzata = ""
    for i  in range(len(lista)):
        moltiplicatore = 1
        segno = "+"
        if(i%2 == 0):
            moltiplicatore = -1
            segno = "-"

        if(i == len(lista)-1):
            segno = "="

        somma += lista[i]*moltiplicatore
        stringaVisualizzata += str(lista[i])+segno

    print(f"somma: {stringaVisualizzata}{somma}")

listaNumeri = []
ferma = False
while(not ferma):
    numero =  input("inscerisci una sequenza di numeri (premere invio ogni numero e per terminare stringa vuota):")
    if(numero == ""):
        ferma = True
    else:
     listaNumeri.append(int(numero))

calcolaSomma(listaNumeri)
