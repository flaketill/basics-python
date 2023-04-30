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

#	Arbitrary Keyword Arguments, **kwargs
def get_member_info(**kwargs):
	"""Return arbitrary keyword arguments"""

	data = []
	for key, value in kwargs.items():
		data.append(f"{key} = {value}")
	
	return ', '.join(data)


if __name__ == '__main__':
	

	# 1 keyword argument
	print(f"{get_student_info(firstname ='Armando')}")

	
	# 2 keyword arguments
	print(f"{get_student_info(firstname ='Delta', standard ='Seventh')}")

	
	# 2 keyword arguments
	print(f"{get_student_info(lastname ='Llanas', firstname ='Valentina')}")
	
	#Arbitrary positional arguments
	print(f"\n The team members: \n \n \t {get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")

	#Arbitrary keyword arguments (**kwargs)
	print(f"\n The information related to member: \n \n \t {get_member_info(name='Armando', age=30, city='Chihuahua')}")
