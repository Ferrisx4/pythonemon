from pkmn_classes import *
from combat import *

def mainLoop():
    pikachu = pokemon('Pikachu', 50)
    pikachu.printParty()
    
    foe = pokemon('Goldeen', 30)
    foe.printParty()
    
    print calculate_effectiveness('Fire','Grass','Water')
        
mainLoop()