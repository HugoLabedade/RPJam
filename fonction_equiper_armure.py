from conn_liste import conn
from fonction_print_armures import print_armure

def equiper_armure(user) :
    
    liste_armures_inventaire = print_armure(user)
    for i in liste_armures_inventaire :
        print (i)

    arme_equiper = input("Quel arme voulez vous équiper ? : ")

    for i in liste_armures_inventaire :
    
        if i.nom == arme_equiper :
            update_cursor=conn.cursor()

            if i.type_armure == "casque" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_casque", i.id, user.id))
            elif i.type_armure == "plastron" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_plastron", i.id, user.id))
            elif i.type_armure == "jambières" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_jambières", i.id, user.id))
            elif i.type_armure == "bottes" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_bottes", i.id, user.id))
            elif i.type_armure == "anneau" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_anneau", i.id, user.id))
            elif i.type_armure == "collier" :
                update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_collier", i.id, user.id))

            update_cursor.execute(update_query)
            conn.commit()
