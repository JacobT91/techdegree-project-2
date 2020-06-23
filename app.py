import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
num_players_team = int(round(len(constants.PLAYERS) / len(constants.TEAMS)))

# This line creates a teams dict()
# teams_cleaned = []
# teams_dict = dict.fromkeys(teams, [])

experienced = []
inexperienced = []
holding_area = []
sorted_teams = []


def clean_data():
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = bool('T') if i['experience'] == 'YES' else bool()
        i['guardians'] = i['guardians'].split(' and ')
        experienced.append(i) if i['experience'] == True else inexperienced.append(i)
    

def balance_teams():
    for num, key in enumerate(teams):
        add_team = {
            key: []
        }
        sorted_teams.append(add_team)
        holding_area.clear()
        print(holding_area)
        while len(holding_area) < num_players_team:
            
            rand_player_ex = random.choice(experienced)
            holding_area.append(rand_player_ex)
            experienced.remove(rand_player_ex)

            rand_player_in = random.choice(inexperienced)
            holding_area.append(rand_player_in)
            inexperienced.remove(rand_player_in)
        
        sorted_teams[num] = holding_area






        
        
        
        
            

if __name__ == "__main__":
    clean_data()
    balance_teams()
    

