"""Créez une classe Personne avec des attributs nom et age. Créez ensuite une instance de cette classe et affichez les attributs."""
# class Personne():
#     def __init__(self, nom,age):
#         self.nom=nom
#         self.age=age
# personne = Personne("yas",19)
# print(personne.nom)
# print(personne.age)

"""Déclarez une classe Rectangle avec des attributs largeur et hauteur. Ajoutez une méthode pour calculer l'aire du rectangle."""
# class rectangle():
#     def __init__(self,largeur, hauteur):
#         self.largeur=largeur
#         self.hauteur=hauteur
#     def Calcul(self):
#         air = self.largeur*self.largeur
#         return air
# taille=rectangle(12,12)
# cal= taille.Calcul()
# print(f"l'aire du triangle est {cal}")



class Compteur():
    def __init__(self, nombre):
        self.nombre = nombre
         
    def incrementation(self):
            return self.nombre + self.nombre   
compteur1 = Compteur(2)
compteur2= Compteur(4)
calcul=compteur1.incrementation()
calcul=compteur2.incrementation()
print(compteur1.nombre)
print(compteur2.nombre)


class Compteur:
    nombre = 0
    
    def __init__(self):
        Compteur.nombre += 1
    
    @classmethod
    def afficher_nombre(cls):
        print("Le nombre total d'instances créées est:", cls.nombre)

# Création de plusieurs instances de la classe Compteur
instance1 = Compteur()
instance2 = Compteur()
instance3 = Compteur()

# Affichage du nombre total d'instances créées
Compteur.afficher_nombre()
