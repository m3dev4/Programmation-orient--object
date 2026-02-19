class Tache:
    def __init__(self, nom, description, categorie):
        self.nom = nom
        self.description = description
        self.categorie = categorie


class Depense(Tache):
    def __init__(self, nom, description, categorie, montant):
        super().__init__(nom, description, categorie)
        self.montant = montant
    def __str__(self):
        return f"{self.nom} | {self.description} | {self.categorie} | {self.montant}"
        

class Categorie:
    def __init__(self):
        self.categorie = []

    def add_categorie(self, nom):
        if nom in self.categorie:
            print("Cette categorie existe déja")
            return False
        else:
            self.categorie.append(nom)
            print("Categorie ajoutée avec succés")
            return True

    def modify_categorie(self, new_categorie, nom):
        if not self.categorie:
            print("La liste des categories est vide")
        else:
            for categorie in self.categorie:
                if categorie == new_categorie:
                    print("Cette categorie existe déja")
                elif nom == categorie:
                    categorie = new_categorie
                    print("Categorie mise à jour avec succés")
                else:
                    print("Catégorie non trouve")

    def remove_categorie(self, nom):
        if not self.categorie:
            print("La liste des categories est vide")
        else:
            for categorie in self.categorie:
                if nom == categorie:
                    self.categorie.remove(categorie)
                    print("Categorie supprimée avec succés")
                else:
                    print("Catégorie non trouve")

    def liste_categorie(self):
        if not self.categorie:
            print("La liste des categories est vide")
            return False
        else:
            for categorie in self.categorie:
                print(categorie)


class GestionDepense:
    def __init__(self):
        self.list_depenses = []
        self.list_categorie = Categorie()

    def add_depense(self, titre, description, montant, categorie):
        if not isinstance(titre, str):
            raise ValueError("Le titre doit être une chaine de caractères")
        if not titre.isalpha():
            raise ValueError("Le titre doit contenir seulement des lettres")
        if montant <= 0:
            raise ValueError("Le montant doit etre supérieur à zéro")
        if categorie not in self.list_categorie.categorie:
            print("Cette categorie n'existe pas")
            return False

        depense = Depense(titre, description, categorie, montant)
        self.list_categorie.add_categorie(categorie)
        self.list_depenses.append(depense)
        print("depense ajouté")
        return depense

    def list_depense(self):
        if not self.list_depenses:
            print("La liste des depenses est vide")
        for depense in self.list_depenses:
            print(depense)

    def modify_depense(
        self, titre=None, description=None, montant=None, categorie=None
    ):
        for value, depense in enumerate(self.list_depenses, 1):
            print(value, depense)

        choiceModify = int(input("Quel numero de depense voulez vous modifier? "))
        if choiceModify > len(self.list_depenses):
            print("Ce numéro ne correspond à une depense")
        else:
            titre = input("Nouveau titre: ")
            if titre != "":
                if titre.isalpha():
                    self.list_depenses[choiceModify - 1].nom = titre
                    print("Titre modifié avec succés")
                else:
                    print("Le titre doit contenir seulement des lettres")
            description = input("Nouvelle description: ")
            if description != "":
                self.list_depenses[choiceModify - 1].description = description
                print("Description modifiée avec succés")
            else:
                print("Description non modifié")
            montant = input("Veullez saisir le nouveau montant")
            if montant != "":
                montant = int(montant)
                if montant > 0:
                    self.list_depenses[choiceModify - 1].montant = montant
                else:
                    print("Le montant doit etre supperieur à zéro")

    def remove_depense(self, titre):
        for depense in self.list_depenses:
            if titre == depense.nom:
                self.list_depenses.remove(depense)
                print("Dépense supprimée avec succès")
            else:
                print("Dépense non trouvé")


class Menu:
    def __init__(self):
        self.gestion = GestionDepense()

    def Menu_Principal(self):
        while True:
            print("\n===== MENU PRINCIPAL =====")
            print("1. Ajouter dépenses")
            print("2. Modifier les depenses")
            print("3. Supprimer des depenses")
            print("4. Liste des depenses")
            print("5. Ajouter categories")
            print("6. Liste categories")
            print("7. Supprimer categories")
            print("8. Quitter")

            choice = input("Entre votre choix: ")
            match choice:
                case "1":
                    titre = input("titre: ")
                    description = input("description: ")
                    montant = int(input("montant: "))
                    categorie = input("categorie: ")
                    self.gestion.add_depense(titre, description, montant, categorie)
                case "2":
                    self.gestion.modify_depense()
                case "3":
                    self.gestion.remove_depense()
                case "4":
                    self.gestion.list_depense()
                case "5":
                    self.gestion.list_categorie.add_categorie(
                        input("Nom de la categorie: ")
                    )
                case "6":
                    self.gestion.list_categorie.liste_categorie()
                case "7":
                    self.gestion.list_categorie.remove_categorie()
                case "8":
                    print("Bye Bye")
                    break


menu = Menu()
menu.Menu_Principal()
