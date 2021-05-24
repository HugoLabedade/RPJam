from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_lancement_menu_combat as jeu
from fonctions.fonction_ShowCompétence import ShowCompétences
from fonctions.fonction_Attaque_user import Attaque_user
from fonctions.fonction_ShowObjet import ShowObjets


def ShowCombat(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement) :
    #Ici svp
    global frameBase

    print("montstre PV : {0}".format(monstre_PV))
    print("user PV : {0}".format(user_PV))

    clear_frame()

    
    
    # mise en place du canvas
    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()

    font = tkFont.Font(family='Helvetica', size=15)

    labelvie_monstre = Label(frameBase, text="PV : {0}/{1}".format(monstre_PV, monstre_PV_Max), background="#7acbf9", font=font)
    labelvie_monstre.place(x=1000, y=175)

    labelvie_user = Label(frameBase, text="PV : {0}/{1}".format(user_PV, user_PV_Max), background="#7acbf9", font=font)
    labelvie_user.place(x=50, y=175)
    labelvie_monstre = Label(frameBase, text="PM : {0}/{1}".format(user.PM, user_PM_Max), background="#7acbf9", font=font)
    labelvie_monstre.place(x=50, y=250)

    # init des sprites
    sprite_gentil = PhotoImage(file="assets/Jam.gif")
    sprite_mechant = PhotoImage(file="assets/monstres/{0}.png".format(monstre_actuel.sprite_name))
    canvas_1.create_image(250, 500, image=sprite_gentil)
    canvas_1.create_image(1000, 450, image=sprite_mechant)

    # les boutons d'attaque
    canvas_1.create_rectangle(25, 610, 500, 715)
    font = tkFont.Font(family='Helvetica', size=15)

    boutonAttaques = Button(frameBase, text="Attaques", borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: Attaque_user(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=20)
    boutonAttaques.place(x=30, y=620)

    boutonCompetences = Button(frameBase, text="Competences", borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: ShowCompétences(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=20)
    boutonCompetences.place(x=270, y=620)

    boutonObjets = Button(frameBase, text="Objets", borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: ShowObjets(user, monstre_actuel, monstre_PV, monstre_PV_Max, user_PV, user_PV_Max, user_PM_Max, user_Attaque_base, user_Défense_base, user_Vitesse_base, vérif_equipement), font=font, height=1, width=20)
    boutonObjets.place(x=30, y=670)

    frameBase.mainloop()
