from fonctions.fonction_monstre import monstre
from fonctions.conn_liste import conn
from fonctions.fonction_level_up import level_up

def gain_xp_gold(user, monstre_id) :
    
    monstre_actuel = monstre(monstre_id)

    update_golds_cursor=conn.cursor()
    update_golds_query = ("UPDATE Users SET Golds = Golds + {0} WHERE id = {1}".format(monstre_actuel.Golds_Give, user.id))
    update_golds_cursor.execute(update_golds_query)
    conn.commit()


    update_xp_cursor=conn.cursor()
    update_xp_query = ("UPDATE Users SET XP = XP + {0} WHERE id = {1}".format(monstre_actuel.XP_Give, user.id))
    update_xp_cursor.execute(update_xp_query)
    conn.commit()


    vérification_level_up_cursor=conn.cursor()
    vérification_level_up_query = ("SELECT XP_For_Next_LV, XP FROM Users WHERE id = {0}".format(user.id))
    vérification_level_up_cursor.execute(vérification_level_up_query)
    data_vérification_level_up = vérification_level_up_cursor.fetchone()

    

    if data_vérification_level_up[1] >= data_vérification_level_up[0] :

        level_up(user)