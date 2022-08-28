# -*- coding: latin-1 -*-
import csv
from pkmn_classes import pokemon_instance

# Does party have to be a class at all? For convenience, sure

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


def loadParty():
    # Open the party db/file
    with open('data/party.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        imported_party_members = 0
        temp_party = []
        # Load each party member
        for row in csv_reader:
            temp_party.append(pokemon_instance(row["species"],row["nickname"],row["level"],row["status"],[row["move1"],row["move2"],row["move3"],row["move4"]]))
            imported_party_members += 1

        for x in range(imported_party_members+1, 7):
            temp_party.append(pokemon_instance(None,None,None,[None,None,None,None]))
        print('Imported ' + str(imported_party_members) + ' into the party.')
    # Add them to an official party class
        return party(temp_party[0],temp_party[1],temp_party[2],temp_party[3],temp_party[4],temp_party[5])


    # ...
    # party_member = classes.combatant('name','stats 1', 'stats 2'...)
    # return party_member
    # 