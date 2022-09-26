
def calcoloSussidio(reddito, numerofigli):
    sussidio =0
    if(reddito>= 30000 and reddito <= 40000 and numerofigli>=3):
        sussidio = 1000*numerofigli
    elif(reddito >=20000 and reddito <=30000 and numerofigli >=2):
        sussidio = 1500*numerofigli
    elif(reddito <=20000):
        sussidio = 2000*numerofigli
    else:
        sussidio = 0

    return sussidio
termina = False

while (not termina):
    reddito_annuo = float(input("Inserisci il reddito annuo: "))
    numero_figli = int(input("Inserisci il numero dei figli:"))
    sussidio = calcoloSussidio(reddito_annuo,numero_figli)

    print(f"il sussidio è di {sussidio} euro")
    print("inserire -1 per terminare")
    if(input()==-1):
        termina = True