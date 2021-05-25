from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_inventaire as next
import fonctions.fonction_ShowChoixInventaire as back


def ShowChoixGestionArmure(user) :
    
    clear_frame()

    font = tkFont.Font(family='Helvetica', size=15)

    # mise en place du canvas
    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()

    boutonInscrip = Button(frameBase, text="Gérer son arme", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: next.inventaire(user, 2, 1), font=font, height=1, width=20)
    boutonInscrip.place(x=400, y=250)
    boutonConnex = Button(frameBase, text="Gérer ses armures", borderwidth=0, activebackground="#7acbf9",
                        background="#7acbf9", command= lambda: next.inventaire(user, 2, 2), font=font, height=1, width=20)
    boutonConnex.place(x=600, y=250)

    retour = Button(frameBase, text="Retour", borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: back.ShowChoixInventaire(user), font=font, height=1, width=16)
    retour.place(x=1030, y=30)

    frameBase.mainloop()

