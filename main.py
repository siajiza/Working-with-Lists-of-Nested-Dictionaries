# Dictionary inside of a list

# teams is going to be a list that contains various dictionaries, so every items is going to be a Dictionary.

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

print(teams)
# [{'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}, {'angels': {'OF': 'Trout', 'DH': 'Pujols'}}]

print(teams[0]) 
# {'astros': {'2B': 'Altuve', 'SS': 'Correa', '3B': 'Bregman'}}

# we can use [0] b´ teams is a list. So if is was not a list we would need to use "print(list(teams.items))"



angels = teams[1].get('a', 'Team not found')

print(angels)

