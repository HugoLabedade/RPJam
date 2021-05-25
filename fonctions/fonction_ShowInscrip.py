from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
import tkinter.font as tkFont
from création_fenetre_jeu import frameBase
import fonctions.fonction_lancement_menu_combat as jeu


classe_user = ""

def showInscrip():

    clear_frame()

    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()

    #input de la connexion
    font = tkFont.Font(family='Helvetica', size=15)

    labelPseudo = Label(frameBase, text="Pseudo", background="#7acbf9", font=font)
    labelPseudo.place(x=500, y=175)
    inputPseudo = Entry(frameBase)
    inputPseudo.place(x=600, y=175)

    labelPassw = Label(frameBase, text="Mot de Passe", background="#7acbf9", font=font)
    labelPassw.place(x=440, y=200)
    inputPassw = Entry(frameBase, show="*")
    inputPassw.place(x=600, y=200)

    guerrier = PhotoImage(file="assets/guerrier.png")
    boutonGuerrier = Button(frameBase, image=guerrier, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: classe("Guerrier"))
    boutonGuerrier.place(x=410, y=240)

    mage = PhotoImage(file="assets/mage.png")
    boutonMage = Button(frameBase, image=mage, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: classe("Mage"))
    boutonMage.place(x=580, y=240)

    assassin = PhotoImage(file="assets/assassin.png")
    boutonAssassin = Button(frameBase, image=assassin, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: classe("Assassin"))
    boutonAssassin.place(x=750, y=240)

    boutonInscrip = Button(frameBase, text="Inscription", command=lambda: jeu.create_user(inputPseudo.get(), inputPassw.get(), classe_user))
    boutonInscrip.place(x=600, y=400)

    frameBase.mainloop()

def classe(input) :
    global classe_user
    classe_user = input