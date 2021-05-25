
from classes.class_user import User
from random import randrange
from fonctions.conn_liste import liste_armes, liste_armures, conn
from fonctions.variables import *
from fonctions.fonction_monstre import monstre
from fonctions.fonction_attaque_normal_user import Attaque_normal_user
from fonctions.fonction_print_compétences import print_compétences
from fonctions.fonction_compétence_physique import compétence_physique
from fonctions.fonction_compétence_magique import compétence_magique
from fonctions.fonction_compétence_sans_dommages import compétence_sans_dommages
from fonctions.fonction_print_objets import print_objets
from fonctions.fonction_utilisation_objet import utilisation_objet
from fonctions.fonction_critique import critique
from fonctions.fonction_loot import loot
from fonctions.fonction_gain_xp_golds import gain_xp_gold
from fonctions.fonction_boutique import boutique
from fonctions.fonction_attaque_monstre import attaque_monstre
import hashlib
import tkinter.font as tkFont
from tkinter import *
from création_fenetre_jeu import frameBase, fenetre
from fonctions.fonction_ShowArmures import ShowArmures
from fonctions.fonction_ShowArmes import ShowArmes
from fonctions.fonction_ShowBoutique import ShowBoutique
from fonctions.fonction_clear_frame import clear_frame
from fonctions.fonction_VoirInventaire import VoirInventaire
from fonctions.fonction_ShowMenu import ShowMenu
from fonctions.fonction_ShowCombat import ShowCombat
from fonctions.fonction_ShowInscrip import showInscrip
from fonctions.fonction_ShowConnex import showConnex
from fonctions.fonction_ShowChoixInventaire import ShowChoixInventaire
from fonctions.fonction_choix_monstre import choix_monstre




def lancement():
    global frameBase
    global boutonInscrip
    global boutonConnex

    clear_frame()

    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()
    
    font = tkFont.Font(family='Helvetica', size=15)
    boutonInscrip = Button(frameBase, text="Inscription", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: showInscrip(), font=font, height=1, width=20)
    boutonInscrip.place(x=400, y=250)
    boutonConnex = Button(frameBase, text="Connexion", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: showConnex(), font=font, height=1, width=20)
    boutonConnex.place(x=600, y=250)

    fenetre.mainloop() 


def connexion(pseudo, mdp):
    
    #algo connexion
    hashpass = hashlib.md5(mdp.encode('utf8')).hexdigest()

    user_cursor=conn.cursor()
    user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, hashpass))
    user_cursor.execute(user)
    data_user = user_cursor.fetchone()

    
    if data_user is None :
        lancement()

    else : 
        global User_actuel
        User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15], data_user[16])

        global user_PV_Max
        user_PV_Max = User_actuel.PV
        global user_PM_Max
        user_PM_Max = User_actuel.PM
        global user_Attaque_base
        user_Attaque_base = User_actuel.Attaque
        global user_Défense_base
        user_Défense_base = User_actuel.Défense
        global user_Vitesse_base
        user_Vitesse_base = User_actuel.Vitesse
        global user_PV
        user_PV = User_actuel.PV
        global vérif_equipement
        vérif_equipement = False

        ShowMenu(User_actuel)


