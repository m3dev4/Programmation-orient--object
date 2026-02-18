import subprocess

class Service:
    def __init__(self, nom):
        self.nom = nom

    def demarrer(self):
        print(f"Démarrage du service {self.nom}")
        subprocess.run(["sudo", "systemctl", "start", self.nom])

    def arreter(self):
        print(f"Arrêt du service {self.nom}")
        subprocess.run(["sudo", "systemctl", "stop", self.nom])

    def redemarrer(self):
        print(f"Redémarrage du service {self.nom}")
        subprocess.run(["sudo", "systemctl", "restart", self.nom])