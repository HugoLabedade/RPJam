from fonctions.conn_liste import conn
from classes.class_arme import Arme
from classes.class_armure import Armure
from classes.class_objet import Objet

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

