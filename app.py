import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

experienced = []
inexperienced = []

panthers = []
bandits = []
warriors = []

# Reformats players height and experience from players list
def clean_data():
    for player in players:
        # Replaces letter characters with empty string value
        player['height'] = player['height'].replace(' inches', '')
        
        # If, Else, creates a bool value from a key value and adds players to a list
        player['experience'] = bool("TRUE") if player['experience'] == 'YES' else bool()
        experienced.append(player) if player['experience'] == bool('TRUE') else inexperienced.append(player)
        

# Selects players randomly by experience bool statement
def random_player(x_team):
    rand_player = random.choice(experienced)
    x_team.append(rand_player)
    experienced.remove(rand_player)
    rand_player2 = random.choice(inexperienced)
    x_team.append(rand_player2)
    inexperienced.remove(rand_player2)


# Assigns random players to specified teams
def balance_team(p_team, b_team, w_team):
    while len(experienced) and len(inexperienced) != 0:
        random_player(p_team)
        random_player(b_team)
        random_player(w_team)
        

def stats_tool():
    print('\nBASKETBALL TEAM STATS TOOL\n')
    print('\n---- MENU ----\n')
    print('\nHere are you choices:\n1) Display team stats\n2) Quit\n')
    while True:
        try:
            menu_opt = int(input('Enter an option > '))
            print()
        except:
            print('\n\nThat is not a valid option')
            print('Your options are > [1] or > [2]\n\n')
            continue
        
        if menu_opt == 2:
            print('\nQuitting...\n')
            break
        
        elif menu_opt == 1:
            print('Pick your team:\n1) Panthers\n2) Bandits\n3) Warriors')
            menu_opt = input('Enter an option > ')

        else:
            print('\n\nThat is not a valid option\n\n')
            continue
        


clean_data()
balance_team(panthers, bandits, warriors)
stats_tool()
# print(f'\nPlayers on Panthers: {len(panthers)}\n{panthers}\n')
# print(f'\nPlayers on Bandits: {len(bandits)}\n{bandits}\n')
# print(f'\nPlayers on Warriors: {len(warriors)}\n{warriors}\n')