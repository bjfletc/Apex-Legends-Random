# module that holds a list of the current weapons available in Apex Legends.

from unique_list import *
from apex_players import *
import random

weapons = ["HAVOC", "Flatline", "Hemlock", "R-301",
           "Alternator", "Prowler", "R-99", "Volt",
           "C.A.R.", "Devotion", "L-Star", "Spitfire", "Rampage",
           "G7 Scout", "Triple Take", "30-30", "Bocek", "Charge Rifle",
           "Longbow", "Sentinel", "Kraber", "EVA-8", "Mozambique",
           "Peacekeeper", "Mastiff", "RE-45", "P2020", "Wingman",
           "Care Package Weapons", "Grenades", "Fists"]

# COMPLETED(1): Create function that only returns non-care package weapons.
care_package_weapons = ["Bocek", "Kraber", "Rampage", "RE-45"]


def weapons_to_play_with():
    unique_weapons_list = generate_unique_list(weapons, len(get_players()) * 2)

    # convert from integers to weapon names
    for i in range(0, len(unique_weapons_list)):
        unique_weapons_list[i] = weapons[unique_weapons_list[i]]

    # go through to check if weapon is a care package weapon
    for j in range(0, len(unique_weapons_list)):

        while unique_weapons_list[j] in care_package_weapons:

            random_weapon = random.randint(0, len(weapons) - 1)
            if weapons[random_weapon] in unique_weapons_list:
                random_weapon = random.randint(0, len(weapons) - 1)
            else:
                unique_weapons_list[j] = weapons[random_weapon]

    return unique_weapons_list
