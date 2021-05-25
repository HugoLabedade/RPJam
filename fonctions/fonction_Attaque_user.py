import fonctions.fonction_lancement_menu_combat as jeu

def Attaque_user(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement) :
    jeu.combat(user, monstre_actuel, "Attaque", None, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement)
