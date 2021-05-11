# -*- coding: utf-8 -*-

import pymysql
from class_monstre import Monstres
from class_user import User
from class_compétence import Competence
from class_arme import Arme
from class_armure import Armure
from class_objet import Objet
from random import randrange



# def connection(valeur):
conn = pymysql.connect("localhost", "root", "", "rpjam" )


# Création des curseurs
user_cursor=conn.cursor()
monstres_cursor=conn.cursor()
compétence_cursor=conn.cursor()



# Récupère les données du User
Users = ("SELECT * FROM {0}".format("Users"))
user_cursor.execute(Users)

# Récupère les données des Monstres
all_monstres = ("SELECT * FROM {0}".format("Monstres"))
monstres_cursor.execute(all_monstres)

# Récupère les données des Compétences
compétences = ("SELECT * FROM {0}".format("compétences"))
compétence_cursor.execute(compétences)


# sqltest = ("UPDATE Users SET Golds = 50150 WHERE id=1;")
# a.execute(sqltest)
# conn.commit()


# Stockage des données dans des variables
data_user = user_cursor.fetchone()
data_monstres = monstres_cursor.fetchall()
data_compétences = compétence_cursor.fetchall()


# Initialisation des listes
liste_monstre = []
liste_compétences = []



print (data_user)

User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15])


