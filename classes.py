class combatant:
    def __init__(self,species,level):
        #partyLoadout = ['1', '4', '9'] #List of IDs to stored Pythonemons
        self.species = species
        self.level = level
        self.status = "0"
        self.hp = combatant.getBaseHP(species, level)
        self.moves = (5,0,0,0)
    
    def printParty(self):
        print self.level, self.species
    
    # Looks up the value of the HP for the pokemon by species and level
    @staticmethod
    def getBaseHP(species, level):
        return 50