class User(object) :

    def __init__( self, id, pseudo, password, classe, points_de_compétences, LV, PV, PM, Attaque, Puissance_Magique, Défense, Résistance_Magique, Vitesse, Esquive, Golds, XP_For_Next_LV, XP ) :

        self.id = id
        self.pseudo = pseudo
        self.password = password
        self.classe = classe
        self.points_de_compétences = points_de_compétences
        self.LV = LV
        self.PV = PV
        self.PM = PM
        self.Attaque = Attaque
        self.Puissance_Magique = Puissance_Magique
        self.Défense = Défense
        self.Résistance_Magique = Résistance_Magique
        self.Vitesse = Vitesse
        self.Esquive = Esquive
        self.Golds = Golds
        self.XP_For_Next_LV = XP_For_Next_LV
        self.XP = XP


    def __str__( self ) :
        return ("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16}".format(
            self.id, 
            self.pseudo,
            self.password,
            self.classe,
            self.points_de_compétences,
            self.LV, 
            self.PV,
            self.PM,
            self.Attaque,
            self.Puissance_Magique,
            self.Défense,
            self.Résistance_Magique,
            self.Vitesse,
            self.Esquive,
            self.Golds,
            self.XP_For_Next_LV,
            self.XP
            ))




