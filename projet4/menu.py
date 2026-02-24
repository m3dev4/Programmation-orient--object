from classe.bibliothecaire import Bibliothecaire
from classe.livre import Livre
from classe.magazine import Magazine


# ============================================
# @Author Mouhamed Lo & Ndeye Fassa Samb
# ============================================

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
                        print(
                            e
                        )  # Affiche le message d'erreur si membre/livre introuvable

                case "4":
                    # --- Enregistrement d'un retour ---
                    while True:
                        nom = input("Veillez entrer votre nom: ")
                        if nom.isalpha():
                            break
                        else:
                            print("Veuillez entrer un nom valide")

                    titre = input("Veuillez saisir le titre du livre: ")

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
if __name__ == "__main__":
    interface = Interface()
    interface.menu()
