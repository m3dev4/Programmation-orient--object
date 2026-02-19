from rich.console import Console
from rich.panel import Panel
from categories import Categories
from depenseManagement import DepenseMangement



class Menu:
    console = Console()
    def __init__(self):
        pass
    
    def display(self):
        print("mise a jour")
        
        choice = self.console.input("Entrez votre choix : ")
        if choice == "1":
            task_name = self.console.input("Entrez le nom de la tache : ")
            categories = Categories()
            categories.add_categorie(task_name)
        
        if choice == "2":
           depense = DepenseMangement()
           titre = input("titre: ")
           description = input("description: ")
           montant = input("montant: ")
           categorie = input("categorie: ")
           depense.add_depense(titre, description, montant, categorie)
        if choice == "3":
           depense = DepenseMangement()       
           depense.list_depense()
        
        if choice == "4":
           depense = DepenseMangement()       
           depense.update_depense()
        

menu = Menu()
menu.display()