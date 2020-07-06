# -*- coding: latin-1 -*-
class pokemon:
    def __init__(self,species,level):
        #partyLoadout = ['1', '4', '9'] #List of IDs to stored Pythonemons
        self.species = species
        self.level = level
        self.status = "0"
        self.hp = pokemon.getBaseHP(species, level)
        self.moves = (None,None,None,None)
    
    def printParty(self):
        print(self.level, self.species)

    def printMoves(self):
        from ROM import moves
        print(self.species + '\'s moves:')
        for move in self.moves:
            try:
                print(moves[move].name)
            except:
                print('-')
    
    """
    Set this Pokémon's moves
    Parameters: array with 1 to 4 elements indicating move IDs
    """
    def getMoves(self):
        #this is where the moves would be gotten from
        print('hi')

    def setMoves(self):
        #this is where the moves would be set
        print('hi')

    # Looks up the value of the HP for the Pythonemon by species and level
    @staticmethod
    def getBaseHP(species, level):
        return 50
        
class move:
    def __init__(self,name,move_type,move_class,power,accuracy,pp,priority,critical_hit_ratio):
        self.name = name
        self.move_type = move_type
        self.move_class = move_class
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority
        self.critical_hit_ratio = critical_hit_ratio
    
    # handle special case moves ()
    def special_cases(self,name,conditions):
        return 0