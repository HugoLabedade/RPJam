class Armure(object) :
    
    def __init__( self, id, nom, type_armure, stat_boost, bonus_stat, sprite_name) :

        self.id = id
        self.nom = nom
        self.type_armure = type_armure
        self.stat_boost = stat_boost
        self.bonus_stat = bonus_stat
        self.sprite_name = sprite_name


    def __str__( self ) :
        return ("{0} {1} {2} {3} {4} {5}".format(
            self.id,
            self.nom,
            self.type_armure,
            self.stat_boost,
            self.bonus_stat,
            self.sprite_name))

            
