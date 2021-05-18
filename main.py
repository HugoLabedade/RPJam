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
monstres_cursor=conn.cursor()
compétence_cursor=conn.cursor()
objets_cursor=conn.cursor()
arme_cursor=conn.cursor()
armure_cursor=conn.cursor()



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



User_actuel = ""


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
    
    new_arme = Arme (i[0], i[1], i[2], i[3], i[4], i[5])
    liste_armes.append(new_arme)


for i in data_armures :
    
    new_armure = Armure (i[0], i[1], i[2], i[3], i[4], i[5])
    liste_armures.append(new_armure)


def monstre(id) :

    return (liste_monstre[id-1])
    




def Attaque_normal_user(attaque_user, défense_monstre) :

    if attaque_user - défense_monstre < 0 :
        return(0)
    else :
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

    

    if data_vérification_level_up[1] >= data_vérification_level_up[0] :

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

    
    apprentissage_compétence_cursor=conn.cursor()
    apprentissage_compétence_query = ("SELECT classe, LV FROM Users WHERE id = {0}".format(User_actuel.id))
    apprentissage_compétence_cursor.execute(apprentissage_compétence_query)
    data_apprentissage_compétence = apprentissage_compétence_cursor.fetchall()

    LV = 0
    classe = ""

    for i in data_apprentissage_compétence :
        LV = i[1]
        classe = i[0]

    
    vérif_compétence_cursor=conn.cursor()
    vérif_compétence_query = ("SELECT id_compétences FROM compétences_par_lv WHERE classe = '{0}' AND LV_Obtention = {1}".format(classe, LV))
    vérif_compétence_cursor.execute(vérif_compétence_query)
    data_vérif_compétence = vérif_compétence_cursor.fetchone()

    if data_vérif_compétence is not None :

        id_max_compétence_cursor=conn.cursor()
        id_max_compétence_query = ("SELECT MAX(id) FROM compétences_apprises")
        id_max_compétence_cursor.execute(id_max_compétence_query)
        data_id_max_compétence = id_max_compétence_cursor.fetchone()

        max_id = 0
        id_compétence = 0

        if data_id_max_compétence is not None :
            for i in data_id_max_compétence :
                max_id = i

        for j in data_vérif_compétence :
            id_compétence = j

        insert_compétence_cursor=conn.cursor()
        insert_compétence_query = ("INSERT INTO compétences_apprises VALUES({0}, {1}, {2})".format(max_id+1, User_actuel.id, id_compétence))
        insert_compétence_cursor.execute(insert_compétence_query)
        conn.commit()


def attaque_monstre(monstre, user) :

    degats = 0

    if monstre.Attaque >= monstre.Puissance_Magique :
        degats = monstre.Attaque - user.Défense
    else :
        degats = monstre.Puissance_Magique - user.Résistance_Magique

    if degats < 0 :
        degats = 0


    return degats


def print_arme() :
    
    liste_armes_inventaire = []
    armes_inventaire_cursor=conn.cursor()


    armes_inventaire = ("SELECT id_item FROM {0} WHERE {1} = {2}".format("inventaire_armes", "id_Users", User_actuel.id))
    armes_inventaire_cursor.execute(armes_inventaire)


    data_armes_inventaire = armes_inventaire_cursor.fetchall()

    for i in data_armes_inventaire :
    
        for j in i :

            liste_armes_inventaire.append(liste_armes[j-1])


    return (liste_armes_inventaire)


def print_armure() :
    
    liste_armures_inventaire = []
    armures_inventaire_cursor=conn.cursor()


    armures_inventaire = ("SELECT id_item FROM {0} WHERE {1} = {2}".format("inventaire_armures", "id_Users", User_actuel.id))
    armures_inventaire_cursor.execute(armures_inventaire)


    data_armures_inventaire = armures_inventaire_cursor.fetchall()

    for i in data_armures_inventaire :
    
        for j in i :

            liste_armures_inventaire.append(liste_armures[j-1])


    return (liste_armures_inventaire)


def combat(monstre_id) :

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

        loot(monstre_id)
        gain_xp_gold(monstre_id)

        combat(1)



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

        menu()

    


def boutique() :

    liste_boutique = []
    

    boutique_cursor=conn.cursor()
    boutique_query = ("SELECT * FROM boutique")
    boutique_cursor.execute(boutique_query)
    data_boutique = boutique_cursor.fetchall()

    for i in data_boutique :

        liste_items = []

        boutique_cursor2=conn.cursor()
        boutique_query2 = ("SELECT * FROM {0} WHERE id = {1}".format(i[2], i[1]))
        boutique_cursor2.execute(boutique_query2)
        data_boutique2 = boutique_cursor2.fetchone()
        j = data_boutique2

        if i[2] == "objet" :
            item = Objet(j[0], j[1], j[2], j[3])
            liste_items.append(item)
        elif i[2] == "arme" :
            item = Arme(j[0], j[1], j[2], j[3], j[4], j[5])
            liste_items.append(item)
        elif i[2] == "armure" :
            item = Armure(j[0], j[1], j[2], j[3], j[4], j[5])
            liste_items.append(item)

        liste_items.append(i[3])
        liste_items.append(i[2])
        liste_boutique.append(liste_items)

    return(liste_boutique)




