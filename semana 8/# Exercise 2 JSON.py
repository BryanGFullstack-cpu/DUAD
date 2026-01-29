# Exercise 2 JSON 


import json


json_file = "pokemons"

try:
    with open(json_file, "r", encoding="utf-8") as file:
        pokemons = json.load(file)
except FileNotFoundError:
    print("File not found. A new one will be created.")
    pokemons = []


print("Add a new Pokémon:")
name = input("English name: ")
type_ = input("Type (comma-separated if multiple): ").split(",")
hp = int(input("HP: "))
attack = int(input("Attack: "))
defense = int(input("Defense: "))
sp_attack = int(input("Sp. Attack: "))
sp_defense = int(input("Sp. Defense: "))
speed = int(input("Speed: "))

new_pokemon = {
    "name": {"english": name},
    "type": [t.strip() for t in type_],
    "base": {
        "HP": hp,
        "Attack": attack,
        "Defense": defense,
        "Sp. Attack": sp_attack,
        "Sp. Defense": sp_defense,
        "Speed": speed
    }
}


pokemons.append(new_pokemon)

with open(json_file, "w", encoding="utf-8") as file:
    json.dump(pokemons, file, indent=4, ensure_ascii=False)

print(f"{name} has been added successfully!")


print("\nCurrent Pokémon List:")
for p in pokemons:
    print(f"{p['name']['english']} ({', '.join(p['type'])})")
    for stat, value in p["base"].items():
        print(f"  {stat}: {value}")
    print("-" * 20)