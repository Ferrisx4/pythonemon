# -*- coding: latin-1 -*-
from pkmn_classes import *
from combat import combat

# This is a series of functions to test the actual functions of the program

def test_pokemon_creation():
    pikachu = pokemon_instance('Pikachu', 50)
    pikachu.printParty()
    pikachu.setMoves( [0] )
    pikachu.printMoves()
    foe = pokemon_instance('Goldeen', 30)
    foe.printParty()

def test_type_effectiveness():
    print('Electric vs Goldeen: ')
    print(combat.calculate_effectiveness('Electric','Water',None))
    print('Electric vs Diglett: ')
    print(combat.calculate_effectiveness('Electric','Ground','Rock'))
    print('Electric vs Gyarados: ')
    print(combat.calculate_effectiveness('Electric','Water','Flying'))
    print('Electric vs Bellsprout: ')
    print(combat.calculate_effectiveness('Electric','Grass',None))

def test_move_import():
    from ROM import moves
    print('Imported ' + str(len(moves)) + ' moves.')
    print(moves[0].name + ' has ' + moves[0].accuracy + '% accuracy.')

def mainLoop():
    test_pokemon_creation()

    print('====================')

    test_type_effectiveness()
    
    print('====================')

    test_move_import()

mainLoop()