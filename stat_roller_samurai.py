import random
import time
def samurai_stats():

    # Global variable
    roll_agility = input("Press enter to roll for Agility. ")
    print("Rolling the die for Agility... ")
    # make a delay of 1 second
    time.sleep(1)
    # create a random number b/w 1 to 10
    agility_die = random.randint(1, 10)
    # print the number
    print("Agility: ", agility_die)
    # ask the user to roll_again or not
    
    roll_strength = input("You get a Strength bonus for being a Street Samurai. Hit enter to roll for Strength ")
    print("Rolling the die for Strength... ")
    time.sleep(1)
    strength_die = random.randint(1, 10+3)
    print("Strength: ", strength_die)
    
    roll_logic = input("Hit enter to roll for Logic ")
    print("Rolling the die for Logic... ")
    time.sleep(1)
    logic_die = random.randint(1, 10)
    print("Logic: ", logic_die)

    roll_hacking = input("Hit enter to roll for Hacking ")
    print("Rolling the die for Hacking... ")
    time.sleep(1)
    hacking_die = random.randint(1, 10) 
    print("Hacking: ", hacking_die)
    print("Here's your stats ", 
    "Agility: ", agility_die,
    "Strength: ", strength_die, 
    "Logic: ", logic_die, 
    "Hacking: ", hacking_die)

    

    return {
        "agility": agility_die,
        "strength": strength_die,
        "logic": logic_die,
        "hacking": hacking_die
    }