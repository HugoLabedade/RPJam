from random import randrange
from conn_liste import conn
from variables import *
from class_arme import Arme
from class_armure import Armure
from class_objet import Objet

def loot(user, monstre_id) :
    
    # Loots possible du monstre
    loot_cursor=conn.cursor()
    loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("loot", "id_monstre", monstre_id))
    loot_cursor.execute(loot)
    data_loot = loot_cursor.fetchall()

    liste_loot = []
    new_liste_loot = []


    number_random = randrange(0, 100)
    number = 0


    for i in data_loot :
        
        liste_loot.append(i)


    for j in liste_loot :

        if j[2] == "arme" :

            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("arme", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Arme (i[0], i[1], i[2], i[3], i[4], i[5])
                new_liste_loot.append(new_loot)


            if number_random > number and number_random < (number + j[4]):

                print("drop d'une arme")

                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire_armes", "id", j[3], "id_Users", user.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armes"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire_armes VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire_armes", "id", j[3], "id_Users", user.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            
            number += j[4]

        elif j[2] == "armure" :
    
            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("armure", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Armure (i[0], i[1], i[2], i[3], i[4], i[5])
                new_liste_loot.append(new_loot)


            if number_random > number and number_random < (number + j[4]):

                print("drop d'une armure")
    
                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire_armures", "id", j[3], "id_Users", user.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire_armures"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire_armures VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire_armures", "id", j[3], "id_Users", user.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            number += j[4]

        elif j[2] == "objet" :
        
            # Loots possible du monstre
            new_loot_cursor=conn.cursor()
            new_loot = ("SELECT * FROM {0} WHERE {1} = {2}".format("objet", "id", j[3]))
            new_loot_cursor.execute(new_loot)
            data_new_loot = new_loot_cursor.fetchall()

            for i in data_new_loot :
            
                new_loot = Objet (i[0], i[1], i[2], i[3])
                new_liste_loot.append(new_loot)

            
            if number_random > number and number_random < (number + j[4]):

                print("drop d'un objet")
        
                existe_cursor=conn.cursor()
                existe_query = ("SELECT MAX(id) FROM {0} WHERE {1} = {2} AND {3} = {4}".format("inventaire", "id", j[3], "id_Users", user.id))
                existe_cursor.execute(existe_query)
                data_existe = existe_cursor.fetchone()

                existe = ""

                for i in data_existe :

                    existe = i


                if existe is None :

                    max_id_cursor=conn.cursor()
                    max_id_query = ("SELECT MAX(id) FROM {0}".format("inventaire"))
                    max_id_cursor.execute(max_id_query)
                    data_max_id = max_id_cursor.fetchall()
                    max_id = 0

                    for i in data_max_id :
                    
                        for k in i :

                            if k is None :

                                max_id = 0

                            else :
                                
                                max_id = k



                    insert_cursor=conn.cursor()
                    insert_query = ("INSERT INTO inventaire VALUES({0}, {1}, {2}, {3})".format(max_id+1, user.id, j[3], 1))
                    insert_cursor.execute(insert_query)
                    conn.commit()

                else :

                    update_cursor=conn.cursor()
                    update_query = ("UPDATE {0} SET quantité = quantité + 1 WHERE {1} = {2} AND {3} = {4}".format("inventaire", "id", j[3], "id_Users", user.id))
                    update_cursor.execute(update_query)
                    conn.commit()

            number += j[4]