def create_user(pseudo, mdp, classe):

    hashpass = hashlib.md5(mdp.encode('utf8')).hexdigest()

    user_cursor=conn.cursor()
    user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, hashpass))
    user_cursor.execute(user)
    data_user = user_cursor.fetchone()

    if data_user is None :

        max_id_cursor=conn.cursor()
        max_id_query = ("SELECT MAX(id) FROM {0}".format("Users"))
        max_id_cursor.execute(max_id_query)
        data_max_id = max_id_cursor.fetchone()
        max_id = 0

        for i in data_max_id :

            if i is None :

                max_id = 0

            else :
                
                max_id = i


        insert_cursor=conn.cursor()

        if classe == "Assassin" :
            insert_query = ("INSERT INTO {0} VALUES({1}, '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format("Users", max_id+1, pseudo, hashpass, classe, 0, 1, 10, 10, 10, 10, 10, 10, 10, 5, 0, 4, 0))
        else :
            insert_query = ("INSERT INTO {0} VALUES({1}, '{2}', '{3}', '{4}', {5}, {6}, {7}, {8}, {9}, {10}, {11}, {12}, {13}, {14}, {15}, {16}, {17})".format("Users", max_id+1, pseudo, hashpass, classe, 0, 1, 10, 10, 10, 10, 10, 10, 10, 0, 0, 4, 0))
        insert_cursor.execute(insert_query)
        conn.commit()

        user_cursor=conn.cursor()
        user = ("SELECT * FROM {0} WHERE pseudo = '{1}' AND password = '{2}'".format("Users", pseudo, hashpass))
        user_cursor.execute(user)
        data_user = user_cursor.fetchone()

        global User_actuel
        User_actuel = User (data_user[0], data_user[1], data_user[2], data_user[3], data_user[4], data_user[5], data_user[6], data_user[7], data_user[8], data_user[9], data_user[10], data_user[11], data_user[12], data_user[13], data_user[14], data_user[15], data_user[16])

        insert_equipement_cursor=conn.cursor()
        insert_equipement_query = ("INSERT INTO equipement_users(id_Users) VALUES({0})".format(max_id+1))
        insert_equipement_cursor.execute(insert_equipement_query)
        conn.commit()
        
        global user_PV_Max
        user_PV_Max = User_actuel.PV
        global user_PM_Max
        user_PM_Max = User_actuel.PM
        global user_Attaque_base
        user_Attaque_base = User_actuel.Attaque
        global user_Défense_base
        user_Défense_base = User_actuel.Défense
        global user_Vitesse_base
        user_Vitesse_base = User_actuel.Vitesse
        global user_PV
        user_PV = User_actuel.PV
        global vérif_equipement
        vérif_equipement = False

        ShowMenu(User_actuel)

    else :

        lancement()


def combat(user, monstre, action, compétence_objet, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement):

    

    # Dire qu'on peut modifier nos variables d'effet
    global Brûlure
    global Confusion
    global Sommeil
    global Poison
    global Paralysie

    global Brûlure_ennemi
    global Confusion_ennemi
    global Sommeil_ennemi
    global Poison_ennemi
    global Paralysie_ennemi

    global Boost_Esquive
    global Aura_de_peur
    global Souffle_du_sage
    global Psychocanalisation
    global Clic_clac_zap
    global Grâce_de_la_Déesse
    global Cercle_du_carnage
    global Décuplo
    global Protection
    global Hâte

    global Count_Brûlure
    global Count_Confusion
    global Count_Sommeil
    global Count_Poison
    global Count_Paralysie

    global Count_Brûlure_ennemi
    global Count_Confusion_ennemi
    global Count_Sommeil_ennemi
    global Count_Poison_ennemi
    global Count_Paralysie_ennemi

    global Count_Boost_Esquive
    global Count_Aura_de_peur
    global Count_Souffle_du_sage
    global Count_Psychocanalisation
    global Count_Clic_clac_zap
    global Count_Grâce_de_la_Déesse
    global Count_Cercle_du_carnage
    global Count_Décuplo
    global Count_Protection
    global Count_Hâte

    global frameBase

    
    if Décuplo == True :
        user.Attaque = user_Attaque_base * 2
    else : 
        user.Attaque = user_Attaque_base

    if Protection == True :
        user.Défense = user_Défense_base * 2
    else : 
        user.Défense = user_Défense_base

    if Hâte == True :
        user.Vitesse = user_Vitesse_base * 2
    else : 
        user.Vitesse = user_Vitesse_base

    if Cercle_du_carnage == True :
        chances_crit = 10
    else :
        chances_crit = 5

    if Souffle_du_sage == True :
        user.PM += round(user_PM_Max/20)
        if user.PM > user_PM_Max :
            user.PM = user_PM_Max

    if Clic_clac_zap == True :
        Brûlure = False
        Poison = False
        Sommeil = False
        Paralysie = False
        Confusion = False

    if user.Vitesse <= monstre.Vitesse :

        # Code tour du monstre
        if Brûlure_ennemi == True :
            print("Avant brulure : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/20))
            print("Après brulure : {0}".format(monstre_PV))

        elif Poison_ennemi == True :
            print("Avant poison : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/20))
            print("Après poison : {0}".format(monstre_PV))

        elif Confusion_ennemi == True :
            print("Avant confusion : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/5))
            print("Après confusion : {0}".format(monstre_PV))


        if Sommeil_ennemi == False and Paralysie_ennemi == False and monstre_PV > 0 :
            degats_monstre = attaque_monstre(monstre, user)
            print(degats_monstre)

            if Boost_Esquive == True :
                randomint = randrange(1,101)
                if randomint <= user.Esquive + 15 :
                    degats_monstre = 0

            else :
                randomint = randrange(1,101)
                if randomint <= user.Esquive :
                    degats_monstre = 0

            if Grâce_de_la_Déesse == True and degats_monstre >= user_PV:
                user_PV = user_PM_Max
                print("Grâce de la déesse activé")
            else :
                user_PV -= degats_monstre

    
        # Code tour du user
        if Brûlure == True :
            print("Avant brulure : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après brulure : {0}".format(user_PV))

        elif Poison == True :
            print("Avant poison : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après poison : {0}".format(user_PV))

        elif Confusion == True :
            print("Avant confusion : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/5))
            print("Après confusion : {0}".format(user_PV))

        
        if Sommeil == False and Paralysie == False and user_PV > 0 :

            if action == "Attaque" :
                
                monstre_PV -= Attaque_normal_user(user.Attaque, monstre.Défense)
                print("PV du monstre : {0}".format(monstre_PV))

            elif action == "Compétences" :
        
                if user.PM >= compétence_objet.PM_Utilisé : 

                    if compétence_objet.Magique_Physique == "Physique" :
                        données = compétence_physique(user, monstre, compétence_objet, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi)
                        degats = critique(données[0], données[3])
                        monstre_PV -= degats
                        user.PM -= données[1]
                        user_PV += données[2]
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Confusion_ennemi = données[4]
                        Sommeil_ennemi = données[5]
                        Poison_ennemi = données[6]
                        Paralysie_ennemi = données[7]
                        Brûlure_ennemi = données[8]
                        Count_Brûlure_ennemi = données[9]
                        Count_Confusion_ennemi = données[10]
                        Count_Sommeil_ennemi = données[11]
                        Count_Poison_ennemi = données[12]
                        Count_Paralysie_ennemi = données[13]

                    elif compétence_objet.Magique_Physique == "Magique" :
                        données = compétence_magique(user, monstre, compétence_objet, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Aura_de_peur, Psychocanalisation)
                        degats = critique(données[0], données[3])
                        monstre_PV -= degats
                        user.PM -= données[1]
                        user_PV += données[2]
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Confusion_ennemi = données[4]
                        Sommeil_ennemi = données[5]
                        Poison_ennemi = données[6]
                        Paralysie_ennemi = données[7]
                        Brûlure_ennemi = données[8]
                        Count_Brûlure_ennemi = données[9]
                        Count_Confusion_ennemi = données[10]
                        Count_Sommeil_ennemi = données[11]
                        Count_Poison_ennemi = données[12]
                        Count_Paralysie_ennemi = données[13]

                        

                    else :
                        données = compétence_sans_dommages(user_PV_Max, compétence_objet)
                        user_PV += données[0]
                        user.PM -= données[1]
                        print(user.PM)
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Boost_Esquive = données[2]
                        Count_Boost_Esquive = données[3]
                        Aura_de_peur = données[4]
                        Count_Aura_de_peur = données[5]
                        Souffle_du_sage = données[6]
                        Count_Souffle_du_sage = données[7]
                        Psychocanalisation = données[8]
                        Count_Psychocanalisation = données[9]
                        Clic_clac_zap = données[10]
                        Count_Clic_clac_zap = données[11]
                        Grâce_de_la_Déesse = données[12]
                        Count_Grâce_de_la_Déesse = données[13]
                        Cercle_du_carnage = données[14]
                        Count_Cercle_du_carnage = données[15]
                        Poison_ennemi = données[16]
                        Count_Poison_ennemi = données[17]
                        Confusion_ennemi = données[18]
                        Count_Confusion_ennemi = données[19]
                        Brûlure_ennemi = données[20]
                        Count_Brûlure_ennemi = données[21]
                        Sommeil_ennemi = données[22]
                        Count_Sommeil_ennemi = données[23]
                        Décuplo = données[24]
                        Count_Décuplo = données[25]
                        Protection = données[26]
                        Count_Protection = données[27]
                        Hâte = données[28]
                        Count_Hâte = données[29]

                else :

                    print("PM insuffisants")

            elif action == "Objet" :

                
                données = utilisation_objet(user, compétence_objet)

                user_PV += données[0]
                if user_PV > user_PV_Max :
                    user_PV = user_PV_Max

                user.PM += données[1]
                if user.PM > user_PM_Max :
                    user.PM = user_PM_Max

                Décuplo = données[2]
                Count_Décuplo = données[3]
                Hâte = données[4]
                Count_Hâte = données[5]
                Protection = données[6]
                Count_Protection = données[7]

                print(user_PV)
                print(user.PM)



        

    if user.Vitesse >= monstre.Vitesse :
    
    
        # Code tour du user
        if Brûlure == True :
            print("Avant brulure : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après brulure : {0}".format(user_PV))

        elif Poison == True :
            print("Avant poison : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/20))
            print("Après poison : {0}".format(user_PV))

        elif Confusion == True :
            print("Avant confusion : {0}".format(user_PV))
            user_PV -= round((user_PV_Max/5))
            print("Après confusion : {0}".format(user_PV))

        
        if Sommeil == False and Paralysie == False and user_PV > 0 :

            if action == "Attaque" :
                
                monstre_PV -= Attaque_normal_user(user.Attaque, monstre.Défense)
                print("PV du monstre : {0}".format(monstre_PV))

            elif action == "Compétences" :
        
                if user.PM >= compétence_objet.PM_Utilisé : 

                    if compétence_objet.Magique_Physique == "Physique" :
                        données = compétence_physique(user, monstre, compétence_objet, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi)
                        degats = critique(données[0], données[3])
                        monstre_PV -= degats
                        user.PM -= données[1]
                        user_PV += données[2]
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Confusion_ennemi = données[4]
                        Sommeil_ennemi = données[5]
                        Poison_ennemi = données[6]
                        Paralysie_ennemi = données[7]
                        Brûlure_ennemi = données[8]
                        Count_Brûlure_ennemi = données[9]
                        Count_Confusion_ennemi = données[10]
                        Count_Sommeil_ennemi = données[11]
                        Count_Poison_ennemi = données[12]
                        Count_Paralysie_ennemi = données[13]

                    elif compétence_objet.Magique_Physique == "Magique" :
                        données = compétence_magique(user, monstre, compétence_objet, chances_crit, Confusion_ennemi, Sommeil_ennemi, Poison_ennemi, Paralysie_ennemi, Brûlure_ennemi, Aura_de_peur, Psychocanalisation)
                        degats = critique(données[0], données[3])
                        monstre_PV -= degats
                        user.PM -= données[1]
                        user_PV += données[2]
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Confusion_ennemi = données[4]
                        Sommeil_ennemi = données[5]
                        Poison_ennemi = données[6]
                        Paralysie_ennemi = données[7]
                        Brûlure_ennemi = données[8]
                        Count_Brûlure_ennemi = données[9]
                        Count_Confusion_ennemi = données[10]
                        Count_Sommeil_ennemi = données[11]
                        Count_Poison_ennemi = données[12]
                        Count_Paralysie_ennemi = données[13]

                        

                    else :
                        données = compétence_sans_dommages(user_PV_Max, compétence_objet)
                        user_PV += données[0]
                        user.PM -= données[1]
                        print(user.PM)
                        if user_PV > user_PV_Max :
                            user_PV = user_PV_Max

                        Boost_Esquive = données[2]
                        Count_Boost_Esquive = données[3]
                        Aura_de_peur = données[4]
                        Count_Aura_de_peur = données[5]
                        Souffle_du_sage = données[6]
                        Count_Souffle_du_sage = données[7]
                        Psychocanalisation = données[8]
                        Count_Psychocanalisation = données[9]
                        Clic_clac_zap = données[10]
                        Count_Clic_clac_zap = données[11]
                        Grâce_de_la_Déesse = données[12]
                        Count_Grâce_de_la_Déesse = données[13]
                        Cercle_du_carnage = données[14]
                        Count_Cercle_du_carnage = données[15]
                        Poison_ennemi = données[16]
                        Count_Poison_ennemi = données[17]
                        Confusion_ennemi = données[18]
                        Count_Confusion_ennemi = données[19]
                        Brûlure_ennemi = données[20]
                        Count_Brûlure_ennemi = données[21]
                        Sommeil_ennemi = données[22]
                        Count_Sommeil_ennemi = données[23]
                        Décuplo = données[24]
                        Count_Décuplo = données[25]
                        Protection = données[26]
                        Count_Protection = données[27]
                        Hâte = données[28]
                        Count_Hâte = données[29]

                else :

                    print("PM insuffisants")

            elif action == "Objet" :

                
                données = utilisation_objet(user, compétence_objet)

                user_PV += données[0]
                if user_PV > user_PV_Max :
                    user_PV = user_PV_Max

                user.PM += données[1]
                if user.PM > user_PM_Max :
                    user.PM = user_PM_Max

                Décuplo = données[2]
                Count_Décuplo = données[3]
                Hâte = données[4]
                Count_Hâte = données[5]
                Protection = données[6]
                Count_Protection = données[7]

                print(user_PV)
                print(user.PM)



        # Code tour du monstre
        if Brûlure_ennemi == True :
            print("Avant brulure : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/20))
            print("Après brulure : {0}".format(monstre_PV))

        elif Poison_ennemi == True :
            print("Avant poison : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/20))
            print("Après poison : {0}".format(monstre_PV))

        elif Confusion_ennemi == True :
            print("Avant confusion : {0}".format(monstre_PV))
            monstre_PV -= round((monstre_PV_Max/5))
            print("Après confusion : {0}".format(monstre_PV))


        if Sommeil_ennemi == False and Paralysie_ennemi == False and monstre_PV > 0 :
            degats_monstre = attaque_monstre(monstre, user)
            print(degats_monstre)

            if Boost_Esquive == True :
                randomint = randrange(1,101)
                if randomint <= user.Esquive + 15 :
                    degats_monstre = 0

            else :
                randomint = randrange(1,101)
                if randomint <= user.Esquive :
                    degats_monstre = 0

            if Grâce_de_la_Déesse == True and degats_monstre >= user_PV:
                user_PV = user_PM_Max
                print("Grâce de la déesse activé")
            else :
                user_PV -= degats_monstre


    # Décompte des tours des effets
    if Count_Brûlure > 0 :
        Count_Brûlure -= 1
        if Count_Brûlure == 0 :
            Brûlure = False
    if Count_Confusion > 0 :
        Count_Confusion -= 1
        if Count_Confusion == 0 :
            Confusion = False
    if Count_Sommeil > 0 :
        Count_Sommeil -= 1
        if Count_Sommeil == 0 :
            Sommeil = False
    if Count_Poison > 0 :
        Count_Poison -= 1
        if Count_Poison == 0 :            
            Poison = False
    if Count_Paralysie > 0 :
        Count_Paralysie -= 1
        if Count_Paralysie == 0 :
            Paralysie = False

    if Count_Brûlure_ennemi > 0 :
        Count_Brûlure_ennemi -= 1
        if Count_Brûlure_ennemi == 0 :
            Brûlure_ennemi = False
    if Count_Confusion_ennemi > 0 :
        Count_Confusion_ennemi -= 1
        if Count_Confusion_ennemi == 0 :
            Confusion_ennemi = False
    if Count_Sommeil_ennemi > 0 :
        Count_Sommeil_ennemi -= 1
        if Count_Sommeil_ennemi == 0 :
            Sommeil_ennemi = False
    if Count_Poison_ennemi > 0 :
        Count_Poison_ennemi -= 1
        if Count_Poison_ennemi == 0 :
            Poison_ennemi = False
    if Count_Paralysie_ennemi > 0 :
        Count_Paralysie_ennemi -= 1
        if Count_Paralysie_ennemi == 0 :
            Paralysie_ennemi = False

    if Count_Boost_Esquive > 0 :
        Count_Boost_Esquive -= 1
        if Count_Boost_Esquive == 0 :
            Boost_Esquive = False
    if Count_Aura_de_peur > 0 :
        Count_Aura_de_peur -= 1
        if Count_Aura_de_peur == 0 :
            Aura_de_peur = False
    if Count_Souffle_du_sage > 0 :
        Count_Souffle_du_sage -= 1
        if Count_Souffle_du_sage == 0 :
            Souffle_du_sage = False
    if Count_Psychocanalisation > 0 :
        Count_Psychocanalisation -= 1
        if Count_Psychocanalisation == 0 :
            Psychocanalisation = False
    if Count_Clic_clac_zap > 0 :
        Count_Clic_clac_zap -= 1
        if Count_Clic_clac_zap == 0 :
            Clic_clac_zap = False
    if Count_Grâce_de_la_Déesse > 0 :
        Count_Grâce_de_la_Déesse -= 1
        if Count_Grâce_de_la_Déesse == 0 :
            Grâce_de_la_Déesse = False
    if Count_Cercle_du_carnage > 0 :
        Count_Cercle_du_carnage -= 1
        if Count_Cercle_du_carnage == 0 :
            Cercle_du_carnage = False
    if Count_Décuplo > 0 :
        Count_Décuplo -= 1
        if Count_Décuplo == 0 :
            Décuplo = False
    if Count_Protection > 0 :
        Count_Protection -= 1
        if Count_Protection == 0 :
            Protection = False
    if Count_Hâte > 0 :
        Count_Hâte -= 1
        if Count_Hâte == 0 :
            Hâte = False



    if monstre_PV > 0 and user_PV > 0 :
        ShowCombat(user, monstre, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement)

    elif monstre_PV <= 0 :
        
        loot(user, monstre.id)
        gain_xp_gold(user, monstre.id)

        level_up_user_cursor=conn.cursor()
        level_up_user = ("SELECT * FROM {0} WHERE id = '{1}'".format("Users", user.id))
        level_up_user_cursor.execute(level_up_user)
        data_user_level_up = level_up_user_cursor.fetchone()

        userPM = user.PM

        User_actuel = User (data_user_level_up[0], data_user_level_up[1], data_user_level_up[2], data_user_level_up[3], data_user_level_up[4], data_user_level_up[5], data_user_level_up[6], data_user_level_up[7], data_user_level_up[8], data_user_level_up[9], data_user_level_up[10], data_user_level_up[11], data_user_level_up[12], data_user_level_up[13], data_user_level_up[14], data_user_level_up[15], data_user_level_up[16])

        user_PV_Max = User_actuel.PV
        user_PM_Max = User_actuel.PM
        user_Attaque_base = User_actuel.Attaque
        user_Défense_base = User_actuel.Défense
        user_Vitesse_base = User_actuel.Vitesse
        user = User_actuel
        user.PM = userPM

        
        randomint = randrange(user.LV - 4, user.LV + 1)
        if randomint < 1 :
            randomint = 1

        choix_monstre(user, randomint, User_actuel, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, user_PV, vérif_equipement)

    else :

        user.PM = user_PM_Max
        ShowMenu(user)


def menu(user, action):

    global User_actuel
    global user_PV_Max
    global user_PM_Max
    global user_Attaque_base
    global user_Défense_base
    global user_Vitesse_base
    global user_PV
    global vérif_equipement
    
    if action == "combat" :
        
        randomint = randrange(user.LV - 4, user.LV + 1)
        if randomint < 1 :
            randomint = 1

        choix_monstre(user, randomint, User_actuel, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, user_PV, vérif_equipement)

    elif action == "boutique" :

        ShowBoutique(user)


    elif action == "inventaire":

        ShowChoixInventaire(user)


    elif action == "quitter" :
        print("stop")

    else :
        menu(user)

