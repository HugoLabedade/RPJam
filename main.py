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
objets_cursor=conn.cursor()
arme_cursor=conn.cursor()
armure_cursor=conn.cursor()



# Récupère les données du User
Users = ("SELECT * FROM {0}".format("Users"))
user_cursor.execute(Users)

# Récupère les données des Monstres
all_monstres = ("SELECT * FROM {0}".format("Monstres"))
monstres_cursor.execute(all_monstres)

# Récupère les données des Compétences
compétences = ("SELECT * FROM {0}".format("compétences"))
compétence_cursor.execute(compétences)

# Récupère les données des Objets
objets = ("SELECT * FROM {0}".format("objet"))
objets_cursor.execute(objets)

# Récupère les données des Armes
armes = ("SELECT * FROM {0}".format("arme"))
arme_cursor.execute(armes)

# Récupère les données des Armures
armures = ("SELECT * FROM {0}".format("armure"))
armure_cursor.execute(armures)


# Stockage des données dans des variables
data_user = user_cursor.fetchone()
data_monstres = monstres_cursor.fetchall()
data_compétences = compétence_cursor.fetchall()
data_objets = objets_cursor.fetchall()
data_armes = arme_cursor.fetchall()
data_armures = armure_cursor.fetchall()


# Initialisation des listes
liste_monstre = []
liste_compétences = []
liste_objets = []
liste_armes = []
liste_armures = []



print (data_user)

User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15])



Brûlure = False
Confusion = False
Sommeil = False
Poison = False
Paralysie = False

Brûlure_ennemi = False
Confusion_ennemi = False
Sommeil_ennemi = False
Poison_ennemi = False
Paralysie_ennemi = False


Boost_Esquive = False
Aura_de_peur = False
Souffle_du_sage = False
Psychocanalisation = False
Clic_clac_zap = False
Grâce_de_la_Déesse = False
Cercle_du_carnage = False
Décuplo = False
Protection = False
Hâte = False

Count_Brûlure = 0
Count_Confusion = 0
Count_Sommeil = 0
Count_Poison = 0
Count_Paralysie = 0

Count_Brûlure_ennemi = 0
Count_Confusion_ennemi = 0
Count_Sommeil_ennemi = 0
Count_Poison_ennemi = 0
Count_Paralysie_ennemi = 0

Count_Boost_Esquive = 0
Count_Aura_de_peur = 0
Count_Souffle_du_sage = 0
Count_Psychocanalisation = 0
Count_Clic_clac_zap = 0
Count_Grâce_de_la_Déesse = 0
Count_Cercle_du_carnage = 0
Count_Décuplo = 0
Count_Protection = 0
Count_Hâte = 0



