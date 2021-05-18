from fonctions.conn_liste import conn, liste_compétences

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