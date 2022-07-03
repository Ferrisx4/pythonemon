# -*- coding: latin-1 -*-
from pkmn_classes import pokemon_instance
from combat import combat
from party import *

# This is a series of functions to test the actual functions of the program

def test_pokemon_creation():
    from ROM import pokemon_dict
    # Get an instance of a Pokémon
    pokemon_1_instance = pokemon_instance('Ivysaur', 50)
    # Get the data for that Pokémon
    pokemon_1_data=pokemon_dict[pokemon_1_instance.species]

    # Explore the new Pokémon
    pokemon_1_instance.setMoves( [0,1] )
    pokemon_1_instance.printMoves()
    #print('Types: ' + pokemon_1_data.get_types()[0] + ', ' + pokemon_1_data.get_types()[1])
    print(repr(pokemon_1_data))
    print(pokemon_1_data)
    print(pokemon_1_data.get_types())
    foe = pokemon_instance('Goldeen', 30)

    # Put the pokemon_instance into a party, print it.
    my_party = party(pokemon_1_instance,None,None,None,None,None)
    my_party.print_party()

def test_type_effectiveness():
    print('Electric vs Goldeen: ')
    print(combat.calculate_effectiveness('Electric','Water',None))
    print('Electric vs Diglett: ')
    print(combat.calculate_effectiveness('Electric','Ground','Rock'))
    print('Electric vs Gyarados: ')
    print(combat.calculate_effectiveness('Electric','Water','Flying'))
    print('Electric vs Bellsprout: ')
    print(combat.calculate_effectiveness('Electric','Grass',None))
    #combat.do_move(3,scene)
def test_move_import():
    from ROM import moves
    print('Imported ' + str(len(moves)) + ' moves.')
    print(moves[0].name + ' has ' + moves[0].accuracy + '% accuracy.')

def test_party_import():
    my_party = loadParty()
    my_party.print_party()

def mainLoop():
    test_pokemon_creation()

    print('====================')

    test_type_effectiveness()
    
    print('====================')

    test_move_import()

    print('====================')

    test_party_import()

mainLoop()