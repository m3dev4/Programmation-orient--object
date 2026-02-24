# ============================================================
#  CLASSE : Adherent
#  Représente un membre inscrit à la bibliothèque.
#  Gère sa liste d'emprunts personnels.
# ============================================================
class Adherent:
    """
    Représente un adhérent (membre) de la bibliothèque.

    Attributs:
        nom (str)                   : Nom de l'adhérent.
        liste_emprunts (list)       : Liste des documents actuellement empruntés.
    """

    def __init__(self, nom):
        """
        Initialise un adhérent avec son nom et une liste d'emprunts vide.

        Args:
            nom (str): Nom de l'adhérent.
        """
        self.nom = nom
        self.liste_emprunts = []  # Aucun emprunt au départ

    def __str__(self):
        """Retourne une représentation lisible de l'adhérent."""
        return f"--> {self.nom}"

    def emprunter(self, livre):
        """
        Ajoute un document à la liste des emprunts de l'adhérent.

        Args:
            livre (Document): Le document à emprunter.
        """
        # On ajoute simplement le document à la liste personnelle
        self.liste_emprunts.append(livre)

    def liste_emprunt(self):
        """
        Affiche la liste de tous les documents empruntés par l'adhérent.
        Affiche un message si aucun emprunt n'est en cours.
        """
        if self.liste_emprunts == []:
            print("Aucun Emprunt")
            return  # On arrête l'exécution si la liste est vide

        # Parcours et affichage de chaque document emprunté
        for emprunt in self.liste_emprunts:
            print(f"Titre : {emprunt.titre} | Auteur : {emprunt.auteur}")

    def retourner(self, document):
        """
        Retourne un document emprunté et le retire de la liste personnelle.

        Args:
            document (Document): Le document à retourner.
        """
        if document in self.liste_emprunts:
            document.retourner()  # Met le document comme disponible
            self.liste_emprunts.remove(document)  # Retire de la liste de l'adhérent
        else:
            # Le document n'appartient pas aux emprunts de cet adhérent
            print("Ce document nest pas dans la liste des emprunts de", self.nom)
