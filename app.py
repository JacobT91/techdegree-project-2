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
        experienced.append(i) if i['experience'] == bool('T') \
            else inexperienced.append(i)


def sort_teams(team_list):
    for key in (teams):
        add_team = {
            'team': key,
            'names': [],
            'heights': [],
            'guardians': [],
            'experience': 0,
            'inexperience': 0,
            'players': []
        }
        team_list.append(add_team)


def balance_teams(team_list):
    for num in range(0, len(teams)):
        while len(team_list[num]['players']) < num_players_team:
            team_list[num]['players'].append(experienced.pop())
            team_list[num]['players'].append(inexperienced.pop())


def get_stats(team_list, opt):
    for num in range(0, len(team_list['players'])):
        team_list['names'].append(team_list['players'][num]['name'])
        team_list['heights'].append(team_list['players'][num]['height'])
        team_list['guardians'] += team_list['players'][num]['guardians']

        if team_list['players'][num]['experience'] == bool('T'):
            team_list['experience'] += 1

        elif team_list['players'][num]['experience'] == bool():
            team_list['inexperience'] += 1


def print_stats(team_list, opt):
    sep = ', '
    print(f'Team: {teams[opt - 1]} stats')
    print('-' * 20)
    print('Total players: {}\n'.format(len(team_list['names'])))
    print('Total experienced: {}'.format(team_list['experience']))
    print('Total inexperienced: {}'.format(team_list['inexperience']))
    print('Average height: {}\n'.format(round(
        sum(team_list['heights']) / len(team_list['heights']), 1)))

    print('Players on team:\n   {}\n'.format(sep.join(team_list['names'])))
    print('Guardians:\n   {}\n'.format(sep.join(team_list['guardians'])))


def stats_tool():
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
            print('\nYour options are > 1 - 2./nPlease try agian...\n')
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
                    menu_opt = int(input('Enter an option > '))

                except ValueError:
                    print('\nYour options are > 1 - 2./nPlease try agian...\n')
                    continue

                if menu_opt > len(teams) or menu_opt <= 0:
                    print(
                        '\nThat is not a valid option.',
                        'Please try agian...\n')
                    continue

                if menu_opt <= len(teams):
                    input_team = sorted_teams[menu_opt - 1]
                    get_stats(input_team, menu_opt)
                    print_stats(input_team, menu_opt)
                    print()
                    input('Press enter to continue... ')
                    print()
                    break


if __name__ == "__main__":
    clean_data()
    sort_teams(sorted_teams)
    balance_teams(sorted_teams)
    stats_tool()
