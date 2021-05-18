from conn_liste import conn, liste_armures

def print_armure(user) :
    
    liste_armures_inventaire = []
    armures_inventaire_cursor=conn.cursor()


    armures_inventaire = ("SELECT id_item FROM {0} WHERE {1} = {2}".format("inventaire_armures", "id_Users", user.id))
    armures_inventaire_cursor.execute(armures_inventaire)


    data_armures_inventaire = armures_inventaire_cursor.fetchall()

    for i in data_armures_inventaire :
    
        for j in i :

            liste_armures_inventaire.append(liste_armures[j-1])


    return (liste_armures_inventaire)