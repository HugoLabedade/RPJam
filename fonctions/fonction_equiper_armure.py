from fonctions.conn_liste import conn
from fonctions.fonction_print_armures import print_armure
import fonctions.fonction_lancement_menu_combat as jeu

def equiper_armure(user, armure) :
    
    update_cursor=conn.cursor()

    if armure.type_armure == "casque" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_casque", armure.id, user.id))
    elif armure.type_armure == "plastron" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_plastron", armure.id, user.id))
    elif armure.type_armure == "jambières" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_jambières", armure.id, user.id))
    elif armure.type_armure == "bottes" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_bottes", armure.id, user.id))
    elif armure.type_armure == "anneau" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_anneau", armure.id, user.id))
    elif armure.type_armure == "collier" :
        update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_collier", armure.id, user.id))

    update_cursor.execute(update_query)
    conn.commit()

    jeu.ShowMenu(user)
