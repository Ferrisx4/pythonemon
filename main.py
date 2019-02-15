from pkmn_classes import *
from combat import *

def mainLoop():
    pikachu = pokemon('Pikachu', 50)
    pikachu.printParty()
    
    foe = pokemon('Goldeen', 30)
    foe.printParty()
    
    print 'Electric vs Goldeen: '
    print calculate_effectiveness('Electric','Water',None)
    print 'Electric vs Diglett: '
    print calculate_effectiveness('Electric','Ground','Rock')
    print 'Electric vs Gyarados: '
    print calculate_effectiveness('Electric','Water','Flying')
    print 'Electric vs Bellsprout: '
    print calculate_effectiveness('Electric','Grass',None)
        
mainLoop()