def main():
    with open("dna.txt", "r", encoding="utf-8") as dna, open("codicegenetico.txt", "r", encoding="utf-8") as codiceGenetico:
        listaDna=[]
        for i in dna:
            val=i.strip(">").split()
            listaDna.append(val)
        codiceGen=[]
        for i in codiceGenetico:
            val=i.strip().split(":")
            if val[0]!="STOP":
                dizCodice={"lettera":val[0], "tripletta": val[1:]}
                codiceGen.append(dizCodice)

    listaDnaCompleta=[]
    for i in range(0,len(listaDna),2):
        dizDna={"codice":listaDna[i], "dna":listaDna[i+1]}
        #print(dizDna)
        listaDnaCompleta.append(dizDna)


    listaFinCodifica2=[]
    for i in listaDnaCompleta:
        result=""
        for j in i["dna"]:
            #print(j)
            for k in codiceGen:
                for f in k["tripletta"]:
                    #print(f)
                    if j in f:
                        result+=k["lettera"]
                    break
                else:
                    continue
        dizCompleto={"codiceId":i["codice"],"result":result}
        listaFinCodifica2.append(dizCompleto)


    with open("proteins.txt", "w", encoding="utf-8") as file:
        for i in listaFinCodifica2:
            print(i)
            file.write(">")
            file.write(f"{i['codiceId']}\n")
            file.write(f"{i['result']}\n")



main()