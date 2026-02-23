from abc import ABC, abstractmethod


class Paimennt:

    @abstractmethod
    def payer(self, compte, amount):
        pass

    @abstractmethod
    def deposer(self, compte, amount):
        pass


class CompteClient:
    def __init__(self, numero_compte, nom, solde):
        self.numero_compte = numero_compte
        self.nom = nom
        self.__solde = solde # Encapstilation

    @property
    def solde(self):
        return self.__solde   ### ===> GETTERS

    @solde.setter
    def deposer(self, amount):
        if amount <= self.__solde:
            raise ValueError("Le montant ne peut pas etre négative")
        self.__solde += amount

    def retirer(self, amount):
        # if amount <= self.__solde:
        #     raise ValueError("Le montant ne peut pas etre negative")
        self.__solde -= amount


class ModePaimentWave(Paimennt):
    def __init__(self,):
        super().__init__()

    def payer(self, compte, amount):
        compte.retirer(amount)
        print("Paiement effectué avec succès")

    def deposer(self, compte, amount):
        compte.deposer(amount)
        print("Dépôt effectué avec succès")

    def __str__(self):
        return f"ModePaimentWave(solde={self.solde})"


compte1 = CompteClient("001", "John Doe", 10000)
print(compte1.solde)
paiement = ModePaimentWave()
paiement.payer(compte1, 5000)

print("Solde après paiement :", compte1.solde)
