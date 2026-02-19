from data import SaveDataFileCategorie


class Categories:
    def __init__(self):
        self.categories = SaveDataFileCategorie()

    def add_categorie(self, name):
        data = self.categories.load_data()

        if data is None:
            data = []

        for categorie in data:
            if categorie["name"] == name:
                print("la categorie existe deja")
                return

        data.append({"name": name})
        name = name.capitalize().strip()
        self.categories.save_data(data)
        print("Categorie ajouter avec succées")

    def update_categorie(self):
        data = self.categories.load_data()

        if data is None:
            data = []

        if not data:
            print("Aucune categorie")
        else:
            for index, categorie in enumerate(data, 1):
                print(index, categorie)

            choiceModify = int(input("Quel numero de categorie voulez vous modifier? "))
            if choiceModify > len(data):
                print("Ce numéro ne correspond à une categorie")
                return
            else:
                new_name = input("Nouveau nom de la categorie: ")
                data[choiceModify - 1]["name"] = new_name
                self.categories.save_data(data)
                print("Categorie modifier avec succées")

    def delete_categorie(self):
        data = self.categories.load_data()

        if data is None:
            data = []

        if not data:
            print("Aucune categorie")
        else:
            for index, categorie in enumerate(data, 1):
                print(index, categorie)

            choiceDelete = int(
                input("Quel numero de categorie voulez vous supprimer? ")
            )
            if choiceDelete > len(data):
                print("Ce numéro ne correspond à une categorie")
                return
            else:
                del data[choiceDelete - 1]
                self.categories.save_data(data)
                print("Categorie supprimé avec succées")
    
    def list_categorie(self):
        data = self.categories.load_data()

        if data is None:
            data = []

        if not data:
            print("Aucune categorie")
        else:
            print("Liste des categories :")
            for index, categorie in enumerate(data, 1):
                print(index, categorie["name"])

