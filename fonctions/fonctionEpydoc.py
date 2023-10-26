'''
créé le 21/10/2023
author: iut

'''
vingt=20
def CalculeTermesSuites(a:float,b:int,U:int,n:int)->list:
        """

        fonction qui calcule
        les premiers termes 
        successifs d'une suite de la 
        forme a*Un+b

        paramètres:
        ============
                - a ; un réel positif ou négatif
                - b un entier positif ou négatif
                - U:Le premier terme de la suite
                - n: le nombre de termes à calculer
        retourne la liste des n premiers termes de la suite.
        """
        valeurs=[]
        i=0
        while i<n:
                valeurs.append(U)
                U=a*U+b
                i=i+1
        return valeurs
def Bonjour()->str:
        """fonction qui retourne bonjour"""
        return bonjour

print(CalculeTermesSuites(0.5,8,2,3))
