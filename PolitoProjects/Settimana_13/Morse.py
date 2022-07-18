def main():

    with open("morse.txt", "r", encoding="utf-8") as fin:
        dizionario_codifica, dizionario_decodifica = leggo_alfabeto(fin)

    with open("comandi.txt", "r", encoding="utf-8") as f_comandi:
        for line in f_comandi:
            l = line.split()
            comando = l[0]
            nome_file = l[1]
            try:
                with open(nome_file,"r", encoding="utf-8") as f_line:
                    if comando == "c":
                        print(f"Codifica del file {nome_file}")
                        codifica(f_line,dizionario_codifica)
                    elif comando == "d":
                        print(f"Decodifica del file {nome_file}")
                        decodifica(f_line,dizionario_decodifica)
                    else:
                        print(f"comando non riconosciuto: {comando}")
            except FileNotFoundError as ex:
                print(f"Errore nell'apertura del file:{nome_file}")

def leggo_alfabeto(file):
    da_lettera_a_morse = dict()
    da_morse_a_lettera = dict()
    for line in file:
        lista = line.split();
        lettera = lista[0].upper()
        codice = lista[1]
        da_lettera_a_morse[lettera] = codice
        da_morse_a_lettera[codice] = lettera
    return da_lettera_a_morse, da_morse_a_lettera

def codifica(file, dizionario_codifica):
    lista_codifica = [] #uso una lista per memorizzare i caratteri convertiti
    carattere  = file.read(1)
    while carattere != "":
        carattere = carattere.upper()
        print(f"DEBUG: ho letto {carattere} ({ord(carattere)})")#ord restituisce il codice ascii del carattere
        if carattere in dizionario_codifica:
            codice = dizionario_codifica[carattere]
            lista_codifica.append(codice)

        carattere = file.read(1)
        print(" ".join(lista_codifica)) #al posto che fare il ciclo for, nelle virgolette c'è il separatore

    print()

def decodifica(file,dizionario_decodifica):
    line = file.readline()
    l = line.split()
    for codice in l:
        lettera = dizionario_decodifica[codice]
        print(lettera,end = "")
    print("\n")

if __name__ == "__main__":
    main()