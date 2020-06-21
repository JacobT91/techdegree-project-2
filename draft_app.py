import constants
import copy
import random

teams = copy.deepcopy(constants.TEAMS)
players = copy.deepcopy(constants.PLAYERS)

experienced = []
inexperienced = []

panthers = []
bandits = []
warriors = []


# Reformats players height, guardians, and experience from players list
def clean_data():
    for player in players:
        # Replaces letter characters with empty string value
        player['height'] = player['height'].replace(' inches', '')
        player['height'] = int(player['height'])
        # If, Else, creates a bool value from a key
        # value and adds players to a list
        player['experience'] = bool("TRUE") if player['experience'] == 'YES' else bool()
        experienced.append(player) if player['experience'] == bool('TRUE') else inexperienced.append(player)
        # Split up the guardian string into a List
        player['guardians'] = player['guardians'].split(' and ')


# Selects players randomly by experience bool statement
def random_player(x_team):
    rand_player = random.choice(experienced)
    x_team.append(rand_player)
    experienced.remove(rand_player)
    rand_player2 = random.choice(inexperienced)
    x_team.append(rand_player2)
    inexperienced.remove(rand_player2)


# Assigns random players to specified teams
def balance_team(p_team, b_team, w_team):
    while len(experienced) and len(inexperienced) != 0:
        random_player(p_team)
        random_player(b_team)
        random_player(w_team)


def stats_tool():
    print('\nBASKETBALL TEAM STATS TOOL')

    while True:
        print('\n\n------- MENU -------\n')
        print('\nHere are you choices:\n1) Display team stats\n2) Quit\n')

        while True:
            try:
                menu_opt = int(input('Enter an option > '))
                if menu_opt < 1 or menu_opt > 2:
                    raise ValueError('That value is outside of the range.')

            except ValueError as err:
                print('\n\n({})'.format(err))
                print('Your options are > [1 - 2]\n')
                continue

            else:
                if menu_opt == 2:
                    print('\nQuitting...\n')
                    exit()

                elif menu_opt == 1:
                    print(
                        '\nPick your team:\n'
                        '1) Panthers\n'
                        '2) Bandits\n'
                        '3) Warriors\n'
                    )
            while True:
                try:
                    menu_opt = int(input('Enter an option > '))
                    if menu_opt < 1 or menu_opt > 3:
                        raise ValueError('That value is outside of the range.')

                except ValueError as err:
                    print('\n\n{}'.format(err))
                    print('Your options are > [1 - 3]\n\n')\

                else:
                    if menu_opt == 1:
                        input_team = panthers
                        print('\nTeam: Panthers Stats')

                    elif menu_opt == 2:
                        input_team = bandits
                        print('\nTeam: Bandits Stats')

                    elif menu_opt == 3:
                        input_team = warriors
                        print('\nTeam: Warriors Stats')

                    team_exper = int()
                    team_inexper = int()
                    sep = ', '

                    for i in input_team:
                        if i['experience'] == bool('TRUE'):
                            team_exper += 1

                        elif i['experience'] == bool():
                            team_inexper += 1

                    team_height = [i['height'] for i in input_team]
                    team_names = [i['name'] for i in input_team]
                    team_guard = [sep.join(i['guardians']) for i in input_team]
                    team_names = sep.join(team_names)

                    print('-' * 20)
                    print('Total players: {}'.format(len(input_team)))
                    print('Total experienced: {}'.format(team_exper))
                    print('Total inexperienced: {}'.format(team_inexper))
                    print('Average height: {}'.format(round(sum(team_height) /
                          len(team_height), 1))
                          )
                    print('\n\nPlayers on Team:\n  {}.\n\n'.format(team_names))
                    print('Guardians:\n  {}.\n\n'.format(sep.join(team_guard)))
                    input("Press [ENTER] to continue...")
                    break
            break

if __name__ == "__main__":
    clean_data()
    balance_team(panthers, bandits, warriors)
    stats_tool()