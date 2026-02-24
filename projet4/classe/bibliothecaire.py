from classe.adherent import Adherent


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
        self.liste_document = []  # Aucun document au départ
        self.liste_adherant = []  # Aucun adhérent au départ

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
        for doc in self.liste_document:
            print(doc)  # Appelle __str__ de chaque document

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

    def inscrire_membre(self, nom):
        """
        Crée un nouvel adhérent et l'inscrit dans la bibliothèque.

        Args:
            nom (str): Nom du nouveau membre.
        """
        try:
            membre = Adherent(nom)  # Création de l'objet Adherent
            self.liste_adherant.append(membre)  # Ajout à la liste
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
                ad_trouve = adherent  # Adhérent trouvé
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
            doc_trouve.est_disponible = True  # Remet le document disponible
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
                membre_choisi.emprunter(document_choisi)  # Ajout à la liste adhérent
                document_choisi.est_disponible = False  # Marque comme non disponible
                print(f"Emprunt enregistre. Titre : {p_doc} | Adherant : {p_membre}")
            else:
                print("Livre non disponible")  # Le document est déjà emprunté
        else:
            # Levée d'exception selon ce qui manque
            if p_doc == False:
                raise Exception(f" Livre non valide ")
            if p_membre == False:
                raise Exception(f" Membre non valide ")
