class Monstres(object) :

    def __init__( self, id, nom, LV, PV, PM, Attaque, Puissance_Magique, Défense, Résistance_Magique, Vitesse, Golds_Give, XP_Give, id_Famille, sprite_name) :

        self.id = id
        self.nom = nom
        self.LV = LV
        self.PV = PV
        self.PM = PM
        self.Attaque = Attaque
        self.Puissance_Magique = Puissance_Magique
        self.Défense = Défense
        self.Résistance_Magique = Résistance_Magique
        self.Vitesse = Vitesse
        self.Golds_Give = Golds_Give
        self.XP_Give = XP_Give
        self.id_Famille = id_Famille
        self.sprite_name = sprite_name

    def __str__( self ) :
        return ("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13}".format(
            self.id,
            self.nom, 
            self.LV, 
            self.PV, 
            self.PM, 
            self.Attaque, 
            self.Puissance_Magique, 
            self.Défense, 
            self.Résistance_Magique, 
            self.Vitesse, 
            self.Golds_Give, 
            self.XP_Give, 
            self.id_Famille, 
            self.sprite_name))
         