# Build a very basic Pokémon class that allows you to simulate battles
# in a Rock-Paper-Scissors game mechanic, as well as feed your Pokémon.
#
# The class should follow these specifications:
#
# - Each Pokemon should have a `name`, `primary_type`, `max_hp` and `hp`
# - Primary types should be limited to `water`, `fire` and `grass`
# - Implement a `battle()` method based on rock-paper-scissors that
#   decides who wins based only on the `primary_type`:
#       water > fire > grass > water
# - Display messages that explain who won or lost a battle
# - If a Pokemon loses a battle, they lose some of their `hp`
# - If you call the `feed()` method on a Pokemon, they regain some `hp`

# Pokemon Game Project

class Pokemon():
    
    def __init__(self, name, primary_type, max_hp, hp):
        self.name = name
        self.primary_type = primary_type
        self.max_hp = max_hp
        self.hp = hp
    
    def __str__(self):
        my_str = f"Pokemon {self.name}'s health is {self.hp}/{self.max_hp}."
        return my_str
    
    def battle(self, other):
        if self.primary_type == other.primary_type:
            outcome = "Draw"
            complem = "Draw"
        elif self.primary_type == "water" and other.primary_type == "fire":
            outcome = "Win"
            complem = "Loss"
        elif self.primary_type == "fire" and other.primary_type == "grass":
            outcome = "Win"
            complem = "Loss"
        elif self.primary_type == "grass" and other.primary_type == "water":
            outcome = "Win"
            complem = "Loss"
        else:
            outcome = "Loss"
            complem = "Win"
        
        print(f"{self.name} - {outcome} & {other.name} - {complem}")
        
        if outcome == "Loss":
            self.hp -= 10
        if complem == "Loss":
            other.hp -= 10
    
    def feed(self):
        if self.hp < self.max_hp - 5:
            self.hp += 5
            print(f"{self.name}'s health has increased to {self.hp}.")
        elif self.hp == self.max_hp:
            print(f"{self.name}'s health is already full.")
        else:
            self.hp = self.max_hp
            print(f"{self.name}'s health is restored to full.")
    
    def type_change(self, new_type):
        self.hp //= 2
        self.primary_type = new_type
        print(f"The Pokemon type has changed but {self.name}'s health is reduced to {self.hp}.")


# Pokemon Game Battle Simulator

import random
import requests

my_name = input("Enter your Pokemon's name: ")
my_type = input("Enter your Pokemon's type (grass, fire or water): ")
length = len(my_name)

if length == 1 or length > 40:
    your_name = "Enemy Pokemon"
else:
    api_url = f"https://uzby.com/api.php?min={length}&max={length}"
    response = requests.get(api_url)
    your_name = response.text

print("Your opponent's Pokemon is called", your_name)

def rand_type():
    n = random.randint(0,2)
    if n == 0:
        your_type = "grass"
    elif n == 1:
        your_type = "fire"
    else:
        your_type = "water"
    return your_type

your_type = rand_type()

my_poke = Pokemon(my_name, my_type, 50, 50)
your_poke = Pokemon(your_name, your_type, 50, 50)

print("Turn based game; each player has 15 rounds.")

for i in range(0,15):
    user_input = input("Enter 1 to battle your opponent, 2 to feed your Pokemon, and 3 to change your Pokemon's type: ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            # Do Battle
            my_poke.battle(your_poke)
        elif user_input == 2:
            # Feed
            my_poke.feed()
        elif user_input == 3:
            # Change Type
            user_input = input("What type would you like to change to: ")
            my_poke.type_change(user_input)
        else:
            print("You did not enter 1, 2 or 3!")
        
    else:
        print("You did not enter 1, 2 or 3!")
    
    print()
    print("Now the enemy Pokemon makes a move!")
    b = random.randint(0,2)
    if b == 0:
        # Do Battle
        your_poke.battle(my_poke)
    elif b == 1:
        # Opponent feeds Pokemon
        your_poke.feed()
    else:
        # Opponent changes Pokemon type
        your_poke.type_change(rand_type())
    
    # If either Pokemon have hp <= 0 then game is over (use break).
    if my_poke.hp <= 0:
        print("Your pokemon has died! - you lose.")
        break
    if your_poke.hp <= 0:
        print("Your opponent's Pokemon has died! - you win.")
        break
    
    print("End of round", i+1, "!")
    print(f"{my_poke.name} is on {my_poke.hp} health")
    print(f"{your_poke.name} is on {your_poke.hp} health")
    rounds = i+1

# When code reaches here the game is over.
print(f"After {rounds} rounds, the game is over.")
print(f"{my_poke.name} ends with {my_poke.hp} health, while {your_poke.name} ends with {your_poke.hp} health.")