def equiper_arme() :
    
    liste_armes_inventaire = print_arme()
    for i in liste_armes_inventaire :
        print (i)

    arme_equiper = input("Quel arme voulez vous équiper ? : ")

    for i in liste_armes_inventaire :
    
        if i.nom == arme_equiper :

            update_cursor=conn.cursor()
            update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_arme", i.id, User_actuel.id))
            update_cursor.execute(update_query)
            conn.commit()




def equiper_armure() :
    
    liste_armures_inventaire = print_armure()
    for i in liste_armures_inventaire :
        print (i)

    arme_equiper = input("Quel arme voulez vous équiper ? : ")

    for i in liste_armures_inventaire :
    
        if i.nom == arme_equiper :
            update_cursor=conn.cursor()

            if i.type_armure == "casque" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_casque", i.id, User_actuel.id))
            elif i.type_armure == "plastron" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_plastron", i.id, User_actuel.id))
            elif i.type_armure == "jambières" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_jambières", i.id, User_actuel.id))
            elif i.type_armure == "bottes" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_bottes", i.id, User_actuel.id))
            elif i.type_armure == "anneau" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_anneau", i.id, User_actuel.id))
            elif i.type_armure == "collier" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_collier", i.id, User_actuel.id))

            update_cursor.execute(update_query)
            conn.commit()


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

        menu()

    else :

        lancement()


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

        

        menu()


def lancement():
    conn_create = input("Connexion / Inscription : ")

    if conn_create == "Connexion" :
        connexion()
    elif conn_create == "Inscription" :
        create_user()


def inventaire() :

    action = int(input("voir l'inventaire d'objet(1) / gérer l'équipement(2) : "))

    if action == 1 :
        liste_objets_inventaire = print_objets(User_actuel.id)
        for i in liste_objets_inventaire :
            print (i)

    elif action == 2 :
        
        arme_armure = int(input("Gérer son arme(1) / Gérer ses armures(2) : "))

        if arme_armure == 1 :
            equiper_arme()
            menu()

        elif arme_armure == 2 :
            equiper_armure()
            menu()

        else :
            menu()

    else :
        menu()


def menu():
    action = input("combat / boutique / inventaire / quitter ? : ")
    if action == "combat" :
        id_monstre = int(input("id du monstre à affronter ? : "))
        combat(id_monstre)

    elif action == "boutique" :
        print("entrer boutique")
        liste_boutique = boutique()
        for i in liste_boutique :
            print ("{0} , prix : {1}".format(i[0].nom, i[1], i[2]))

        achat = input("Que voulez vous acheter ? : ")

        for i in liste_boutique :
        
            if i[0].nom == achat and i[1] <= User_actuel.Golds :

                # Update inventaire, arme, armure ou objet
                print(i[0], i[1], i[2])
                print(User_actuel.id)
                update_golds_cursor=conn.cursor()
                update_golds_query = ("UPDATE Users SET Golds = Golds - {0} WHERE id = {1}".format(i[1], User_actuel.id))
                update_golds_cursor.execute(update_golds_query)
                conn.commit()

                if i[2] == "arme" :

                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire_armes WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire_armes SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
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
                        insert_query = ("INSERT INTO inventaire_armes VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()

                elif i[2] == "armure" :

                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire_armures WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire_armures SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
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
                        insert_query = ("INSERT INTO inventaire_armures VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()

                elif i[2] == "objet" :
                    
                    select_cursor=conn.cursor()
                    select_query = ("SELECT * FROM inventaire WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
                    select_cursor.execute(select_query)
                    data_select = select_cursor.fetchone()

                    if data_select is not None :
                        
                        update_inventaire_cursor=conn.cursor()
                        update_inventaire_query = ("UPDATE inventaire SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(User_actuel.id, i[0].id))
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
                        insert_query = ("INSERT INTO inventaire VALUES({0}, {1}, {2}, {3})".format(max_id+1, User_actuel.id, i[0].id, 1))
                        insert_cursor.execute(insert_query)
                        conn.commit()


            elif i[0].nom == achat and i[1] > User_actuel.Golds :

                print("pas assez de golds")
                
        menu()

    elif action == "inventaire":

        inventaire()


    elif action == "quitter" :
        print("stop")

    else :
        menu()



lancement()