
from fonctions.fonction_VoirInventaire import VoirInventaire
from fonctions.fonction_print_objets import print_objets
from fonctions.fonction_ShowArmes import ShowArmes
from fonctions.fonction_ShowArmures import ShowArmures

def inventaire(user, action, arme_armure) :
    

    if action == 1 :

        VoirInventaire(user)

        liste_objets_inventaire = print_objets(user.id)
        for i in liste_objets_inventaire :
            print (i)
        

    elif action == 2 :

        if arme_armure == 1 :
            ShowArmes(user)

        elif arme_armure == 2 :
            ShowArmures(user)

        