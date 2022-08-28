# Status Conditions

 - Non-volatile
    - Burn
    - Freeze
    - Paralysis
    - Poison
    - Poison 2.0
    - Sleep
 - Volatile
    - Bound
    - Trapped
    - Confusion
    - Curse
    - Flinch

# Data Designs

## Pokémon

Pokémon Instance:
 - Individual Pokémon with nickname, OT, etc.
 - Outside of battle

|Name    |      Type|
|---|---:|
Nickname|string
Species|int
Level|int
Experience|int
Moves|array of ints
MovePP|array of ints
Status|array
OT ID|int
HP|int
Attack|int
Defense|int
Special Attack|int
Special Defense|int
Speed|int
IVs|array
EVs|array

Pokémon Species
 - Default stats and Pokédexy-type info

|Name    |      Type|
|---|---:|
DexID|int
Name|string
Type1|int
Type2|int
BaseHP|int
BaseAttack|int
BaseDefense|int
BaseSpecialAttack|int
BaseSpecialDefense|int
BaseSpeed|int
learnset|array


Moves

|Name|Type|
|---|---:|
Name|string
Type|string
PP|int
Accuracy|int
Power|int
Effects|array of ints
