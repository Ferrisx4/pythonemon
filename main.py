from pkmn_classes import *
from combat import combat

# This is where the magic begins.

# Asks the user for their Pokémon and the foe's Pokémon
def user_options():
    pokemon1 = input("Please type the name of the Pokémon you want to use: ")
    pokemon2 = input("Please type the name of the Pokémon used by the foe: ")
    return [pokemon1, pokemon2]

def mainLoop():
    the_pokemon = user_options()

mainLoop()