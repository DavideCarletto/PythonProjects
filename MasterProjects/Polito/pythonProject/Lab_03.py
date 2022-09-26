'''
a = 3
b = 4
c = 5

if(a<b<<c):
    print("crescente")
elif (a>b>c):
    print("decrescente")
else:
    print("nessuno dei due")
    '''
'''#Esercizio 2

voto = input("Inserisci un voto:")

votoNumerico = voto[0:1]
segnoNumero = voto[1:2]
votoFinale = -1

if votoNumerico == "A":
    votoFinale = 4
elif votoNumerico == "B":
    votoFinale = 3
elif votoNumerico == "C":
    votoFinale = 2
elif votoNumerico == "D":
    votoFinale = 1
elif votoNumerico == "F":
    votoFinale = 0
else:
    print("numero errato")

if votoNumerico == "B" or votoNumerico == "C" or votoNumerico == "D" or votoNumerico=="A":
    if votoNumerico != "A" and segnoNumero == "+" and votoNumerico != "F":
        votoFinale += 0.3

    if segnoNumero == "-":
        votoFinale -= 0.3

if votoFinale != -1:
    print(f"il tuo voto finale è {votoFinale}")
else:
    print("non si riesce a calcolare il voto finale")'''

'''#esercizio 3
stringa = input("Inserisci una stringa:")

if stringa.isupper():
    print("la stringa contiene solo caratteri maiuscoli")
if stringa.islower():
    print("la stringa contiene solo caratteri minuscoli")
if stringa.isalpha():
    print("la stringa contiene soltanto lettere")
elif stringa.isdecimal():
    print("la stringa contiene soltanto numeri")
else:
    print("la stringa contiene sia lettere che numeri")
if stringa[0].isupper():
    print("la stringa inizia con una lettera maiuscola")
if stringa.endswith("."):
    print("la stringa termina con un punto")'''

'''#esercizio 5

anno = int (input("insersci un anno:"))
if anno%4 ==0 and (anno%100!=0 or anno%400==0):
    print("l'anno selezionato è bisestile")
else:
    print("l'anno selezionato non è bisestile")'''

'''
#esercizio 6
voto = float(input("Inserisci un voto:"))
partedecimale = voto%1
votoStringa = ""
if 0<=voto<1:
    if partedecimale<0.5:
        votoStringa = "F"
    else:
        votoStringa = "D"

if 1<=voto<2:
    if voto<0.5:
        votoStringa = "D"
    else:
        votoStringa = "C"

if 2<=voto<3:
    if partedecimale<0.5:
        votoStringa = "C"
    else:
        votoStringa = "B"

if 3<=voto<=4:
    if partedecimale<0.5:
        votoStringa = "B"
    else:
        votoStringa = "A"

print(partedecimale)
'''