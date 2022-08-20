import random
import requests


def get_pokemon():
    pokemon_number = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    pokemon1 = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'base_experience': pokemon['base_experience']
    }
    return pokemon1


user_pokemon = get_pokemon()
opponent_pokemon = get_pokemon()

print('Selecting Pokemons...')


def compare_lives(my_lives, opponent_lives):
    print('Your Pokemon is {}'.format(user_pokemon['name']))
    print("Your opponent's Pokemon is {}".format(opponent_pokemon['name']))
    while my_lives > 0 and opponent_lives > 0:

        stat = input('What stat do you want to compare? (height / weight / id / base_experience) ')
        print('Your {} is {}'.format(stat, user_pokemon[stat]))
        print("Your opponent's pokemon {} is {}".format(stat, opponent_pokemon[stat]))
        print('-------------------------------------')

        if user_pokemon[stat] > opponent_pokemon[stat]:

            opponent_lives = opponent_lives - 1
            print('You won this round!')
            print("Your opponent have {} lives left ".format(opponent_lives))
            print("And you have {} lives left ".format(my_lives))
            print('-------------------------------------')
        elif user_pokemon[stat] < opponent_pokemon[stat]:
            my_lives = my_lives - 1
            print('Your opponent won this round!')
            print("Your opponent have {} lives left ".format(opponent_lives))
            print("And you have {} lives left ".format(my_lives))
            print('-------------------------------------')

        else:
            print("Your states are the same! This round is a draw!")

    if my_lives == 0:
        print("Game over! You lost! (︶︹︺)")

    elif opponent_lives == 0:
        print("Game over! You won! °˖✧◝(⁰▿⁰)◜✧˖°")


while user_pokemon == opponent_pokemon:
    user_pokemon = get_pokemon()
    opponent_pokemon = get_pokemon()

if user_pokemon['name'] == 'pikachu':
    print("You're lucky today! Your pokemon is Pikachu, you're an ultimate winner!")
elif opponent_pokemon['name'] == 'pikachu':
    print("Oh no! Your opponent's pokemon is Pikachu, so he won! Better luck next time!")
else:
    compare_lives(3, 3)
