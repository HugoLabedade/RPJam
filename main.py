# -*- coding: utf-8 -*-

import pymysql
from class_monstre import Monstres
from class_user import User
from class_compétence import Competence
from class_arme import Arme
from class_armure import Armure
from class_objet import Objet
from random import randrange

from conn_liste import liste_monstre
from conn_liste import liste_armes
from conn_liste import liste_armures
from conn_liste import liste_compétences
from conn_liste import liste_objets
from conn_liste import conn

from variables import *

from fonction_menu_inventaire_combat_connexion import lancement


lancement()