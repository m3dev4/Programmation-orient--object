class Produit:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix


class Commande:
    def __init__(self):
        self.article = []

    def add_product(self, produit):
        self.article.append(produit)
        print(f"Produits ajouté avec succéss")

    def calculate_total(self):
        total = 0
        for p in self.article:
            total += p.prix
        return total

    def paiement(self):
        print(f"{client} votre commande est confirmer pour un total de: {self.calculate_total()}")

client = "John"

produit = Produit("Iphone 17", 550000)
produit2 = Produit("Hp", 275000)
commande = Commande()
commande.add_product(produit)
commande.add_product(produit2)
commande.paiement()

