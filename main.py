from tkinter import *
import random
from config import *
import customtkinter
import time

class Jeu(customtkinter.CTkFrame):
    def __init__(self, master, niveau):
        super().__init__(master)
        self.app = master
        self.niveau = niveau
        self.grid_columnconfigure(0, weight=1)

        if self.niveau == "Facile":
            self.jouerFacile()
        elif self.niveau == "Normal":
            #self.jouerNormal()
            self.after(500, self.retourMenu)  # Appel avec un petit délai


    def jouerFacile(self):
        self.nombreDeviner = [random.randint(0, 9) for _ in range(NOMBRE_FACILE_DEVINER)]
        print(f"Chiffre à deviner {self.nombreDeviner}")
        self.labelsResultats = []
        
        # Création d'une zone de texte où l'utilisateur peut taper
        self.textbox = customtkinter.CTkTextbox(self, width=400, height=200)
        self.textbox.grid(row=0, column=0, padx=20, pady=20)
        self.textbox.bind("<KeyPress>", self.restrictInputFacile)

        # Création d'un bouton pour récupérer les chiffres
        self.button = customtkinter.CTkButton(self, text="Récupérer les chiffres", command=self.getText)
        self.button.grid(row=1, column=0, padx=20, pady=10)
    


    def restrictInputFacile(self, event):
        # Vérifier si la touche pressée est un chiffre, ou une touche de suppression (Backspace ou Delete)
        if not event.char.isdigit() and event.keysym not in ("BackSpace", "Delete", "Return"):
            return "break"  # Ignore l'entrée si ce n'est pas un chiffre et pas une touche de suppression

        # Vérifier si la longueur du texte dépasse la limite après l'ajout d'un caractère
        if len(self.textbox.get("1.0", "end-1c")) >= NOMBRE_FACILE_DEVINER and event.keysym != "BackSpace":
            return "break"  # Ignore l'entrée si la longueur maximale est atteinte et ce n'est pas une suppression


    def compareReponse(self, nombreDeviner, reponseUtilisateur):
       # Liste pour stocker les résultats
        resultats = []
        
        # Comparaison chiffre par chiffre
        for i, chiffre in enumerate(reponseUtilisateur):
            if chiffre == nombreDeviner[i]:
                resultats.append("Bon et bien placé")
            elif chiffre in nombreDeviner:
                resultats.append("Bon mais mal placé")
            else:
                resultats.append("Mauvais")
        
        # Afficher les résultats dans l'interface
        self.afficherResultat(resultats)
        self.jeuFini(resultats)

    
    def afficherResultat(self, resultats):
        # Supprimer les anciens labels
        for label in self.labelsResultats:
            label.destroy()
        self.labelsResultats.clear()

        for i, result in enumerate(resultats):
            labelResult = customtkinter.CTkLabel(self, text=f"Chiffre {i+1}: {result}")
            labelResult.grid(row=i+2, column=0, padx=10, pady=5)
            self.labelsResultats.append(labelResult)

        self.update()  # Forcer la mise à jour de l'interface


    def jeuFini(self, resultat):
        if all(i == "Bon et bien placé" for i in resultat):
            message = customtkinter.CTkLabel(self, text="Félicitations ! Vous avez trouvé la bonne combinaison !", text_color="green", font=("Arial", 18))
            message.grid(row=len(resultat) + 2, column=0, padx=10, pady=20)
            self.after(3000, self.retourMenu)


    def retourMenu(self):
        self.grid_forget()
        self.app.menu.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
            

    def getText(self):
        # Récupérer le texte de la zone de texte
        text = self.textbox.get("1.0", "end-1c")  # Récupère tout le texte, sauf la dernière ligne vide
        # Convertir en tableau (liste) de chiffres
        digits = [int(digit) for digit in text if digit.isdigit()]
        if len(digits) != NOMBRE_FACILE_DEVINER:
            message = customtkinter.CTkLabel(self, text=f"Erreur : Vous devez entrer exactement {NOMBRE_FACILE_DEVINER} chiffres.", text_color="red", font=("Arial", 14))
            message.grid(row=4, column=0, padx=10, pady=10)
            self.after(1500, message.grid_forget)  # Le message disparaît après 3 secondes

            return
        print(f"Tableau des chiffres: {digits}")
        # Effacer la zone de texte après récupération
        self.textbox.delete("1.0", "end")

        # Appeler la méthode pour comparer la réponse avec la liste nombreDeviner
        self.compareReponse(self.nombreDeviner, digits)  # Utilise self.nombreDeviner ici





class NiveauDifficulte(customtkinter.CTkFrame):
    def __init__(self, master, values):
        super().__init__(master)
        self.values = values
        self.radioButtons = []
        self.selection = customtkinter.StringVar(value="")  # Valeur sélectionnée

        # Centrage des boutons
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        for i, value in enumerate(self.values):
            radio = customtkinter.CTkRadioButton(
                self,
                text=value,
                variable=self.selection,
                value=value
            )
            radio.grid(row=i, column=1, padx=10, pady=(10, 0), sticky="ew")
            self.radioButtons.append(radio)

    def get(self):
        return self.selection.get()

        


class Menu(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.app = master
        
        self.grid_columnconfigure(0, weight=1)
        self.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        # Création d'un texte pour le label
        self.titleText = TITRE_MENU
        
        # Création d'un label et l'ajout à la frame
        self.titleLabel = customtkinter.CTkLabel(self, text=self.titleText, corner_radius=6, font=("Arial", 24))
        self.titleLabel.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.NiveauDifficulte = NiveauDifficulte(self, values=["Facile", "Normal"])
        self.NiveauDifficulte.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="ew")
        self.NiveauDifficulte.configure(fg_color="transparent")

        self.button = customtkinter.CTkButton(self, text="Lancer Jeu", command=self.app.lancerJeu)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("MasterMind")
        self.geometry("720x480")
        # Configuration du grid de la fenêtre principale
        self.grid_columnconfigure(0, weight=1)

        # Création et ajout du menu à la fenêtre
        self.menu = Menu(self)
        self.menu.configure(fg_color="transparent")

    def lancerJeu(self):
        niveau = self.menu.NiveauDifficulte.get()
        self.menu.grid_forget()
        self.jeu = Jeu(self, niveau)
        self.jeu.grid(row=0, column=0, sticky="nsew")

# Exécution de l'application
app = App()
app.mainloop()  
