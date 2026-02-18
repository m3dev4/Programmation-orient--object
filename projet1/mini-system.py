class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def emprunter(self):
        if self.disponible:
            print("Le livre est emprunter")
            self.disponible = False

    def retourner(self):
        if not self.disponible:
            print("Le livre est de nouveau disponibe")
            self.disponible = True


class Membre():
    def __init__(self, nom):
        self.nom = nom
        self.livres_emprunte = []

    def emprunter(self, livre):
        if livre.disponible:
            self.livres_emprunte.append(livre)
            livre.disponible = False
    def retourner(self, livre):
        if not livre.disponible:
            self.livres_emprunte.remove(livre)
            livre.disponible = True


class Bibliotheque():
    def __init__(self, liste_livre):
        self.liste_livre = liste_livre

    def ajouter_livre(self, livre):
            self.liste_livre.append(livre)

    def afficher_livre_disponible(self):
            for livre in self.liste_livre:
                print(livre.titre, livre.auteur)

livre1 = Livre("Le soleil", "John", True)
livre2 = Livre("La nuit", "Jess", True)
membre1 = Membre("Moulaye")
bib = Bibliotheque([])
bib.ajouter_livre(livre1)
bib.ajouter_livre(livre2)
print(bib.afficher_livre_disponible())

membre1.emprunter(livre1)
print(livre1.disponible)



