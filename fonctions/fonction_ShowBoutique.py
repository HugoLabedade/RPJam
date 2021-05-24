from création_fenetre_jeu import frameBase
from fonctions.fonction_clear_frame import clear_frame
from tkinter import *
from fonctions.fonction_boutique import boutique
import tkinter.font as tkFont
from fonctions.fonction_achat_boutique import achat_boutique


def ShowBoutique(user) :

    clear_frame()
    
    # mise en place du canvas
    canvas_1 = Canvas(frameBase, width=1280, height=720)
    bg = PhotoImage(file="assets/bg.png")
    canvas_1.create_image(0, 0, image=bg, anchor="nw")
    canvas_1.pack()
    font = tkFont.Font(family='Helvetica', size=15)

    liste_boutique = boutique()

    
    if user.LV <= 10 :
        
        achat1 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[0][0].nom, liste_boutique[0][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[0]), font=font, height=1, width=16)
        achat1.place(x=30, y=620)
        achat2 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[1][0].nom, liste_boutique[1][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[1]), font=font, height=1, width=16)
        achat2.place(x=30, y=670)
        achat3 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[5][0].nom, liste_boutique[5][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[5]), font=font, height=1, width=16)
        achat3.place(x=230, y=620)
        achat4 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[12][0].nom, liste_boutique[12][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[12]), font=font, height=1, width=16)
        achat4.place(x=230, y=670)
        achat5 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[27][0].nom, liste_boutique[27][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[27]), font=font, height=1, width=16)
        achat5.place(x=430, y=620)
        achat6 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[31][0].nom, liste_boutique[31][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[31]), font=font, height=1, width=16)
        achat6.place(x=430, y=670)
        achat7 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[35][0].nom, liste_boutique[35][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[35]), font=font, height=1, width=16)
        achat7.place(x=630, y=620)
        achat8 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[39][0].nom, liste_boutique[39][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[39]), font=font, height=1, width=16)
        achat8.place(x=630, y=670)
        achat9 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[43][0].nom, liste_boutique[43][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[43]), font=font, height=1, width=16)
        achat9.place(x=830, y=620)
        achat10 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[47][0].nom, liste_boutique[47][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[47]), font=font, height=1, width=16)
        achat10.place(x=830, y=670)

    elif user.LV > 10 and user.LV <= 20 :
        
        achat1 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[2][0].nom, liste_boutique[2][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[2]), font=font, height=1, width=16)
        achat1.place(x=30, y=620)
        achat2 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[3][0].nom, liste_boutique[3][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[3]), font=font, height=1, width=16)
        achat2.place(x=30, y=670)
        achat3 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[4][0].nom, liste_boutique[4][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[4]), font=font, height=1, width=16)
        achat3.place(x=230, y=620)
        achat4 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[6][0].nom, liste_boutique[6][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[6]), font=font, height=1, width=16)
        achat4.place(x=230, y=670)
        achat5 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[7][0].nom, liste_boutique[7][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[7]), font=font, height=1, width=16)
        achat5.place(x=430, y=620)
        achat6 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[13][0].nom, liste_boutique[13][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[13]), font=font, height=1, width=16)
        achat6.place(x=430, y=670)
        achat7 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[14][0].nom, liste_boutique[14][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[14]), font=font, height=1, width=16)
        achat7.place(x=630, y=620)
        achat8 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[15][0].nom, liste_boutique[15][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[15]), font=font, height=1, width=16)
        achat8.place(x=630, y=670)
        achat9 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[16][0].nom, liste_boutique[16][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[16]), font=font, height=1, width=16)
        achat9.place(x=830, y=620)
        achat10 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[18][0].nom, liste_boutique[18][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[18]), font=font, height=1, width=16)
        achat10.place(x=830, y=670)

    elif user.LV > 20 and user.LV <= 30 :
        
        achat1 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[8][0].nom, liste_boutique[8][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[8]), font=font, height=1, width=16)
        achat1.place(x=30, y=620)
        achat2 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[9][0].nom, liste_boutique[9][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[9]), font=font, height=1, width=16)
        achat2.place(x=30, y=670)
        achat3 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[10][0].nom, liste_boutique[10][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[10]), font=font, height=1, width=16)
        achat3.place(x=230, y=620)
        achat4 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[19][0].nom, liste_boutique[19][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[19]), font=font, height=1, width=16)
        achat4.place(x=230, y=670)
        achat5 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[28][0].nom, liste_boutique[28][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[28]), font=font, height=1, width=16)
        achat5.place(x=430, y=620)
        achat6 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[32][0].nom, liste_boutique[32][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[32]), font=font, height=1, width=16)
        achat6.place(x=430, y=670)
        achat7 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[36][0].nom, liste_boutique[36][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[36]), font=font, height=1, width=16)
        achat7.place(x=630, y=620)
        achat8 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[40][0].nom, liste_boutique[40][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[40]), font=font, height=1, width=16)
        achat8.place(x=630, y=670)
        achat9 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[44][0].nom, liste_boutique[44][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[44]), font=font, height=1, width=16)
        achat9.place(x=830, y=620)
        achat10 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[48][0].nom, liste_boutique[48][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[48]), font=font, height=1, width=16)
        achat10.place(x=830, y=670)

    elif user.LV > 30 and user.LV <= 40 :
        
        achat1 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[10][0].nom, liste_boutique[10][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[10]), font=font, height=1, width=16)
        achat1.place(x=30, y=620)
        achat2 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[11][0].nom, liste_boutique[11][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[11]), font=font, height=1, width=16)
        achat2.place(x=30, y=670)
        achat3 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[20][0].nom, liste_boutique[20][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[20]), font=font, height=1, width=16)
        achat3.place(x=230, y=620)
        achat4 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[21][0].nom, liste_boutique[21][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[21]), font=font, height=1, width=16)
        achat4.place(x=230, y=670)
        achat5 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[29][0].nom, liste_boutique[29][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[29]), font=font, height=1, width=16)
        achat5.place(x=430, y=620)
        achat6 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[33][0].nom, liste_boutique[33][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[33]), font=font, height=1, width=16)
        achat6.place(x=430, y=670)
        achat7 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[37][0].nom, liste_boutique[37][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[37]), font=font, height=1, width=16)
        achat7.place(x=630, y=620)
        achat8 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[41][0].nom, liste_boutique[41][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[41]), font=font, height=1, width=16)
        achat8.place(x=630, y=670)
        achat9 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[45][0].nom, liste_boutique[45][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[45]), font=font, height=1, width=16)
        achat9.place(x=830, y=620)
        achat10 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[49][0].nom, liste_boutique[49][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[49]), font=font, height=1, width=16)
        achat10.place(x=830, y=670)

    elif user.LV > 40 :
        
        achat1 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[22][0].nom, liste_boutique[22][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[22]), font=font, height=1, width=16)
        achat1.place(x=30, y=620)
        achat2 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[23][0].nom, liste_boutique[23][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[23]), font=font, height=1, width=16)
        achat2.place(x=30, y=670)
        achat3 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[24][0].nom, liste_boutique[24][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[24]), font=font, height=1, width=16)
        achat3.place(x=230, y=620)
        achat4 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[25][0].nom, liste_boutique[25][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[25]), font=font, height=1, width=16)
        achat4.place(x=230, y=670)
        achat5 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[26][0].nom, liste_boutique[26][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[26]), font=font, height=1, width=16)
        achat5.place(x=430, y=620)
        achat6 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[30][0].nom, liste_boutique[30][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[30]), font=font, height=1, width=16)
        achat6.place(x=430, y=670)
        achat7 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[34][0].nom, liste_boutique[34][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[34]), font=font, height=1, width=16)
        achat7.place(x=630, y=620)
        achat8 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[38][0].nom, liste_boutique[38][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[38]), font=font, height=1, width=16)
        achat8.place(x=630, y=670)
        achat9 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[42][0].nom, liste_boutique[42][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[42]), font=font, height=1, width=16)
        achat9.place(x=830, y=620)
        achat10 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[46][0].nom, liste_boutique[46][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[46]), font=font, height=1, width=16)
        achat10.place(x=830, y=670)
        achat11 = Button(frameBase, text="{0} : {1} Golds".format(liste_boutique[50][0].nom, liste_boutique[50][1]), borderwidth=1, activebackground="#80ad72", bg="#80ad72", command=lambda: achat_boutique(user, liste_boutique[50]), font=font, height=1, width=16)
        achat11.place(x=1030, y=620)

    frameBase.mainloop()

