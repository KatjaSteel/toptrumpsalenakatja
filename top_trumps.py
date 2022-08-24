import random
import requests

play_again = "Y"

def round():
    def get_pokemon():
        pokemon_number = random.randint(1, 151)

        url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
        response = requests.get(url)
        pokemon = response.json()

        return {
            'name': pokemon['name'],
            'id': pokemon['id'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'base_experience': pokemon['base_experience'],

        }

    print('Selecting Pokemons...')

    pokemon_1 = get_pokemon()
    pokemon_2 = get_pokemon()
    pokemon_3 = get_pokemon()
    opponent_pokemon = get_pokemon()

    print('You have these pokemons in your party: {}, {}, {} '.format(pokemon_1['name'], pokemon_2['name'], pokemon_3['name']))
    pokemon_choice = input('Which pokemon do you want to use? ')

    if pokemon_choice == pokemon_1['name']:
        user_pokemon = pokemon_1

    elif pokemon_choice == pokemon_2['name']:
        user_pokemon = pokemon_2

    else:
        user_pokemon = pokemon_3

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
        opponent_pokemon = get_pokemon()

    if user_pokemon['name'] == 'pikachu':
        print("You're lucky today! Your pokemon is Pikachu, you're an ultimate winner!")
    elif opponent_pokemon['name'] == 'pikachu':
        print("Oh no! Your opponent's pokemon is Pikachu, so he won! Better luck next time!")
    else:
        compare_lives(3, 3)


while play_again == "Y":
    round()
    play_again = input("Would you like to play gain? Y/N ")

print("The game has ended. Thanks for playing!")
