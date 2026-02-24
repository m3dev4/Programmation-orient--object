from classe.Document import Document


# ============================================================
#  CLASSE : Magazine
#  Hérite de Document. Représente un magazine dans la bibliothèque.
#  Même comportement que Livre (peut être différencié plus tard).
# ============================================================
class Magazine(Document):
    """
    Représente un magazine, sous-classe concrète de Document.

    Hérite de:
        Document: Classe abstraite parente.
    """

    def __init__(self, titre, auteur):
        """
        Initialise un magazine en appelant le constructeur parent.

        Args:
            titre  (str): Titre du magazine.
            auteur (str): Auteur / éditeur du magazine.
        """
        super().__init__(titre, auteur)

    def emprunt(self):
        """
        Marque le magazine comme non disponible s'il est disponible.
        """
        if self.est_disponible == True:
            self.est_disponible = False  # Le magazine est maintenant emprunté

    def retourner(self):
        """
        Marque le magazine comme disponible s'il était emprunté,
        et affiche un message de confirmation.
        """
        if not self._est_disponible:
            print("Le livre est de nouveau disponible")
            self.est_disponible = True  # Le magazine est de nouveau en rayon
