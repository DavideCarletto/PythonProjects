import operator


def main():
    lista_monitoraggi =  leggi_file()
    lista_superamento = crea_lista_superamento(lista_monitoraggi)

    stampa(ordina_lista(lista_superamento))

def leggi_file():

    lista_monitoraggi = []
    with open("glucometers.txt", "r", encoding="utf-8") as file:

         for line in file:
            misurazione_string = line.strip().split(" ")
            monitoraggio = dict()

            monitoraggio["codice"] = misurazione_string[0]
            monitoraggio["orario"] = misurazione_string[1]
            monitoraggio["glicemia"] = int(misurazione_string[2])
            monitoraggio["temperatura"] = float(misurazione_string[3])
            monitoraggio["frequenza_cardiaca"] = int(misurazione_string[4])

            lista_monitoraggi.append(monitoraggio)

    return lista_monitoraggi

def crea_lista_superamento(lista_monitoriaggi):
    lista_superamento = dict()


    for monitoraggio in lista_monitoriaggi:
        if(monitoraggio.get("codice") not in lista_superamento):
            lista_superamento[monitoraggio.get("codice")] = []

        if(monitoraggio.get("glicemia")>=200):
            lista_superamento[monitoraggio.get("codice")].append(monitoraggio.get("glicemia"))

    return lista_superamento
def ordina_lista(lista_superamento):
    print(lista_superamento)
    return sorted(lista_superamento.items(), key=lambda x: len(x[1]), reverse=True)

def stampa(lista_ordinata):
    for key, value in lista_ordinata:
        for valor in value:
            print(f"{key}  {valor}")
        print()
if __name__ == "__main__":
    main()