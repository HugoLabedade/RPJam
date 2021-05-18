
from class_user import User
from random import randrange

from conn_liste import liste_armes
from conn_liste import liste_armures
from conn_liste import conn

from variables import *

from fonction_monstre import monstre

from fonction_attaque_normal_user import Attaque_normal_user

from fonction_print_compétences import print_compétences

from fonction_compétence_physique import compétence_physique

from fonction_compétence_magique import compétence_magique

from fonction_compétence_sans_dommages import compétence_sans_dommages

from fonction_print_objets import print_objets

from fonction_utilisation_objet import utilisation_objet

from fonction_critique import critique

from fonction_loot import loot

from fonction_gain_xp_golds import gain_xp_gold

from fonction_boutique import boutique

from fonction_equiper_arme import equiper_arme

from fonction_attaque_monstre import attaque_monstre

from fonction_equiper_armure import equiper_armure


def lancement():
    conn_create = input("Connexion / Inscription : ")

    if conn_create == "Connexion" :
        connexion()
    elif conn_create == "Inscription" :
        create_user()

def connexion():
    
    pseudo = input("Pseudo : ")
    mdp = input("password : ")

    user_cursor=conn.cursor()
    user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, mdp))
    user_cursor.execute(user)
    data_user = user_cursor.fetchone()

    
    if data_user is None :

        lancement()

    else : 
        global User_actuel
        User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15], data_user[16])

        global user_PV_Max
        user_PV_Max = User_actuel.PV
        global user_PM_Max
        user_PM_Max = User_actuel.PM
        global user_Attaque_base
        user_Attaque_base = User_actuel.Attaque
        global user_Défense_base
        user_Défense_base = User_actuel.Défense
        global user_Vitesse_base
        user_Vitesse_base = User_actuel.Vitesse
        global user_PV
        user_PV = User_actuel.PV
        global vérif_equipement
        vérif_equipement = False

        

        menu(User_actuel)

def create_user():
    
    print("test")

    pseudo = input("Pseudo : ")
    mdp = input("password : ")
    classe = input("classe : ")

    user_cursor=conn.cursor()
    user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, mdp))
    user_cursor.execute(user)
    data_user = user_cursor.fetchone()

    if data_user is None :

        max_id_cursor=conn.cursor()
        max_id_query = ("SELECT MAX(id) FROM {0}".format("Users"))
        max_id_cursor.execute(max_id_query)
        data_max_id = max_id_cursor.fetchone()
        max_id = 0

        for i in data_max_id :

            if i is None :

                max_id = 0

            else :
                
                max_id = i


        insert_cursor=conn.cursor()

        if classe == "Assassin" :
            insert_query = ("INSERT INTO {0} VALUES({1}, '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format("Users", max_id+1, pseudo, mdp, classe, 0, 1, 10, 10, 10, 10, 10, 10, 10, 5, 0, 4, 0))
        else :
            insert_query = ("INSERT INTO {0} VALUES({1}, '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format("Users", max_id+1, pseudo, mdp, classe, 0, 1, 10, 10, 10, 10, 10, 10, 10, 0, 0, 4, 0))
        insert_cursor.execute(insert_query)
        conn.commit()

        user_cursor=conn.cursor()
        user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, mdp))
        user_cursor.execute(user)
        data_user = user_cursor.fetchone()

        global User_actuel
        User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15], data_user[16])

        insert_equipement_cursor=conn.cursor()
        insert_equipement_query = ("INSERT INTO equipement_users(id, id_Users) VALUES({0}, {1})".format(max_id+1, max_id+1))
        insert_equipement_cursor.execute(insert_equipement_query)
        conn.commit()
        
        global user_PV_Max
        user_PV_Max = User_actuel.PV
        global user_PM_Max
        user_PM_Max = User_actuel.PM
        global user_Attaque_base
        user_Attaque_base = User_actuel.Attaque
        global user_Défense_base
        user_Défense_base = User_actuel.Défense
        global user_Vitesse_base
        user_Vitesse_base = User_actuel.Vitesse
        global user_PV
        user_PV = User_actuel.PV
        global vérif_equipement
        vérif_equipement = False

        menu(User_actuel)

    else :

        lancement()



