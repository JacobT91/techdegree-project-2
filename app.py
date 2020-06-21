import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
num_players_team = int(round(len(constants.PLAYERS) / len(constants.TEAMS)))

# This line creates a teams dict()
teams_dict = dict.fromkeys(teams, [])

experienced = []
inexperienced = []


def clean_data():
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = bool('T') if i['experience'] == 'YES' else bool()
        i['guardians'] = i['guardians'].split(' and ')
        experienced.append(i) if i['experience'] == True else inexperienced.append(i)
        

# Please help me write this function. I was told I have to use the teams list to create either a dict() or list() to add players to
def balance_teams():




        
        
        
        
            

if __name__ == "__main__":
    clean_data()
    balance_teams()

