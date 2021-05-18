from conn_liste import conn
from random import randrange

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
                                .format(grosse_stat1, moyenne_stat1, grosse_stat2, petite_stat1, moyenne_stat2, petite_stat2, moyenne_stat3, user.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()

    
    elif user.classe == "Mage" :

        update_stats_cursor=conn.cursor()
        update_stats_query = ("UPDATE Users SET LV = LV + 1, PV = PV + {0}, PM = PM + {1}, Attaque = Attaque + {2}, Puissance_Magique = Puissance_Magique + {3}, Défense = Défense + {4}, Résistance_Magique = Résistance_Magique + {5}, Vitesse = Vitesse + {6}, XP_For_Next_LV = XP_For_Next_LV * 1.5, XP = 0, points_de_compétences = points_de_compétences + 3 WHERE id = {7}"
                                .format(moyenne_stat1, grosse_stat1, petite_stat1, grosse_stat2, petite_stat2, moyenne_stat2, moyenne_stat3, user.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()


    elif user.classe == "Assassin" :

        update_stats_cursor=conn.cursor()
        update_stats_query = ("UPDATE Users SET LV = LV + 1, PV = PV + {0}, PM = PM + {1}, Attaque = Attaque + {2}, Puissance_Magique = Puissance_Magique + {3}, Défense = Défense + {4}, Résistance_Magique = Résistance_Magique + {5}, Vitesse = Vitesse + {6}, XP_For_Next_LV = XP_For_Next_LV * 1.5, XP = 0, points_de_compétences = points_de_compétences + 3 WHERE id = {7}"
                                .format(moyenne_stat1, moyenne_stat2, grosse_stat1, moyenne_stat3, petite_stat1, petite_stat2, grosse_stat2, user.id))
        update_stats_cursor.execute(update_stats_query)
        conn.commit()

    
    apprentissage_compétence_cursor=conn.cursor()
    apprentissage_compétence_query = ("SELECT classe, LV FROM Users WHERE id = {0}".format(user.id))
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
        insert_compétence_query = ("INSERT INTO compétences_apprises VALUES({0}, {1}, {2})".format(max_id+1, user.id, id_compétence))
        insert_compétence_cursor.execute(insert_compétence_query)
        conn.commit()
