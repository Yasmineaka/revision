def est_multiple_de(nbr):
    if type(nbr) is not int:
        return "erreur"
    else:
        continuer_partie = True
        while continuer_partie:
            nbr = int(input(' > : '))
            if (nbr % 3 == 0):
                return('CE nombre ' + str(nbr) + ' est un multiple de 3')
            else:
                return('CE nombre ' + str(nbr) + ' n\'est pas un multiple de 3')
    
print(est_multiple_de(3))



# nombre aleatoire compris entre 0 et 100
# dire a l 'utilisateur s'il doit entrer un nombre superieur ou inferieur du nombre qu'il a entrée