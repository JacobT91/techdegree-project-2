import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

num_players_team = int(round(len(constants.PLAYERS) / len(constants.TEAMS)))
teams_dict = dict.fromkeys(teams, {})
experienced = []
inexperienced = []


def clean_data():
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = bool('T') if i['experience'] == 'YES' else bool()
        i['guardians'] = i['guardians'].split(' and ')
        experienced.append(i) if i['experience'] == True else inexperienced.append(i)
        

def balance_teams():
    for v in teams_dict.values():
        while len(v) != num_players_team:
            rand_player = random.choice(experienced)
            v.update(rand_player)
            experienced.remove(rand_player)
            rand_player_2 = random.choice(inexperienced)
            v.update(rand_player_2)
            experienced.remove(rand_player_2)

        


# def balance_teams(teams_list):
    # clean_teams = {k: v for k, v in enumerate(teams, 1)}
    # teams_dict.update(clean_teams)
    
    # for k, v in teams_dict:

    
        # if len(i) == num_players_team:
        # rand_player = random.choice(experienced)
        # i.update(rand_player)
        # experienced.remove(rand_player)
            # rand_player2 = random.choice(inexperienced)
            # i.update(rand_player2)
            # inexperienced.remove(rand_player2)
        


        
        
        
        
            

if __name__ == "__main__":
    clean_data()
    balance_teams()
    print(teams_dict)
    
