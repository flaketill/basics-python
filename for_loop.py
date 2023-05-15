#!/usr/bin/env python3


def get_team_members(*members):
	team = []
	
	
	for index, member in enumerate(members):
		team.append(f"{index} - {member}")
		
	return ', '.join(team)


def get_team_members_list(*members):
    team = []
    
    
    for index in range(1, len(members)+1):
        team.append(f"{index}")
        
    return '\n '.join(team)


def get_team_info_rows(*members):
    team_info = []
    members = members
    rows = [ index for index in range(1, len(members)+1)]

    
    for member, row  in zip(members,rows):
        team_info.append(f"{row} - {member}")
        
    return '\n '.join(team_info)


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")


    print(f"\n Exists the next rows: \n {get_team_members_list('Armando', 'Danna', 'Keyra', 'Dante')}")


    print(f"\n The team info: \n {get_team_info_rows('Armando', 'Danna', 'Keyra', 'Dante')}")
