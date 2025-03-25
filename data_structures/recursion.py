def compte_a_rebours(n):
    if n==0:
        print("Boom")
    else:
        print(n)
        return compte_a_rebours(n-1)

def somme(n):
    if n==1:
        return 1
    else:
        return  n+somme(n-1)
    


def longueur(s):
    if s=="":
        return 0
    else:
        return 1 + longueur(s[1:])
        
def factorile(n):
    if n==1:
        return 1
    else:
        return n*factorile(n-1)

def inverse(s):
    if s=="":
        return ""
    else: 
        return  s[-1] +inverse(s[:-1])




def est_palindrome(s):
    if len(s)==0 or len(s)==1:
        return True
    else:
        if s[0]==s[-1]:
            return est_palindrome(s[1:-1])
        else:
            return False



def puissance(a,b):
    if b==0:
        return 1
    else:
        return a * puissance(a,b-1)
    
    
def somme(s):
    if s=="":
        return 0
    else:
        return int(s[0])+somme(s[1:])
    

def occurences(s,a):
    if s=="":
        return 0
    else:
        if  s[0]==a:
            return 1+occurences(s[1:],a)
        else:
            return occurences(s[1:],a)



def somme_liste(liste):
    if len(liste)==0:
        return 0
    else:
        return  liste[0]+somme_liste(liste[1:])   
def compter_occurences(liste,e):
    if len(liste)==0:
        return 0
    else:
        if liste[0]==e:
            return 1+compter_occurences(liste[1:])
        else:
            return compter_occurences(liste[1:])


def maximum(liste):
    if len(liste)==1:
        return liste[0]
    else:
        if liste[0]>maximum(liste[1:]):
            return liste[0]
        else:
            return maximum(liste[1:])
def est_trie(liste):
    print(liste)
    print(f"premier element {liste[0]} , deuxime element {liste[1]} ")
    if len(liste)==1:
        return True
    else:
        if  liste[0]>liste[1]:
            return False
        else:
            print("rappel")
            print(liste)
            return est_trie(liste[1:])

def inv_liste(liste):
    if len(liste)==1:
        return liste[0]
    else:
        print(liste)
        liste.append(liste[0])
        return inv_liste(liste[1:])

        

liste=[1,2,3,4,5,6]
liste_inv=inv_liste(liste)


    
