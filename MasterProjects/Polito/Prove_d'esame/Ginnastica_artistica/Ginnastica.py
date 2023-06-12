import operator


def main():
    lista_ginnasti = leggi_file()
    calcolo_punteggio_totale(lista_ginnasti)

    stampa_vincitrice_femminile(lista_ginnasti)
    classifica = classifica_nazioni(lista_ginnasti)

    stampa_classifica(classifica)
def leggi_file():

    lista_ginnasti = []
    with open("punteggi.txt", "r", encoding="utf-8") as file:

        for line in file:
            ginnasta = dict()
            ginnasta_string = line.strip().split(" ")

            ginnasta["nome"] = ginnasta_string[0]
            ginnasta["cognome"] = ginnasta_string[1]
            ginnasta["sesso"] = ginnasta_string[2]
            ginnasta["nazione"] = ginnasta_string[3]
            ginnasta["punteggi"] = []
            for i in range(4,len(ginnasta_string)):
                if(ginnasta_string[i] != ""):
                    ginnasta["punteggi"].append(float(ginnasta_string[i].rstrip()))
            lista_ginnasti.append(ginnasta)
    return lista_ginnasti

def calcolo_punteggio_totale(lista_ginnasti):
    for ginnasta in lista_ginnasti:
        totale = 0
        lista_punteggi = ginnasta.get("punteggi")
        lista_punteggi.sort()
        del lista_punteggi[0]
        del lista_punteggi[-1]
        for punteggio in lista_punteggi:
            totale+= punteggio
        ginnasta["punteggio_totale"] = totale

def stampa_vincitrice_femminile(lista_ginnasti):

    lista_ginnasti.sort(key = operator.itemgetter("punteggio_totale"), reverse=True )
    for ginnasta in lista_ginnasti:
        if(ginnasta.get("sesso") == "F"):
            print("Vincitrice femminile:")
            print(ginnasta.get("nome"),ginnasta.get("cognome"),",", ginnasta.get("nazione"), "-", "Punteggio:",ginnasta.get("punteggio_totale"))
            print()
            break

def classifica_nazioni(lista_ginnasti):
    classifica = dict()
    for ginnasta in lista_ginnasti:
        if(ginnasta.get("nazione") not in classifica):
            classifica[ginnasta.get("nazione")] =0

        classifica[ginnasta.get("nazione")]+= ginnasta.get("punteggio_totale")

    return dict(sorted(classifica.items(), key = operator.itemgetter(1), reverse= True))

def stampa_classifica(classifica):
    posizione =1
    print("Classifica complessiva nazioni:")
    for key, value in classifica.items():
        if(posizione<=3):
            print(f"{posizione})°", key, f"- Punteggio totale: {value}")
            posizione+=1
        else:
            break
if __name__ == "__main__":
    main()