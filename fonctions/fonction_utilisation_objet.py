from fonctions.variables import *
from fonctions.conn_liste import conn

def utilisation_objet(user, objet) :

    select_quantité=conn.cursor()
    update_delete=conn.cursor()

    objets = ("SELECT * FROM {0} WHERE id_Users = {1} AND id_item = {2}".format("inventaire", user.id, objet.id))
    select_quantité.execute(objets)
    data_objet = select_quantité.fetchone()

    if data_objet[3] > 1 :
    
        update_delete_query = ("UPDATE {0} SET {1} = {2} - 1 WHERE id_Users = {3} AND id_item = {4}".format("inventaire", "quantité", "quantité", user.id, objet.id))
        update_delete.execute(update_delete_query)
        conn.commit()

    else :
        
        update_delete_query = ("DELETE FROM {0} WHERE id_Users = {1} AND id_item = {2}".format("inventaire", user.id, objet.id))
        update_delete.execute(update_delete_query)
        conn.commit()


    print(data_objet)

    
    
    heal = 0
    heal_PM = 0
    Décuplo = False
    Count_Décuplo = 0
    Hâte = False
    Count_Hâte = 0
    Protection = False
    Count_Protection = 0
    effets = True


    if objet.id == 1 :
        heal = 40
    
    elif objet.id == 2 :
        heal = 80

    elif objet.id == 3 :
        heal = 120

    elif objet.id == 4 :
        heal = 200

    elif objet.id == 5 :
        effets = False
        
    elif objet.id == 6 :
        heal_PM = 30

    elif objet.id == 7 :
        heal_PM = 60

    elif objet.id == 8 :
        heal_PM = 120

    elif objet.id == 9 :
        heal = 400
        heal_PM = 250

    elif objet.id == 10 :
        Décuplo = True
        Count_Décuplo = 5

    elif objet.id == 11 :
        Hâte = True
        Count_Hâte = 15

    elif objet.id == 12 :
        Protection = True
        Count_Protection = 5

    
    return(heal, heal_PM, Décuplo, Count_Décuplo, Hâte, Count_Hâte, Protection, Count_Protection, effets)


    