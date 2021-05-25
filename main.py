# -*- coding: utf-8 -*-
from tkinter import *
import fonctions.fonction_lancement_menu_combat as jeu
import socket

#lancement

hote = "localhost"
port = 15555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))


jeu.lancement()
