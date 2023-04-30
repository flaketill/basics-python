#!/usr/bin/env python3


def get_student_info(firstname, lastname ='Ibarra', standard ='Fifth'):
	"""Return Fixed arguments"""
	return f"{firstname} {lastname} 'studies in': {standard}, 'Standard'"

def get_team_members(*members):
	"""Return Arbitrary positional arguments"""
	
	team = []
	
	
	for member in members:
		team.append(member)
		
	return ', '.join(team)
	
if __name__ == '__main__':
	

	# 1 keyword argument
	print(f"{get_student_info(firstname ='Armando')}")

	
	# 2 keyword arguments
	print(f"{get_student_info(firstname ='Delta', standard ='Seventh')}")

	
	# 2 keyword arguments
	print(f"{get_student_info(lastname ='Llanas', firstname ='Valentina')}")
	
	print(f"\n The team members: \n \n \t {get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")
	