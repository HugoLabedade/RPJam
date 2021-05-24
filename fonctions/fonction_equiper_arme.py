from fonctions.fonction_print_arme import print_arme
from fonctions.conn_liste import conn
import fonctions.fonction_lancement_menu_combat as jeu

def equiper_arme(user, id_arme) :

    update_cursor=conn.cursor()
    update_query = ("UPDATE equipement_users SET {0} = {1} WHERE id_Users = {2}".format("id_arme", id_arme, user.id))
    update_cursor.execute(update_query)
    conn.commit()

    jeu.ShowMenu(user)