from création_fenetre_jeu import frameBase

def clear_frame() :
    global frameBase

    for widget in frameBase.winfo_children():
        widget.destroy()
