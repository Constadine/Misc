pokemon_types = {
    "Charmander": "Fire",
    "Squirtle": "Water",
    "Bulbasaur": "Brocoli",
    "Picatsu": "Thunder",
    "Growlith": "Fire"
}

# for key, value in pokemon_types.items():
#     print(f'{key} is {value} type.')


# for key in sorted(pokemon_types.keys()):
#     print(f'{key} is {pokemon_types[key]}')

for key in set(pokemon_types.values()):
    print(key, end=", ")
