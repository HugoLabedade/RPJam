from fonctions.conn_liste import conn
import fonctions.fonction_lancement_menu_combat as jeu


def achat_boutique(user, achat) :

        
    if achat[1] <= user.Golds :

        # Update inventaire, arme, armure ou objet
        print(achat[0], achat[1], achat[2])
        print(user.id)
        update_golds_cursor=conn.cursor()
        update_golds_query = ("UPDATE Users SET Golds = Golds - {0} WHERE id = {1}".format(achat[1], user.id))
        update_golds_cursor.execute(update_golds_query)
        conn.commit()

        if achat[2] == "arme" :

            select_cursor=conn.cursor()
            select_query = ("SELECT * FROM inventaire_armes WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
            select_cursor.execute(select_query)
            data_select = select_cursor.fetchone()

            if data_select is not None :
                
                update_inventaire_cursor=conn.cursor()
                update_inventaire_query = ("UPDATE inventaire_armes SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
                update_inventaire_cursor.execute(update_inventaire_query)
                conn.commit()

            else :

                max_id_cursor=conn.cursor()
                max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armes"))
                max_id_cursor.execute(max_id_query)
                data_max_id = max_id_cursor.fetchone()
                max_id = 0

                for j in data_max_id :
                    max_id = j

                insert_cursor=conn.cursor()
                insert_query = ("INSERT INTO inventaire_armes VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, achat[0].id, 1))
                insert_cursor.execute(insert_query)
                conn.commit()

        elif achat[2] == "armure" :

            select_cursor=conn.cursor()
            select_query = ("SELECT * FROM inventaire_armures WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
            select_cursor.execute(select_query)
            data_select = select_cursor.fetchone()

            if data_select is not None :
                
                update_inventaire_cursor=conn.cursor()
                update_inventaire_query = ("UPDATE inventaire_armures SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
                update_inventaire_cursor.execute(update_inventaire_query)
                conn.commit()

            else :

                max_id_cursor=conn.cursor()
                max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armures"))
                max_id_cursor.execute(max_id_query)
                data_max_id = max_id_cursor.fetchone()
                max_id = 0

                for j in data_max_id :
                    max_id = j

                insert_cursor=conn.cursor()
                insert_query = ("INSERT INTO inventaire_armures VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, achat[0].id, 1))
                insert_cursor.execute(insert_query)
                conn.commit()

        elif achat[2] == "objet" :
            
            select_cursor=conn.cursor()
            select_query = ("SELECT * FROM inventaire WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
            select_cursor.execute(select_query)
            data_select = select_cursor.fetchone()

            if data_select is not None :
                
                update_inventaire_cursor=conn.cursor()
                update_inventaire_query = ("UPDATE inventaire SET quantité = quantité + 1 WHERE id_Users = {0} AND id_item = {1}".format(user.id, achat[0].id))
                update_inventaire_cursor.execute(update_inventaire_query)
                conn.commit()

            else :

                max_id_cursor=conn.cursor()
                max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire"))
                max_id_cursor.execute(max_id_query)
                data_max_id = max_id_cursor.fetchone()
                max_id = 0

                for j in data_max_id :
                    max_id = j

                insert_cursor=conn.cursor()
                insert_query = ("INSERT INTO inventaire VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, achat[0].id, 1))
                insert_cursor.execute(insert_query)
                conn.commit()


    elif achat[0].nom == achat and achat[1] > user.Golds :

        print("pas assez de golds")
                
    jeu.ShowMenu(user)
