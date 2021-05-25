from tkinter import *
import tkinter.font as tkFont

fenetre = Tk()
fenetre.title("RPJam")
fenetre.geometry("1280x720")

frameBase = Frame(fenetre)
frameBase.pack()

canvas_1 = Canvas(frameBase, width=1280, height=720)
bg = PhotoImage(file="assets/bg.png")
canvas_1.create_image(0, 0, image=bg, anchor="nw")
canvas_1.pack()

