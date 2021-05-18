def attaque_monstre(monstre, user) :
    
    degats = 0

    if monstre.Attaque >= monstre.Puissance_Magique :
        degats = monstre.Attaque - user.Défense
    else :
        degats = monstre.Puissance_Magique - user.Résistance_Magique

    if degats < 0 :
        degats = 0


    return degats