import operator


def main():
    lista_artisti = leggi_artista()
    stampa_artisti(crea_tabella_artisti(lista_artisti))

def leggi_artista():

    with open("artisti.txt", "r", encoding="utf-8") as file_artisti:
        lista_artisti = []
        for line in file_artisti:
            artista = dict()
            stringhe_file = line.strip().split(";")
            artista["codice"] = stringhe_file[0]
            with open(stringhe_file[1],"r", encoding="utf-8") as file_brani:
                for line in file_brani:
                    stringhe_artista = []
                    tupla  = (line.strip().split(";")[1],line.strip().split(";")[0])
                    stringhe_artista.append(tupla)
                    artista[tupla[0]] = tupla[1]
            lista_artisti.append(artista)
    return lista_artisti

def crea_tabella_artisti(lista_artisti):
    artisti = dict()
    for artista in lista_artisti:
        for(chiave, valore) in artista.items():
            if(chiave!= "codice"):
                if (valore not in artisti):
                    artisti[valore] = []

                artisti[valore].append((chiave,artista.get("codice")))

    artisti_ordinati = dict(sorted(artisti.items(),key= operator.itemgetter(0)))
    return artisti_ordinati

def stampa_artisti(dict_artisti):
    for (anno, canzoni) in dict_artisti.items():
        print(f"{anno}:")
        for canzone in canzoni:
            print(f"{canzone[0]:50} {canzone[1]:10}")

if __name__ == "__main__":
    main()