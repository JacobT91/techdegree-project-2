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
        
        #If, Else, creates a bool value from a key value and adds play to a list
        player['experience'] = bool("TRUE") if player['experience'] == 'YES' else bool()
        experienced.append(player) if player['experience'] == bool('TRUE') else inexperienced.append(player)
        

        
def balance_team():
    while len(experienced) > 0 :
        random_player1 = random.choice(experienced) 
        panthers.append(random_player1)
        experienced.remove(random_player1)

        random_player2 = random.choice(experienced) 
        bandits.append(random_player2)
        experienced.remove(random_player2)

        random_player3 = random.choice(experienced) 
        warriors.append(random_player3)
        experienced.remove(random_player3)




clean_data()
balance_team()
print(f'Panthers:\n{panthers}\n\nBandits:\n{bandits}\n\nWarriors:\n{warriors}')
