class Persona:
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


    def saluta(self):
        print(f"Buongiorno sono {self.nome} {self.cognome}", end=" ")


class Studente(Persona):
    def __init__(self, nome,cognome,matricola):
        super().__init__(nome,cognome)
        self.matricola = matricola

    def saluta(self):
        super(Studente, self).saluta()
        print("e la mia matriola da studente è "+str(self.matricola))

def main():

    persona = Persona(nome="Davide", cognome="Carletto")
    studente = Studente("Luca", "Di Ruggiero", 34567)
    persona.saluta()
    print()
    studente.saluta()




if __name__ == "__main__":
    main()

