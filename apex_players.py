# module that contains a dictionary of the current friends I play Apex Legends with, and theri
# locked characters.

players_and_their_locked_characters = {'Brandon': [],
                                       'Dakota': ["Horizon", "Seer", "Mad Maggie", "Newcastle", "Catalyst"],
                                       'Ryan': ["Rampart", "Horizon", "Ash", "Mad Maggie", "Newcastle",
                                                "Catalyst"],
                                       'Tanner': []}


# function used to return the list of locked characters for a given player
def get_players_locked_characters(player_name):
    return players_and_their_locked_characters.get(player_name)


# returns list of player names
def get_players():

    player_names = []

    for player in players_and_their_locked_characters.keys():
        player_names.append(player)

    return player_names
