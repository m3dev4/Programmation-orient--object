class Tache:
    def __init__(self, nom, description, categorie):
        self.nom = nom
        self.description = description
        self.categorie = categorie

    def __str__(self):
        return f"{self.nom} | {self.description} | {self.categorie}"


class Depense(Tache):
    def __init__(self, nom, description, categorie, montant):
        super().__init__(nom, description, categorie)
        self.montant = montant
        return True


class Categorie:
    def __init__(self):
        self.categorie = []

    def add_categorie(self, nom):
        if nom in self.categorie:
            print("Cette categorie existe déja")
            return False
        else:
            self.categorie.append(nom)
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
        self.list_depense = []
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
        self.list_depense.append(depense)
        print("depense ajouté")   
        return depense
    
    def list_depense(self):
        if not self.list_depense:
            print("La liste des depenses est vide")
        for depense in self.list_depense:
            print(depense)
            
    def modify_depense(self, titre=None, description=None, montant=None, categorie=None ):
        for value, depense in enumerate(self.list_depense, 1):
            print(value, depense)
 
categorieAliment = Categorie()
categorieAliment.add_categorie("Alimentation")      
print(categorieAliment.liste_categorie()) 
depense = GestionDepense()
depense.add_depense("aliments", "Achat de legumes", 5000, "Alimentation")
