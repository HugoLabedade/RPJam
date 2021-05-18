from random import randrange
from fonctions.variables import *

def compétence_avec_effet_supp(compétence, degats, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi) :

    heal = 0

    if compétence.id == 4 :
        heal = round(degats/5)

    if compétence.id == 12 :
        if Confusion_ennemi == True or Sommeil_ennemi == True :
            randomint = randrange(1,5)
            if randomint == 1 :
                degats*=6

    if compétence.id == 14 :
        if Poison_ennemi == True or Paralysie_ennemi == True :
            randomint = randrange(1,5)
            if randomint == 1 :
                degats*=6

    if compétence.id == 28 :
        chances_crit *= 3


    return(heal, degats, chances_crit)

