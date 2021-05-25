from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
from fonctions.fonction_print_objets import print_objets
import fonctions.fonction_lancement_menu_combat as jeu

def ShowObjets(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement):
    global frameBase

    clear_frame()
    
    # mise en place du canvas
    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()

    font = tkFont.Font(family='Helvetica', size=15)

    # init des sprites
    sprite_gentil = PhotoImage(file="assets/Jam.gif")
    sprite_mechant = PhotoImage(file="assets/monstres/{0}.png".format(monstre_actuel.sprite_name))
    canvas_1.create_image(250, 500, image=sprite_gentil)
    canvas_1.create_image(1000, 450, image=sprite_mechant)


    liste_objets_inventaire = print_objets(user.id)
    lenght = len(liste_objets_inventaire)

    if lenght == 0 :
        print("0")
    elif lenght == 1 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
    elif lenght == 2 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)

    elif lenght == 3 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)

    elif lenght == 4 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)

    elif lenght == 5 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)

    elif lenght == 6 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)

    elif lenght == 7 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)

    elif lenght == 8 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)
        objet8 = Button(frameBase, text="{0}".format(liste_objets_inventaire[7].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[7], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet8.place(x=630, y=670)

    elif lenght == 9 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)
        objet8 = Button(frameBase, text="{0}".format(liste_objets_inventaire[7].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[7], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet8.place(x=630, y=670)
        objet9 = Button(frameBase, text="{0}".format(liste_objets_inventaire[8].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[8], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet9.place(x=830, y=620)

    elif lenght == 10 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)
        objet8 = Button(frameBase, text="{0}".format(liste_objets_inventaire[7].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[7], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet8.place(x=630, y=670)
        objet9 = Button(frameBase, text="{0}".format(liste_objets_inventaire[8].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[8], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet9.place(x=830, y=620)
        objet10 = Button(frameBase, text="{0}".format(liste_objets_inventaire[9].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[9], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet10.place(x=830, y=670)

    elif lenght == 11 :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)
        objet8 = Button(frameBase, text="{0}".format(liste_objets_inventaire[7].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[7], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet8.place(x=630, y=670)
        objet9 = Button(frameBase, text="{0}".format(liste_objets_inventaire[8].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[8], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet9.place(x=830, y=620)
        objet10 = Button(frameBase, text="{0}".format(liste_objets_inventaire[9].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[9], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet10.place(x=830, y=670)
        objet11 = Button(frameBase, text="{0}".format(liste_objets_inventaire[10].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[10], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet11.place(x=1030, y=620)

    else :
        objet1 = Button(frameBase, text="{0}".format(liste_objets_inventaire[0].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[0], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet1.place(x=30, y=620)
        objet2 = Button(frameBase, text="{0}".format(liste_objets_inventaire[1].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[1], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet2.place(x=30, y=670)
        objet3 = Button(frameBase, text="{0}".format(liste_objets_inventaire[2].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[2], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet3.place(x=230, y=620)
        objet4 = Button(frameBase, text="{0}".format(liste_objets_inventaire[3].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[3], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet4.place(x=230, y=670)
        objet5 = Button(frameBase, text="{0}".format(liste_objets_inventaire[4].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[4], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet5.place(x=430, y=620)
        objet6 = Button(frameBase, text="{0}".format(liste_objets_inventaire[5].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[5], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet6.place(x=430, y=670)
        objet7 = Button(frameBase, text="{0}".format(liste_objets_inventaire[6].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[6], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet7.place(x=630, y=620)
        objet8 = Button(frameBase, text="{0}".format(liste_objets_inventaire[7].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[7], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet8.place(x=630, y=670)
        objet9 = Button(frameBase, text="{0}".format(liste_objets_inventaire[8].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[8], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet9.place(x=830, y=620)
        objet10 = Button(frameBase, text="{0}".format(liste_objets_inventaire[9].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[9], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet10.place(x=830, y=670)
        objet11 = Button(frameBase, text="{0}".format(liste_objets_inventaire[10].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[10], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet11.place(x=1030, y=620)
        objet12 = Button(frameBase, text="{0}".format(liste_objets_inventaire[11].nom), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: jeu.combat(user, monstre_actuel, "Objet", liste_objets_inventaire[11], monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=16)
        objet12.place(x=1030, y=670)
    

    frameBase.mainloop()
