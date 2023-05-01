#!/usr/bin/env python3


def get_team_members(*members):
	team = []
	
	
	for index, member in enumerate(members):
		team.append(f"{index} - {member}")
		
	return ', '.join(team)


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")
