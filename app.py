import constants
import copy

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


def clean_data():
    for data in players:
        print(int(data['height'].replace('inches', '')))
        


clean_data()