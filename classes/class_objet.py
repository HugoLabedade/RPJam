class Objet(object) :
    
    def __init__( self, id, nom, Description, sprite_name) :

        self.id = id
        self.nom = nom
        self.Description = Description
        self.sprite_name = sprite_name


    def __str__( self ) :
        return ("{0} {1} {2} {3}".format(
            self.id,
            self.nom,
            self.Description,
            self.sprite_name))


