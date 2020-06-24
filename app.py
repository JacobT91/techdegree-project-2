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
        experienced.append(i) if i['experience'] == bool('T')\
            else inexperienced.append(i)


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


def stats_tool():
    sep = ', '
    print('\nBASKETBALL TEAM STATS TOOL\n')
    print('---- MENU----\n')
    while True:
        print(
            'Here are your choices:\n'
            '1) Display Team Stats\n'
            '2) Quit\n'
        )

        try:
            menu_opt = int(input('Enter an option > '))

        except ValueError:
            print('\nYour options are > 1 - 2\nPlease try agian...\n')
            continue

        print()
        if menu_opt >= 3:
            print('That is not a valid option. Please try agian...\n')
            continue

        elif menu_opt == 2:
            print('Quiting...\n')
            exit()

        elif menu_opt == 1:
            while True:
                for num, team in enumerate(teams, 1):
                    print(f'{num}) {team}')

                print()

                try:
                    menu_opt = menu_opt = int(input('Enter an option > '))

                except ValueError:
                    print('\nYour options are > 1 - {}\nPlease try agian...\n'.format(len(teams)))
                    continue

                if menu_opt > len(teams):
                    print(
                        '\nThat is not a valid option.'
                        ' Please try agian...\n'
                    )
                    continue

                if menu_opt <= len(teams):
                    input_team = sorted_teams[menu_opt - 1]
                    team_names = []
                    team_heights = []
                    team_exper = 0
                    team_inexper = 0
                    team_guard = []

                    for num in range(0, len(input_team['players'])):
                        team_names.append(input_team['players'][num]['name'])
                        team_heights.append(
                            input_team['players'][num]['height']
                        )
                        team_guard += input_team['players'][num]['guardians']

                        if input_team['players'][num]['experience'] == \
                                bool('T'):
                            team_exper += 1

                        elif input_team['players'][num]['experience'] == \
                                bool():
                            team_inexper += 1

                    print()
                    print(f'Team: {teams[menu_opt - 1]} stats')
                    print('-' * 20)
                    print(f'Total players: {len(team_names)}\n')
                    print('Total experienced: {}'.format(team_exper))
                    print('Total inexperienced: {}'.format(team_inexper))
                    print('Average height: {}\n'.format(
                        round(sum(team_heights) / len(team_heights), 1)
                        )
                    )

                    print('Players on team:\n   {}\n'.format(
                        sep.join(team_names)
                        )
                    )
                    print('Guardians:\n   {}\n'.format(sep.join(team_guard)))
                    input('Press enter to continue... ')
                    print()
                    break


if __name__ == "__main__":
    clean_data()
    sort_teams(sorted_teams)
    balance_teams(sorted_teams)
    stats_tool()