for i in data_monstres :

    new_monstre = Monstres (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
    liste_monstre.append(new_monstre)


for i in data_compétences :
    
    new_compétences = Competence (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
    liste_compétences.append(new_compétences)


def monstre(id) :

    return (liste_monstre[id-1])
    




def Attaque_normal_user(attaque_user, défense_monstre) :

    return (attaque_user - défense_monstre)



def print_compétences(id_user) :


    liste_compétences_apprises = []
    compétence_apprises_cursor=conn.cursor()


    compétences_apprises = ("SELECT id_compétences FROM {0} WHERE {1} = {2}".format("compétences_apprises", "id_Users", id_user))
    compétence_apprises_cursor.execute(compétences_apprises)


    data_compétences_apprises = compétence_apprises_cursor.fetchall()

    for i in data_compétences_apprises :
    
        for j in i :

            liste_compétences_apprises.append(liste_compétences[j])


    return (liste_compétences_apprises)


def compétence_physique(user, monstre, compétence) :

    # Faiblesses du monstre
    faiblesse_cursor=conn.cursor()
    faiblesse = ("SELECT {0} FROM {1} WHERE {2} = {3}".format("id_type_faiblesse", "faiblesse", "id_monstre", monstre.id))
    faiblesse_cursor.execute(faiblesse)
    data_faiblesse = faiblesse_cursor.fetchall()

    liste_faiblesse = []

    for i in data_faiblesse :
        
        liste_faiblesse.append(i[0])


    # Résistances du monstre
    résistance_cursor=conn.cursor()
    résistance = ("SELECT {0} FROM {1} WHERE {2} = {3}".format("id_type_résisté", "résistance", "id_monstre", monstre.id))
    résistance_cursor.execute(résistance)
    data_résistance = résistance_cursor.fetchall()

    liste_résistance = []

    for i in data_résistance :
        
        liste_résistance.append(i[0])


    # dégats
    degats = (user.Attaque - monstre.Défense) + compétence.Puissance

    # Vérification si la compétence est efficace sur le monstre
    if monstre.id_Famille == compétence.id_Famille_Efficace :
        degats *= 1.5

    # Vérification si le monstre est faible au type de la compétence
    if compétence.id_type in liste_faiblesse :
        degats *= 1.5

    # Vérification si le monstre résiste au type de la compétence
    if compétence.id_type in liste_résistance :
        degats /= 1.5

    degats = round(degats)

    if degats < 0 :
        degats = 0

    return (degats, compétence.PM_Utilisé)


def compétence_magique(user, monstre, compétence) :

    # Faiblesses du monstre
    faiblesse_cursor=conn.cursor()
    faiblesse = ("SELECT {0} FROM {1} WHERE {2} = {3}".format("id_type_faiblesse", "faiblesse", "id_monstre", monstre.id))
    faiblesse_cursor.execute(faiblesse)
    data_faiblesse = faiblesse_cursor.fetchall()

    liste_faiblesse = []

    for i in data_faiblesse :
        
        liste_faiblesse.append(i[0])


    # Résistances du monstre
    résistance_cursor=conn.cursor()
    résistance = ("SELECT {0} FROM {1} WHERE {2} = {3}".format("id_type_résisté", "résistance", "id_monstre", monstre.id))
    résistance_cursor.execute(résistance)
    data_résistance = résistance_cursor.fetchall()

    liste_résistance = []

    for i in data_résistance :
        
        liste_résistance.append(i[0])


    # degats
    degats = (user.Puissance_Magique - monstre.Résistance_Magique) + compétence.Puissance * 2

    # Vérification si la compétence est efficace sur le monstre
    if monstre.id_Famille == compétence.id_Famille_Efficace :
        degats *= 1.5

    # Vérification si le monstre est faible au type de la compétence
    if compétence.id_type in liste_faiblesse :
        degats *= 1.5

    # Vérification si le monstre résiste au type de la compétence
    if compétence.id_type in liste_résistance :
        degats /= 1.5

    degats = round(degats)

    if degats < 0 :
        degats = 0

    return (degats, compétence.PM_Utilisé)



def compétence_sans_dommages(compétence) :

    print("autre")



def loot(monstre_id) :

    # Loots possible du monstre
    loot_cursor=conn.cursor()
    loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("loot", "id_monstre", monstre_id))
    loot_cursor.execute(loot)
    data_loot = loot_cursor.fetchall()

    liste_loot = []
    new_liste_loot = []


    number_random = randrange(0, 100)
    number = 0


    for i in data_loot :
        
        liste_loot.append(i)


    for j in liste_loot :

        if j[2] == "arme" :

            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("arme", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Arme (i[0], i[1], i[2], i[3], i[4], i[5])
                new_liste_loot.append(new_loot)


            if number_random > number and number_random < (number + j[4]):

                print("drop d'une arme")

                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire_armes", "id", j[3], "id_Users", User_actuel.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armes"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire_armes VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire_armes", "id", j[3], "id_Users", User_actuel.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            
            number += j[4]

        elif j[2] == "armure" :
    
            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("armure", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Armure (i[0], i[1], i[2], i[3], i[4], i[5])
                new_liste_loot.append(new_loot)


            if number_random > number and number_random < (number + j[4]):

                print("drop d'une armure")
    
                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire_armures", "id", j[3], "id_Users", User_actuel.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armures"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire_armures VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire_armures", "id", j[3], "id_Users", User_actuel.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            number += j[4]

        elif j[2] == "objet" :
        
            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("objet", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Objet (i[0], i[1], i[2], i[3])
                new_liste_loot.append(new_loot)

            
            if number_random > number and number_random < (number + j[4]):

                print("drop d'un objet")
        
                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire", "id", j[3], "id_Users", User_actuel.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire", "id", j[3], "id_Users", User_actuel.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            number += j[4]



    


    #print(new_liste_loot)



def gain_xp_gold(monstre_id) :

    monstre_actuel = monstre(monstre_id)

    update_golds_cursor=conn.cursor()
    update_golds_query = ("UPDATE Users SET Golds = Golds + {0} WHERE id = {1}".format(monstre_actuel.Golds_Give, User_actuel.id))
    update_golds_cursor.execute(update_golds_query)
    conn.commit()


    update_xp_cursor=conn.cursor()
    update_xp_query = ("UPDATE Users SET XP = XP + {0} WHERE id = {1}".format(monstre_actuel.XP_Give, User_actuel.id))
    update_xp_cursor.execute(update_xp_query)
    conn.commit()


    vérification_level_up_cursor=conn.cursor()
    vérification_level_up_query = ("SELECT XP_For_Next_LV, XP FROM Users WHERE id = {0}".format(User_actuel.id))
    vérification_level_up_cursor.execute(vérification_level_up_query)
    data_vérification_level_up = vérification_level_up_cursor.fetchone()

    

    if data_vérification_level_up[1] > data_vérification_level_up[0] :

        level_up(User_actuel)



def level_up(user) :

    grosse_stat1 = randrange(3,5)
    grosse_stat2 = randrange(3,5)
    moyenne_stat1 = randrange(2,4)
    moyenne_stat2 = randrange(2,4)
    moyenne_stat3 = randrange(2,4)
    petite_stat1 = randrange(1,3)
    petite_stat2 = randrange(1,3)

    if user.classe == "Guerrier" :

        update_stats_cursor=conn.cursor()
        update_stats_query = ("UPDATE Users SET LV = LV + 1, PV = PV + {0}, PM = PM + {1}, Attaque = Attaque + {2}, Puissance_Magique = Puissance_Magique + {3}, Défense = Défense + {4}, Résistance_Magique = Résistance_Magique + {5}, Vitesse = Vitesse + {6}, XP_For_Next_LV = XP_For_Next_LV * 1.5, XP = 0, points_de_compétences = points_de_compétences + 3 WHERE id = {7}"
                                .format(grosse_stat1, moyenne_stat1, grosse_stat2, petite_stat1, moyenne_stat2, petite_stat2, moyenne_stat3, User_actuel.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()

    
    elif user.classe == "Mage" :

        update_stats_cursor=conn.cursor()
        update_stats_query = ("UPDATE Users SET LV = LV + 1, PV = PV + {0}, PM = PM + {1}, Attaque = Attaque + {2}, Puissance_Magique = Puissance_Magique + {3}, Défense = Défense + {4}, Résistance_Magique = Résistance_Magique + {5}, Vitesse = Vitesse + {6}, XP_For_Next_LV = XP_For_Next_LV * 1.5, XP = 0, points_de_compétences = points_de_compétences + 3 WHERE id = {7}"
                                .format(moyenne_stat1, grosse_stat1, petite_stat1, grosse_stat2, petite_stat2, moyenne_stat2, moyenne_stat3, User_actuel.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()


    elif user.classe == "Assassin" :

        update_stats_cursor=conn.cursor()
        update_stats_query = ("UPDATE Users SET LV = LV + 1, PV = PV + {0}, PM = PM + {1}, Attaque = Attaque + {2}, Puissance_Magique = Puissance_Magique + {3}, Défense = Défense + {4}, Résistance_Magique = Résistance_Magique + {5}, Vitesse = Vitesse + {6}, XP_For_Next_LV = XP_For_Next_LV * 1.5, XP = 0, points_de_compétences = points_de_compétences + 3 WHERE id = {7}"
                                .format(moyenne_stat1, moyenne_stat2, grosse_stat1, moyenne_stat3, petite_stat1, petite_stat2, grosse_stat2, User_actuel.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()




def combat(monstre_id) :

    monstre_actuel = monstre(monstre_id)

    #monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV
    #user_PV_Max = User_actuel.PV
    user_PV = User_actuel.PV



    print("Début du combat contre un {0}".format(monstre_actuel.nom))
    print("PV du monstre : {0}".format(monstre_PV))



    while monstre_PV > 0 and user_PV > 0:
    
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
                            données = compétence_physique(User_actuel, monstre_actuel, i)
                            monstre_PV -= données[0]
                            User_actuel.PM -= données[1]

                        elif i.Magique_Physique == "Magique" :
                            données = compétence_magique(User_actuel, monstre_actuel, i)
                            monstre_PV -= données[0]
                            User_actuel.PM -= données[1]

                        else :
                            compétence_sans_dommages(i)

                    else :

                        print("PM insuffisants")


    if user_PV > 0 :
        print ("fin du combat PV monstre = {0}".format(monstre_PV))

        loot(monstre_id)
        gain_xp_gold(monstre_id)



    else :
        print ("fin du combat PV user = {0}".format(user_PV))

combat(1)