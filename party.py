# -*- coding: latin-1 -*-

# Define a 'party' class, which consists of 6 pokemon_instance objects
class party:
    def __init__(self,p1,p2,p3,p4,p5,p6):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6

    def print_party(self):
        print('1: ' + str(self.p1))
        print('2: ' + str(self.p2))
        print('3: ' + str(self.p3))
        print('4: ' + str(self.p4))
        print('5: ' + str(self.p5))
        print('6: ' + str(self.p6))


def getParty(member_no):
    print("hello")
    # Open the party db/file
    
    # Load the party member
    # currentHP = db.getCurrentHP(member_no)
    # currentHPMax = db.getCurrentHPMax(member_no)
    # ...
    # party_member = classes.combatant('name','stats 1', 'stats 2'...)
    # return party_member
    # 