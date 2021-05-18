from fonctions.variables import *
from fonctions.fonction_heal import heal

def compétence_sans_dommages(max_pv_user, compétence) :
    
    PV_heal = 0
    print("autre")

    Boost_Esquive = False
    Count_Boost_Esquive = 0
    Aura_de_peur = False
    Count_Aura_de_peur = 0
    Souffle_du_sage = False
    Count_Souffle_du_sage = 0
    Psychocanalisation = False
    Count_Psychocanalisation = 0
    Clic_clac_zap = False
    Count_Clic_clac_zap = 0
    Grâce_de_la_Déesse = False
    Count_Grâce_de_la_Déesse = 0
    Cercle_du_carnage = False
    Count_Cercle_du_carnage = 0
    Poison_ennemi = False
    Count_Poison_ennemi = 0
    Confusion_ennemi = False
    Count_Confusion_ennemi = 0
    Brûlure_ennemi = False
    Count_Brûlure_ennemi = 0
    Sommeil_ennemi = False
    Count_Sommeil_ennemi = 0
    Décuplo = False
    Count_Décuplo = 0
    Protection = False
    Count_Protection = 0
    Hâte = False
    Count_Hâte = 0

    if compétence.id == 8 or compétence.id == 9 or compétence.id == 10 :
        PV_heal = heal(max_pv_user, compétence)


    elif compétence.id == 15 :
        Boost_Esquive = True
        Count_Boost_Esquive = 3

    elif compétence.id == 18 :
        Aura_de_peur = True
        Count_Aura_de_peur = 4

    elif compétence.id == 19 :
        Souffle_du_sage = True
        Count_Souffle_du_sage = 10

    elif compétence.id == 20 :
        Psychocanalisation = True
        Count_Psychocanalisation = 4

    elif compétence.id == 24 :
        Clic_clac_zap = True
        Count_Clic_clac_zap = 10

    elif compétence.id == 25 :
        Grâce_de_la_Déesse = True
        Count_Grâce_de_la_Déesse = 15
    
    elif compétence.id == 30 :
        Cercle_du_carnage = True
        Count_Cercle_du_carnage = 8

    elif compétence.id == 44 :
        Poison_ennemi = True
        Count_Poison_ennemi = 3

    elif compétence.id == 45 :
        Confusion_ennemi = True
        Count_Confusion_ennemi = 3

    elif compétence.id == 46 :
        Brûlure_ennemi = True
        Count_Brûlure_ennemi = 5

    elif compétence.id == 47 :
        Sommeil_ennemi = True
        Count_Sommeil_ennemi = 3

    elif compétence.id == 57 :
        Décuplo = True
        Count_Décuplo = 5

    elif compétence.id == 58 :
        Protection = True
        Count_Protection = 5

    elif compétence.id == 59 :
        Hâte = True
        Count_Hâte = 15

        
    return(PV_heal, compétence.PM_Utilisé, Boost_Esquive, Count_Boost_Esquive, Aura_de_peur, Count_Aura_de_peur, Souffle_du_sage, 
    Count_Souffle_du_sage, Psychocanalisation, Count_Psychocanalisation, Clic_clac_zap, Count_Clic_clac_zap, Grâce_de_la_Déesse, 
    Count_Grâce_de_la_Déesse, Cercle_du_carnage, Count_Cercle_du_carnage, Poison_ennemi, 
    Count_Poison_ennemi, Confusion_ennemi, Count_Confusion_ennemi, Brûlure_ennemi, Count_Brûlure_ennemi,Sommeil_ennemi, Count_Sommeil_ennemi,
    Décuplo, Count_Décuplo, Protection, Count_Protection, Hâte, Count_Hâte)
