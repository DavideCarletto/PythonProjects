def caricaManutenzioni(nomeFile): #funzione per prendere i dati dal file, il cui nome è stato acquistato in input
    try:
        listaManutenzioni = []
        infile = open(nomeFile, "r", encoding="utf-8")
        for line in infile:
            riga = line.rstrip().split(" ")
            nomeLavoro = riga[0]
            data = riga[1]
            costo = riga[2]
            listaManutenzioni.append((nomeLavoro,data,costo))
        infile.close()
        return listaManutenzioni
    except IOError:
        print("Error: FileNotFoundError")

def modalitaA(data, elenco): #funzione che analizza i lavori che sono stati effettuati prima della data fornita in input
    print("Le operazioni effettuate prima del %s sono:"%(data))
    elencoManutenzioniA = []
    elencoCosti = []
    giorno = data[0]+data[1]
    mese = data[3]+data[4]
    anno = data[6]+data[7]+data[8]+data[9]

    for i in range(0, len(elenco), 1):
        gestioneData = elenco[i][1].split("/")
        giornoElenco = gestioneData[0]
        if len(gestioneData[1])==1:
            meseElenco = "0"+gestioneData[1]
        else:
            meseElenco = gestioneData[1]
        annoElenco = gestioneData[2]
        if (giornoElenco <= giorno and meseElenco <= mese and annoElenco == anno) or annoElenco < anno:
            elencoManutenzioniA.append(elenco[i])
            elencoCosti.append((elenco[i][2],elenco[i][0],elenco[i][1]))

    elencoCosti.sort(reverse=False)
    for i in range(0, len(elencoManutenzioniA), 1):
       print(elencoManutenzioniA[i][0], elencoManutenzioniA[i][1], elencoManutenzioniA[i][2])
    print("")
    print("La manutenione più costosa è stata ", elencoCosti[0][1], "del",elencoCosti[0][2],"costata ", elencoCosti[0][0])
    print("La manutenione più economica è stata ", elencoCosti[len(elencoCosti)-1][1], "del",elencoCosti[0][2],"costata ", elencoCosti[len(elencoCosti)-1][0]) #indice modificato dopo

def modalitaP(data, elenco): #funzione che analizza i lavori che sono stati effettuati dopo la data fornita in input
    print("Le operazioni effettuate dopo il %s sono:" % (data))
    elencoManutenzioniP = []
    elencoCosti = []
    giorno = data[0] + data[1]
    mese = data[3] + data[4]
    anno = data[6] + data[7] + data[8] + data[9]

    for i in range(0, len(elenco), 1):
        gestioneData = elenco[i][1].split("/")
        giornoElenco = gestioneData[0]
        if len(gestioneData[1])==1:
            meseElenco = "0"+gestioneData[1]
        else:
            meseElenco = gestioneData[1]
        annoElenco = gestioneData[2]
        if (giornoElenco > giorno and meseElenco >= mese and annoElenco == anno) or annoElenco > anno:
            elencoManutenzioniP.append(elenco[i])
            elencoCosti.append((elenco[i][2],elenco[i][0],elenco[i][1]))

    elencoCosti.sort(reverse=False)
    for i in range(0, len(elencoManutenzioniP), 1):
       print(elencoManutenzioniP[i][0], elencoManutenzioniP[i][1], elencoManutenzioniP[i][2])
    print("")
    print("La manutenione più costosa è stata ", elencoCosti[0][1], "del",elencoCosti[0][2],"costata ", elencoCosti[0][0])
    print("La manutenione più economica è stata ", elencoCosti[len(elencoCosti)-1][1], "del",elencoCosti[len(elencoCosti)-1][2],"costata ", elencoCosti[len(elencoCosti)-1][0])

def main():
    elencoManutenzioni = []
    nomeFileManutenzioni = input("Inserire il nome del file con le manutenzioni: ")
    elencoManutenzioni = caricaManutenzioni(nomeFileManutenzioni)

    dataControllo = input("Inserire una data su cui effettuare il controllo (formato gg/mm/aaaa): ")
    modalita = input("Inserire la modalità di controllo (a: operazioni effettuate precedentemente\p: operazioni ancora da effettuare): ")
    modalita = modalita.lower()

    if modalita=='a':
        print("Modalità a")
        modalitaA(dataControllo, elencoManutenzioni)
    elif modalita=='p':
        print("Modalità p")
        modalitaP(dataControllo, elencoManutenzioni)

main()
