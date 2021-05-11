import tkinter as tk
import tkinter.font as tkFont

hauteur = 720
largeur = 1280

class Jeu(tk.Tk) :
    def __init__(self):
        tk.Tk.__init__(self)
        self.bg = tk.PhotoImage(file="assets/bg.png")
        self.label1 = tk.Label(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Menu, Combat):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("Menu")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class Combat(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # mise en place du canvas
        self.canvas_1 = tk.Canvas(self, width=largeur, height=hauteur)
        self.bg = tk.PhotoImage(file="assets/bg.png")
        self.canvas_1.create_image(0, 0, image=self.bg, anchor="nw")
        self.canvas_1.pack()

        # init des sprites
        self.sprite_gentil = tk.PhotoImage(file="assets/Jam.gif")
        self.sprite_mechant = tk.PhotoImage(file="assets/mechant1.png")       
        self.canvas_1.create_image(250, 500, image=self.sprite_gentil)
        self.canvas_1.create_image(1000, 450, image=self.sprite_mechant)
    
class Menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # mise en place du canvas
        self.canvas_1 = tk.Canvas(self, width=largeur, height=hauteur)
        self.bg = tk.PhotoImage(file="assets/bg.png")
        self.canvas_1.create_image(0, 0, image=self.bg, anchor="nw")
        font = tkFont.Font(family='Helvetica', size=36)
        self.canvas_1.create_text(640, 200, text="RPJam", font=font)
        self.canvas_1.pack()
        
        # boutons pour changer de vues
        self.sword = tk.PhotoImage(file="assets/sword.png")
        self.boutton = tk.Button(self, image=self.sword, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: controller.show_frame("Combat"))
        self.boutton.place(x = 410, y = 270)

        self.coin = tk.PhotoImage(file="assets/coin.png")
        self.boutton2 = tk.Button(self, image=self.coin, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: controller.show_frame("Combat"))
        self.boutton2.place(x=610, y=270)

        self.backpack = tk.PhotoImage(file="assets/backpack.png")
        self.boutton3 = tk.Button(self, image=self.backpack, borderwidth=0, activebackground="#7acbf9", bg="#7acbf9", command=lambda: controller.show_frame("Combat"))
        self.boutton3.place(x=810, y=270)
        

if __name__ == "__main__":
    app = Jeu()
    app.mainloop()
