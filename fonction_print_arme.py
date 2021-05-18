from conn_liste import conn, liste_armes

def print_arme(user) :
    
    liste_armes_inventaire = []
    armes_inventaire_cursor=conn.cursor()


    armes_inventaire = ("SELECT id_item FROM {0} WHERE {1} = {2}".format("inventaire_armes", "id_Users", user.id))
    armes_inventaire_cursor.execute(armes_inventaire)


    data_armes_inventaire = armes_inventaire_cursor.fetchall()

    for i in data_armes_inventaire :
    
        for j in i :

            liste_armes_inventaire.append(liste_armes[j-1])


    return (liste_armes_inventaire)