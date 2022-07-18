import operator
def main():
        lista_giocatori = leggi_file()
        calcolo_punteggio_finale(lista_giocatori)
        genera_classifica(lista_giocatori)
def leggi_file():

   lista_giocatori = []
   with open("bowling/bowling.txt", "r" , encoding="utf-8") as file:
       for line in file:
         giocatore = dict()
         lista_giocatore = line.split(";")
         giocatore["cognome"] = lista_giocatore[0]
         giocatore["nome"]  = lista_giocatore[1]
         giocatore["lista tiri"] = []
         strike = 0
         miss = 0
         for i in range (2, len(lista_giocatore)):
             giocatore["lista tiri"].append(int(lista_giocatore[i]))
             if(int(lista_giocatore[i])== 10):
                 strike+=1
             elif (int(lista_giocatore[i])==0):
                 miss+=1

         giocatore["strike"] = strike
         giocatore["miss"] = miss
         lista_giocatori.append(giocatore)

   return lista_giocatori

def calcolo_punteggio_finale(lista_giocatori):
    for giocatore in lista_giocatori:
        punteggio_totale = 0
        lista_punteggi = giocatore.get("lista tiri")
        for i in range (0,len(lista_punteggi)):
            punteggio_totale += lista_punteggi[i]

        giocatore["lista tiri"] = punteggio_totale
def genera_classifica(lista_giocatori):
       lista_strike = []
       lista_miss = []
       lista_giocatori.sort(key = operator.itemgetter("lista tiri") , reverse= True)
       for i in range(0, len(lista_giocatori)):

           for chiave,valore in lista_giocatori[i].items():
               if(chiave != "strike" and chiave != "miss"):
                print(f"{valore :10} ", end= "        ")
               else:
                   nominativo = lista_giocatori[i].get("nome") +" "+ lista_giocatori[i].get("cognome")
                   if(chiave == "strike" and valore != 0):
                       lista_strike.append((nominativo,valore))
                   elif (chiave == "miss" and valore != 0):
                       lista_miss.append((nominativo, valore))
           print()


       print()
       for giocatore in lista_strike:
           print(f"{giocatore[0]} ha fatto {giocatore[1]} strike")
       for giocatore in lista_miss:
           print(f"{giocatore[0]} ha missato {giocatore[1]} volte")

if __name__ == "__main__":
    main()