def menu(user):
    action = input("combat / boutique / inventaire / quitter ? : ")
    if action == "combat" :
        id_monstre = int(input("id du monstre à affronter ? : "))
        combat(user, id_monstre)

    elif action == "boutique" :
        print("entrer boutique")
        liste_boutique = boutique()
        for i in liste_boutique :
            print ("{0} , prix : {1}".format(i[0].nom, i[1], i[2]))

        achat = input("Que voulez vous acheter ? : ")

        for i in liste_boutique :
        
            if i[0].nom == achat and i[1] <= user.Golds :

                # Update inventaire, arme, armure ou objet
                print(i[0], i[1], i[2])
                print(user.id)
                update_golds_cursor=conn.cursor()
                update_golds_query = ("UPDATE Users SET Golds = Golds - {0} WHERE id = {1}".format(i[1], user.id))
                update_golds_cursor.execute(update_golds_query)
                conn.commit()

                if i[2] == "arme" :

                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire_armes WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire_armes SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                        update_inventaire_cursor.execute(update_inventaire_query)
                        conn.commit()

                    else :

                        max_id_cursor=conn.cursor()
                        max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armes"))
                        max_id_cursor.execute(max_id_query)
                        data_max_id = max_id_cursor.fetchone()
                        max_id = 0

                        for j in data_max_id :
                            max_id = j

                        insert_cursor=conn.cursor()
                        insert_query = ("INSERT INTO inventaire_armes VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()

                elif i[2] == "armure" :

                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire_armures WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire_armures SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                        update_inventaire_cursor.execute(update_inventaire_query)
                        conn.commit()

                    else :

                        max_id_cursor=conn.cursor()
                        max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armures"))
                        max_id_cursor.execute(max_id_query)
                        data_max_id = max_id_cursor.fetchone()
                        max_id = 0

                        for j in data_max_id :
                            max_id = j

                        insert_cursor=conn.cursor()
                        insert_query = ("INSERT INTO inventaire_armures VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()

                elif i[2] == "objet" :
                    
                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, i[0].id))
                        update_inventaire_cursor.execute(update_inventaire_query)
                        conn.commit()

                    else :

                        max_id_cursor=conn.cursor()
                        max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire"))
                        max_id_cursor.execute(max_id_query)
                        data_max_id = max_id_cursor.fetchone()
                        max_id = 0

                        for j in data_max_id :
                            max_id = j

                        insert_cursor=conn.cursor()
                        insert_query = ("INSERT INTO inventaire VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()


            elif i[0].nom == achat and i[1] > user.Golds :

                print("pas assez de golds")
                
        menu(user)

    elif action == "inventaire":

        inventaire(user)


    elif action == "quitter" :
        print("stop")

    else :
        menu(user)

def inventaire(user) :
    
    action = int(input("voir l'inventaire d'objet(1) / gérer l'équipement(2) : "))

    if action == 1 :
        print("début")
        print(user)
        print("fin")
        liste_objets_inventaire = print_objets(user.id)
        for i in liste_objets_inventaire :
            print (i)
        
        menu(user)

    elif action == 2 :
        
        arme_armure = int(input("Gérer son arme(1) / Gérer ses armures(2) : "))

        if arme_armure == 1 :
            equiper_arme(user)
            menu(user)

        elif arme_armure == 2 :
            equiper_armure(user)
            menu(user)

        else :
            menu(user)

    else :
        menu(user)

def combat(user, monstre_id) :

    monstre_actuel = monstre(monstre_id)

    monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV


    global User_actuel
    global user_PV_Max
    global user_PM_Max
    global user_Attaque_base
    global user_Défense_base
    global user_Vitesse_base
    global user_PV
    global vérif_equipement

    equipement_cursor=conn.cursor()
    equipement = ("SELECT * FROM {0} WHERE id = {1}".format("equipement_users", User_actuel.id))
    equipement_cursor.execute(equipement)
    data_equipement = equipement_cursor.fetchone()

    

    if data_equipement[2] is not None and vérif_equipement == False:
        casque = liste_armures[data_equipement[2]-1]        
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

    if data_equipement[3] is not None and vérif_equipement == False:
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

    if data_equipement[4] is not None and vérif_equipement == False:
        jambières = liste_armures[data_equipement[2]-1]        
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

    if data_equipement[5] is not None and vérif_equipement == False:
        bottes = liste_armures[data_equipement[2]-1]        
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

    if data_equipement[6] is not None and vérif_equipement == False:
        anneau = liste_armures[data_equipement[2]-1]        
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

    if data_equipement[7] is not None and vérif_equipement == False:
        collier = liste_armures[data_equipement[2]-1]        
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

    if data_equipement[8] is not None and vérif_equipement == False:
        arme = liste_armes[data_equipement[2]-1]        
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



    # Dire qu'on peut modifier nos variables d'effet
    global Brûlure
    global Confusion
    global Sommeil
    global Poison
    global Paralysie

    global Brûlure_ennemi
    global Confusion_ennemi
    global Sommeil_ennemi
    global Poison_ennemi
    global Paralysie_ennemi

    global Boost_Esquive
    global Aura_de_peur
    global Souffle_du_sage
    global Psychocanalisation
    global Clic_clac_zap
    global Grâce_de_la_Déesse
    global Cercle_du_carnage
    global Décuplo
    global Protection
    global Hâte

    global Count_Brûlure
    global Count_Confusion
    global Count_Sommeil
    global Count_Poison
    global Count_Paralysie

    global Count_Brûlure_ennemi
    global Count_Confusion_ennemi
    global Count_Sommeil_ennemi
    global Count_Poison_ennemi
    global Count_Paralysie_ennemi

    global Count_Boost_Esquive
    global Count_Aura_de_peur
    global Count_Souffle_du_sage
    global Count_Psychocanalisation
    global Count_Clic_clac_zap
    global Count_Grâce_de_la_Déesse
    global Count_Cercle_du_carnage
    global Count_Décuplo
    global Count_Protection
    global Count_Hâte

    

    while monstre_PV > 0 and user_PV > 0:

        
        if Décuplo == True :
            User_actuel.Attaque = user_Attaque_base * 2
        else : 
            User_actuel.Attaque = user_Attaque_base

        if Protection == True :
            User_actuel.Défense = user_Défense_base * 2
        else : 
            User_actuel.Défense = user_Défense_base

        if Hâte == True :
            User_actuel.Vitesse = user_Vitesse_base * 2
        else : 
            User_actuel.Vitesse = user_Vitesse_base

        if Cercle_du_carnage == True :
            chances_crit = 10
        else :
            chances_crit = 5

        if Souffle_du_sage == True :
            User_actuel.PM += round(user_PM_Max/20)
            if User_actuel.PM > user_PM_Max :
                User_actuel.PM = user_PM_Max

        if Clic_clac_zap == True :
            Brûlure = False
            Poison = False
            Sommeil = False
            Paralysie = False
            Confusion = False


        if User_actuel.Vitesse >= monstre_actuel.Vitesse :

            # Code tour du user
            if Brûlure == True :
                print("Avant brulure : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/20))
                print("Après brulure : {0}".format(user_PV))

            elif Poison == True :
                print("Avant poison : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/20))
                print("Après poison : {0}".format(user_PV))

            elif Confusion == True :
                print("Avant confusion : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/5))
                print("Après confusion : {0}".format(user_PV))

            
            if Sommeil == False and Paralysie == False and user_PV > 0 :

                print(User_actuel.Attaque)

                action = input("Attaque/Compétence/Objet : ")

                if action == "Attaque" :
                    
                    monstre_PV -= Attaque_normal_user(User_actuel.Attaque, monstre_actuel.Défense)
                    print("PV du monstre : {0}".format(monstre_PV))

                elif action == "Compétence" :
                    
                    liste_compétences_apprises = print_compétences(User_actuel.id)
                    for i in liste_compétences_apprises :
                        print (i)
                    
                    nom_compétence = input("Quelle compétence voulez vous utiliser ? : ")

                    for i in liste_compétences_apprises :

                        if i.nom == nom_compétence :

                            if User_actuel.PM > i.PM_Utilisé : 

                                if i.Magique_Physique == "Physique" :
                                    données = compétence_physique(User_actuel, monstre_actuel, i, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Confusion_ennemi = données[3]
                                    Sommeil_ennemi = données[4]
                                    Poison_ennemi = données[5]
                                    Paralysie_ennemi = données[6]
                                    Brûlure_ennemi = données[7]
                                    Count_Brûlure_ennemi = données[8]
                                    Count_Confusion_ennemi = données[9]
                                    Count_Sommeil_ennemi = données[10]
                                    Count_Poison_ennemi = données[11]
                                    Count_Paralysie_ennemi = données[12]

                                elif i.Magique_Physique == "Magique" :
                                    données = compétence_magique(User_actuel, monstre_actuel, i, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Aura_de_peur, Psychocanalisation)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Confusion_ennemi = données[3]
                                    Sommeil_ennemi = données[4]
                                    Poison_ennemi = données[5]
                                    Paralysie_ennemi = données[6]
                                    Brûlure_ennemi = données[7]
                                    Count_Brûlure_ennemi = données[8]
                                    Count_Confusion_ennemi = données[9]
                                    Count_Sommeil_ennemi = données[10]
                                    Count_Poison_ennemi = données[11]
                                    Count_Paralysie_ennemi = données[12]

                                    

                                else :
                                    données = compétence_sans_dommages(user_PV_Max, i)
                                    user_PV += données[0]
                                    User_actuel.PM -= données[1]
                                    print(User_actuel.PM)
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Boost_Esquive = données[2]
                                    Count_Boost_Esquive = données[3]
                                    Aura_de_peur = données[4]
                                    Count_Aura_de_peur = données[5]
                                    Souffle_du_sage = données[6]
                                    Count_Souffle_du_sage = données[7]
                                    Psychocanalisation = données[8]
                                    Count_Psychocanalisation = données[9]
                                    Clic_clac_zap = données[10]
                                    Count_Clic_clac_zap = données[11]
                                    Grâce_de_la_Déesse = données[12]
                                    Count_Grâce_de_la_Déesse = données[13]
                                    Cercle_du_carnage = données[14]
                                    Count_Cercle_du_carnage = données[15]
                                    Poison_ennemi = données[16]
                                    Count_Poison_ennemi = données[17]
                                    Confusion_ennemi = données[18]
                                    Count_Confusion_ennemi = données[19]
                                    Brûlure_ennemi = données[20]
                                    Count_Brûlure_ennemi = données[21]
                                    Sommeil_ennemi = données[22]
                                    Count_Sommeil_ennemi = données[23]
                                    Décuplo = données[24]
                                    Count_Décuplo = données[25]
                                    Protection = données[26]
                                    Count_Protection = données[27]
                                    Hâte = données[28]
                                    Count_Hâte = données[29]

                            else :

                                print("PM insuffisants")

                elif action == "Objet" :

                    liste_objets_inventaire = print_objets(User_actuel.id)
                    for i in liste_objets_inventaire :
                        print (i)

                    nom_objet = input("Quelle objet voulez vous utiliser ? : ")

                    for i in liste_objets_inventaire :
        
                        if i.nom == nom_objet :     
                            données = utilisation_objet(i)

                            user_PV += données[0]
                            if user_PV > user_PV_Max :
                                user_PV = user_PV_Max

                            User_actuel.PM += données[1]
                            if User_actuel.PM > user_PM_Max :
                                User_actuel.PM = user_PM_Max

                            Décuplo = données[2]
                            Count_Décuplo = données[3]
                            Hâte = données[4]
                            Count_Hâte = données[5]
                            Protection = données[6]
                            Count_Protection = données[7]

                            print(user_PV)
                            print(User_actuel.PM)
            
            elif Sommeil == True :
                print("Gros dodo")

            elif Paralysie == True :
                print("Paralysé ne peut pas attaquer")

            # Code tour du monstre
            if Brûlure_ennemi == True :
                print("Avant brulure : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/20))
                print("Après brulure : {0}".format(monstre_PV))

            elif Poison_ennemi == True :
                print("Avant poison : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/20))
                print("Après poison : {0}".format(monstre_PV))

            elif Confusion_ennemi == True :
                print("Avant confusion : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/5))
                print("Après confusion : {0}".format(monstre_PV))


            if Sommeil_ennemi == False and Paralysie_ennemi == False and monstre_PV > 0 :
                degats_monstre = attaque_monstre(monstre_actuel, User_actuel)

                if Boost_Esquive == True :
                    randomint = randrange(1,101)
                    if randomint <= User_actuel.Esquive + 15 :
                        degats_monstre = 0

                else :
                    randomint = randrange(1,101)
                    if randomint <= User_actuel.Esquive :
                        degats_monstre = 0

                if Grâce_de_la_Déesse == True and degats_monstre >= user_PV:
                    user_PV = user_PM_Max
                    print("Grâce de la déesse activé")
                else :
                    user_PV -= degats_monstre

            elif Sommeil_ennemi == True :
                print("Gros dodo du monstre")
                
            elif Paralysie_ennemi == True :
                print("Paralysé le monstre ne peut pas attaquer")



        
        else :

            # Code tour du monstre
            if Brûlure_ennemi == True :
                print("Avant brulure : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/20))
                print("Après brulure : {0}".format(monstre_PV))

            elif Poison_ennemi == True :
                print("Avant poison : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/20))
                print("Après poison : {0}".format(monstre_PV))

            elif Confusion_ennemi == True :
                print("Avant confusion : {0}".format(monstre_PV))
                monstre_PV -= round((monstre_PV_Max/5))
                print("Après confusion : {0}".format(monstre_PV))


            if Sommeil_ennemi == False and Paralysie_ennemi == False and monstre_PV > 0 :
                degats_monstre = attaque_monstre(monstre_actuel, User_actuel)

                if Boost_Esquive == True :
                    randomint = randrange(1,101)
                    if randomint <= User_actuel.Esquive + 15 :
                        degats_monstre = 0

                else :
                    randomint = randrange(1,101)
                    if randomint <= User_actuel.Esquive :
                        degats_monstre = 0

                if Grâce_de_la_Déesse == True and degats_monstre >= user_PV:
                    user_PV = user_PM_Max
                    print("Grâce de la déesse activé")
                else :
                    user_PV -= degats_monstre

            elif Sommeil_ennemi == True :
                print("Gros dodo du monstre")
                
            elif Paralysie_ennemi == True :
                print("Paralysé le monstre ne peut pas attaquer")


            if Brûlure == True :
                print("Avant brulure : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/20))
                print("Après brulure : {0}".format(user_PV))

            elif Poison == True :
                print("Avant poison : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/20))
                print("Après poison : {0}".format(user_PV))

            elif Confusion == True :
                print("Avant confusion : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/5))
                print("Après confusion : {0}".format(user_PV))

            if Sommeil == False and Paralysie == False and user_PV > 0 :
                action = input("Attaque/Compétence/Objet : ")

                if action == "Attaque" :
                    
                    monstre_PV -= Attaque_normal_user(User_actuel.Attaque, monstre_actuel.Défense)
                    print("PV du monstre : {0}".format(monstre_PV))

                elif action == "Compétence" :
                    
                    liste_compétences_apprises = print_compétences(User_actuel.id)
                    for i in liste_compétences_apprises :
                        print (i)
                    
                    nom_compétence = input("Quelle compétence voulez vous utiliser ? : ")

                    for i in liste_compétences_apprises :

                        if i.nom == nom_compétence :

                            if User_actuel.PM > i.PM_Utilisé : 

                                if i.Magique_Physique == "Physique" :
                                    données = compétence_physique(User_actuel, monstre_actuel, i, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Confusion_ennemi = données[3]
                                    Sommeil_ennemi = données[4]
                                    Poison_ennemi = données[5]
                                    Paralysie_ennemi = données[6]
                                    Brûlure_ennemi = données[7]
                                    Count_Brûlure_ennemi = données[8]
                                    Count_Confusion_ennemi = données[9]
                                    Count_Sommeil_ennemi = données[10]
                                    Count_Poison_ennemi = données[11]
                                    Count_Paralysie_ennemi = données[12]

                                elif i.Magique_Physique == "Magique" :
                                    données = compétence_magique(User_actuel, monstre_actuel, i, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Aura_de_peur, Psychocanalisation)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Confusion_ennemi = données[3]
                                    Sommeil_ennemi = données[4]
                                    Poison_ennemi = données[5]
                                    Paralysie_ennemi = données[6]
                                    Brûlure_ennemi = données[7]
                                    Count_Brûlure_ennemi = données[8]
                                    Count_Confusion_ennemi = données[9]
                                    Count_Sommeil_ennemi = données[10]
                                    Count_Poison_ennemi = données[11]
                                    Count_Paralysie_ennemi = données[12]

                                else :
                                    données = compétence_sans_dommages(user_PV_Max, i)
                                    user_PV += données[0]
                                    User_actuel.PM -= données[1]
                                    print(User_actuel.PM)
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                    Boost_Esquive = données[2]
                                    Count_Boost_Esquive = données[3]
                                    Aura_de_peur = données[4]
                                    Count_Aura_de_peur = données[5]
                                    Souffle_du_sage = données[6]
                                    Count_Souffle_du_sage = données[7]
                                    Psychocanalisation = données[8]
                                    Count_Psychocanalisation = données[9]
                                    Clic_clac_zap = données[10]
                                    Count_Clic_clac_zap = données[11]
                                    Grâce_de_la_Déesse = données[12]
                                    Count_Grâce_de_la_Déesse = données[13]
                                    Cercle_du_carnage = données[14]
                                    Count_Cercle_du_carnage = données[15]
                                    Poison_ennemi = données[16]
                                    Count_Poison_ennemi = données[17]
                                    Confusion_ennemi = données[18]
                                    Count_Confusion_ennemi = données[19]
                                    Brûlure_ennemi = données[20]
                                    Count_Brûlure_ennemi = données[21]
                                    Sommeil_ennemi = données[22]
                                    Count_Sommeil_ennemi = données[23]
                                    Décuplo = données[24]
                                    Count_Décuplo = données[25]
                                    Protection = données[26]
                                    Count_Protection = données[27]
                                    Hâte = données[28]
                                    Count_Hâte = données[29]


                            else :

                                print("PM insuffisants")

                elif action == "Objet" :

                    liste_objets_inventaire = print_objets(User_actuel.id)
                    for i in liste_objets_inventaire :
                        print (i)

                    nom_objet = input("Quelle objet voulez vous utiliser ? : ")

                    for i in liste_objets_inventaire :
        
                        if i.nom == nom_objet :     
                            données = utilisation_objet(i)

                            user_PV += données[0]
                            if user_PV > user_PV_Max :
                                user_PV = user_PV_Max

                            User_actuel.PM += données[1]
                            if User_actuel.PM > user_PM_Max :
                                User_actuel.PM = user_PM_Max
                            
                            Décuplo = données[2]
                            Count_Décuplo = données[3]
                            Hâte = données[4]
                            Count_Hâte = données[5]
                            Protection = données[6]
                            Count_Protection = données[7]

                            if données[8] == False :
                                Brûlure = False
                                Confusion = False
                                Sommeil = False
                                Poison = False
                                Paralysie = False

                                Count_Brûlure = 0
                                Count_Confusion = 0
                                Count_Sommeil = 0
                                Count_Poison = 0
                                Count_Paralysie = 0

                            print(user_PV)
                            print(User_actuel.PM)

            elif Sommeil == True :
                print("Gros dodo")

            elif Paralysie == True :
                print("Paralysé ne peut pas attaquer")
                  


        # Décompte des tours des effets
        if Count_Brûlure > 0 :
            Count_Brûlure -= 1
            if Count_Brûlure == 0 :
                Brûlure = False
        if Count_Confusion > 0 :
            Count_Confusion -= 1
            if Count_Confusion == 0 :
                Confusion = False
        if Count_Sommeil > 0 :
            Count_Sommeil -= 1
            if Count_Sommeil == 0 :
                Sommeil = False
        if Count_Poison > 0 :
            Count_Poison -= 1
            if Count_Poison == 0 :            
                Poison = False
        if Count_Paralysie > 0 :
            Count_Paralysie -= 1
            if Count_Paralysie == 0 :
                Paralysie = False

        if Count_Brûlure_ennemi > 0 :
            Count_Brûlure_ennemi -= 1
            if Count_Brûlure_ennemi == 0 :
                Brûlure_ennemi = False
        if Count_Confusion_ennemi > 0 :
            Count_Confusion_ennemi -= 1
            if Count_Confusion_ennemi == 0 :
                Confusion_ennemi = False
        if Count_Sommeil_ennemi > 0 :
            Count_Sommeil_ennemi -= 1
            if Count_Sommeil_ennemi == 0 :
                Sommeil_ennemi = False
        if Count_Poison_ennemi > 0 :
            Count_Poison_ennemi -= 1
            if Count_Poison_ennemi == 0 :
                Poison_ennemi = False
        if Count_Paralysie_ennemi > 0 :
            Count_Paralysie_ennemi -= 1
            if Count_Paralysie_ennemi == 0 :
                Paralysie_ennemi = False

        if Count_Boost_Esquive > 0 :
            Count_Boost_Esquive -= 1
            if Count_Boost_Esquive == 0 :
                Boost_Esquive = False
        if Count_Aura_de_peur > 0 :
            Count_Aura_de_peur -= 1
            if Count_Aura_de_peur == 0 :
                Aura_de_peur = False
        if Count_Souffle_du_sage > 0 :
            Count_Souffle_du_sage -= 1
            if Count_Souffle_du_sage == 0 :
                Souffle_du_sage = False
        if Count_Psychocanalisation > 0 :
            Count_Psychocanalisation -= 1
            if Count_Psychocanalisation == 0 :
                Psychocanalisation = False
        if Count_Clic_clac_zap > 0 :
            Count_Clic_clac_zap -= 1
            if Count_Clic_clac_zap == 0 :
                Clic_clac_zap = False
        if Count_Grâce_de_la_Déesse > 0 :
            Count_Grâce_de_la_Déesse -= 1
            if Count_Grâce_de_la_Déesse == 0 :
                Grâce_de_la_Déesse = False
        if Count_Cercle_du_carnage > 0 :
            Count_Cercle_du_carnage -= 1
            if Count_Cercle_du_carnage == 0 :
                Cercle_du_carnage = False
        if Count_Décuplo > 0 :
            Count_Décuplo -= 1
            if Count_Décuplo == 0 :
                Décuplo = False
        if Count_Protection > 0 :
            Count_Protection -= 1
            if Count_Protection == 0 :
                Protection = False
        if Count_Hâte > 0 :
            Count_Hâte -= 1
            if Count_Hâte == 0 :
                Hâte = False










    if user_PV > 0 :
        print ("fin du combat PV monstre = {0}".format(monstre_PV))

        loot(User_actuel, monstre_id)
        gain_xp_gold(User_actuel, monstre_id)

        combat(user, 1)



    else :
        print ("fin du combat PV user = {0}".format(user_PV))

        user_cursor2=conn.cursor()
        user2 = ("SELECT * FROM {0} WHERE id = {1}".format("Users", User_actuel.id))
        user_cursor2.execute(user2)
        data_user2 = user_cursor2.fetchone()


        User_actuel = User (data_user2[0], data_user2[1], data_user2[2], data_user2[3], data_user2[4], data_user2[5], data_user2[6], data_user2[7], data_user2[8], data_user2[9], data_user2[10], data_user2[11], data_user2[12], data_user2[13], data_user2[14], data_user2[15], data_user2[16])
        
        user_PV_Max = User_actuel.PV
        user_PM_Max = User_actuel.PM
        user_Attaque_base = User_actuel.Attaque
        user_Défense_base = User_actuel.Défense
        user_Vitesse_base = User_actuel.Vitesse
        user_PV = User_actuel.PV
        vérif_equipement = False

        menu(user)