for i in data_monstres :

    new_monstre = Monstres (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
    liste_monstre.append(new_monstre)


for i in data_compétences :
    
    new_compétences = Competence (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
    liste_compétences.append(new_compétences)


for i in data_objets :
    
    new_objet = Objet (i[0], i[1], i[2], i[3])
    liste_objets.append(new_objet)


for i in data_armes :
    
    new_arme = Objet (i[0], i[1], i[2], i[3])
    liste_armes.append(new_arme)


for i in data_armures :
    
    new_armure = Objet (i[0], i[1], i[2], i[3])
    liste_armures.append(new_armure)


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

            liste_compétences_apprises.append(liste_compétences[j-1])


    return (liste_compétences_apprises)


def compétence_physique(user, monstre, compétence, chances_crit) :

    heal = 0

    if compétence.id_effet is not None :
        randomint = randrange(1, 101)
        if randomint <= compétence.Pourcentage_Effet :
            if compétence.id_effet == 1 :
                global Brûlure_ennemi
                Brûlure_ennemi = True
            elif compétence.id_effet == 2 :
                global Confusion_ennemi
                Confusion_ennemi = True
            elif compétence.id_effet == 3 :
                global Sommeil_ennemi
                Sommeil_ennemi = True
            elif compétence.id_effet == 4 :
                global Poison_ennemi
                Poison_ennemi = True
            elif compétence.id_effet == 5 :
                global Paralysie_ennemi
                Paralysie_ennemi = True


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

    if compétence.Autres == 1 :
        données = compétence_avec_effet_supp(compétence, degats, chances_crit)

        degats = données[1]
        heal = données[0]
        chances_crit = données[2]

    return (degats, compétence.PM_Utilisé, heal, chances_crit)


def compétence_magique(user, monstre, compétence, chances_crit) :

    heal = 0

    if compétence.id_effet is not None :
        randomint = randrange(1, 101)
        if randomint <= compétence.Pourcentage_Effet :
            if compétence.id_effet == 1 :
                global Brûlure_ennemi
                Brûlure_ennemi = True
            elif compétence.id_effet == 2 :
                global Confusion_ennemi
                Confusion_ennemi = True
            elif compétence.id_effet == 3 :
                global Sommeil_ennemi
                Sommeil_ennemi = True
            elif compétence.id_effet == 4 :
                global Poison_ennemi
                Poison_ennemi = True
            elif compétence.id_effet == 5 :
                global Paralysie_ennemi
                Paralysie_ennemi = True

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

    if compétence.Autres == 1 :
        données = compétence_avec_effet_supp(compétence, degats, chances_crit)

        degats = données[1]
        heal = données[0]
        chances_crit = données[2]

    if Aura_de_peur == True :
        degats = round(degats * 2)

    if Psychocanalisation == True :
        degats = round(degats * 2.5)

    return (degats, compétence.PM_Utilisé, heal, chances_crit)


def compétence_sans_dommages(max_pv_user, compétence) :

    PV_heal = 0
    print("autre")

    if compétence.id == 8 or compétence.id == 9 or compétence.id == 10 :
        PV_heal = heal(max_pv_user, compétence)


    elif compétence.id == 15 :
        global Boost_Esquive
        Boost_Esquive = True
        global Count_Boost_Esquive
        Count_Boost_Esquive = 3

    elif compétence.id == 18 :
        global Aura_de_peur
        Aura_de_peur = True
        global Count_Aura_de_peur
        Count_Aura_de_peur = 4

    elif compétence.id == 19 :
        global Souffle_du_sage
        Souffle_du_sage = True
        global Count_Souffle_du_sage
        Count_Souffle_du_sage = 10

    elif compétence.id == 20 :
        global Psychocanalisation
        Psychocanalisation = True
        global Count_Psychocanalisation
        Count_Psychocanalisation = 4

    elif compétence.id == 24 :
        global Clic_clac_zap
        Clic_clac_zap = True
        global Count_Clic_clac_zap
        Count_Clic_clac_zap = 10

    elif compétence.id == 25 :
        global Grâce_de_la_Déesse
        Grâce_de_la_Déesse = True
        global Count_Grâce_de_la_Déesse
        Count_Grâce_de_la_Déesse = 15
    
    elif compétence.id == 30 :
        global Cercle_du_carnage
        Cercle_du_carnage = True
        global Count_Cercle_du_carnage
        Count_Cercle_du_carnage = 8

    elif compétence.id == 44 :
        global Poison_ennemi
        Poison_ennemi = True
        global Count_Poison_ennemi
        Count_Poison_ennemi = 3

    elif compétence.id == 45 :
        global Confusion_ennemi
        Confusion_ennemi = True
        global Count_Confusion_ennemi
        Count_Confusion_ennemi = 3

    elif compétence.id == 46 :
        global Brûlure_ennemi
        global Count_Brûlure_ennemi

    elif compétence.id == 47 :
        global Sommeil_ennemi
        Sommeil_ennemi = True
        global Count_Sommeil_ennemi
        Count_Sommeil_ennemi = 3

    elif compétence.id == 57 :
        global Décuplo
        Décuplo = True
        global Count_Décuplo
        Count_Décuplo = 5

    elif compétence.id == 58 :
        global Protection
        Protection = True
        global Count_Protection
        Count_Protection = 5

    elif compétence.id == 59 :
        global Hâte
        Hâte = True
        global Count_Hâte
        Count_Hâte = 15

        
    return(PV_heal, compétence.PM_Utilisé)


def compétence_avec_effet_supp(compétence, degats, chances_crit) :


    if compétence.id == 4 :
        heal = round(degats/5)

    if compétence.id == 12 :
        if Confusion_ennemi == True or Sommeil_ennemi == True :
            randomint = randrange(1,5)
            if randomint == 1 :
                degats*=6

    if compétence.id == 14 :
        if Poison_ennemi == True or Paralysie_ennemi == True :
            randomint = randrange(1,5)
            if randomint == 1 :
                degats*=6

    if compétence.id == 28 :
        chances_crit *= 3


    return(heal, degats, chances_crit)


def print_objets(id_user) :
    

    liste_objets_inventaire = []
    objets_inventaire_cursor=conn.cursor()


    objets_inventaire = ("SELECT id_item FROM {0} WHERE {1} = {2}".format("inventaire", "id_Users", id_user))
    objets_inventaire_cursor.execute(objets_inventaire)


    data_objets_inventaire = objets_inventaire_cursor.fetchall()

    for i in data_objets_inventaire :
    
        for j in i :

            liste_objets_inventaire.append(liste_objets[j-1])


    return (liste_objets_inventaire)


def utilisation_objet(objet) :

    heal = 0
    heal_PM = 0


    if objet.id == 1 :
        heal = 40
    
    elif objet.id == 2 :
        heal = 80

    elif objet.id == 3 :
        heal = 120

    elif objet.id == 4 :
        heal = 200

    elif objet.id == 5 :
        global Brûlure
        Brûlure = False
        global Confusion
        Confusion = False
        global Sommeil
        Sommeil = False
        global Poison
        Poison = False
        global Paralysie
        Paralysie = False

        global Count_Brûlure
        Count_Brûlure = 0
        global Count_Confusion
        Count_Confusion = 0
        global Count_Sommeil
        Count_Sommeil = 0
        global Count_Poison
        Count_Poison = 0
        global Count_Paralysie
        Count_Paralysie = 0
        
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
        global Décuplo
        Décuplo = True
        global Count_Décuplo
        Count_Décuplo = 5

    elif objet.id == 11 :
        global Hâte
        Hâte = True
        global Count_Hâte
        Count_Hâte = 15

    elif objet.id == 12 :
        global Protection
        Protection = True
        global Count_Protection
        Count_Protection = 5

    
    return(heal, heal_PM)


def heal(max_pv_user, compétence) :

    if compétence.id == 8 :
        return round(max_pv_user/4)

    elif compétence.id == 9 :
        return round(max_pv_user/2)

    elif compétence.id == 10 :
        return max_pv_user

    else :
        return 0


def critique(degats, chances_crit) :
    randomint = randrange(1, 101) 
    if randomint <= chances_crit :
        degats *= 2

    return(degats)


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




def user_turn(monstre_id) :

    monstre_actuel = monstre(monstre_id)

    #monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV
    user_PV_Max = User_actuel.PV
    user_PM_Max = User_actuel.PM
    user_Attaque_base = User_actuel.Attaque
    user_Défense_base = User_actuel.Défense
    user_Vitesse_base = User_actuel.Vitesse
    user_PV = User_actuel.PV


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

        if Brûlure == True :
            print("Avant brulure : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après brulure : {0}".format(user_PV))

        elif Poison == True :
            print("Avant poison : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après poison : {0}".format(user_PV))

        elif Sommeil == True :
            #Attaque_monstre
            print("rien pour l'instant")
            
        elif Paralysie == True :
            #Attaque_monstre
            print("rien pour l'instant")

        elif Confusion == True :
            randomint = randrange(1,3)
            if randomint == 1 :

                # Dérouler normal du combat
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
                                    données = compétence_physique(User_actuel, monstre_actuel, i, chances_crit)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                elif i.Magique_Physique == "Magique" :
                                    données = compétence_magique(User_actuel, monstre_actuel, i, chances_crit)
                                    degats = critique(données[0], données[3])
                                    monstre_PV -= degats
                                    User_actuel.PM -= données[1]
                                    user_PV += données[2]
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                                else :
                                    données = compétence_sans_dommages(user_PV_Max, i)
                                    user_PV += données[0]
                                    User_actuel.PM -= données[1]
                                    print(User_actuel.PM)
                                    if user_PV > user_PV_Max :
                                        user_PV = user_PV_Max

                            else :

                                print("PM insuffisants")
            
            else : 
                print("Avant confusion : {0}".format(user_PV))
                user_PV -= round((user_PV_Max/10))
                print("Après confusion : {0}".format(user_PV))

        else :

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
                                données = compétence_physique(User_actuel, monstre_actuel, i, chances_crit)
                                degats = critique(données[0], données[3])
                                monstre_PV -= degats
                                User_actuel.PM -= données[1]
                                user_PV += données[2]
                                if user_PV > user_PV_Max :
                                    user_PV = user_PV_Max

                            elif i.Magique_Physique == "Magique" :
                                données = compétence_magique(User_actuel, monstre_actuel, i, chances_crit)
                                degats = critique(données[0], données[3])
                                monstre_PV -= degats
                                User_actuel.PM -= données[1]
                                user_PV += données[2]
                                if user_PV > user_PV_Max :
                                    user_PV = user_PV_Max

                            else :
                                données = compétence_sans_dommages(user_PV_Max, i)
                                user_PV += données[0]
                                User_actuel.PM -= données[1]
                                print(User_actuel.PM)
                                if user_PV > user_PV_Max :
                                    user_PV = user_PV_Max

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

                        print(user_PV)
                        print(User_actuel.PM)





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

        loot(monstre_id)
        gain_xp_gold(monstre_id)



    else :
        print ("fin du combat PV user = {0}".format(user_PV))








user_turn(3)





#Boost_Esquive = False # Encore à faire après l'attaque du monstre
#Grâce_de_la_Déesse = False # Encore à faire après l'attaque du monstre