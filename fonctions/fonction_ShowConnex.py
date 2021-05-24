
from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_lancement_menu_combat as jeu

def showConnex():

    clear_frame()

    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()
    
    font = tkFont.Font(family='Helvetica', size=15)

    #input de la connexion
    labelPseudo = Label(frameBase, text="Pseudo", background="#7acbf9", font=font)
    labelPseudo.place(x=500, y=225)
    inputPseudo = Entry(frameBase)
    inputPseudo.place(x=600, y=225)

    labelPassw = Label(frameBase, text="Mot de Passe", background="#7acbf9", font=font)
    labelPassw.place(x=440, y=260)
    inputPassw = Entry(frameBase, show="*")
    inputPassw.place(x=600, y=260)

    boutonConnect = Button(frameBase, text="Connexion", command=lambda: jeu.connexion(inputPseudo.get(), inputPassw.get()))
    boutonConnect.place(x=600, y=300)

    frameBase.mainloop()


