from fonctions.conn_liste import conn, liste_objets

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