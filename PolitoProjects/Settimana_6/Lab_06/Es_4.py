
def calcoloSaldoBancario(numero_anni,saldo_iniziale,tasso_interesse):
    saldoTotale=saldo_iniziale
    for i in range(numero_anni):
        saldoTotale += saldo_iniziale*tasso_interesse

    return saldoTotale

numero_anni = int(input("inserisci il numero di anni:"))
saldo_iniziale = float (input("inserisci il saldo iniziale:"))
tasso_interesse = float(input("inserisci il tasso di interesse:"))

saldoBancario = calcoloSaldoBancario(numero_anni,saldo_iniziale,tasso_interesse)
print(f"il tuo saldo bancario dopo {numero_anni} anni è di {saldoBancario}")