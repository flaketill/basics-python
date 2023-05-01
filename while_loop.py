#!/usr/bin/env python3


def get_team_members(*members):
    team = []
    index = 0
    
    
    while index < len(members):
        team.append(f"{index} - {members[index]}")
        index += 1
    
    return ', '.join(team)


def get_team_info_rows(*members):
    team_info = []
    members = members
    rows = [ index for index in range(1, len(members)+1)]
    index = 0

    
    while index < len(members):
        team_info.append(f"{rows[index]} - {members[index]}")
        index += 1
        
    return '\n '.join(team_info)


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")

    print(f"\n The team info: \n {get_team_info_rows('Armando', 'Danna', 'Keyra', 'Dante')}")
