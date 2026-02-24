from abc import ABC, abstractmethod


# ============================================================
#  CLASSE ABSTRAITE : Document
#  Sert de modèle de base pour tous les types de documents
#  (Livre, Magazine, etc.). Elle ne peut pas être instanciée
#  directement grâce au module ABC.
# ============================================================
class Document(ABC):
    """
    Classe abstraite représentant un document de bibliothèque.

    Attributs:
        titre (str)         : Le titre du document.
        auteur (str)        : L'auteur du document.
        _est_disponible (bool): Indique si le document est disponible
                                (protégé, accessible via property).
    """

    def __init__(self, titre, auteur):
        """
        Initialise un document avec un titre, un auteur,
        et le marque comme disponible par défaut.

        Args:
            titre  (str): Titre du document.
            auteur (str): Auteur du document.
        """
        self.titre = titre
        self.auteur = auteur
        self._est_disponible = True  # Attribut protégé : disponible par défaut

    def __str__(self):
        """
        Retourne une représentation lisible du document
        avec son titre, son auteur et sa disponibilité.
        """
        # Détermine le statut à afficher selon la valeur du booléen
        disponible = "Disponible" if self.est_disponible else "Non Disponible"
        return f"--> {self.titre} | {self.auteur} : {disponible}"

    # ----------------------------------------------------------
    #  PROPERTY : est_disponible
    #  Encapsule l'attribut protégé _est_disponible pour
    #  contrôler les lectures et les écritures.
    # ----------------------------------------------------------
    @property
    def est_disponible(self):
        """Getter : retourne l'état de disponibilité du document."""
        return self._est_disponible

    @est_disponible.setter
    def est_disponible(self, valeur):
        """
        Setter : modifie la disponibilité du document.

        Args:
            valeur (bool): Nouvelle valeur de disponibilité.

        Raises:
            TypeError: Si la valeur fournie n'est pas un booléen.
        """
        if not isinstance(valeur, bool):
            # On s'assure que seule une valeur booléenne est acceptée
            raise TypeError("La valeur doit imperativement etre un booleen !!!")
        else:
            self._est_disponible = valeur

    # ----------------------------------------------------------
    #  MÉTHODES ABSTRAITES
    #  Chaque sous-classe DOIT implémenter ces deux méthodes.
    # ----------------------------------------------------------
    @abstractmethod
    def emprunt():
        """Méthode abstraite : logique d'emprunt du document."""
        pass

    @abstractmethod
    def retourner():
        """Méthode abstraite : logique de retour du document."""
        pass
