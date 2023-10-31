# def isAnagram(ch1,ch2):
#   if isinstance(ch1,str) and isinstance(ch2,str):
#     if sorted(ch1) == sorted(ch2):
#       return "true"
#     return "false"
#   return -1

# print(isAnagram("azert", "azer"))
# print(isAnagram("azert", "azetr"))
# print(isAnagram("azert", "azetrr"))
# print(isAnagram("azert", "azert"))


# def isAnagram(ch1,ch2):
#   if isinstance(ch1,str) and isinstance(ch2,str):
#     if sorted(ch1) == sorted(ch2):
#       return "true"
#     else:
#         return "false"
#   else:
#      return -1
# print(isAnagram("azert", "azer"))
# print(isAnagram("azert", "azetr"))
# print(isAnagram("azert", "azetrr"))
# print(isAnagram("azert", "azert"))
# print(sorted("azert"))


# def count_number(nombre):
#     # Vérifier si le paramètre est un entier
#     if not isinstance(nombre, int):
#         return -1
    
#     # Convertir le nombre en une chaîne de caractères pour accéder à chaque chiffre
#     nombre_str = str(nombre)
    
#     # Initialiser une variable pour stocker la somme des chiffres
#     somme_chiffres = 0
    
#     # Parcourir chaque chiffre dans la chaîne et les ajouter à la somme
#     for chiffre in nombre_str:
#         somme_chiffres += int(chiffre)
    
#     return somme_chiffres

# # Exemples d'utilisation de la fonction
# resultat1 = count_number(12345)
# print(resultat1)  # Output: 15 (car 1 + 2 + 3 + 4 + 5 = 15)

# resultat2 = count_number(9876)
# print(resultat2)  # Output: 30 (car 9 + 8 + 7 + 6 = 30)

# resultat3 = count_number("abc")
# print(resultat3)  # Output: -1 (car le paramètre n'est pas un entier)




# def count_number(nombre):
#     if not isinstance(nombre, int):
#         return -1
#     chiffres = [int(chiffre) for chiffre in str(nombre)]
#     somme_chiffres = sum(chiffres)
#     return somme_chiffres
# print(count_number(12345))
# print(count_number(9876))
# print(count_number("abc"))


def tupleLike(iterable):
  if isinstance(iterable, (tuple,list,str)):
    return [len(iterable), iterable[0]]
  return -1

print(tupleLike("safshg"))