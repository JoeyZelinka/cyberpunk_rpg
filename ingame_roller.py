import random
import time

def success_roll():
    success_roll = input("Hit enter to make your success roll ")
    print("Rolling the dice...")
    time.sleep(2)
    dice = random.randint(1, 20)
    return dice





