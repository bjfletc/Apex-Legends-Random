from unique_legends import *
from apex_weapons import *

players = get_players()
selected_legends_for_players = legends_to_play_as()
selected_weapons = weapons_to_play_with()

# needed to iterate through selected_weapons list while going through dictionary.
index = 0
for player, legend in selected_legends_for_players.items():

    weapon_1 = selected_weapons[index]
    weapon_2 = selected_weapons[index + 1]

    print("{:10}: {:20}: {:20}: {}".format(player, legend, weapon_1, weapon_2))

    index = index + 2
