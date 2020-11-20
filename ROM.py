# -*- coding: latin-1 -*-
import csv
from pkmn_classes import *

'''
        Type effectiveness
'''
# Declare an array to hold move type effectiveness values
# Example Ef['Fire']['Water] = 0.5 (Fire is attacking, Water is defending)
#Ef = [[0 for x in range(w)] for y in range(h)] 
#Ef1['Fire']['Water'] = 0.5
#Ef1['Fire']['Bug']   = 2.0
#Ef1['Fire']['Flying] = 1.0 (caught by KeyError)

# Ef1 = Type Effectiveness based on Generation 1
Ef1 = {
    'Normal' : {
        'Rock':0.5,
        'Ghost':0
    },
    'Fighting' : {
        'Normal':2.0,
        'Flying':0.5,
        'Poison':0.5,
        'Rock':2.0,
        'Bug':0.5,
        'Ghost':0,
        'Psychic':0.5,
        'Ice':2.0
    },
    'Flying' : {
        'Fight':2.0,
        'Rock':0.5,
        'Bug':2.0,
        'Grass':2.0,
        'Electric':0.5
    },
    'Poison' : {
        'Poison':0.5,
        'Ground':0.5,
        'Rock':0.5,
        'Bug':2.0,
        'Ghost':0.5,
        'Grass':2.0
    },
    'Ground' : {
        'Flying':0,
        'Poison':2.0,
        'Rock':2.0,
        'Bug':0.5,
        'Fire':2.0,
        'Grass':0.5,
        'Electric':2.0
    },
    'Rock' : {
        'Fight':0.5,
        'Flying':2.0,
        'Ground':0.5,
        'Bug':2.0,
        'Fire':2.0,
        'Ice':2.0
    },
    'Bug'  : {
        'Fighting':0.5,
        'Flying':0.5,
        'Poison':2.0,
        'Ghost':0.5,
        'Fire':0.5,
        'Grass':2.0,
        'Psychic':2.0
    },
    'Ghost' : {
        'Normal':0,
        'Ghost':2.0,
        'Psychic':0
    },
    'Fire' : {
        'Rock':0.5,
        'Bug':2.0,
        'Fire':0.5,
        'Water':0.5,
        'Grass':2.0,
        'Ice':2.0,
        'Dragon':0.5             
    },
    'Water' : {
        'Ground':2.0,
        'Rock':2.0,
        'Fire':2.0,
        'Water':0.5,
        'Grass':0.5,
        'Dragon':0.5
    },
    'Grass' : {
        'Flying':0.5,
        'Poison':0.5,
        'Ground':2.0,
        'Rock':2.0,
        'Bug':0.5,
        'Fire':0.5,
        'Water':2.0,
        'Grass':0.5,
        'Dragon':0.5
    },
    'Electric' : {
        'Flying':2.0,
        'Ground':0,
        'Water':2.0,
        'Grass':0.5,
        'Electric':0.5,
        'Dragon':0.5
    },
    'Psychic' : {
        'Fight':2.0,
        'Poison':2.0,
        'Psychic':0.5
    },
    'Ice' : {
        'Flying':2.0,
        'Ground':2.0,
        'Water':0.5,
        'Grass':2.0,
        'Ice':0.5,
        'Dragon':2.0
    },
    'Dragon' : {
        'Dragon':2.0
    }
}

# Get the move data from a file.

with open('data/moves.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    imported_moves = 0
    moves = []
    for row in csv_reader:
        # Create new move instance from data in CSV
        #Moves stored as such: name,type,class,power,accuracy,pp,priority,crit
        moves.append(move(row["name"],row["type"],row["class"],row["power"],row["accuracy"],row["pp"],row["priority"],row["crit"]))
        imported_moves += 1
    print('Imported ' + str(imported_moves) + ' moves.')


#
# Pokémon Data
#

# Get the Pokémon data from the .csv file

with open('data/pokemon.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    imported_pokemon = 0
    pokemon_list = []
    for row in csv_reader:
        # Create new Pokémon instance from data in CSV
        # Pokémon stored as such: species,type1,type2,base_hp,base_attack,base_defense,base_sa,base_sd,base_speed,experience_curve,dex_info,dex_no
        pokemon_list.append(pokemon_data(row["species"],row["type1"],row["type2"],row["base_hp"],row["base_attack"],row["base_defense"],row["base_sa"],row["base_sd"],row["base_speed"],row["experience_curve"],row["dex_info"],row["dex_no"],))
        imported_pokemon += 1
    print('Imported ' + str(imported_pokemon) + ' Pokémon.')