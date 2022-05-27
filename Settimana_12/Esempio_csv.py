import csv
from operator import itemgetter

libri = []

with open("Prova2_csv.csv", "r") as file:

    csv_reader = csv.reader(file, delimiter = ";")

    for riga in csv_reader:
        nuovo_libro = dict()

        nuovo_libro["Autore"] = riga[0]
        nuovo_libro["Titolo"]  = riga[1]
        nuovo_libro["Data"] = riga[2]

        libri.append(nuovo_libro)

print(libri[1])
libri.sort(key=itemgetter("Titolo"))
print(libri)
