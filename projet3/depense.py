from task import Tasks


class Depense(Tasks):
    def __init__(self, title, description, categorie, montant):
        super().__init__(title, description, categorie)
        self.montant = montant

    def __str__(self):
        return f"{self.title} - {self.description} - {self.categorie} - {self.montant}"
