def main():
    percorso_file_leggere = input("file da leggere:")
    percorso_file_scrivere = input("file da scrivere:")
    elenco_sequenze =  leggi_dna(percorso_file_leggere)
    elenco_codice_genetico = leggi_codice_genetico()
    traduci(elenco_sequenze, elenco_codice_genetico, percorso_file_scrivere)

def leggi_dna(percorso):
    try:
        elenco_sequenze = []
        with open(percorso, "r", encoding="utf-8") as file:
            for line in file:
                    id = line.strip()
                    elenco_basi = file.readline().rstrip().split(" ")
                    dna = dict()
                    dna["id"] = id
                    dna["elenco_basi"] = elenco_basi
                    elenco_sequenze.append(dna)
    except Exception:
        print("file non valido")

    print(elenco_sequenze)
    return elenco_sequenze

def leggi_codice_genetico():
    elenco_proteine = []
    with open ("codicegenetico.txt", "r", encoding="utf-8") as file:
        for line in file:
            proteina = dict()
            sequenza = line.strip().split(":")

            proteina[sequenza[0]] = sequenza[1]
            elenco_proteine.append(proteina)
    return elenco_proteine

def traduci (elenco_sequenze, elenco_codice_genetico, percorso):

        elenco_finale = dict()
        for sequenza in elenco_sequenze:
            serie_amminoacidi = []
            id = sequenza.get("id")
            sequenza_basi = sequenza.get("elenco_basi")
            for tripletta in sequenza_basi:
                for elenco in elenco_codice_genetico:
                    for chiave, valore in elenco.items():
                        if tripletta in valore and chiave != "STOP":
                            serie_amminoacidi.append(chiave)
            elenco_finale[id] = serie_amminoacidi
            scrivi_su_file(elenco_finale, percorso)

def scrivi_su_file(elenco_finale, percorso):
    with open(percorso,"w", encoding="utf-8") as file:
       for id, elenco in elenco_finale.items():
           file.write(f"{id}\n")
           for proteina in elenco:
               file.write(proteina)
           file.write("\n")

if __name__ == "__main__":
    main()