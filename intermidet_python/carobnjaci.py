class Carobnjak:
    def __init__(self, ime):
        if not ime:
            raise ValueError("Ime ne moze biti prazno")
        self.ime = ime 

class Ucenik(Carobnjak): # nasledjuje klasu Carobnjak (roditeljsku klasu)
    def __init__(self, ime, kuca):
        super().__init__(ime) # poziva konstruktor roditeljske klase Carobnjak
        self.kuca = kuca

class Profesor(Carobnjak): # nasledjuje klasu Carobnjak (roditeljsku klasu)
    def __init__(self, ime, predmet):
        super().__init__(ime)
        self.predmet = predmet

carobnjak = Carobnjak("Severus Piton")
ucenik = Ucenik("Hermiona", "Grifindor")
profesor = Profesor("Dambldor", "Necromantija")
