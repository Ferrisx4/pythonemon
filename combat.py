w, h = 5, 5;
Ef = [[0 for x in range(w)] for y in range(h)] 
Ef['Fire']['Water'] = 0.5
Ef['Fire']['Bug'] = 2

def combat():
    return 0
    
def calculate_damage():
    return 0

def calculate_effectiveness(move_type, foe_type1, foe_type2):
    return Ef['Fire']['Water']