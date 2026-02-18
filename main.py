class Apprenant:
    def __init__(self, prenom, filiere):
        self.prenom = prenom
        self.filiere = filiere
        
    def se_presenter(self):
        print(f"Bonjour {self.prenom}. Votre filiere est {self.filiere}")
        
#Instences
apprenant1 = Apprenant("Moussa", "Développement Web")
apprenant2 = Apprenant("Fatou", "Data Science")

#On affiche le prenom via un print
print(apprenant1.prenom)

#Appel la methode pour les deux objects
apprenant1.se_presenter()
apprenant2.se_presenter()

#Modification du prenom apprenant1
apprenant1.prenom = "Moustapha"
apprenant1.se_presenter()
