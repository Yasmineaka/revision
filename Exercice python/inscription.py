nom=input("Entrez votre nom ")
prenom=input("Entrez votre prenom ")
age=input("Entrez votre age ")
email=input("Entrez votre email ")
mdp=input("Entrez votre mdp ")

def inscription():
    return(f"votre nom est {nom}, {prenom}, vous avez {age} ans, votre email est: {email} votre mot de passe est caché")
print(inscription())

def connexion():
    entre_email= input("entrez votre email : ")
    entre_mdp= input("entrez votre mdp : ")
    if entre_email  == email and entre_mdp== mdp:
        return (f"Bienvenu votre nom est {nom}, {prenom}, vous avez {age} ans, votre email est: {email} votre mot de passe est caché")
    else:
        print("email ou mdp incorrect reprenez : ")
        return connexion()
print(connexion())        
    
 

