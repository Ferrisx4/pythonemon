w, h = 5, 5
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

def combat():
    return 0
    
def calculate_damage():
    return 0

def calculate_effectiveness(move_type, defender_type1, defender_type2):
    effectiveness = 1
    # Defender Type 1
    try:
        effectiveness = effectiveness * Ef1[move_type][defender_type1]
    except KeyError:
        #print "Unknown type or type effectiveness, assuming 1x"
        pass
        
    # Defender Type 1
    try:
        effectiveness = effectiveness * Ef1[move_type][defender_type2]
    except KeyError:
        #print "Unknown type or type effectiveness, assuming 1x"
        pass
        
    
    return effectiveness