from unique_list import *
from apex_legends import *
from apex_players import *
import random

players = get_players()
unique_list_of_legends = generate_unique_list(legends, len(players))
selected_legends_for_players = {}

# convert unique list of ints to unique list of legend names
for i in range(0, len(unique_list_of_legends)):

    unique_list_of_legends[i] = legends[unique_list_of_legends[i]]

# verifies that the legend isn't locked for the player
for j in range(0, len(players)):

    player = players[j]
    legend = unique_list_of_legends[j]
    random_legend = ""

    for locked_legend in players_and_their_locked_characters.get(player):

        if legend == locked_legend:
            random_legend = legends[random.randint(0, len(legends) - 1)]

            while random_legend in unique_list_of_legends:
                random_legend = legends[random.randint(0, len(legends) - 1)]

            unique_list_of_legends[j] = random_legend


# returns a dictionary of player name : legend
def legends_to_play_as():

    for k in range(0, len(players)):
        selected_legends_for_players.update({players[k]: unique_list_of_legends[k]})

    return selected_legends_for_players
