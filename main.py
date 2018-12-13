import classes
import combat
from myGraphics import *

def mainLoop():
    pikachu = classes.combatant('Pikachu', 50)
    pikachu.printParty()
    
    foe = classes.combatant('Goldeen', 30)
    foe.printParty()
    
    #drawSquares()
    drawLineCurve()
        
    
mainLoop()