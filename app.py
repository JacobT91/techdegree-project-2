import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

teams_dict = {}


def clean_data():
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = [bool('T') if i['experience'] == 'YES' else bool()]
        i['guardians'] = i['guardians'].split(' and ')
        

def balance_teams(teams_list):
    clean_teams = {k: v for k, v in enumerate(teams, 1)}
    teams_dict.update(clean_teams)
    


    
        
    
    

    
    
        
    







if __name__ == "__main__":
    clean_data()
    balance_teams(teams)
