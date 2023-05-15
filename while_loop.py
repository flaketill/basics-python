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


def search_member(name, **members):
    team = []
    index = 0
    items = members.items()
    itr = iter(items)
    
    
    while index < len(members.items()):
        item = next(itr)
        key, value = item[0], item[1]
        
        if key == name:            
            #return f"{key}: {value}"
            return value
            break

        index += 1

    return ', '.join(team)


if __name__ == '__main__':


    print(f"{get_team_members('Armando', 'Danna', 'Keyra', 'Dante')}")


    print(f"\n The team info: \n {get_team_info_rows('Armando', 'Danna', 'Keyra', 'Dante')}")
    
    
    print(f"\n Searching Armando index: \n {search_member(name='Armando', Armando=0, Danna=1, Keyra=2, Dante=3)}" )

    
    print(f"\n Searching Danna index: \n {search_member(name='Danna', Armando=0, Danna=1, Keyra=2, Dante=3)}" )

