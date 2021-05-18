from fonctions.fonction_print_arme import print_arme
from fonctions.conn_liste import conn

def equiper_arme(user) :
    
    liste_armes_inventaire = print_arme(user)
    for i in liste_armes_inventaire :
        print (i)

    arme_equiper = input("Quel arme voulez vous équiper ? : ")

    for i in liste_armes_inventaire :
    
        if i.nom == arme_equiper :

            update_cursor=conn.cursor()
            update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_arme", i.id, user.id))
            update_cursor.execute(update_query)
            conn.commit()