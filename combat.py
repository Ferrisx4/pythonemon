# -*- coding: latin-1 -*-

import random
class combat:
    def __init__(self,party1,party2):
        self.p1 = party1
        self.p2 = party2
        # Define stat changes for this battle
        self.c1_sc = (0,0,0,0,0)
        self.turn = 0

    @staticmethod
    def calculate_effectiveness(move_type, defender_type1, defender_type2):
        from ROM import Ef1
        effectiveness = 1
        # Defender Type 1
        try:
            effectiveness = effectiveness * Ef1[move_type][defender_type1]
        except KeyError:
            #print "Unknown type or type effectiveness, assuming 1x"
            pass
            
        # Defender Type 2
        try:
            effectiveness = effectiveness * Ef1[move_type][defender_type2]
        except KeyError:
            #print "Unknown type or type effectiveness, assuming 1x"
            pass
            
        
        return effectiveness

    @staticmethod
    def calculate_damage(level, power, attack, defense, movetype, target_type1, target_type2):
        # Damage formula: (basically Generation 1 but using type split from generation 4+)
        # damage =   (((((2 * level * Critical) / 5) + 2) * (power * (attack/defense)) / 50) + 2 ) * modifier
        # level:  attacker's level
        # Critical: 1 normal, 2 if critical
        # 
        # modifier = rand(0.85,1) * STAB * type_effectiveness()
        #return 0

        # Save time, is the move effective?
        effectiveness = combat.calculate_effectiveness(movetype, target_type1, target_type2)
        if effectiveness == 0:
            return 0
        # Looks like the move is not useless, continue calculating damage
        modifier = random.uniform(0.85,1.0)
        damage = ((((( 2 * level ) / 5 ) + 2) * ( power * (attack/defense)) / 50) + 2) * modifier
        return damage

    # 
    # Takes into consideration whether the move still has PP, is not disabled, and is not blocked
    #  by other conditions of the 'scene'.

    @staticmethod
    def do_move(move, scene):
        """Attempts to perform a move. This is after the game has confirmed the move can be performed."""
        return 0