continuer_partie = True

while continuer_partie:
    try:
        nbr = int(input(' > : '))
        if (nbr % 3 == 0):
            print('CE nombre ' + str(nbr) + ' est un multiple de 3')
        else:
            print('CE nombre ' + str(nbr) + ' n\'est pas un multiple de 3')
    except ValueError:
        print('Erreur : veuillez entrer un nombre valide')

    except KeyboardInterrupt:
        reponse = input('voulez vous réellement quitter : ')
        if reponse == 'oui':
            continuer_partie = False
        print('Impossible de sortir')