from fonctions.variables import *

def utilisation_objet(objet) :
    
    heal = 0
    heal_PM = 0
    Décuplo = False
    Count_Décuplo = 0
    Hâte = False
    Count_Hâte = 0
    Protection = False
    Count_Protection = 0
    effets = True


    if objet.id == 1 :
        heal = 40
    
    elif objet.id == 2 :
        heal = 80

    elif objet.id == 3 :
        heal = 120

    elif objet.id == 4 :
        heal = 200

    elif objet.id == 5 :
        effets = False
        
    elif objet.id == 6 :
        heal_PM = 30

    elif objet.id == 7 :
        heal_PM = 60

    elif objet.id == 8 :
        heal_PM = 120

    elif objet.id == 9 :
        heal = 400
        heal_PM = 250

    elif objet.id == 10 :
        Décuplo = True
        Count_Décuplo = 5

    elif objet.id == 11 :
        Hâte = True
        Count_Hâte = 15

    elif objet.id == 12 :
        Protection = True
        Count_Protection = 5

    
    return(heal, heal_PM, Décuplo, Count_Décuplo, Hâte, Count_Hâte, Protection, Count_Protection, effets)


    