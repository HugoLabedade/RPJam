
from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_lancement_menu_combat as jeu
from fonctions.fonction_inventaire import inventaire
from fonctions.fonction_ShowChoixGestionArmure import ShowChoixGestionArmure
import fonctions.fonction_ShowMenu as back

def ShowChoixInventaire(user) :

    clear_frame()
    
    # mise en place du canvas
    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()

    font = tkFont.Font(family='Helvetica', size=15)

    boutonInscrip = Button(frameBase, text="Voir l'inventaire d'objet", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: inventaire(user, 1, None), font=font, height=1, width=20)
    boutonInscrip.place(x=400, y=250)
    boutonConnex = Button(frameBase, text="Gérer l'équipement", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: ShowChoixGestionArmure(user), font=font, height=1, width=20)
    boutonConnex.place(x=600, y=250)

    retour = Button(frameBase, text="Retour", borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: back.ShowMenu(user), font=font, height=1, width=16)
    retour.place(x=1030, y=30)

    frameBase.mainloop()
