import pymysql
from classes.class_monstre import Monstres
from classes.class_user import User
from classes.class_compétence import Competence
from classes.class_arme import Arme
from classes.class_armure import Armure
from classes.class_objet import Objet

# def connection(valeur):
conn = pymysql.connect("localhost", "root", "", "rpjam" )


# Création des curseurs
monstres_cursor=conn.cursor()
compétence_cursor=conn.cursor()
objets_cursor=conn.cursor()
arme_cursor=conn.cursor()
armure_cursor=conn.cursor()


# Récupère les données des Monstres
all_monstres = ("SELECT * FROM {0}".format("Monstres"))
monstres_cursor.execute(all_monstres)

# Récupère les données des Compétences
compétences = ("SELECT * FROM {0}".format("compétences"))
compétence_cursor.execute(compétences)

# Récupère les données des Objets
objets = ("SELECT * FROM {0}".format("objet"))
objets_cursor.execute(objets)

# Récupère les données des Armes
armes = ("SELECT * FROM {0}".format("arme"))
arme_cursor.execute(armes)

# Récupère les données des Armures
armures = ("SELECT * FROM {0}".format("armure"))
armure_cursor.execute(armures)


# Stockage des données dans des variables
data_monstres = monstres_cursor.fetchall()
data_compétences = compétence_cursor.fetchall()
data_objets = objets_cursor.fetchall()
data_armes = arme_cursor.fetchall()
data_armures = armure_cursor.fetchall()


# Initialisation des listes
liste_monstre = []
liste_compétences = []
liste_objets = []
liste_armes = []
liste_armures = []


for i in data_monstres :
    
    new_monstre = Monstres (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13])
    liste_monstre.append(new_monstre)


for i in data_compétences :
    
    new_compétences = Competence (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10])
    liste_compétences.append(new_compétences)


for i in data_objets :
    
    new_objet = Objet (i[0], i[1], i[2], i[3])
    liste_objets.append(new_objet)


for i in data_armes :
    
    new_arme = Arme (i[0], i[1], i[2], i[3], i[4], i[5])
    liste_armes.append(new_arme)


for i in data_armures :
    
    new_armure = Armure (i[0], i[1], i[2], i[3], i[4], i[5])
    liste_armures.append(new_armure)
