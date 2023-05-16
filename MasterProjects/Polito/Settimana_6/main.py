import math


def area_cerchio(raggio=1.0):  # valore che il raggio assume di default
    return math.pow(raggio, 2) * math.pi


def mia_funzione(a, b):
    return (a + b) * 2


def scambia_valori(a, b):
    a2 = b
    b2 = a
    return a2,b2


y = area_cerchio(5)

print(y)

print(scambia_valori(1, 2))
c = scambia_valori(3,5)
print(c[0],c[1])

v1 = 5
v2 = 3

v1,v2 = scambia_valori(v1,v2)
print(v1,v2)
