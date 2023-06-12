

def countVowels(string):
    stringaVocali= ""
    for lettera in string:
        lettera.lower()
        if lettera in "AaEeIiOoUu":
            stringaVocali += lettera

    return stringaVocali


print(countVowels(input("inserisci una stringa:")))