# -*- coding: latin-1 -*-
# Keep track of an individual Pokémon, like what would be in the player's party or PC
class pokemon_instance:
    def __init__(self,species,level,status,moves):
        self.species = species
        self.level = level
        self.status = "0"
        #self.hp = pokemon.getBaseHP(species, level)
        self.moves = (None,None,None,None)
    
    # TODO does this make sense to have here?
    def printParty(self):
        print(self.level, self.species)

    def __str__(self):
        return('Pokemon: ' + self.species + ' \tLevel: ' + str(self.level))

    def printMoves(self):
        from ROM import moves
        print(self.species + '\'s moves:')
        for move in self.moves:
            try:
                print(moves[move].name)
            except:
                print('-')
    
    """
    Get and set this Pokémon's moves
    Parameters: array with 1 to 4 elements indicating move IDs
    """
    def getMoves(self):
        #this is where the moves would be gotten from
        return self.moves

    def setMoves(self, moveset):
        #this is where the moves would be set
        self.moves = moveset

    # Looks up the value of the HP for the Pythonemon by species and level
    @staticmethod
    def getBaseHP(species, level):
        return 50

# Define a class that keeps track of all Generic data for a Pokémon species, i.e. Bulbasaur
class pokemon_data:
    def __init__(self,species,type1,type2,baseHP,baseAttack,baseDefense,baseSpecialAttack,baseSpecialDefense,baseSpeed,experience_group,dex_info,dex_no):
        self.species = species
        self.type1 = type1
        self.type2 = type2
        self.baseHP = baseHP
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpecialAttack = baseSpecialAttack
        self.baseSpecialDefense = baseSpecialDefense
        self.baseSpeed = baseSpeed
        self.experience_group = experience_group
        self.dex_info = dex_info
        self.dex_no = dex_no

    # Define how to print this class for users. Probably useless
    def __str__(self):
        return 'I am a ' + self.species

    # Define how to print this class for debugging. Probably not useless. We'll see...
    def __repr__(self):
        return self.species + ' are in the ' + self.experience_group + ' experience group.'

    # Define some getters and setters
    def get_baseStatTotal(self):
        return self.baseHP + self.baseAttack + self.baseDefense + self.baseSpecialAttack + self.baseSpecialDefense + self.baseSpeed

    def get_types(self):
        return [self.type1, self.type2]

    # Checks the legality of a move
    def check_move_legality(self, move, level):
        return True

# Define a class that keeps track of info for a move
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