# Working-with-Lists-of-Nested-Dictionaries
Dictionary inside of a list, the variable is going to be a list that contains various dictionaries, so every items is going to be a Dictionary.


<h3>In this case, teams is going to be a list that contains various dictionaries, so every items is going to be a Dictionary.</h3>

    teams = [
      { # item one
        'astros': {
          '2B': 'Altuve',
          'SS': 'Correa',
          '3B': 'Bregman',
        }
      },
      { # item two
        'angels': {
          'OF': 'Trout',
          'DH': 'Pujols',
        }
      }
    ]
    
    
<h3>Check everething is working propely</h3>

    print(teams)
    # [{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'OF': 'Trout', 'DH': 'Pujols'}}]


<h3>we can use [0] b´ teams is a list. So if is was not a list we would need to use "print(list(teams.items))"</h3>

    print(teams[0]) 
    # {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}


<h3>with get( ), find a item on the list</h3>

    angels = teams[1].get('a', 'Team not found')

    print(angels)

