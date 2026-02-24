from abc import ABC, abstractmethod


#============================================
# @Author Mouhamed Lo & Ndeye Fassa Samb
#============================================

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
            document.retourner()                    # Met le document comme disponible
            self.liste_emprunts.remove(document)    # Retire de la liste de l'adhérent
        else:
            # Le document n'appartient pas aux emprunts de cet adhérent
            print("Ce document nest pas dans la liste des emprunts de", self.nom)


# ============================================================
#  CLASSE : Bibliothecaire
#  Gère l'ensemble de la bibliothèque :
#  - la liste des documents disponibles
#  - la liste des adhérents inscrits
#  - les opérations de prêt et de retour
# ============================================================
class Bibliothecaire:
    """
    Gère les documents et les adhérents de la bibliothèque.

    Attributs:
        liste_document (list)  : Tous les documents enregistrés.
        liste_adherant (list)  : Tous les adhérents inscrits.
    """

    def __init__(self):
        """Initialise la bibliothèque avec des listes vides."""
        self.liste_document = []   # Aucun document au départ
        self.liste_adherant = []   # Aucun adhérent au départ

    def ajout_document(self, document):
        """
        Ajoute un document à la bibliothèque si son titre est unique.

        Args:
            document (Document): Le document à ajouter.
        """
        present = False  # Indicateur : le document existe-t-il déjà ?

        # Vérification de l'unicité du titre dans la liste
        for livre in self.liste_document:
            if document.titre == livre.titre:
                present = True  # Un document avec ce titre existe déjà

        if not present:
            # Le titre est unique, on peut ajouter le document
            self.liste_document.append(document)
            print("Document enregistre")
        else:
            print("Document existe deja")

    def afficher_document(self):
        """Affiche tous les documents enregistrés dans la bibliothèque."""
        for livre in self.liste_document:
            print(livre)  # Appelle __str__ de chaque document

    def afficher_adherent(self):
        """Affiche tous les adhérents inscrits dans la bibliothèque."""
        for adherant in self.liste_adherant:
            print(adherant)  # Appelle __str__ de chaque adhérent

    def afficher_emprunt(self, nom):
        """
        Affiche la liste des emprunts d'un adhérent donné.

        Args:
            nom (str): Nom de l'adhérent recherché.
        """
        for adherant in self.liste_adherant:
            if adherant.nom == nom:
                adherant.liste_emprunt()  # Délègue l'affichage à l'adhérent
            else:
                print("Aderant Introuvable")

    def inscrire_membre(self, nom):
        """
        Crée un nouvel adhérent et l'inscrit dans la bibliothèque.

        Args:
            nom (str): Nom du nouveau membre.
        """
        try:
            membre = Adherent(nom)               # Création de l'objet Adherent
            self.liste_adherant.append(membre)   # Ajout à la liste
            print("Aderant Ajoute")
        except Exception as e:
            print(e)  # Affiche l'erreur si la création échoue

    def retour(self, titre, nom_membre):
        """
        Enregistre le retour d'un document par un adhérent.

        Args:
            titre      (str): Titre du document à retourner.
            nom_membre (str): Nom de l'adhérent qui retourne le document.
        """
        # --- Étape 1 : Recherche de l'adhérent par son nom ---
        d_doc = False
        for adherent in self.liste_adherant:
            if nom_membre == adherent.nom:
                ad_trouve = adherent   # Adhérent trouvé
                d_doc = True

        # --- Étape 2 : Recherche du document dans les emprunts de l'adhérent ---
        doc = False
        for document in ad_trouve.liste_emprunts:
            if titre == document.titre:
                doc_trouve = document  # Document trouvé
                doc = True

        # --- Étape 3 : Enregistrement du retour si les deux sont trouvés ---
        if d_doc == True and doc == True:
            ad_trouve.liste_emprunts.remove(doc_trouve)  # Retire de la liste d'emprunts
            doc_trouve.est_disponible = True              # Remet le document disponible
            print(f"Retour enregistre. Titre : {doc_trouve} | Adherant : {ad_trouve}")

    def valider_pret(self, nom_membre, titre_document):
        """
        Valide le prêt d'un document à un adhérent si les deux existent
        et si le document est disponible.

        Args:
            nom_membre      (str): Nom de l'adhérent emprunteur.
            titre_document  (str): Titre du document à emprunter.

        Raises:
            Exception: Si le livre ou le membre est introuvable.
        """
        # --- Étape 1 : Recherche du document dans la bibliothèque ---
        p_doc = False
        for document in self.liste_document:
            if document.titre == titre_document:
                p_doc = True
                document_choisi = document  # Document trouvé

        # --- Étape 2 : Recherche du membre dans la bibliothèque ---
        p_membre = False
        for membre in self.liste_adherant:
            if membre.nom == nom_membre:
                membre_choisi = membre  # Membre trouvé
                p_membre = True

        # --- Étape 3 : Validation du prêt si tout est correct ---
        if p_doc == True and p_membre == True:
            if document_choisi.est_disponible:
                # Le document est disponible : on effectue le prêt
                membre_choisi.emprunter(document_choisi)       # Ajout à la liste adhérent
                document_choisi.est_disponible = False          # Marque comme non disponible
                print(f"Emprunt enregistre. Titre : {p_doc} | Adherant : {p_membre}")
            else:
                print("Livre non disponible")  # Le document est déjà emprunté
        else:
            # Levée d'exception selon ce qui manque
            if p_doc == False:
                raise Exception(f" Livre non valide ")
            if p_membre == False:
                raise Exception(f" Membre non valide ")


