from random import randrange

def critique(degats, chances_crit) :
    randomint = randrange(1, 101) 
    if randomint <= chances_crit :
        degats *= 2

    return(degats)