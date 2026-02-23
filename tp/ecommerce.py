class Article:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

    def presenter(self):
        raise NotImplementedError("Sous-classe doit implémenter cette méthode")


class Coque(Article):
    def __init__(self, nom, prix, modele_telephonique):
        super().__init__(nom, prix)
        self.modele_telephonique = modele_telephonique

    def presenter(self):
        print(f"Ce produit est un {self.nom} du telephone {self.modele_telephonique}")


class Accessoire(Article):
    def __init__(self, nom, prix, categorie):
        super().__init__(nom, prix)
        self.categorie = categorie

    def presenter(self):
        print(f"Ce produit est un {self.nom} de categorie {self.categorie}")


class Panier:
    def __init__(self):
        self.articles = []
        
    def ajouter_article(self, article):
        self.articles.append(article)

    # Dunder
    def __add__(self, autre_panier):
        nouveau_panier = Panier()
        nouveau_panier.articles = self.articles + autre_panier.articles
        return nouveau_panier

    def __len__(self):
        return len(self.articles)

    def display(self):
        for article in self.articles:
            article.presenter()

# Création des articles
coque1 = Coque("Coque Transparente", 10, "iPhone 14")
coque2 = Coque("Coque Silicone", 15, "Samsung S23")

chargeur = Accessoire("Chargeur Rapide", 20, "Chargeur")
ecouteur = Accessoire("AirPods", 50, "Audio")

# Création des paniers
panier1 = Panier()
panier1.ajouter_article(coque1)
panier1.ajouter_article(chargeur)

panier2 = Panier()
panier2.ajouter_article(coque2)
panier2.ajouter_article(ecouteur)

# Fusion avec +
panier_final = panier1 + panier2

print("Articles du panier final :")
panier_final.display()

print("\nNombre total d’articles :", len(panier_final))