def main():
    with open("artisti.txt", "r", encoding="utf-8") as f_artisti:
        for line in f_artisti:
            l = line.split(";")

            codice = l[0]
            nome_file = l[1].strip()

            try:
                with open(nome_file,"r", encoding="utf-8") as f_secondario:
                    leggo_file(f_secondario)
            except Exception as ex:
                print("non funziona coglione")

def leggo_file(file):
    pass
if __name__ == "__main__":
    main()

