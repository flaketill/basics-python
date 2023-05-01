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


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")


    print(f"\n Exists the next rows: \n {get_team_members_list('Armando', 'Danna', 'Keyra', 'Dante')}")

    
