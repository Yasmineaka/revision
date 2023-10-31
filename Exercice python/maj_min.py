def changer_chaine(chaine):
   
    if not isinstance(chaine, str): 
        return -1 
     
    changement = " "
    for caractere in chaine: 
        if caractere.islower(): 
            changement += caractere.upper() 
        elif caractere.isupper(): 
            changement += caractere.lower() 
    return changement  

print(changer_chaine("b rjuhUmr"))