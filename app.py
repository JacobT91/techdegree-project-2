import constants
import copy

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)


def clean_data():
    #Loops through list of dict
    for player in players:
        #Replace letter charactors with empty string value
        h_task = player['height'].replace(' inches', '')
        
        #If, El, creates a bool value from a key value
        if player['experience'] == 'YES':
            bool_task = bool('TRUE')

        else:
            bool_task = bool()
        

        print(int(h_task), bool_task)

        


clean_data()