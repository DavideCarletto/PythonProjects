import operator


def main():
    lista_calciatori = []
    lista_calciatori = leggi_file_calciatori()
    calciatori_dict = ordina_lista_calciatori(lista_calciatori)
    crea_formazione(calciatori_dict)
def leggi_file_calciatori():
    lista_calciatori = []
    with open("fantacalcio.txt", "r", encoding="utf-8") as file_calciatori:
        for line in file_calciatori:
            calciatore = dict()
            calciatore_string = line.strip().split(",")
            calciatore["nome"] = calciatore_string[0]
            calciatore["squadra"] = calciatore_string[1]
            calciatore["ruolo"] = calciatore_string[2]
            calciatore["fantamilioni"] = int(calciatore_string[3])
            lista_calciatori.append(calciatore)

    return lista_calciatori

def ordina_lista_calciatori(lista_calciatori):
    calciatori_dict= dict()
    lista_calciatori.sort(key=operator.itemgetter("fantamilioni"), reverse=True)
    for calciatore in lista_calciatori:
        ruolo = calciatore.get("ruolo").lstrip()
        if(ruolo not in calciatori_dict):
            calciatori_dict[ruolo] = []

        calciatori_dict.get(ruolo).append((calciatore.get("nome"),calciatore.get("fantamilioni")))

    print(calciatori_dict)
    return calciatori_dict

def crea_formazione(calciatori_dict):

    budget = 0
    num_giocatori_da_acquistare = 0
    for ruolo, calciatori in calciatori_dict.items():
        if(ruolo == "attaccante"):
            budget = 120
            num_giocatori_da_acquistare = 6
        elif(ruolo == "portiere"):
            budget = 20
            num_giocatori_da_acquistare = 3
        elif (ruolo == "difensore"):
            budget = 40
            num_giocatori_da_acquistare = 8
        else:
            budget = 80
            num_giocatori_da_acquistare = 8

        for calciatore in calciatori:
            if(calciatore[1]<= budget and calciatore[1]<= budget-(num_giocatori_da_acquistare-1)):
                budget = budget - calciatore[1]
                num_giocatori_da_acquistare = num_giocatori_da_acquistare-1
                print(calciatore[0], calciatore[1], ruolo)



if __name__ == "__main__":
    main()