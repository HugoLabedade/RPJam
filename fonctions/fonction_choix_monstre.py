from fonctions.fonction_monstre import monstre
from fonctions.conn_liste import conn, liste_armures, liste_armes
from fonctions.fonction_ShowCombat import ShowCombat


def choix_monstre(user, monstre_id, User_actuel, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, user_PV, vérif_equipement) :

    monstre_actuel = monstre(monstre_id)

    print(user)

    monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV

    
    equipement_cursor=conn.cursor()
    equipement = ("SELECT * FROM {0} WHERE id_Users = {1}".format("equipement_users", User_actuel.id))
    equipement_cursor.execute(equipement)
    data_equipement = equipement_cursor.fetchone()
    

    if data_equipement[1] is not None and vérif_equipement == False:
        casque = liste_armures[data_equipement[1]-1]        
        if casque.stat_boost == "Attaque" :
            user_Attaque_base += casque.bonus_stat
        elif casque.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += casque.bonus_stat
        elif casque.stat_boost == "Défense" :
            user_Défense_base += casque.bonus_stat
        elif casque.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += casque.bonus_stat
        elif casque.stat_boost == "Vitesse" :
            user_Vitesse_base += casque.bonus_stat
        elif casque.stat_boost == "Esquive" :
            User_actuel.Esquive += casque.bonus_stat

    if data_equipement[2] is not None and vérif_equipement == False:
        plastron = liste_armures[data_equipement[2]-1]        
        if plastron.stat_boost == "Attaque" :
            user_Attaque_base += plastron.bonus_stat
        elif plastron.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += plastron.bonus_stat
        elif plastron.stat_boost == "Défense" :
            user_Défense_base += plastron.bonus_stat
        elif plastron.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += plastron.bonus_stat
        elif plastron.stat_boost == "Vitesse" :
            user_Vitesse_base += plastron.bonus_stat
        elif plastron.stat_boost == "Esquive" :
            User_actuel.Esquive += plastron.bonus_stat

    if data_equipement[3] is not None and vérif_equipement == False:
        jambières = liste_armures[data_equipement[3]-1]        
        if jambières.stat_boost == "Attaque" :
            user_Attaque_base += jambières.bonus_stat
        elif jambières.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += jambières.bonus_stat
        elif jambières.stat_boost == "Défense" :
            user_Défense_base += jambières.bonus_stat
        elif jambières.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += jambières.bonus_stat
        elif jambières.stat_boost == "Vitesse" :
            user_Vitesse_base += jambières.bonus_stat
        elif jambières.stat_boost == "Esquive" :
            User_actuel.Esquive += jambières.bonus_stat

    if data_equipement[4] is not None and vérif_equipement == False:
        bottes = liste_armures[data_equipement[4]-1]        
        if bottes.stat_boost == "Attaque" :
            user_Attaque_base += bottes.bonus_stat
        elif bottes.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += bottes.bonus_stat
        elif bottes.stat_boost == "Défense" :
            user_Défense_base += bottes.bonus_stat
        elif bottes.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += bottes.bonus_stat
        elif bottes.stat_boost == "Vitesse" :
            user_Vitesse_base += bottes.bonus_stat
        elif bottes.stat_boost == "Esquive" :
            User_actuel.Esquive += bottes.bonus_stat

    if data_equipement[5] is not None and vérif_equipement == False:
        anneau = liste_armures[data_equipement[5]-1]        
        if anneau.stat_boost == "Attaque" :
            user_Attaque_base += anneau.bonus_stat
        elif anneau.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += anneau.bonus_stat
        elif anneau.stat_boost == "Défense" :
            user_Défense_base += anneau.bonus_stat
        elif anneau.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += anneau.bonus_stat
        elif anneau.stat_boost == "Vitesse" :
            user_Vitesse_base += anneau.bonus_stat
        elif anneau.stat_boost == "Esquive" :
            User_actuel.Esquive += anneau.bonus_stat

    if data_equipement[6] is not None and vérif_equipement == False:
        collier = liste_armures[data_equipement[6]-1]        
        if collier.stat_boost == "Attaque" :
            user_Attaque_base += collier.bonus_stat
        elif collier.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += collier.bonus_stat
        elif collier.stat_boost == "Défense" :
            user_Défense_base += collier.bonus_stat
        elif collier.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += collier.bonus_stat
        elif collier.stat_boost == "Vitesse" :
            user_Vitesse_base += collier.bonus_stat
        elif collier.stat_boost == "Esquive" :
            User_actuel.Esquive += collier.bonus_stat

    if data_equipement[7] is not None and vérif_equipement == False:
        arme = liste_armes[data_equipement[7]-1]        
        if arme.stat_boost == "Attaque" :
            user_Attaque_base += arme.bonus_stat
        elif arme.stat_boost == "Puissance_Magique" :
            User_actuel.Puissance_Magique += arme.bonus_stat
        elif arme.stat_boost == "Défense" :
            user_Défense_base += arme.bonus_stat
        elif arme.stat_boost == "Résistance_Magique" :
            User_actuel.Résistance_Magique += arme.bonus_stat
        elif arme.stat_boost == "Vitesse" :
            user_Vitesse_base += arme.bonus_stat
        elif arme.stat_boost == "Esquive" :
            User_actuel.Esquive += arme.bonus_stat

    vérif_equipement = True

    print("user pv : {0}".format(user_PV))
    print("user pm : {0}".format(User_actuel.PM))

    print("Début du combat contre un {0}".format(monstre_actuel.nom))
    print("PV du monstre : {0}".format(monstre_PV))


    ShowCombat(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement)

