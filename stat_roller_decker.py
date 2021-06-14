import random
import time
def decker_stats():

    
    roll_agility = input("Press enter to roll for Agility. ")
    print("Rolling the die for Agility... ")
    time.sleep(1)
    agility_die = random.randint(1, 10)
    print("Agility: ", agility_die)
    
    roll_strength = input("Hit enter to roll for Strength ")
    print("Rolling the die for Strength... ")
    time.sleep(1)
    strength_die = random.randint(1, 10)
    print("Strength: ", strength_die)
    
    roll_logic = input("Hit enter to roll for Logic ")
    print("Rolling the die for Logic... ")
    time.sleep(1)
    logic_die = random.randint(1, 10)
    print("Logic: ", logic_die)

    roll_hacking = input("You get a bonus to Hacking for being a Decker. Hit enter to roll for Hacking ")
    print("Rolling the die for Hacking... ")
    time.sleep(1)
    hacking_die = random.randint(1, 10 +3) 
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
