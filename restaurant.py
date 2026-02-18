class Restaurant:
    def __init__(self, commande):
          self.commande = commande
          
    def passer_commande(self):
        print(f"La commande {self.commande} est passé avec succées. Veuillez patienter pour la validation...")
    
    def commande_receive(self):
        print("Commande accepté, en préparation")
        
    def assignation_livreur(self, livreur):
        print(f"Le livreur {livreur.nom} est affecté à la commande {self.commande}")

class Livreur:
    def __init__(self, nom, position):
        self.nom = nom
        self.position = position    
    
    def change_position(self, new_position):
        self.position = new_position
        print(f"La nouvelle position du livreur {self.nom} est {self.position}")
    
    def confirm_livraison(self):
        print(f"Le livreur {self.nom} a livré la commande")
        
    
    
    
client1 = Restaurant(input("Quelle est votre commande ? "))
client1.passer_commande()
client1.commande_receive()
livreur1 = Livreur("Moussa", "Restaurant")
livreur1.change_position("En Livraison")
livreur1.confirm_livraison() 