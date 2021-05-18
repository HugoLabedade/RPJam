def Attaque_normal_user(attaque_user, défense_monstre) :
    
    if attaque_user - défense_monstre < 0 :
        return(0)
    else :
        return (attaque_user - défense_monstre)