import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)
num_players_team = int(round(len(constants.PLAYERS) / len(constants.TEAMS)))
experienced = []
inexperienced = []
sorted_teams = []


def clean_data():
    random.shuffle(players)
    for i in players:
        i['height'] = int(i['height'].replace(' inches', ''))
        i['experience'] = bool('T') if i['experience'] == 'YES' else bool()
        i['guardians'] = i['guardians'].split(' and ')
        experienced.append(i) if i['experience'] == True else inexperienced.append(i)
    

def sort_teams(team_list):
    for key in (teams):
        add_team = {
            'team': key,
            'players': []
        }
        team_list.append(add_team)
        
    return team_list


def balance_teams(team_list):
    for num in range(0, len(teams)):
        while len(team_list[num]['players']) < num_players_team:
            team_list[num]['players'].append(experienced.pop())
            team_list[num]['players'].append(inexperienced.pop())





# def stats_tool():
#     sep = ', '
#     print('\nBASKETBALL TEAM STATS TOOL\n')
#     print('---- MENU----\n')
#     while True:
#         print(
#         'Here are your choices:\n'
#         '1) Display Team Stats\n'
#         '2) Quit\n'
#         )
#         menu_opt = int(input('Enter an option > '))
#         print()
        
#         if menu_opt == 2:
#             print('Quiting...\n')
#             exit()

#         elif menu_opt == 1:
#             for num, team in enumerate(teams, 1):
#                 print(f'{num}) {team}')

#             print()
#             menu_opt = menu_opt = int(input('Enter an option > '))
#             input_team = sorted_teams[menu_opt - 1]
#             team_exper = 0
#             team_inexper = 0
#             team_names = [i['name'] for i in input_team]
#             team_heights = [i['height'] for i in input_team]
#             average_height = round(sum(team_heights) / len(input_team), 1)
#             team_guard = [sep.join(i['guardians']) for i in input_team]
#             for i in input_team:
#                 if i['experience'] == bool('TRUE'):
#                     team_exper += 1

#                 elif i['experience'] == bool():
#                     team_inexper += 1

#             print()
#             print(f'Team: {teams[menu_opt - 1]} stats')
#             print('-' * 20)
#             print(f'Total players: {len(input_team)}\n')
#             print('Total experienced: {}'.format(team_exper))
#             print('Total inexperienced: {}'.format(team_inexper))
#             print('Average height: {}\n'.format(average_height))
            
#             print('Players on team:\n   {}\n'.format(sep.join(team_names)))
#             print('Guardians:\n   {}\n'.format(team_guard))
#             input('Press enter to continue... ')
#             print()
#             continue






        
        
        
        
            

if __name__ == "__main__":
    clean_data()
    sort_teams(sorted_teams)
    balance_teams(sorted_teams)
    for name in sorted_teams[0]['players']:
        print(name['name'])
    print()
    for name in sorted_teams[1]['players']:
        print(name['name'])

    # for num, team in enumerate(sorted_teams):
    #     print(team[teams[num]][0])
    # # stats_tool()
    
