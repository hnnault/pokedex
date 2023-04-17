import json #import json module

with open("pokedex.json", "r") as in_file: # find and open json file
    pokedex = json.load(in_file) # load json file

def user_interface():
    print("\n************** POKEDEX **************\n")

    while True:
        # Interface
        print("\n-------- MENU --------\n")
        print("1: List all pokemon")
        print("2: List pokemon by type")
        print("3: Get a pokemon")
        print("4: Get pokemon evolutions")
        print("0: Quit")

        # Prompt
        choice = int(input("Make a Selection: "))

        # if they responded by 1,2,3,4,0
        if choice == 1:
            list_all() # list all pokemon
        elif choice == 2:
            list_by_type() # list all pokemon by certain type
        elif choice == 3:
            display_pokemon() # display a list of every pokemon
        elif choice == 4:
            get_evolutions() # display the evolutions of the pokemon
        elif choice == 0:
            break
        else:
            print("Invalid Selection")


# get name of pokemon 
def get_pokemon(type="all"):
    if type == "all":
        # loop through the pokedex to find the pokemon name if there they requested every type
        names = [p['name'] for p in pokedex['pokemon']] 
    else:
        # loop through the pokedex to find the pokemon name if they requested a specific type
        names = [p['name'] for p in pokedex['pokemon'] if type in p['type']]  
         
    return names


def list_all():
    print("\n")
    names = get_pokemon() # run the get_pokemon function 
    for i, name in enumerate(names): 
        print(f"{i + 1}: {name}") # print off the index number of pokemon and the name 
    print("\n") 


# list pokemon by type
def list_by_type():
    print("\n")
    poke_type = input("Give a type: ")

    names = get_pokemon(poke_type)
    print(f"\n{poke_type} pokemon:")
    for i, name in enumerate(names):
        print(f"{i+1}: {name}") # prints out the id of the pokemon and name

    print("\n")


# return the pokemon's stats based on name
def get_pokemon_name(pokename):
    for value in pokedex['pokemon']: 
        if value['name'] == pokename: # if the name lines up in the json file with the input
            return value # return the pokemon's statistics


def display_pokemon():
    poke_name = input("Give a name: ") # input

    print("\n")
    for k in get_pokemon_name(poke_name):
        print(f"{k}: {get_pokemon_name(poke_name)[k]}") # prints out the stat type then the stat related to the stat type 


# Function to display the next and previous evolutions if there is any
def get_evolutions():
    poke_name = input("Give a name: ") # input

    print("\n*** Next Evolution(s) ***")

    if "next_evolution" in get_pokemon_name(poke_name): # if next evolution is found the json file
        evolution_data = get_pokemon_name(poke_name)["next_evolution"]

        for i in range(len(evolution_data)): # loop through the data inside of the evolution_data 
            if evolution_data[i]["num"]: # if the value is the number then print the number
                print(f"ID: {evolution_data[i]['num']}")

            if evolution_data[i]["name"]: # if the value is the name then print the name
                print(f"Name: {evolution_data[i]['name']}\n")

    else: # If there is no next evolution
        print("This pokemon is at max evolution")

    print("\n*** Previous Evolution(s) ***")

    if "prev_evolution" in get_pokemon_name(poke_name): # if prev_evolution exists
        evolution_data = get_pokemon_name(poke_name)["prev_evolution"]

        for i in range(len(evolution_data)): # loop through the data inside of the evolution_data 
            if evolution_data[i]["num"]: # if the value is the number then print the number
                print(f"ID: {evolution_data[i]['num']}")

            if evolution_data[i]["name"]: # if the value is the name then print the name
                print(f"Name: {evolution_data[i]['name']}\n")

    else: # if there is no previous evolution
        print("This Pokemon is at it's lowest evolution.")


user_interface()