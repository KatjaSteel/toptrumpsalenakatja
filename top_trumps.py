import random
import requests

def get_pokemon():
  pokemon_number = random.randint(1,151)

  url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
  response = requests.get(url)
  pokemon = response.json()

  pokemon1 = {
    'name': pokemon['name'],
    'id': pokemon['id'],
    'height': pokemon['height'],
    'weight': pokemon['weight']
  }
  return pokemon1


def compare_states(user_pokemon, opponent_pokemon):
  print('Your Pokemon is {}'.format(user_pokemon['name']))
  print("Your opponent's Pokemon is {}".format(opponent_pokemon['name']))

  stat = input('What stat do you want to compare? (height / weight / id) ')
  print('Your {} is {}'.format(stat, user_pokemon[stat]))
  print("Your opponent's pokemon {} is {}".format(stat, opponent_pokemon[stat]))

  if user_pokemon[stat] > opponent_pokemon[stat]:
    print('You won this round!')
  else:
    print('Your opponent won this round!')


user_pokemon = get_pokemon()
opponent_pokemon = get_pokemon()

while user_pokemon == opponent_pokemon:
  user_pokemon = get_pokemon()
  opponent_pokemon = get_pokemon()

if user_pokemon['name'] == 'pikachu':
  print("You're lucky today! Your pokemon is Pikachu, you're an ultimate winner!")
elif opponent_pokemon['name'] == 'pikachu':
  print("Oh no! Your opponent's pokemon is Pikachu, so he won! Better luck next time!")
else:
  compare_states(user_pokemon, opponent_pokemon)








