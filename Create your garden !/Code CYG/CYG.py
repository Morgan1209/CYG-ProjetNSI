import pyxel
#from  Barretexte import *

pyxel.init(175, 175, title="Create your garden !")
pyxel.load("plans.pyxres")
pyxel.mouse(True)
pyxel.fullscreen(True)

class App:
    class ecriture:
        def __init__(self,x,y,largeur,longueur):
            self.text = str(7)
            self.largeur = largeur
            self.longueur = longueur
            self.x=x
            self.y=y
            self.actif=False
            self.longueur_texte_max=2
            self.couleur=5
            
            
        
        def est_vide(self):
            if self.text=="":
                return True
            return False
        
        def fini_ecrire(self):
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.actif=False
                if self.text == "":
                    self.couleur = 0
                else:
                    self.couleur=int(self.text)
                if int(self.text) >=16:
                    self.text=str(15)
            return self.text if self.text != "" else "0"
            
        def barre_texte_selection(self):
            if pyxel.mouse_x > self.x and pyxel.mouse_x < self.x+self.longueur :
                if pyxel.mouse_y > self.y and pyxel.mouse_y <self.y+self.largeur :
                    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                        self.actif = True

        def draw(self):
            
            pyxel.rect(self.x, self.y, self.largeur, self.longueur, self.couleur)
            pyxel.rectb(self.x, self.y, self.largeur, self.longueur, 7)
            if str("7") in self.text:
                pyxel.text(self.x+4, self.y+5, self.text, 0)
            else:
                pyxel.text(self.x+4, self.y+5, self.text, 7)

        def update(self):
            self.barre_texte_selection()
            self.fini_ecrire()
            if self.actif== True:
                for touche, caractere in touches.items():
                    if pyxel.btnp(touche):
                        if len(self.text)+1 <= self.longueur_texte_max:
                            self.text+= caractere

                if pyxel.btnp(pyxel.KEY_SPACE):
                    if len(self.text)+1 <= self.longueur_texte_max:
                        self.text+= " "

                if pyxel.btnp(pyxel.KEY_BACKSPACE):
                    self.text = self.text[:-1]

    def __init__(self):
        """
        Initialisation
        """
        self.rectangle=[]
        self.triangle=[]
        self.cercle=[]
        self.sprite=[]
        self.choix= "None"
        self.barre1 = self.ecriture(150,155,15,15)
        self.barre2 = self.ecriture(140,75,25,15)
        self.barre1.couleur=7
        self.selection_sprite=0
        pyxel.run(self.update, self.draw)

    

    def UI(self):
        """
        Création du menu 
        """
        # Six carrés : un pour le cercle, triangle, rectangle, le none, la gomme et +
        pyxel.rectb(155,15,12,12,7) #cercle
        pyxel.circ(161,21,3,7)
        pyxel.rectb(135,35,12,12,7) #triangle
        pyxel.tri(137,43,140,37,144,43,7)
        pyxel.rectb(135,15,12,12,7) #rectangle
        pyxel.rect(137,17,7,7,7)
        pyxel.rectb(155,35,12,12,7) #None
        pyxel.rectb(130,120,40,12,7) #Gomme
        pyxel.text(140,123,"Gomme", 8)
        pyxel.blt(140, 55, 0, 16 * self.selection_sprite, 0, 16, 16, 0)
        pyxel.rectb(135,55,32,17,7)
        pyxel.rectb(154,58,6,2,8)
        pyxel.rectb(156,56,2,6,8)

        # Lignes du jardin
        pyxel.rectb(5,20,120,130,7)
        
    

    def collision(self, mx, my):
        if 155 <= mx <= 167 and 15 <= my <= 27:
            return "cercle"
        if 135 <= mx <= 147 and 35 <= my <= 47:
            return "triangle"
        if 135 <= mx <= 147 and 15 <= my <= 27:
            return "rectangle"
        if 155 <= mx <= 167 and 35 <= my <= 47:
            return "None"
        if 135 <= mx <= 167 and 55 <= my <= 72:
            return "sprite"
        if 130 <= mx <= 170 and 120 <= my <= 132:
            self.tout_supprimer()
        return None
    
    def placement(self, mx, my):
        if  5<mx<114 and 19<my<142:
            if self.choix == "cercle":
                self.cercle.append((mx, my, int(self.barre1.fini_ecrire())))
            elif self.choix == "triangle":
                self.triangle.append((mx, my ,int(self.barre1.fini_ecrire())))
            elif self.choix == "rectangle":
                self.rectangle.append((mx, my, int(self.barre1.fini_ecrire())))
            elif self.choix == "None":
                pass
            elif self.choix == "sprite":
                if self.barre2.text=="":
                    self.sprite.append((mx, my, self.selection_sprite))
                else:
                    self.sprite.append((mx, my-int(self.barre2.text), self.selection_sprite))
        return None
    
    def couleure(self):
        if self.barre1.text != "":
            self.barre1.couleur = int(self.barre1.text)
            if self.barre1.couleur > 15:
                self.barre1.couleur=15
    
    def tout_supprimer(self):
        self.rectangle.clear()
        self.triangle.clear()
        self.cercle.clear()
        self.sprite.clear()

    def retour_arriere(self):
        if pyxel.btnp(pyxel.KEY_B):
            if self.choix=="rectangle":
                self.rectangle=self.rectangle[:-1]
            if self.choix=="triangle":
                self.triangle=self.triangle[:-1]
            if self.choix=="cercle":
                self.cercle=self.cercle[:-1]
            if self.choix=="sprite":
                self.sprite=self.sprite[:-1]
        
    # =========================================================
    # == UPDATE
    # =========================================================
    def update(self):
        self.couleure()
        self.retour_arriere()
        self.barre1.update()
        self.barre2.update()

        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.selection_sprite += 1

        if pyxel.btnp(pyxel.KEY_LEFT):
            self.selection_sprite -= 1

        # séléction de barre de texte
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            mx = pyxel.mouse_x
            my = pyxel.mouse_y
            # Désactiver toutes les barres
            self.barre1.actif = False
            self.barre2.actif = False

            # Activer celle cliquée
            if self.barre1.x < mx < self.barre1.x + self.barre1.longueur and self.barre1.y < my < self.barre1.y + self.barre1.largeur:
                self.barre1.actif = True

            elif self.barre2.x < mx < self.barre2.x + self.barre2.longueur and self.barre2.y < my < self.barre2.y + self.barre2.largeur:
                self.barre2.actif = True

            else:
                choix = self.collision(mx, my)
                if choix:
                    self.choix = choix
                else:
                    self.placement(mx, my)

    # =========================================================
    # == DRAW
    # =========================================================
    def draw(self):
        pyxel.cls(0)
        pyxel.text(5,5, "CREATE YOUR GARDEN !", 11)
        pyxel.text(130,5, "Construire", 11)
        pyxel.text(5, 160, "B = Retour arriere", 11)
        pyxel.text(110, 160, "Couleur :", 11)
        self.barre1.draw()
        self.barre2.draw()
        
    
        for x, y, c in self.cercle:
            pyxel.circ(x, y, 5, c)
        for x, y, c in self.triangle:
            pyxel.tri(x, y, x+5, y-5, x+10, y, c)
        for x, y ,c in self.rectangle:
            pyxel.rect(x, y, 12, 8, c)
        for x, y, s in self.sprite:
            pyxel.blt(x, y, 0, 16*s, 0, 16, 16, 0)

        pyxel.rectb(130,100,40,12,7)
        pyxel.text(132,103,self.choix,7)
        self.UI()


#Bibliothèque contenant les touches disponibles pour les barres de textes
touches = {
    pyxel.KEY_0: "0",
    pyxel.KEY_1: "1",
    pyxel.KEY_2: "2",
    pyxel.KEY_3: "3",
    pyxel.KEY_4: "4",
    pyxel.KEY_5: "5",
    pyxel.KEY_6: "6",
    pyxel.KEY_7: "7",
    pyxel.KEY_8: "8",
    pyxel.KEY_9: "9",
}
App()

# Realise par Maxime B et Morgan DTF - 2026 - Create your garden !