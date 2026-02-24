from classe.Document import Document


# ============================================================
#  CLASSE : Livre
#  Hérite de Document. Représente un livre dans la bibliothèque.
# ============================================================
class Livre(Document):
    """
    Représente un livre, sous-classe concrète de Document.

    Hérite de:
        Document: Classe abstraite parente.
    """

    def __init__(self, titre, auteur):
        """
        Initialise un livre en appelant le constructeur parent.

        Args:
            titre  (str): Titre du livre.
            auteur (str): Auteur du livre.
        """
        super().__init__(titre, auteur)

    def emprunt(self):
        """
        Marque le livre comme non disponible s'il est disponible.
        Ne fait rien si le livre est déjà emprunté.
        """
        if self.est_disponible == True:
            self.est_disponible = False  # Le livre est maintenant emprunté

    def retourner(self):
        """
        Marque le livre comme disponible s'il était emprunté,
        et affiche un message de confirmation.
        """
        if not self._est_disponible:
            print("Le livre est de nouveau disponible")
            self.est_disponible = True  # Le livre est de nouveau en rayon