# ============================================================
#  CLASSE : Interface
#  Fournit un menu interactif en ligne de commande pour
#  interagir avec la bibliothèque via la classe Bibliothecaire.
# ============================================================
class Interface:
    """
    Interface utilisateur en ligne de commande pour la bibliothèque.

    Attributs:
        bibliotheque (Bibliothecaire): Instance du gestionnaire de bibliothèque.
    """

    def __init__(self):
        """Initialise l'interface avec une instance de Bibliothecaire."""
        self.bibliotheque = Bibliothecaire()

    def menu(self):
        """
        Affiche le menu principal en boucle et traite les choix
        de l'utilisateur jusqu'à ce qu'il choisisse de quitter (option 8).
        """
        while True:

            # --- Affichage du menu ---
            print("===========Menu===========")
            print("1. Ajouter un livre")
            print("2. Ajouter un Membre")
            print("3. Valider un emprunt")
            print("4. Retour")
            print("5. Afficher les livres")
            print("6. Afficher les adherants")
            print("7. Liste des emprunts d'un aderant")
            print("8. Quitter")
            choice = input("Choisir........: ")

            match choice:

                case "1":
                    # --- Ajout d'un document (Livre ou Magazine) ---
                    titre = input("Veuillez saisir le titre du livre: ")
                    auteur = input("Veuillez saisir l'auteur: ")
                    document = Livre(titre, auteur)  # Document par défaut

                    # Boucle jusqu'à saisie d'un type valide
                    while True:
                        type_doc = input(
                            "Veuillez saisir le type de document (Livre ou Magazine) : "
                        ).lower()
                        if type_doc == "magazine":
                            document = Magazine(titre, auteur)
                            break
                        elif type_doc == "livre":
                            document = Livre(titre, auteur)
                            break
                        else:
                            print("Type de document non reconnu")

                    self.bibliotheque.ajout_document(document)

                case "2":
                    # --- Inscription d'un nouvel adhérent ---
                    # Boucle jusqu'à saisie d'un nom alphabétique valide
                    while True:
                        nom = input("Veillez entrer votre nom: ")
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    self.bibliotheque.inscrire_membre(nom)
                    self.bibliotheque.afficher_adherent()  # Affiche la liste mise à jour

                case "3":
                    # --- Validation d'un emprunt ---
                    while True:
                        nom = input("Veillez entrer votre nom: ").lower()
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    titre = input("Veuillez saisir le titre du livre: ")
                    try:
                        self.bibliotheque.valider_pret(nom, titre)
                    except Exception as e:
                        print(e)  # Affiche le message d'erreur si membre/livre introuvable

                case "4":
                    # --- Enregistrement d'un retour ---
                    while True:
                        nom = input("Veillez entrer votre nom: ")
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    while True:
                        title = input("Veillez entrer votre title: ")
                        if title.isalpha():
                            break
                        else:
                            print("Veuillez entrer un title valide")

                    # Appel de la méthode de retour avec nom et titre saisis
                    self.bibliotheque.retour(titre, nom)

                case "5":
                    # --- Affichage de tous les documents ---
                    self.bibliotheque.afficher_document()

                case "6":
                    # --- Affichage de tous les adhérents ---
                    self.bibliotheque.afficher_adherent()

                case "7":
                    # --- Affichage des emprunts d'un adhérent spécifique ---
                    print("dsd")
                    nom = input("Saisir le nom : ")
                    self.bibliotheque.afficher_emprunt(nom)

                case "8":
                    # --- Quitter l'application ---
                    exit()

                case _:
                    # --- Choix non reconnu ---
                    print("Choix invalide")


# ============================================================
#  POINT D'ENTRÉE DU PROGRAMME
#  Création de l'interface et lancement du menu principal.
# ============================================================
menu = Interface()
menu.menu()