

def countParole(string):
    counterParole = 1
    for lettera in string:

        if lettera == " ":
             counterParole += 1

    return counterParole

numeroParole = countParole(input("inserisci una stringa:"))
print(f"ci sono {numeroParole} parole nella stringa")