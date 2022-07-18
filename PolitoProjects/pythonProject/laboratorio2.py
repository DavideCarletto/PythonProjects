''' Esercizio n1
numero1 = 12
numero2 = 15

print(numero1+numero2)
print (numero1-numero2)
print (numero1*numero2)
print ((numero1*numero2)/2)
print(abs(numero1-numero2))
print (max(numero1,numero2))
print (min(numero1,numero2))
'''

''' Esercizio n2
numero = input ("inserisci un numero intero di 5 cifre:")
stringa = ""
if len(numero)<=5:
    for cifra in numero:
       stringa = stringa + numero[numero.find(cifra)]+" "
print (stringa)
'''

''' Esercizio n3
stringa = "Mississippi"
stringaManipolata = ""
if(len(stringa)>=6):
    stringaManipolata = stringa[0:3]+"..."+stringa[(len(stringa)-3):len(stringa)]
    print(stringaManipolata)
'''

''' Esercizio n4
costoLibri = 500.0
numeroLibri = 39
print(f"la tassa sul costo dei libri è di {costoLibri*0.075} euro")
print(f"il costo di spedizione peri i livri è di  {2*numeroLibri} euro")
'''

''' Esercizio n5
import math

base = 12.5
altezza = 15.3

print ("l'area del rettangolo di base", base, "e altezza" , altezza,"vale: ",base*altezza)
print ("l'area del rettangolo di base", base, "e altezza" , altezza,"vale: ",(base+altezza)*2)
print (f"la diagonale del rettangolo di base {base}, e altezza {altezza} vale:  {math.sqrt((math.pow(base,2))+(math.pow(altezza,2)))}")
'''

''' Esercizio n6
numero = "4155551212"
print(f"il tuo numero di telefono formattato è: ({numero[0:3]}){numero[3:6]}-{numero[6:10]}")
'''