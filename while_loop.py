#!/usr/bin/env python3


def get_team_members(*members):
    team = []
    index = 0
    
    
    while index < len(members):
        team.append(f"{index} - {members[index]}")
        index += 1
    
    return ', '.join(team)


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")
    