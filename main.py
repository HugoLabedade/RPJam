import pymysql
from class_monstre import Monstres

# def connection(valeur):
conn = pymysql.connect("localhost", "root", "", "rpjam" )

user_cursor=conn.cursor()
monstres_cursor=conn.cursor()

Users = ("SELECT * FROM {0}".format("Users"))
user_cursor.execute(Users)

all_monstres = ("SELECT * FROM {0}".format("Monstres"))
monstres_cursor.execute(all_monstres)


# sqltest = ("UPDATE Users SET Golds = 50150 WHERE id=1;")
# a.execute(sqltest)
# conn.commit()






data_user = user_cursor.fetchone()
data_monstres = monstres_cursor.fetchall()


liste_monstre = []


print (data_user)


for i in data_monstres :

    new_monstre = Monstres (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
    liste_monstre.append(new_monstre)



def monstre(id) :

    return (liste_monstre[id-1])
    


def combat_test(monstre_id) :
    
    #On récupère les données du monstre qu'on affronte
    monstre_actuel = monstre(monstre_id)

    monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV
    user_PV_Max = data_user[6]
    user_PV = data_user[6]


    while monstre_PV > 0 and user_PV > 0:


        print("combat")
        monstre_PV -= 5

    print ("fin du combat PV monstre = {0}".format(monstre_PV))



def Attaque_normal_user(attaque_user, défense_monstre) :

    return (attaque_user - défense_monstre)





def print_compétences(id_user) :


    liste_compétences = []
    compétence_cursor=conn.cursor()

    compétences = ("SELECT * FROM {0}".format("Users"))
    compétence_cursor.execute(compétences)


    data_compétences = compétence_cursor.fetchall()

    for i in data_compétences :
    
        new_compétences = Monstres (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
        liste_compétences.append(new_monstre)






def combat(monstre_id) :

    monstre_actuel = monstre(monstre_id)

    #monstre_PV_Max = monstre_actuel.PV
    monstre_PV = monstre_actuel.PV
    #user_PV_Max = data_user[6]
    user_PV = data_user[6]



    print("Début du combat contre un {0}".format(monstre_actuel.nom))

    while monstre_PV > 0 and user_PV > 0:


    
        action = input("Attaque/Compétence/Objet : ")

        if action == "Attaque" :
            
            monstre_PV -= Attaque_normal_user(data_user[8], monstre_actuel.Défense)

        elif action == "Compétence" :
            
            monstre_PV -= 5



    print ("fin du combat PV monstre = {0}".format(monstre_PV))

combat(1)