from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_lancement_menu_combat as jeu

def ShowMenu(user) :
    
    clear_frame()

    font = tkFont.Font(family='Helvetica', size=15)

    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.create_text(640, 200, text="RPJam", font=font)
    canvas_1.pack()
    
    # boutons pour changer de vues
    sword = PhotoImage(file="assets/sword.png")
    boutonSword = Button(frameBase, image=sword, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: jeu.menu(user, "combat"))
    boutonSword.place(x=410, y=270)

    coin = PhotoImage(file="assets/coin.png")
    boutonCoin = Button(frameBase, image=coin, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: jeu.menu(user, "boutique"))
    boutonCoin.place(x=610, y=270)

    backpack = PhotoImage(file="assets/backpack.png")
    boutonBackpack = Button(frameBase, image=backpack, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: jeu.menu(user, "inventaire"))
    boutonBackpack.place(x=810, y=270)

    frameBase.mainloop()
