
def main():
    prodotti_dict = leggi_file_prodotti()
    lista_acquisti = leggi_file_acquisti()


    print(prodotti_dict)
    print(lista_acquisti)

    lista_sospetti = controlla_acquisti(prodotti_dict,lista_acquisti)
    stampa_lista_sospetti(lista_sospetti)


def leggi_file_prodotti():
    lista_prodotti = []
    with open("prodotti.txt", "r", encoding="utf-8") as file:
        for line in file:
            prodotti = dict()
            prodotto_string = line.strip().split(" ")
            prodotti ["codice"] = prodotto_string[0]
            prodotti["rivenditore_ufficiale"] = prodotto_string[1]
            lista_prodotti.append(prodotti)

    return lista_prodotti

def leggi_file_acquisti():

    lista_acquisti = []
    with open("acquisti.txt", "r", encoding="utf-8") as file:
        for line in file:
            acquisti = dict()
            acquisto_string = line.strip().split(" ")
            acquisti ["codice"] =  acquisto_string[0]
            acquisti["rivenditore"] = acquisto_string[1]
            lista_acquisti.append(acquisti)

    return lista_acquisti

def controlla_acquisti(lista_prodotti, lista_acquisti):
    lista_sospetti = []

    for prodotto in lista_prodotti:
        lista_rivenditori = []
        for acquisto in lista_acquisti:
            if(acquisto.get("codice")== prodotto.get("codice")):
                lista_rivenditori.append(acquisto.get("rivenditore"))
                if(acquisto.get("rivenditore")!= prodotto.get("rivenditore_ufficiale")):
                    transizione_sospetta = dict()
                    transizione_sospetta["codice_prodotto"] = prodotto.get("codice")
                    transizione_sospetta["rivenditore_ufficiale"] = prodotto.get("rivenditore_ufficiale")
                    transizione_sospetta["lista_rivenditori"] = lista_rivenditori
                    lista_sospetti.append(transizione_sospetta)

    return lista_sospetti

def  stampa_lista_sospetti(lista_sospetti):
    print("Elenco transizioni sospette:")

    for transizione in lista_sospetti:
        print("Codice prodotto: ", transizione.get("codice_prodotto"))
        print("Rivenditore ufficiale: ", transizione.get("rivenditore_ufficiale"))
        print("Lista rivenditori: ", end="")
        for rivenditore in transizione.get("lista_rivenditori"):
            print(rivenditore,end=" ")
        print("\n\n")

if __name__ == "__main__":
    main()