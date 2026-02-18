#Creation du class mere
class Vehicule:
    def __init__(self, marque, modele):
        self.marque = marque
        self.modele = modele

    def demarrer(self):
        print("Vehicule demarrer")

#Creation du class enfant qui prend les attributs et methodes de la class mere d'où la notion héritage
class Moto(Vehicule):
    def __init__(self, marque, modele):
     super().__init__(marque, modele) #super() permet d'appeler la class mere et ses methodes
     self.est_bequille_levee = False
        
    def demarrer(self):
        if self.est_bequille_levee:
            print("Moto demarrer")
        else:
            print("Bequille non levee, impossible de demarrer")

    def lever_bequille(self):
        self.est_bequille_levee =  True
        print("Vrammmmmmmm vrammmmmmm Vrammmmmmm🏍️")
   
   
        
moto = Moto("Yamaha", "TMAX")
moto.demarrer()
moto.lever_bequille()
moto.demarrer()
