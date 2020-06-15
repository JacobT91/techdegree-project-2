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


def clean_data():
    #Loops through list of dict
    for player in players:
        #Replace letter charactors with empty string value
        player['height'] = player['height'].replace(' inches', '')
        
        #If, Else, creates a bool value from a key value and adds players to a list
        player['experience'] = bool("TRUE") if player['experience'] == 'YES' else bool()
        experienced.append(player) if player['experience'] == bool('TRUE') else inexperienced.append(player)
        

#Balances teams randomly by experience bool statement
def balance_team(x_team):
    while len(x_team) < 6 :
        rand_player = random.choice(experienced)
        x_team.append(rand_player)
        experienced.remove(rand_player)
        rand_player = random.choice(inexperienced)
        x_team.append(rand_player)
        inexperienced.remove(rand_player)
        







clean_data()
balance_team(panthers)
balance_team(bandits)
balance_team(warriors)

print(f'Panthers:\n{panthers}\n\nBandits:\n{bandits}\n\nWarriors:\n{warriors}')
