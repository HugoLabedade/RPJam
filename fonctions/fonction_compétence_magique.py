from random import randrange
from fonctions.conn_liste import conn
from fonctions.variables import *
from fonctions.fonction_compétence_avec_effet_supp import compétence_avec_effet_supp

def compétence_magique(user, monstre, compétence, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Aura_de_peur, Psychocanalisation) :
    
    heal = 0
    Count_Brûlure_ennemi = 0
    Count_Confusion_ennemi = 0
    Count_Sommeil_ennemi = 0
    Count_Poison_ennemi = 0
    Count_Paralysie_ennemi = 0

    if compétence.id_effet is not None :
        randomint = randrange(1, 101)
        if randomint <= compétence.Pourcentage_Effet :
            if compétence.id_effet == 1 :
                Brûlure_ennemi = True
                Count_Brûlure_ennemi = 3
            elif compétence.id_effet == 2 :
                Confusion_ennemi = True
                Count_Confusion_ennemi = 3
            elif compétence.id_effet == 3 :
                Sommeil_ennemi = True
                Count_Sommeil_ennemi = 3
            elif compétence.id_effet == 4 :
                Poison_ennemi = True
                Count_Poison_ennemi = 3
            elif compétence.id_effet == 5 :
                Paralysie_ennemi = True
                Count_Paralysie_ennemi = 3

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
        données = compétence_avec_effet_supp(compétence, degats, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi)

        degats = données[1]
        heal = données[0]
        chances_crit = données[2]

    if Aura_de_peur == True :
        degats = round(degats * 2)

    if Psychocanalisation == True :
        degats = round(degats * 2.5)

    return (degats, compétence.PM_Utilisé, heal, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Count_Brûlure_ennemi, Count_Confusion_ennemi, Count_Sommeil_ennemi, Count_Poison_ennemi, Count_Paralysie_ennemi)
