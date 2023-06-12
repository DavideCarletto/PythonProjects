
def main():

    lista_personaggi = leggi_personaggi()
    lista_domande = leggi_domande()

    mosse(lista_personaggi,lista_domande)

def leggi_personaggi():
    lista_personaggi = []
    with open("personaggi.txt", "r", encoding="utf-8") as file:
        prima_riga = file.readline().strip().split(";")
        print(prima_riga)
        for line in file:
            count =0
            personaggio = dict()
            personaggio_string = line.strip().split(";")
            for caratteristica in prima_riga:
                personaggio[caratteristica] = personaggio_string[count]
                count+=1
            lista_personaggi.append(personaggio)

    return lista_personaggi


def leggi_domande():

    lista_domande = dict()
    with open("domande2.txt", "r", encoding="utf-8") as file:
        for line in file:
            domanda_string = line.strip().split("=")
            lista_domande[domanda_string[0]] = domanda_string[1]

    return lista_domande

def mosse(lista_personaggi,lista_domande):
    print("Personaggi del gioco:")
    stampa_personaggi(lista_personaggi)
    count = 1
    lista_personaggi_rimasti = lista_personaggi.copy()

    for chiave, valore in lista_domande.items():

        for personaggio in lista_personaggi:
            if (personaggio.get(chiave)!= valore and personaggio in lista_personaggi_rimasti):
                lista_personaggi_rimasti.remove(personaggio)

        print(f"Mossa {count} - domanda: {chiave} = {valore}")
        stampa_personaggi(lista_personaggi_rimasti)
        count+=1
        print()




def stampa_personaggi(lista_personaggi):
    for personaggio in lista_personaggi:
        for chiave, valore in personaggio.items():
            if(valore == "SI"):
                print(f"{chiave} ", end=" ")
            else:
                if(valore != "NO"):
                    if (chiave == "Nome"):
                        print(f"{valore} - ", end=" ")
                    else:
                        print(f"{chiave}:{valore}", end=", ")
        print()
if __name__ == "__main__":
    main()