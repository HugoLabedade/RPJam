class Monstres(object) :
    
    def __init__( self, id, nom, Puissance, Magique_Physique, Autres, id_Famille_Efficace, id_effet, Pourcentage_Effet, Description, id_type, PM_Utilisé) :

        self.id = id
        self.nom = nom
        self.Puissance = Puissance
        self.Magique_Physique = Magique_Physique
        self.Autres = Autres
        self.id_Famille_Efficace = id_Famille_Efficace
        self.id_effet = id_effet
        self.Pourcentage_Effet = Pourcentage_Effet
        self.Description = Description
        self.id_type = id_type
        self.PM_Utilisé = PM_Utilisé


    def __str__( self ) :
        return ("{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10}".format(
            self.id,
            self.nom, 
            self.Puissance,
            self.Magique_Physique,
            self.Autres,
            self.id_Famille_Efficace,
            self.id_effet,
            self.Pourcentage_Effet,
            self.Description,
            self.id_type,
            self.PM_Utilisé))
         