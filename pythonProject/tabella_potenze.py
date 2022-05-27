import math

BASE_MINIMA = 1
BASE_MASSIMA = 10
ESPONENTE_MINIMO = 1
ESPONENTE_MASSIMO = 4
#per ogni base tra min e max:
base = BASE_MINIMA
esponente = ESPONENTE_MINIMO

while esponente <= ESPONENTE_MASSIMO:
    valore = f"x^{esponente}"
    print(f"{valore:>10}", end=' ')#il maggiore serve per allineare a destra
    esponente+=1

print("\n")

while base<=BASE_MASSIMA:
    #stampa una riga con tutte le potenze di quella base
   # print(f"riga con base {base=}")

    #per ogni esponente tra min e max
    esponente = ESPONENTE_MINIMO
    while esponente <=ESPONENTE_MASSIMO:
        #stampa un valore base elevato a esponente
        #print(f"colonna con {base=} ed esponente {esponente=}")
        valore = math.pow(base, esponente)  #oppure valore = base**esponente
        print(f"{valore:10}",end = " ")    #10 d significa 10 decimali
        esponente = esponente+1

    #vai a capo
    #print("")  #equivale a print("", end = "\n")
    print()     #uguale a sopra
    base+=1
print("\n")


    #se lo volessi fare con il for:
for esponente in range (ESPONENTE_MINIMO,ESPONENTE_MASSIMO+1):
    valore = f"x^{esponente}"
    print(f"{valore:>10}", end=' ')  # il maggiore serve per allineare a destra

print("\n")

for base in range(BASE_MINIMA,BASE_MASSIMA+1):
    for esponente in range(ESPONENTE_MINIMO,ESPONENTE_MASSIMO+1):
        valore = math.pow(base, esponente)
        print(f"{valore:10}",end = " ")

    print()
