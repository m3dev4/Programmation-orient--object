from data import SaveDataFileDepense
from data import SaveDataFileCategorie
from depense import Depense
from categories import Categories


class DepenseMangement:
    def __init__(self):
        self.depenses = SaveDataFileDepense()
        self.categories = SaveDataFileDepense()
        self.categorie = Categories()

    def add_depense(self, titre, description, montant, categorie):
        data = self.depenses.load_data()
        dataCategories = self.categorie.categories.load_data()

        if data is None:
            data = []

        if dataCategories is None:
            dataCategories = []
            raise ValueError(
                "Les categories doivent etre creer avant d'ajouter une depense"
            )

        if not titre.isalpha():
            raise ValueError("Le titre doit etre en lettre")
        if not description.isalpha:
            raise ValueError("La description doit etre en lettre")
        if not montant.isdigit() and montant <= 0:
            raise ValueError("Le montant doit etre un nombre positif")
        for cate in dataCategories:
            if cate["name"] != categorie:
                raise ValueError("la categorie n'existe pas")

        depense = Depense(titre, description, categorie, montant)
        self.categorie.add_categorie(categorie)
        data.append(depense.__dict__)
        self.depenses.save_data(data)
        print("Depense ajouté avec succées")

    def list_depense(self):
        data = self.depenses.load_data()
        for index, depense in enumerate(data, start=1):
            if not depense:
                print("Aucune depense effectué")
            else:
                print(
                    f"{index} - {depense['title']} - {depense['description']} - {depense['montant']} - {depense['categorie']}"
                )

    def update_depense(
        self, title=None, description=None, montant=None
    ):
        data = self.depenses.load_data()
        

        if data is None:
            data = []

        for index, depense in enumerate(data, 1):
            if not depense:
                print("Aucune depense efféctué")
            print(
                f"{index} - {depense['title']} - {depense['description']} - {depense['montant']} - {depense['categorie']}"
            )

        inp = int(input("Quelle depense voulez vous modifier? "))
        if inp > len(data):
            print("Cette depense n'existe pas")
            return False
        else:
            title = input("Nouveau titre: ")
            if title != "":
                if title.isalpha():
                    data[inp - 1]["title"] = title
                    print("Titre modifié avec succés")
                    self.depenses.save_data(data)
                else:
                    print("Le titre doit contenir uniquement des chaines")
                    
            description = input("Nouveau description: ")
            if description != "":
                if description.isalpha():
                    data[inp - 1]["description"] = description
                    print("Description modifiée avec succés")
                    self.depenses.save_data(data)
                else:
                    print("La description doit contenir uniquement des chaines")
                    
            
            montant = (input("Nouveau montant: "))
            if montant != "":
                if montant.isdigit() and montant <= 0:
                    data[inp - 1]["montant"] = montant
                    print("Montant modifié avec succés")
                    self.depenses.save_data(data)
                else:
                    print("Le montant doit être un chiffre superieur à zéro")
