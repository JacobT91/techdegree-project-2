import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


def clean_data():
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = [bool('T') if i['experience'] == 'YES' else bool()]
        i['guardians'] = i['guardians'].split(' and ')
        
        
def balance_teams():
    # for i in teams:
    for i, team in enumerate(teams, 1):
        print("{}) {}".format(i, team['name']))        
        
    








clean_data()
balance_teams()
# print(teams)