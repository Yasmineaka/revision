#Écrire une fonction isAnagram qui prend en paramètre deux mots sous forme de chaînes de caractères et qui retourne "true" si les deux mots sont des anagrammes l'un de l'autre (c'est-à-dire que les mêmes lettres sont présentes dans les deux mots), et "false" sinon.
def isAnagram(mot1,mot2):
    if isinstance(mot1,str) and isinstance(mot2,str):
        if sorted(mot1)==sorted(mot2):
            return True
        return False
    return -1
print(isAnagram("azerty&é","sdfgh"))
print(isAnagram("azerty&é","azerty&é"))

#Écrire une fonction nommée countVowels(chaine) qui prend en entrée une chaîne de caractères et retourne le nombre de voyelles qu'elle contient
def countVowels(chaine):
    if isinstance(chaine,str):
        b="AEYUIOaeyuio"
        tab =[]
        for i in chaine:
            if i in b:
                tab.append(i)
        return len(tab)
    return -1
print(countVowels("mmmaamuimmm"))

#Créer la fonction 'parity' qui fera la comparaison entre les éléments pairs et impairs d'un tableau T passé en paramètre. Si la somme des éléments pairs est supérieure ou éguale à la somme des éléments impairs du tableau, la fonction retounera "true" sinon "false"
def parity(tableau):
    if isinstance(tableau,(list,tuple)):
        tab1=[]
        tab2=[]
        for i in tableau:
            if i%2==0:
                tab1.append(i)
            if i%3==0:
                tab2.append(i)    
            if sum(tab1)>=sum(tab2):
                return "true"
            if sum(tab1)<sum(tab2):
                return "false"
        return tableau([tab1],[tab2])
print(parity([5,6]))      
            


def srt(ch):
    a=ch[::-1]
    return a[::]
print(srt("hello world"))