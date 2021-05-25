
import fonctions.fonction_VoirInventaire as inv
from fonctions.fonction_print_objets import print_objets
import fonctions.fonction_ShowArmes as armes
import fonctions.fonction_ShowArmures as armures

def inventaire(user, action, arme_armure) :
    

    if action == 1 :

        inv.VoirInventaire(user)

        liste_objets_inventaire = print_objets(user.id)
        for i in liste_objets_inventaire :
            print (i)
        

    elif action == 2 :

        if arme_armure == 1 :
            armes.ShowArmes(user)

        elif arme_armure == 2 :
            armures.ShowArmures(user)

        