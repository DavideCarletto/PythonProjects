import csv
import operator
from operator import itemgetter

def main():

    sportivi = leggiCalciatori()
    zodiaco = leggiZodiaco()
    stampaSegni(sommaGoal(sportivi,zodiaco))

def leggiCalciatori():

    lista = []
    with open ("sportivi.csv", "r", encoding="utf-8") as file_calciatori:
        reader = csv.reader(file_calciatori)
        for line in reader:
            sportivi = dict()
            sportivi["nome_cognome"] = line[0]
            sportivi["goal"] = line[1]
            sportivi["nazionalità"] = line[2]
            dataNascita_list = line[3].split("/")
            dataNascita = dataNascita_list[1]+dataNascita_list[0]
            sportivi["dataNascita"] = dataNascita
            lista.append(sportivi)

    return lista

def leggiZodiaco():

    lista  =[]
    with open("zodiaco.csv", "r", encoding="utf-8") as file_zodiaco:
        reader = csv.reader(file_zodiaco)
        for line in reader:
            zodiaco = dict()
            zodiaco["segno"] = line[0]
            periodoInizialeList = line[1].split("/")
            periodoIniziale= periodoInizialeList[1]+periodoInizialeList[0]
            zodiaco["periodoIniziale"] = periodoIniziale
            periodo_finale_list = line[2].split("/")
            periodo_finale = periodo_finale_list[1] + periodo_finale_list[0]
            zodiaco["periodoFinale"] = periodo_finale
            lista.append(zodiaco)
        return lista

def sommaGoal(sportivi, zodiaco):
    segni = dict()
    for calciatore in sportivi:
      for periodo in zodiaco:

          if(calciatore["dataNascita"]>=periodo["periodoIniziale"] and calciatore["dataNascita"]<=periodo["periodoFinale"]):
              if((periodo.get("segno") in segni.keys())== False):
                 segni[periodo.get("segno")] = int(calciatore.get("goal"))
              else:
                  segni[periodo.get("segno")] = segni[periodo.get("segno")] + int(calciatore.get("goal"))
              break
    return segni

def stampaSegni(segni):
    sort_dict = dict(sorted(segni.items(), key=operator.itemgetter(1),reverse=True))
    for k,value in sort_dict.items():
        print(k,value,end = " ")
        for i in range(0,int(value/50)):
            print("*", end="")
        print()

if __name__ == "__main__":
    main()