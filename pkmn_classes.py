# -*- coding: latin-1 -*-
# Keep track of an individual Pokémon, like what would be in the player's party or PC
class pokemon_instance:
    def __init__(self,species,level):
        #partyLoadout = ['1', '4', '9'] #List of IDs to stored Pythonemons
        self.species = species
        self.level = level
        self.status = "0"
        #self.hp = pokemon.getBaseHP(species, level)
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
    def __init__(self,species,type1,type2,baseHP,baseAttack,baseDefense,baseSpecialAttack,baseSpecialDefense,baseSpeed,ability,experience_group,learnset):
        self.species = species
        self.type1 = type1
        self.type2 = type2
        self.baseHP = baseHP
        self.baseAttack = baseAttack
        self.baseDefense = baseDefense
        self.baseSpecialAttack = baseSpecialAttack
        self.baseSpecialDefense = baseSpecialDefense
        self.baseSpeed = baseSpeed
        self.ability = ability
        self.experience_group = experience_group
        self.learnset = learnset

    # Define some getters and setters
    def get_baseStatTotal(self):
        return self.baseHP + self.baseAttack + self.baseDefense + self.baseSpecialAttack + self.baseSpecialDefense + self.baseSpeed


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